# autor : duda carol
# projeto : loop while

numero = int (input ("digite a tabuada desejada :"))
i = int (input("digite o inicio da tabuada:"))
fim = int (input("digite o fim da tabuada : "))

while i <= fim:
    print(f"{numero} x {i} = {numero * i }")
    i = i + 1