#Task2. Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення
x = [(10, 20, 30), (30, 40, 50, 60), (60, 70, 80, 90, 99)]
print (x)
num = int(input("The value to which the last element of the tuple is replaced: "))
print([x[:-1] + (num,) for x in x])