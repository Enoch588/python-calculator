import os
from history_manager import *
import operations

print(f'Доступные операции: {", ".join(operations.Operations.keys())}')

while True:
	
	try:

		# Блок ввода чисел с валидацией
	    nums = []
	    for i in range(2):
	        while True:
	            try:
	                num = float(input(f'Введите число {i+1}: '))
	                nums.append(num)
	                break
	            except ValueError:
	                print("Ошибка: введено не число. Пожалуйста, введите число.")

		# Ввод пользователем операции и перевод в нижний регистор
		op = input('Введите операцию: ').lower().strip()

		# Вывод истории операций
		if op == 'история':
			show_history()
			continue

		# Сохранение истории в файл
		if op == 'сохранить':
			save_history()
			continue

		# Очистка истории
		if op == 'очистить':
			clear_history()
			print('История очищена')
			continue

		# Обработка ошибки когда пользователь ввел несуществующую операцию
		if op not in operations.Operations:
			raise KeyError('Недоступная операция')

		# Обработка ошибки деления на ноль
		if op == 'деление' and nums[1] == 0:
			print('Пожалуйста, введите второе число отличное от нуля')
			while nums[1] == 0:
				nums[1] = float(input('Введите второе число заново: '))

		# Подсчет результата
		result = operations.Operations[op](*nums)

		# Вывод результат с округлением
		print(f'Результат: {result:.2f}' if result % 1 else f'Результат: {int(result)}')

		# Сохранение операции в историю
		str_history = f'{nums[0]} {operations.Operations_Symbols[op]} {nums[1]} = {result:.2f}'
		History.append(str_history)

		#Ограничение истории до 5 операций
		if len(History) > 5:
			del History[0]

	# Вывод ошибок
	except Exception as e:
		print(f'Ошибка: {str(e)}')
		print('Пожалуйста, повторите снова')