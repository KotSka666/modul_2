first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
if first % 2 == 0 and second % 2 == 0 and third % 2 == 0:
    if first == second and third == first:
        print('Все 3 числа равны')
    elif first == second or second == third or third == first:
        print('2 числа равны между сабой')
    else:
        print('0 чисел равны между сабой')
else:
    print('Одно из чисел не целостное!')