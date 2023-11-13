numbers=[1,2,3,4,5,6,7,8,9,10]
suma_parnih = sum(num for num in numbers if num % 2 == 0)
print(suma_parnih)

elements = ('jabuka', 'banana', 10, 'čeri', 20.5)

for element in elements:
    if not isinstance(element, str):
        print("Prvi element koji nije string je:", element)
        break

fruits = {'jabuka', 'banana', 'čeri'}
element = 'banana'
if element in fruits:
    print(f"Element '{element}' je pronađen.")
else:
    print(f"Element '{element}' nije pronađen.")

osoba = {'ime': 'Marko', 'prezime': 'Ilić', 'grad': 'Beograd'}
for ključ in osoba:
    if osoba[ključ][0].isupper():
        print(ključ)
#lambda
kvadrat=lambda x:x**2
broj=5
rezultat=kvadrat(broj)
print(rezultat)

zadnjeSlovo = lambda s: s[-1]
string = "Python"
rezultat = zadnjeSlovo(string)
print(rezultat)

jeParan=lambda x:x%2==0
n=4
rez=jeParan(n)
print(rez)

veciOd=lambda x,y: x if x > y else y
m=5
v=4
rez1=veciOd(m,v)
print(rez1)

lista=[1,2,3,4,5]
suma=lambda lista:sum(lista)
rez2=suma(lista)
print(rez2)