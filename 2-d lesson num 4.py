my_str = input('Введите строку: ')
word = []
for i in range(my_str.count(' ') + 1):
    word = my_str.split()
    if len(str(word)) <= 10:
        print(i + 1, word[i])
    else:
        print(i + 1, word[i][:10])