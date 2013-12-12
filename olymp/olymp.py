def task_1a():
	a = int(input())
	b = int(input())
	
	c = (a**2 + b**2) ** 0.5
	print(c)

	
def task_1f():
	#Дано натуральное число.
	#Выведите его последнюю цифру.
	a = int(input())
	print(a % 10) 
	
	
def task_1g():
	#Дано двузначное число. Найдите число десятков в нем.		
	# 42 -> 4
	a = input()
	print(a[-2])
	
	# альтернативное решение
	#a_int = int(a)
	#print((a_int % 100) // 10 ) 

	
def task_1n():
	#В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.
	#Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок. Выведите два целых числа: время окончания урока в часах и минутах. При решении этой задачи нельзя пользоваться циклами и условными инструкциями.
	a = int(input())
	num_peremen = a - 1
	time_peremen = (num_peremen // 2 * 20) + (num_peremen % 2) * 5
	time_urok = a * 45
	
	time_all_minutes =  time_peremen + time_urok
	
	hours = time_all_minutes // 60 
	minutes = time_all_minutes % 60
	
	print(hours+9, minutes)


def task_1p():
	# Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из моментов времени. Известно, что второй момент времени наступил не раньше первого. Определите, сколько секунд прошло между двумя моментами времени. Программа на вход получает три целых числа — часы, минуты, секунды, задающие первый момент времени и три целых числа, задающих второй момент времени. Выведите число секунд между этими моментами времени.
	a1 = int(input())
	a2 = int(input())
	a3 = int(input())
	b1 = int(input())
	b2 = int(input())
	b3 = int(input())
	
	#a1 = a1 * 3600
	a1 *= 3600
	a2 = a2 * 60
	
	b1 = b1 * 3600
	b2 = b2 * 60
	
	c = (b1 + b2 + b3) - (a1 + a2 + a3)
	print(c)
	
	
def task_2d():
	# В математике функция sign(x) (знак числа) определена так: 
	# sign(x) = 1,   если x > 0, 
	# sign(x) = -1, если x < 0, 
	# sign(x) = 0,   если x = 0.

	# Для данного числа x выведите значение sign(x).
	
	a = int(input())
	
	if a == 0:
		print(0)
	elif a > 0:
		print(1)
	else:
		print(-1)
	
	
def task_3_1_a():
	# Выведите все точные квадраты натуральных чисел, не превосходящие данного числа N.
	n = int(input())
	counter = 1
	while counter <= n:
		print(counter)
		square = counter ** 2
		if square <= n: 
			print(square)
		else:
			break		
		counter += 1

	
def task_3_1_h():
	# По данному числу n определите n-е число Фибоначчи φn.
	n = int(input())
	
	if n == 0: print(0)
	elif n == 1: print(1)
	else:
		n_prev_prev = 0
		n_prev = 1
		counter = 2
		while True:
			n_current = n_prev + n_prev_prev
			
			if counter == n: break
			
			n_prev_prev = n_prev
			n_prev = n_current
			
			counter += 1
			
		print(n_current)	
		
	
task_3_1_h()