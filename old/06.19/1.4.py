#Условия задания:

#На вход программе подаётся два натуральных числа n и m, каждое на
#отдельной строке. Напишите программу, которая печатает прямоугольник из
#символов ‘*’ размерами n×m.


#Алгоритм:

int_input1 = int(input('Введите первое целое число >'))
int_input2 = int(input('Введите второе целое число >'))

for i in range(int_input1):
    for j in range(int_input2):
        print('*', end = '')
    print()