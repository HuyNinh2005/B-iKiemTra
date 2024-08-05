number = input()
number1 = set(number)
for i in number1:
    cou = number.count(i)
    if cou % 5 == 0 and cou % 10 != 0:
        print(i)
