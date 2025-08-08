import os
# Функция вывода истории
def show_history():
		if not History:
			print('История пуста')
		else:
			print('Последние 5 операций:')
			for i, record in enumerate(History[::-1], start = 1):
				print(f'[{i}] {record}')

# Фукнция сохранения истории
def save_history():
	try:
		with open('history.txt', 'w') as file:
			for record in History:
				file.write(record + '\n')
			print('История сохранена в файл history.txt')
	except PermissionError:
			print("Ошибка: нет прав на запись файла")
	except OSError as e:
			print(f"Ошибка ОС: {str(e)}")

# Функция очистки истории
def clear_history():
	History = []
	with open('history.txt', 'w'):
		pass

History = []

# Чтение истории
if os.path.exists('history.txt'):
	with open('history.txt', 'r') as file:
		lines = file.readlines()
		History = [line.strip() for line in lines[-5:]]
else:
	History = []