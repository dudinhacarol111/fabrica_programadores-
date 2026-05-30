# autor :duda querida
# projeto : loop FOR

numero = int (input("digite a tabuada desejada: "))
inicio = int (input (" quero iniciar a tabuada com numero: "))
fim = int (input ("quero termiunar a tabuada com o numero: "))
for i in range(inicio,fim + 1):
    print(f'{numero} x {i} = {numero * i}')