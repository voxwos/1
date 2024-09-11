class Error(Exception):
    pass

def main(input_: str):
    try:
        a = input_.split()
        a[0], a[2] = int(a[0]), int(a[2])
        if len(a) != 3:
            raise Error("Формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")
        if a[0] in range(1, 11) and a[2] in range(1, 11):
            if a[1] == "+":
                print(str(a[0] + a[2]))
            elif a[1] == "-":
                print(str(a[0] - a[2]))
            elif a[1] == "*":
                print(str(a[0] * a[2]))
            elif a[1] == "/":
                print(str(a[0] // a[2]))
            else:
                raise Error("Неверная операция")
        else:
            raise Error("Неверный формат данных")
    except ValueError:
        print("Неверный формат данных")
    except IndexError:
        print("Неверный формат данных")
    except Error as e:
        print(e)

while True:
    main(input())

