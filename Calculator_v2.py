import os
Operations = {
	'сумма': lambda a,b: a + b,
	'вычитание': lambda a,b: a - b,
	'деление': lambda a,b: a / b,
	'умножение': lambda a,b: a * b,
	'степень': lambda a,b: a ** b,
	'остаток': lambda a,b: a % b,
}
# Символы для операций
Operations_Symbols = {
	'сумма': '+',
	'вычитание': '-',
	'деление': '/',
	'умножение': '*',
	'степень': '^',
	'остаток': '%',
}

History = []

# Чтение истории
try:
	if os.path.exists('history.txt'):
		with open('history.txt', 'r') as file:
			History = file.readlines()[-5:]
			History = [line.strip() for line in lines]
	else:
		History = []
except Exception as e:
	print('Ошибка')

print(f'Доступные операции: {", ".join(Operations.keys())}')


while True:
	
	try:

		# Ввод пользователем чисел и преобразование их в список
		nums = list(map(float, input('Ввведите два числа: ').split()))

		# Обработка ошибки когда пользователь ввел не 2 числа
		if len(nums) != 2:
			raise ValueError('Требуется ввести два числа')

		#Ввод пользователем операции и перевод в нижний регистор
		op = input('Введите операцию: ').lower().strip()

		# Вывод истории операций
		if op == 'история':
			if not History:
				print('История пуста')
			else:
				print('Последние 5 операций:')
				for i, record in enumerate(History[::-1], start = 1):
					print(f'[{i}] {record}')
			continue

		# Сохранение истории в файл
		if op == 'сохранить':
			try:
				with open('history.txt', 'w') as file:
					for record in History:
						file.write(record + '\n')
					print('История сохранена в файл history.txt')
			except PermissionError:
			    print("Ошибка: нет прав на запись файла")
			except OSError as e:
			    print(f"Ошибка ОС: {str(e)}")
			continue

		# Очистка истории
		if op == 'очистить':
			History = []
			print('История очищена')
			continue

		# Обработка ошибки когда пользователь ввел несуществующую операцию
		if op not in Operations:
			raise KeyError('Недоступная операция')

		# Обработка ошибки деления на ноль
		if op == 'деление' and nums[1] == 0:
			print('Пожалуйста, введите второе число отличное от нуля')
			while nums[1] == 0:
				nums[1] = float(input('Введите второе число заново: '))

		# Подсчет результата
		result = Operations[op](*nums)

		# Вывод результат с округлением
		print(f'Результат: {result:.2f}' if result % 1 else f'Результат: {int(result)}')

		# Сохранение операции в историю
		str_history = f'{nums[0]} {Operations_Symbols[op]} {nums[1]} = {result:.2f}'
		History.append(str_history)

		#Ограничение истории до 5 операций
		if len(History) > 5:
			del History[0]

	# Вывод ошибок
	except Exception as e:
		print(f'Ошибка: {str(e)}')
		print('Пожалуйста, повторите снова')