my_f = open('test.txt', 'w')
input = input('Введите текст \n')
while line:
    my_f.writelines(line)
    input = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = my_f('test.txt', 'r')
my_f = my_f.readlines()
print(content)
my_f.close()