print("hello world")

x1 = int(input("First number: "))
x2 = int(input("Second number: "))

def func(x1, x2):
    if x1 < 0 or x2 < 0:
        raise Exception("Введіть додатнє число")
    if x1 % x2 == 0:
        res = bool(1)
        print(res)
    else:
        res = bool(0)
        print(res)
    if x2 <= x1:
        print("NoSimpleDigits")
    for i in range(x1, x2 + 1):
        print(i)
func(x1, x2)

old_list = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]
new_list = []

def fun2(temp_list):
    for i in temp_list:
        if type(i) == tuple:
            fun2(i)
        if type(i) == list:
            fun2(i)
        else:
            new_list.append(i)

fun2(old_list)
print(new_list)
