Operations = {
	'сумма': lambda a,b: a + b,
	'вычитание': lambda a,b: a - b,
	'деление': lambda a,b: a / b,
	'умножение': lambda a,b: a * b,
	'степень': lambda a,b: a ** b,
	'остаток': lambda a,b: a % b,
}

History = []

print(f'Доступные операции: {", ".join(Operations.keys())}')


while True:
	
	try:

		# Ввод пользователем чисел и преобразование их в список
		nums = list(map(float, input('Ввведите два числа: ').split()))

		# Обработка ошибки когда пользователь ввел не 2 числа
		if len(nums) != 2:
			raise ValueError('Требуется ввести два числа')

		#Ввод пользователем операции и перевод в нижний регистор
		op = input('Введите операцию: ').lower()

		# Обработка ошибки когда пользователь ввел несуществующую операцию
		if op not in Operations:
			raise KeyError('Недоступная операция')

		# Обработка ошибки деления на ноль
		if op == 'деление' and nums[1] == 0:
			raise ZeroDivisionError('Невозможно поделить на ноль')

		# Подсчет результата
		result = Operations[op](*nums)

		# Сохранение операции в историю
		str_history = f'{a} {operations_symbol} {b} = {result}'
		History.append(str_history)

		#Ограничение истории до 5 операций
		if len(History) > 5:
			del History[0]

		# Вывод результат с округлением
		print(f'Результат: {result:.2f}' if result % 1 else f'Результат: {int(result)}')

	# Вывод ошибок
	except Exception as e:
		print(f'Ошибка: {str(e)}')
		print('Пожалуйста, повторите снова')