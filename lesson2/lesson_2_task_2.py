def is_year_leap():
    yearInput = int(input("Введите год: "))
    result = False
    if (yearInput % 4 == 0):
        result = True
        #print(f'{yearInput} - Високосный год')
    else :
        result = False
        # print(f'{yearInput} -  Не високосный год')
    print(f'год {yearInput}: {result}')
is_year_leap()
