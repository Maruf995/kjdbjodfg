
username = input("Введите свой ник: ")

name = input("Введите свое имя: ")
surname = input("Введите свою фамилию: ")

while True:
    gmail = input("Введите свой gmail: ")
    if gmail[-10:] != "@gmail.com":
        print("Почта должна содержать @gmail.com!")
    else:
        break

phone = input("Введите свой номер: ")
while True:
    age = 2022 - int(input("Введите год вашего рождения: "))
    if age < 18:
        print("Доступ запрещен!")
    else:
        break

while True:
    password1 = input("Введите пароль: ")
    password2 = input("Повторите пароль: ")
    if password1 != password2:
        print("Пароли не совпадают!")
    else:
        break

user = dict(
    username=username,
    name=name,
    surname=surname,
    gmail=gmail,
    age=age,
    phone=phone,
    password=password1
)

print(user)

while True:
    username = input("Введите свой ник: ")
    password = input("Введите пароль: ")
    if username != user["username"] or password1 != user["password"]:
        print("Неверный логин или пароль!")
    else:
        print("Успешная авторизация <3")
        break
