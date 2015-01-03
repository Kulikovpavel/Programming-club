def postfix(s):
	op_stack = []
	res = []
	for i in s:
		if i == ')':
			current = op_stack.pop()
			while current != '(':
				res.append(current)
				current = op_stack.pop()
		elif i == '(':
			op_stack.append(i)
		elif i == '+':
			print(op_stack)
			while op_stack and op_stack[-1] == '*':
				res.append(op_stack.pop())
			op_stack.append(i)
		elif i == '*':
			op_stack.append(i)
		else:
			res.append(i)
	op_stack.reverse()
	res += op_stack
	return res
	
print(postfix("((A+B)*C)*(D+F)"))
