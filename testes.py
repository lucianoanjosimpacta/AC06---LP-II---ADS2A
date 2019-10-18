from banco import Cliente, Banco


cliente1 = Cliente('Luciano Gomes', 6548648, 'luciano@email.com')

cliente2 = Cliente('Gabriel Gonçalves', 54654684, 'gabriel@email.com')


banco_new = Banco('Banco Novo')

banco_new.abre_conta('Luciano Gomes', 100)
banco_new.abre_conta('Gabriel Gonçalves', 100)
