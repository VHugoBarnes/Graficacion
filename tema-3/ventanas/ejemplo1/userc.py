# Programa escrito por Alfredo Santos y Cynthia Barron
class usuario_validar():
    errors = []

    def longitud(self, usercomp):
        if len(usercomp) < 6:
            self.errors.append('El nombre de usuario debe contener al menos 6 caracteres')
            return False

        elif len(usercomp) > 12:
            self.errors.append('El nombre de usuario debe contener maximo 12 caracteres')
            return False

        else:
            return True

    def alfanumerico(self, usercomp):
        if usercomp.isalnum() == False:
            self.errors.append('El nombre de usuario puede contener solo letras y numeros')
            return False
        else:
            return True

    def validar_usuario(self, usercomp):
        valido = self.longitud(usercomp) and self.alfanumerico(usercomp)
        return valido