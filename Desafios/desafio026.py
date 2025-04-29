frase = str(input('Digite uma frase: ')).upper()
fraseclean = frase.strip()
acount = fraseclean.count('A')
aprim = fraseclean.find('A')+1
ault = fraseclean.rfind('A')+1
print(acount)
print(aprim)
print(ault)
