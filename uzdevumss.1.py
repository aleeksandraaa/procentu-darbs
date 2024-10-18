#Aleksandra Valdovska 18/10/24
#Vecums zem 13 bērns, virs tu esi tīnis , 20 un augstāk pieaugušais

vecums = input(input("Ievadiet savu vecumu!: "))
if vecums < 13:
    print("Tu esi bērns!")
elif 13 <= vecums <= 19:
    print("Tu esi tīnis!")
else:
    print("Tu esi pieaugušais!")
    