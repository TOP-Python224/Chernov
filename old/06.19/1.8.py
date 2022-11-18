#Условия задания:

#Напишите программу, которая считывает натуральное число n и выводит
#первые n чисел последовательности Фибоначчи.
#Последовательность Фибоначчи – это последовательность натуральных
#чисел, которая начинается с двух единиц, а каждое последующие число
#является суммой двух предыдущих: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …


#Алгоритм:


int_input = int(input('Введите количество чисел последовательности Фибоначчи >'))
fib1 = 1
fib2 = 1
fib_current = 0
for i in range(int_input):
     if i == 0:
          print(fib1, end = ' ')
     else:
          fib_current += fib1
          print(fib_current, end = ' ')
          fib1 = fib2
          fib2 = fib_current
print()