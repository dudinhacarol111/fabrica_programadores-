# autor :dudinha
# projeto: IMC com input e f-string

# declaração de variaveis 
nome = input ("digite seu nome: ")
peso = float(input("digite o seu peso valor: "))
altura = float(input("digite sua altura : "))
imc = peso / (altura * altura)

# exibindo os resultados
print (nome)
print (f"o resultado do imc é:{imc:.2f}")