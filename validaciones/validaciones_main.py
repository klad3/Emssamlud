class ValidacionMain:
    def validar_opcion_princ(self, opcion):
        try:
            int(opcion)
            self.opcion_valida = True
            if int(opcion) >= 1 and int(opcion) <= 6:
                return True
        except:
            return False

    def validar_opcion_admin(self, opcion):
        try:
            int(opcion)
            self.opcion_valida = True
            if int(opcion) >= 1 and int(opcion) <= 3:
                return True
        except:
            return False