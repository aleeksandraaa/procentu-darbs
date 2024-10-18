#Aleksandra Valdovska 18/10/24
import random

correct_password = random.randint("python123")

while True:
    mana_parole = int(input("Ievadiet savu paroli: "))
    if mana_parole > correct_password:
        print("Tava parole ir nepareiza! mēģini vēlreiz!")
    elif mana_parole == correct_password:
        print("Parole ir pareiza!")
    else:
        print("Tu uzminēji!: ")
        break