def month_to_season(month_num):
    if 1 <= month_num <= 12:
        if month_num in [12, 1, 2]:
            print(f'{month_num} месяц это - Зима')
        if month_num in [3, 4, 5]:
            print(f'{month_num} месяц это - Весна')
        if month_num in [6, 7, 8]:
            print(f'{month_num} месяц это - Лето')
        if month_num in [9, 10, 11]:
            print(f'{month_num} месяц это - Осень')  
    else:
        print(f'Ошибка. {month_num} - неправильный номер месяца.')             

month_to_season(0)
month_to_season(1)
month_to_season(5)
month_to_season(12)
month_to_season(24)
