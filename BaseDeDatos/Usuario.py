class Usuario():
    def __init__(self):
        self.correo = []
        self.tipo = []
        self.contra = []
        self.nombre = []
        self.apellido = []
        self.telefono = []
        self.imagen = []
    
    def Correo_setter(self,correo,existe):
        if existe != 'No existe':
            self.correo[existe] = correo
        else:
            self.correo.append(correo)
    def Contra_setter(self,contra,existe):
        if existe != 'No existe':
            self.contra[existe] = contra
        else:
            self.contra.append(contra)
    def Tipo_setter(self,tipo,existe):
        if existe != 'No existe':
            self.tipo[existe] = tipo
        else:
            self.tipo.append(tipo)
    def Nombre_setter(self,nombre,existe):
        if existe != 'No existe':
            self.nombre[existe] = nombre
        else:
            self.nombre.append(nombre)
    def Apellido_setter(self,apellido,existe):
        if existe != 'No existe':
            self.apellido[existe] = apellido
        else:
            self.apellido.append(apellido)
    def Telefono_setter(self,telefono,existe):
        if existe != 'No existe':
            self.telefono[existe] = telefono
        else:
            self.telefono.append(telefono)
    def Imagen_setter(self,imagen,existe):
        if existe != 'No existe':
            self.imagen[existe] = imagen
        else:
            self.imagen.append(imagen)

    def Correo_get(self,i):
        return self.correo[i]
    def Contra_get(self,i):
        return self.contra[i]
    def Tipo_get(self,i):
        return self.tipo[i]
    def Nombre_get(self,i):
        return self.nombre[i]
    def Apellido_get(self,i):
        return self.apellido[i]
    def Telefono_get(self,i):
        return self.telefono[i]
    def Imagen_get(self,i):
        return self.imagen[i]
   