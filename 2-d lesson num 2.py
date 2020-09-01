my_len = int(input('Введите длину списка'))
my_list = []

for i in range(my_len):
    my_list.append(input('Значения для списка'))
for i in range(my_len//2):
    my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
    i+=2
print(my_list)