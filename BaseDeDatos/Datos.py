from BaseDeDatos.Usuario import Usuario

def Leer_Datos_Guardados():
    with open('BaseDeDatos/Cuentas.txt', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip().replace("\\r", "").replace("\n", "").replace("'", "")
            datos = linea.split(',')
            
            if len(datos) == 8:    
                correo, contra, nombre, apellido, telefono, tipo, imagen, basura = datos
                usu.Correo_setter(correo,'No existe')
                usu.Contra_setter(contra,'No existe')
                usu.Nombre_setter(nombre,'No existe')
                usu.Apellido_setter(apellido,'No existe')
                usu.Telefono_setter(telefono,'No existe')
                usu.Tipo_setter(tipo,'No existe')
                usu.Imagen_setter(imagen,'No existe')
          
def Tomar_Datos(i):
    lista = []
    lista.append(usu.Correo_get(i))
    lista.append(usu.Contra_get(i))
    lista.append(usu.Nombre_get(i))
    lista.append(usu.Apellido_get(i))
    lista.append(usu.Telefono_get(i))
    lista.append(usu.Tipo_get(i))
    lista.append(usu.Imagen_get(i))
    return lista

def Modificar_Datos(dato,i):
    usu.Correo_setter(dato[0],i)
    usu.Contra_setter(dato[1],i)
    usu.Nombre_setter(dato[2],i)
    usu.Apellido_setter(dato[3],i)
    usu.Telefono_setter(dato[4],i)
    usu.Imagen_setter(dato[5],i)
    with open('BaseDeDatos/Cuentas.txt', 'w') as archivo:
        for i in range(len(usu.correo)):
            info = Tomar_Datos(i)
            archivo.write(info[0] + ',' + info[1] + ',' +info[2] + ',' +info[3] + ',' +info[4] + ','+ info[5] + ',' +info[6] + ',' + '\n')
    archivo.close()

def Verificar_Datos(correo_ingre, contra_ingre):
    existe = False
    for i in range(len(usu.correo)):
        if usu.Correo_get(i) == correo_ingre:
            existe = True
            valor = i   #Devuelve la posicion de la persona en la lista
    if  existe == True and usu.Contra_get(valor) == contra_ingre:
        return True , valor
    else:
        print('No existe este chabon')
        return False, None
           
def Agregar_Usuario(usuario,contra,tipo,nombre, apellido,telefono):
    usu.Correo_setter(usuario,'No existe')
    usu.Contra_setter(contra,'No existe')
    usu.Correo_setter(nombre,'No existe')
    usu.Contra_setter(apellido,'No existe')
    usu.Contra_setter(telefono,'No existe')
    usu.Tipo_setter(tipo,'No existe')
    usu.Imagen_setter('Usuario_Inicial.jpg','No existe')
    nuevo_usu = usuario + ',' + contra +  ',' + nombre + ','+ apellido + ',' + telefono + ',' + str(tipo) + ',' + 'BaseDeDatos/Usuario_Inicial.jpg' + ','
    with open('BaseDeDatos/Cuentas.txt', 'a') as archivo:
        archivo.write('\n')
        archivo.write(nuevo_usu)
    archivo.close()
    Leer_Datos_Guardados()
    
usu = Usuario()
