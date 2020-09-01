season_list = ['winter', 'spring', 'summer', 'autumn']
month = int(input('Введите номер месяца: '))
season_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if (month == 12) or (1 <= month <= 2):
    print(season_dict.get(1))
    print(season_list[0])
elif 3 <= month <= 5:
    print(season_dict.get(2))
    print(season_list[1])
elif 6 <= month <= 8:
    print(season_dict.get(3))
    print(season_list[2])
elif 9 <= month <= 11:
    print(season_dict.get(4))
    print(season_list[3])
else:
    print('Что-то пошло не так')
