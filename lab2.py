data = [1, 3, 2, 17, 20, 6, 7, 22, 99, 10, 'c', 'b', 'a', 'd', 'e', 'g', 'f', 'z', 'h', 'i']
#10 елементів типу данних інт, та 10 елементів типу стр
ints = sorted(x for x in data if type(x) is int)#list comprehension
#сортуємо елементи типу інт
strs = sorted(x for x in data if type(x) is str) #list comprehension
#сортуємо елементи типу стр
list = ints + strs
even_numbers = [x for x in ints if x % 2 == 0]#list comprehension
caps = [x.upper() for x in strs]#list comprehension
print('Відсортований список : ',list)
print('Парні числа: ', even_numbers)
print('Капсом: ', caps)