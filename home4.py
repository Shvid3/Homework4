# #1 работа с переменными
#
# var_int = 10
# var_float = 8.4
# var_srt = "No"
# var2_int = var_int * 3.5
# var_float -= 1
# var_int_float = var_int / var_float
# var2_float = var2_int / var_float
# var_srt = "No" + "No" + "Yes" * 3
# print(var_int)
# print(var2_float)
# print(var_float)
# print(var_int_float)
# print(var2_float)
# print(var_srt)
#
# #2 работа со строками
#
# my_string = "For example the first line"
# first_char = my_string[0]
# last_char = my_string[-1]
# third_start = my_string[2]
# last_third_end = my_string[-3]
# length_string = len(my_string)
# print(first_char)
# print(last_char)
# print(third_start)
# print(last_third_end)
# print(length_string)
#
# different_string = "My brother loves my cat and dog"
# first_eight_chars = different_string[:8]
# middle_four_chars = different_string[7:11]
# mutltip_three = different_string[::3]
# reversed_string = different_string[::-1]
# print(first_eight_chars)
# print(middle_four_chars)
# print(mutltip_three)
# print(reversed_string)
#
# original_name_string = "my name is name"
# my_name = "Ann"
# original_name_string2 = original_name_string.replace("name","Ann",2)
# print(original_name_string2)
#
# test_string = "Hello world!"
# position_of_w = test_string.find("w")
# count_of_l = test_string.count("l")
# where_hello = test_string.startswith("Hello")
# end_with_qwe = test_string.endswith("qwe")
# print(position_of_w)
# print(count_of_l)
# print(where_hello)
# print(end_with_qwe)
#
# #3 работа со списками
#
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = ["cat","dog","fox","wolf","rabbit"]
# two_element = list1[1]
# list2[-1] = "monkey"
# print(list2)
# simil_list = list1 + list2
# print(simil_list)
# srez_from_simil = simil_list[1:3]
# new_elements_simil = simil_list.extend(["11","shark"])
# print(new_elements_simil)
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# some_number = list(set(a) & set(b))
# print(some_number)
# unical_number = list(set([1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]))
# print(unical_number)
#
# #4 логические операции
# a = 15
# b = 28
# print(a<b and a > 10)
# print(b > 20 and b>=28)
# print(a>b and a>20)
# print(a>=20 and a>=b)
#
# print(a<b or a > 10)
# print(b > 20 or b>=28)
# print(a>b or a>20)
# print(a>=20 or a>=b)
#
# a1 = "fox"
# a2 = "wolf"
# print(len(a1)>2 and len(a2)>2)

#5 словари

# school = {
#     "1a": 27,
#     "1b": 25,
#     "2a": 23,
#     "4b": 17,
#     "5d": 13
# }
# print(school["1a"])
#
# school["2a"] = 24
# school["4b"] = 20
#
# school["6c"] = 22
# del school["5d"]
# print(school)
#
# #6 преобразование типов
# name_man = "Robin Singh"
# name_string = "I love arrays they are my favorite"
# str1 = name_man.split()
# str2 = name_string.split()
# print(str1)
# print(str2)
#
# names_boy = ["Ivan", "Ivanou"]
# country_with_city = ["Minsk", "Belarus"]
# print(f"Привет,{names_boy[0]} {names_boy[1]}.Добро пожаловать в {country_with_city[0]} {country_with_city[1]}")
#
# lst1 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
# sentence = " ".join(lst1)
# print(sentence)
#
# lstt2 = [1,2,3,4,5,6,7,8,9,10]
# lstt2.insert(2, "15")
# del lstt2[5]
# print(lstt2)
#
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': 5}
# keys_aall = set(a.keys()).union(set(b.keys()))
# a_b = {}
# for key in keys_aall:
#     a_b[key] = [a.get(key, None), b.get(key, None)]
# print(a_b)

# условия
# a = int(input())
# if a>0:
#     a+=1
#     print(a)

# got_year = int(input())
# if (got_year % 4 == 0 and got_year % 100 != 0) or (got_year % 400 == 0):
#     print(366)
# else:
#     print(365)

# days_week =  ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
# a = int(input())
# print(days_week[a - 1])


# unit_num = int(input())
# massa = float(input())
# if unit_num == 1:
#     print(massa)
# elif unit_num == 2:
#     print(massa * 1e-6)
# elif unit_num == 3:
#     print(massa * 1e-3)
# elif unit_num == 4:
#     print(massa * 1000)
# elif unit_num == 5:
#     print(massa * 100)

# Цикл for
# A, B = map(int, input().split())
# numbers_ = sum(range(A, B + 1))
# print(numbers_)

# A, B = map(int, input().split())
# natural_num = sum(x for x in range(A, B + 1) if x > 0)
# print(natural_num)

# swim = {
#     "Бекиш Александр": 21.07,
#     "Будник Алексей": 20.34,
#     "Гребень Анастасия": 22.12,
#     "Давидович Татьяна": 30,
#     "Дешук Дмитрий": 24.01,
#     "Казак Анна": 28.17
# }
# best_swim = min(swim, key=swim.get)
# best_time = swim[best_swim]
# print(f"Лучший результат: {best_swim} - {best_time}")
#
# numbers = [1, 5, 2, 9, 2, 9, 1]
# uni_numb = 0
# for num in numbers:
#     uni_numb ^= num
# print(uni_numb)

# цикл while
# N = int(input())
# number = 1
# for i in range(1, N + 1):
#     number *= i
#     print(number)
#
# N = int(input())
# count = 0
# numb_sum = 0
# while N > 0:
#     numb_sum = N % 10
#     numb_sum+= numb_sum
#     count += 1
#     N //= 10
# print(count,numb_sum)

# G1, G2 = map(int, input().split())
# year = 0
# while G1 >= 0.1 * G2:
#     G1 *= 2
#     G2 *= 3
#     year += 1
# print(year)


























