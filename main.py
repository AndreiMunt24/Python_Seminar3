# def min_flips_to_uniform(coins):
#     # Подсчет количества монеток, лежащих гербом вверх (0)
#     count_zeros = coins.count(0)
#     # Подсчет количества монеток, лежащих решкой вверх (1)
#     count_ones = coins.count(1)
#     # Минимальное количество переворотов будет минимум из этих двух значений
#     return min(count_zeros, count_ones)

# # При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию
# # coins = [0, 1, 0, 1, 1, 0]
# # print(min_flips_to_uniform(coins))

# # Пример использования
# coins = [0, 1, 0, 1, 1, 0]
# print(min_flips_to_uniform(coins))  # Ожидаемый вывод: 3

# sp = list()
# sp = [-1, True, "hello", 5.77, 8.999, "world"]

# print(sp)
# print(sp[2:5])

# for i in range(len(sp)):
#     print(f"{i} - {sp[i]}")

# for el in sp:
#     print(el, end = ' ')

# print(end = '\n')




### vtoroi primer
# sp = list()
# sp = [-1, True, "hello", 5.77, 8.999, "world"]

# # print(sp)
# # print(sp[2:5])

# # for i in range(len(sp)):
# #     print(f"{i} - {sp[i]}")

# # for el in sp:
# #     print(el, end = ' ')

# # print(end = '\n')

# sp.append('last')
# sp.insert(0,'first')
# # print(sp)

# sp.remove(True)
# del sp[0]
# # print(sp)
# a = sp.pop()
# # print(a)
# # print(sp)

### tretii primer
"""
sp = list()
sp = [-1, True, "hello", 5.77, 8.999, "world"]

# print(sp)
# print(sp[2:5])

# for i in range(len(sp)):
#     print(f"{i} - {sp[i]}")

# for el in sp:
#     print(el, end = ' ')

# print(end = '\n')

sp.append('last')
sp.insert(0,'first')
# print(sp)

sp.remove(True)
del sp[0]
# print(sp)
a = sp.pop()
# print(a)
# print(sp)

t = tuple(sp)
# print(t)
# print('hi' in t)
# print('hello' in t)

d = {}
d['дядя ваня'] = 8645464
d['дядя вася'] = 21313231321
# # print(d)
# print(d.keys())
# print(d.values())
"""


##fibonachi

# k = int(input('vvedite chislo k '))
# k = 'ноутбук'

# my_dict =  {'А': 1 , 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3,
#             'Я':3, 'й': 4, 'Ы': 4, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Э': 8, 'Ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10}

# my_dict = {
#     'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#     'D': 2, 'G': 2,
#     'B': 3, 'C': 3, 'M': 3, 'P': 3,
#     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#     'K': 5,
#     'J': 8, 'X': 8,
#     'Q': 10, 'Z': 10
# }

# new_text = input('Введите слово: ').upper()
# sum = 0
# for i in new_text:
#     for k, v in my_dict.items():
#         if i in k:
#             sum += v

# print(f"{sum}")




# Словари стоимости букв для русского и английского алфавитов
russian_dict = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ё': 3,
    'Ь': 3, 'Я': 3, 'Й': 4, 'Ы': 4, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10
}

english_dict = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

def calculate_word_value(word):
    word = word.upper()  # Приведение к верхнему регистру
    total_value = 0
    
    # Определяем, какой словарь использовать
    if all(letter in russian_dict or letter in {'Ё'} for letter in word):
        score_dict = russian_dict
    elif all(letter in english_dict for letter in word):
        score_dict = english_dict
    else:
        raise ValueError("Слово содержит буквы из разных алфавитов или недопустимые символы.")
    
    # Считаем стоимость
    for letter in word:
        if letter in score_dict:
            total_value += score_dict[letter]
        else:
            print(f"Символ '{letter}' не найден в словаре.")
    
    return total_value

# Пример использования
new_text = input('Введите слово: ')
try:
    value = calculate_word_value(new_text)
    print(f"Стоимость слова '{new_text}': {value}")
except ValueError as e:
    print(e)
