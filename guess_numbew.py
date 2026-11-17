from random import randint
print("---УГАДАЙКА---")
print()
a=str(randint(1,100))
b=input("Введите число от 1 до 100: ")
while a!=b:
    if b>a: print(f"Меньше, чем {b}")
    elif a>b: print(f"Больше, чем {b}")
    b=input("Введите число от 1 до 100: ")

print(f"Угадал! Это {a}")