from banco import Cliente
import re

#cliente1 = Cliente('Luciano Gomes', 6548648, 'luciano@email.com')

email = 'examplo@example.com'

#print(email[15:19])


#cont_chars = len(email)
#cont_ate_ponto = cont_chars - 4
#cont_arroba = 0
#for char in email:
#    if char == '@':
#        cont_arroba += 1
#    elif cont_arroba > 1:
#        raise ValueError("email inválido")
#if '' in email:
#    raise ValueError("email inválido")
#elif email[cont_ate_ponto:cont_chars] == '.com':
#    print('ok')
#else:
#    raise ValueError("email inválido")


email_valid = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")

if not email_valid.match(email):
    raise ValueError("email inválido")
else:
    print("ok")