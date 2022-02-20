nome = str(input('Qual o seu nome ? :'))
altura = float(input('Qual a sua altura ? (M):'))
peso = float(input('Qual é o seu peso ? (KG):'))

imc = peso / (altura/100)**2

print(imc)

if imc < 18.5:
    print(f'{nome},seu IMC é de: {imc}, e é classifiacos como magreza')

elif imc >=18.5 and imc <24.9:
    print(f'{nome},seu IMC é de: {imc}, e é classifiacos como normal')

elif imc >=25 and imc <29.9:
    print(f'{nome},seu IMC é de: {imc}, e é classifiacos como sobrepeso')

elif imc >=30 and imc<39.9:
    print(f'{nome},seu IMC é de: {imc}, e é classifiacos como obesidade')

elif imc >= 40:
    print(f'{nome},seu IMC é de: {imc}, e é classifiacos como obesidade grave')