# autor: dudinha
# projeto: coondicionais

# definição das variáveis 
nome = input ("digite seu nome :")
primeira_nota= float (input("digite sua nota: "))
segunda_nota= float (input("digite sua nota: "))
media=(primeira_nota+segunda_nota)/2
if media >=6:
    print(f"(nome) sua nota é (media) - aluno aprovado !")
else:
    print(f"aluno reprovado")