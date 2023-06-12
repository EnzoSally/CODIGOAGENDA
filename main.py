contato = {
    'Enzo' : '+5554993202527',
    'Maria' : 'xxx'
}

# Adicionando novo elemento
contato['Pedro'] = "+555498888888"
#alterar numero
contato['Enzo'] = "55549484000"
#excluir contatos

print(contato.pop('Marias', "Contato nao encontrado!"))

print(contato)