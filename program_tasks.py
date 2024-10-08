import random as rnd

def z1():
    ascii = int(input("Введите код ASCII: "))
    if (65 <= ascii <= 90) or (97 <= ascii <= 122):
        print("Это английская буква")
    else:
        print("Это иной символ")

def z2():
    num = input("Введите натуральное число: ")
    max_z2 = max(num)
    print("Наибольшая цифра: ", max_z2)

def z3():
    array = [rnd.randint(-15,14) for _  in range(20)]

    max_z3 = max(array)

    count_greater = sum(1 for x in array if abs(x) > max_z3)

    print("Сгенерированный массив:", array)
    print("Максимальный элемент:", max_z3)
    print("Количество элементов по модулю, больших максимального:", count_greater)

def z4():
    def count_digits(number):
        return len(str(abs(number)))

    num = int(input("Введите целое число: "))

    digits_count = count_digits(num)
    print("Количество разрядов в числе: ", digits_count)

def z5():
    def main():
        total_sum = 0

        while True:
            user_input = input("Введите число (или 'Enter' для завершения): ")

            if user_input == "":
                break

            try:
                number = float(user_input)
                total_sum += number
            except ValueError:
                print("Пожалуйста, введите корректное число.")

        print("Сумма введенных чисел:", total_sum)

    main()

while True:
    choose = input("Введите номер задания (или 'exit' для выхода): ")
    
    if choose == "1":
        z1()
    elif choose == "2":
        z2()
    elif choose == "3":
        z3()
    elif choose == "4":
        z4()
    elif choose == "5":
        z5()
    elif choose.lower() == 'exit' or 'ex':
        print("Выход из программы.")
        break
    else:
        print("Неверный ввод, попробуйте снова.")