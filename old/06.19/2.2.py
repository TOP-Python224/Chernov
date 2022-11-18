#Условия задания:

#В прошлом веке для отправки коротких текстовых сообщений люди
#использовали телеграммы. Стоимость отправки телеграммы зависела от длины
#сообщения. Напишите программу, которая помогает подсчитать стоимость
#отправки телеграммы, если принять, что стоимость одного символа буквы или
#цифры – восемьдесят копеек.
#На вход программа принимает строку текста. Программа должна вывести
#стоимость в рублях и копейках в том же формате, что и в примере.
#Подсказка: для вывода используйте f-строку.

#Алгоритм:

result = 0
str_input = input('Введите текст сообщения >')
for i in range(len(str_input)):
    if str_input[i] != ' ' : result += 1

print(f'Стоимость отправки {(result * 80) // 100} руб. {(result * 80) % 100} коп.')