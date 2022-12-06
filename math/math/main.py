def start():
    print ('What result of calc?')
    from random import randint
    chislo1 = randint(0, 100)
    chislo2 = randint(0, 100)
    from random import choice
    elements = '+-'
    char = choice(elements)
    primerchik = chislo1 * choice(elements) * chislo2

