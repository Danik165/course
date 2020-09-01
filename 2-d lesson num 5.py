my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг - {my_list}')
rating = int(input('Введите число, для завершения нажмите 0: '))
while rating != 0:
    for i in range(len(my_list)):
        if my_list[i] == rating:
            my_list.insert(i + 1, rating)
            break
        elif my_list[0] < rating:
            my_list.insert(0, rating)
            break
        elif my_list[-1] > rating:
            my_list.append(rating)
            break
        elif my_list[i] > rating > my_list[i + 1]:
            my_list.insert(i + 1, rating)
            break
    print(f"текущий список - {my_list}")
    rating = int(input("Введите число "))
