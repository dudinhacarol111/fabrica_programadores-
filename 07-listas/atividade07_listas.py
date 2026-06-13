# autor : duda cuti cuti
# projetos : listas

penta = ['brasil', 'paraguay','chile']
tetra = ['brasil','italia','alemanha']
#        0            1          2          3
tri = ['brasil' , 'italia', 'alemanha', 'argentina']

# imprimindo os nomes
print ('---campeoes do mundo---')

# excluindo por posição 
# exemplo: excluir o chile
print (penta)
del penta [2]
print (penta)

# excluindo por nome
print(penta)
penta.remove ('paraguay')
print (penta)