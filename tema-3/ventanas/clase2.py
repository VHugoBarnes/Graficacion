# Programa escrito por: yolyrdz.blogspot.com
class Humano:
    def __init__(self):
        self.edad = 25  # aqui le doy un atributo a mi objeto
        print 'soy un humano'

    def hablar(self, mensaje):
        print mensaje

pedro = Humano()
raul= Humano()

print 'Soy Pedro y tengo', pedro.edad
print 'Soy Raul y tengo', raul.edad

pedro.hablar('Hola')
raul.hablar('Hola Pedro')