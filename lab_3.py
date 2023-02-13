# print(" ")
# print("1-esep")
# print(" ")
# print("a = " , end = "")
# a = int(input())
# print("b = " , end = "")
# b = int(input())
# for i in range (a , b + 1):
#     print(i) 
# # 1.Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.

# print(" ")
# print("2-esep")
# print(" ")
# print("a = " , end = "")
# a = int(input())
# print("b = " , end = "")
# b = int(input())
# if a < b:
#     for i in range(a , b):
#         print(i)
# if b < a:
#     for i in range(a , b - 1 , -1):
#         print(i)
# # Даны два целых числа A и В. 
# # Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.   

# print(" ")
# print("3-esep")
# print(" ")
# print("a = " , end = "")
# a = int(input())
# print("b = " , end = "")
# b = int(input())
# for i in range(a -1 , b , -2):
#     print(i)

# # Даны два целых числа A и В, A>B. 
# # Выведите все нечётные числа от A до B включительно, в порядке убывания. В этой задаче можно обойтись без инструкции if.     

import random

print(" ")
print("4-esep")
print(" ")
print("a = " , end = "")
a = int(input())
print("b = " , end = "")
b = int(input())
number = random.randint(a , b)
for i in range(a , b + 1):
   if number == i: 
    print(i)





# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
# Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). Программа должна вывести номер потерянной карточки.
# Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.
