import random

raqib = ['Qaychi', 'Qogoz', 'Tosh']

tanla = input("Tanlang (Qaychi, Qogoz, Tosh): ").title()
randomm = random.choice(raqib)

print(f"Raqib {randomm} ni tanladi.")

if tanla == randomm:
    print("Durrang!")
elif tanla == 'qogoz' and randomm == 'qaychi':
    print("Siz yutqazdingiz 😢")
elif tanla == 'tosh' and randomm == 'qogoz':
    print("Siz yutqazdingiz 😢")
elif tanla == 'qaychi' and randomm == 'tosh':
    print("Siz yutqazdingiz 😢")
else:
    print("Siz yutdingiz! 🎉")
