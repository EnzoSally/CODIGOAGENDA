contato = {
    'Enzo' : '+5554993202527',
    'Maria' : 'xxx'
}

# Adicionando novo elemento
contato['Pedro'] = "+555498888888"
#alterar numero
contato['Enzo'] = "+55549484000"

#print(contato.pop('Maria', "Contato nao encontrado!"))

#print(contato.get("Pedra", "contato nao encontrado"))

print("Enzo" in contato)

for key,value in contato.items():
    print(key,value)