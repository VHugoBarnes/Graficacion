# encoding: UTF-8

def _notas(nota):
    if nota >= 0 and nota <= 3:
        return 'Insuficiente'
    elif nota >= 4 and nota <= 6:
        return 'Suficiente'
    elif nota >= 7 and nota <= 10:
        return 'Felicitaciones'


nota = input('Ingrese la nota: ')

print _notas(nota)