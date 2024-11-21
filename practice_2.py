'''
Создадим переменные с единицами, десятками и окончанием "надцать"
'''
end = 'надцать'
first = ', один, два, три, четыре, пять, шесть, семь, восемь, девять'
tens = 'двадцать тридцать сорок пятьдесят шестьдесят семьдесят восемьдесят девяносто'

'''
Создаём списки, с которыми будем работать
'''
list_one = first.split(',')
list_two = tens.split()
list_three = []
for digits in list_two:
    for numbers in list_one:
        list_three.append(digits + ' ' + numbers)
top_10 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
top_20 = ['один'+end, 'две'+end,'три'+end,'четыр'+end, 'пят'+end, 'шест'+end, 'сем'+end, 'восем'+end, 'девят'+end]
operations = ['минус', 'плюс', 'умножить', 'открывается', 'закрывается']
operators = ['-', '+', '*', '(', ')']
user_list = top_10 + top_20 + list_three
list_hundred = [str(number) for number in range(1,100)]

'''
Создаём словари и объединяем их в один
'''
dct_for_numbers = {value: number for (value, number) in zip(user_list, list_hundred)}
dct_for_operators = {value: number for (value, number) in zip(operations, operators)}
dct_full = {}
dct_full.update(dct_for_numbers)
dct_full.update(dct_for_operators)

'''
Ход работы калькулятора
'''
def calc(user_input):
    if 'умножить на' in user_input or 'скобка открывается' in user_input or 'скобка закрывается' in user_input:
        user_input = user_input.replace('умножить на', 'умножить')
        user_input = user_input.replace('скобка закрывается', 'закрывается')
        user_input = user_input.replace('скобка открывается', 'открывается')
    final = user_input.split()
    smth = ''
    for word in final:
        smth+=dct_full[word]
    numeric_answer = str(eval(smth))
    return {key for key in dct_full if dct_full[key]==numeric_answer}

'''
Выводим результат функции после пользовательского ввода
'''
print(*calc(input('Write your calculation:\n')))
