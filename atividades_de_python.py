import math


""" 
        atividade 1
Faça um Programa que mostre a mensagem "Alo mundo" na tela."""

# print ("Alo mundo")



"""
    atividade 2c
Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
""" 

# numero = input("digite um numero:")
# print (f"o numero pensado foi {numero}")




""" 

    Atividade 3
Faça um Programa que peça dois números e imprima a soma.
"""
# numero1 = input('digite um numero: ') 
# numero2 = input('digite mais um numero: ')
# print(f"a soma dos numero é: {int(numero1) + int(numero2)}")




"""
    atividade 4
Faça um Programa que peça as 4 notas bimestrais e mostre a média.

"""

# num_materias = int(input("Digite o número de matérias: "))
# notas = [int(input(f"Digite a nota da matéria {i + 1}: ")) for i in range(num_materias)]


# #SUM faz a soma dos numeros automaticamente
# print(f"Sua média é: {sum(notas) / num_materias}")




"""
    Atividade 5
Faça um Programa que converta metros para centímetros.

"""
# metros = int(input("Digite o número em metros e ele será convertido para cm: "))
# print(f"Seu número em centímetros fica: {metros * 100} cm")

"""
    Atividade 6
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""

# raio = float(input("Digite o raio do círculo: "))
# print(f"A área do círculo com raio {raio} é: {math.pi * raio**2:.2f}")

"""
    Atividade 7
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

# quadrado = int(input("digite o tamanho do quadradro de uma aresta de um quadradro e mostrarei o area dele e a area dele duplicada "))
# print(f"a area de seu dradrado é {quadrado * 4} e sua area duplicada é {quadrado * 8}")


"""
    atividade 8
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
"""salario_hora = int(input('digite quanto ganha por hora em seu trabalho: '))
numero_de_horas_no_mes = int(input("digite a quantidade de horas que você trabalha no mês: "))
print(f" o seu salario mensal é {salario_hora * numero_de_horas_no_mes * 30}")"""

"""
    atividade 9    
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$


- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). """


def obter_senha_com_tamanho_requisitado(tamanho_requisitado):
    while True:
        senha = input(f"Por favor, digite uma senha que tenha {tamanho_requisitado} caracteres: ")
        if len(senha) == tamanho_requisitado:
            return senha
        print(f"A senha deve ter exatamente {tamanho_requisitado} caracteres. Tente novamente.")


def obter_senha_com_tamanho_requisitado()