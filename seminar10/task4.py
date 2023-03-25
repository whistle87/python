"""
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']
for el in words:
    el_byte = el.encode()
    el_again_str = el_byte.decode()
    print(f"Байтовое представление: {el_byte},строковое представление: {el_again_str}")