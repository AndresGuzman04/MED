class ValidadorContraseña:
    def validar(self, contraseña, longitud_minima=8):
        try:
            if len(contraseña) >= longitud_minima:
                return "La contraseña es válida."
            else:
                return f"Error: La contraseña debe tener al menos {longitud_minima} caracteres."
        except Exception as e:
            return f"Error: {str(e)}"


validador_contraseña = ValidadorContraseña()
resultado = validador_contraseña.validar("abc12345")
print(resultado)
