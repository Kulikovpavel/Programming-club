import unittest


def reconstruct_knapsack_without_reps(case, array):
    w = len(array) - 1
    v = array[-1]
    ans = []
    while v != 0:
        for c in case:
            if c[0] <= w and array[w-c[0]] == v - c[1]:
                v -= c[1]
                w -= c[0]
                ans.append(c)
                break
    return sorted(ans)


def knapsack_simple_with_reconstruct(case, full_w):
    ans = knapsack_simple(case, full_w)
    return ans[full_w], reconstruct_knapsack_without_reps(case, ans)


def knapsack_simple_without_reconstruct(self, case, full_w):
    return knapsack_simple(case, full_w)[full_w]


def knapsack_simple(case, full_w):
    ans = [0] * (full_w + 1)
    for w in range(1, full_w + 1):
        for c in case:
            if c[0] <= w:
                ans[w] = max(ans[w-c[0]] + c[1], ans[w])

    return ans


def knapsack_recursive(self, case, full_w):
    max_val = 0
    for c in case:
        if c[0] <= full_w:
            new_val = knapsack_recursive(self, case, full_w - c[0]) + c[1]
            max_val = max(new_val, max_val)
    return max_val


def knapsack_recursive_memo(self, case, full_w):
    global memo
    if full_w in memo:
        return memo[full_w]
    max_val = 0
    for c in case:
        if c[0] <= full_w:
            new_val = knapsack_recursive_memo(self, case, full_w - c[0]) + c[1]
            max_val = max(new_val, max_val)
    memo[full_w] = max_val
    return max_val


class TestKnapsackSimpleReconstructAns(unittest.TestCase):
    def test_1_simple(self):
        case = [(6, 30), (3, 14), (4, 16), (2, 9)]
        w = 1
        self.assertEqual(knapsack_simple_with_reconstruct(case, w)[0], 0)
        self.assertEqual(knapsack_simple_with_reconstruct(case, w)[1], [])

    def test_2_simple(self):
        case = [(6, 30), (3, 14), (4, 16), (2, 9)]
        w = 2
        self.assertEqual(knapsack_simple_with_reconstruct(case, w)[0], 9)
        ans = [(2, 9)]
        self.assertEqual(knapsack_simple_with_reconstruct(case, w)[1], ans)

    def test_3_more(self):
        case = [(6, 30), (3, 14), (4, 16), (2, 9)]
        w = 10
        self.assertEqual(knapsack_simple_with_reconstruct(case, w)[0], 48)
        ans = [(2, 9), (2, 9), (6, 30)]
        self.assertEqual(knapsack_simple_with_reconstruct(case, w)[1], ans)


class TestKnapsackSimple(unittest.TestCase):
    FUNC = knapsack_simple_without_reconstruct

    def test_1_simple(self):
        case = [(6, 30), (3, 14), (4, 16), (2, 9)]
        w = 1
        self.assertEqual(self.FUNC(case, w), 0)

    def test_2_simple(self):
        case = [(6, 30), (3, 14), (4, 16), (2, 9)]
        w = 2
        self.assertEqual(self.FUNC(case, w), 9)

    def test_3_more(self):
        case = [(6, 30), (3, 14), (4, 16), (2, 9)]
        w = 10
        self.assertEqual(self.FUNC(case, w), 48)


class TestKnapsackRecurs(TestKnapsackSimple):
    FUNC = knapsack_recursive


class TestKnapsackRecursMemo(TestKnapsackSimple):
    FUNC = knapsack_recursive_memo

    def setUp(self):
        global memo
        memo = {}


def reconstruct_k_with_rep(case, array_2d):
    n = len(case)
    w = len(array_2d) - 1
    ans_set = set()
    for i in range(n, 0, -1):
        if array_2d[w][i-1] != array_2d[w][i]:
            ans_set.add(case[i-1])
            w -= case[i-1][0]
    return ans_set


def knapsack_with_rep(self, case, full_w):
    n = len(case)
    array_2d = [([0] * (n+1)) for _ in range(full_w+1)]
    for i in range(1, n+1):
        for w in range(1, full_w + 1):
            array_2d[w][i] = array_2d[w][i-1]
            if case[i-1][0] <= w:
                with_it = array_2d[w-case[i-1][0]][i - 1] + case[i-1][1]
                array_2d[w][i] = max(array_2d[w][i], with_it)

    return array_2d[full_w][n], reconstruct_k_with_rep(case, array_2d)


class TestKnapsackWithRepetition(unittest.TestCase):
    FUNC = knapsack_with_rep

    def test_1_simple(self):
        case = [(6, 30), (3, 14), (4, 16), (2, 9)]
        w = 1
        self.assertEqual(self.FUNC(case, w)[0], 0)

    def test_2_simple(self):
        case = [(6, 30), (3, 14), (4, 16), (2, 9)]
        w = 2
        self.assertEqual(self.FUNC(case, w)[0], 9)

    def test_3_more(self):
        case = [(6, 30), (3, 14), (4, 16), (2, 9)]
        w = 10
        self.assertEqual(self.FUNC(case, w)[0], 46)

    def test_4_reconstruct(self):
        case = [(6, 30), (3, 14), (4, 16), (2, 9)]
        w = 2
        self.assertEqual(self.FUNC(case, w)[1], set([(2, 9)]))
        w = 0
        self.assertEqual(self.FUNC(case, w)[1], set())

    def test_5_reconstruct_more(self):
        case = [(6, 30), (3, 14), (4, 16), (2, 9)]
        w = 10
        self.assertEqual(self.FUNC(case, w)[1], set([(4, 16), (6, 30)]))

if __name__ == '__main__':
    unittest.main(verbosity=2)
