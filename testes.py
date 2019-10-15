from banco import Cliente

#cliente1 = Cliente('Luciano Gomes', 6548648, 'luciano@email.com')

email = 'example@example.com'

#print(email[15:19])


cont_chars = len(email)
cont_ate_ponto = cont_chars - 4
cont_arroba = 0
for char in email:
    if char == '@':
        cont_arroba += 1
    elif cont_arroba > 1:
        raise ValueError("email inválido")
if email[cont_ate_ponto:cont_chars] == '.com':
    print('ok')
else:
    raise ValueError("email inválido")
    
