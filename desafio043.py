# Desenvolva uma lógica que leia o peso e a altura de uma pessoa 
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# -Abaixo de 18.5: Abaixo do peso.
# -Entre 18.5 e 25: Peso ideal.
# - 25 até 30: Sobrepeso.
# - 30 até 40: Obesidade.
# - Acima de 40: Obesidade móbida.

peso = float(input("Digite o seu peso : "))
altura = float(input("Digite a sua altura : "))

imc = peso / (altura * altura)

if imc < 18.5 :
    print("O seu IMC :{:.1f} \nSeu peso esta ABAIXO do peso ".format(imc))
elif imc >= 18.5 and imc <= 25:
    print("O seu IMC :{:.1f} \nEsta IDEAL".format(imc)) 
elif imc <= 30 :
    print("O Seu IMC :{:.1f} \nSeu peso esta SOBREPESO".format(imc))
elif imc <=40 :
    print("O Seu IMC :{:.1f} \n Voce esta com OBESIDADE".format(imc)) 
else:
    print("ATENÇÃO: O Seu IMC :{:.1f} Voce esta com OBESIDADE MÓBIDA".format(imc))


