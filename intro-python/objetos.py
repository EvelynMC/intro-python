# Definición de Clases

class Usuario:           # Primera letra siempre en mayúscula
  def __init__(self, nombre, apellido):           # SE EJECUTA SIEMPRE cuando se crean instancias de clases
    self.nombre = nombre                          
    self.apellido = apellido

usuario = Usuario('Felipe', 'Feliz')     # Instancias en minúsculas     
usuario2 = Usuario('Chancito', 'Feliz')

print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)