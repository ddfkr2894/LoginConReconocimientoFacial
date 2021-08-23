from tkinter import *   # Para realizar la interfaz grafica
import os               # Manejo de archivos
import cv2              # Manejo y aprovechamiento de imagenes
from matplotlib import pyplot   
from mtcnn.mtcnn import MTCNN   # Detector de rostro o red neuronal convolusional
import numpy as np      # Operaciones con matrices

# Lo primero que hacemos es crear una función para la pantalla principal
def pantalla_principal():
    global pantalla     #Globalizamos la variable para usarla en otras funciones
    pantalla = Tk()
    pantalla.geometry("400x300")    # Asignamos el tamaño de la ventana
    pantalla.title("Log-In With Facial Recognition Algorithm")  #Nombre de la ventana
    #Caracteristicas de la ventana
    Label(text="Login con Reconocimiento Facial", bg="gray", width="300", height="2", font=("Verdana", 13)).pack()
    # Creamos los botones
    Label(text = "").pack() # Esto es el espacio entre el titulo y el primer boton
    Button(text = "Iniciar Sesión", height = "2", width = "30", command = login).pack()
    Label(text = "").pack() # Esto es el espacio entre el primer boton y el segundo boton
    Button(text = "Registrar Nuevo Usuario", height = "2", width = "30", command = registro).pack()
    pantalla.mainloop()

# Funcion paraa asignar al boton registro
def registro():
    global usuario
    global contra 
    global usuario_entrada
    global contra_entrada
    global pantalla1
    
    pantalla1 = Toplevel(pantalla)  # Esta pantalla es de un nivel superiro a la principal
    pantalla1.title("Registro")
    pantalla1.geometry("300x250")   # Asignamos el tamaño de la ventana
    
    # Se crean las entradas
    usuario = StringVar()
    contra = StringVar()

    Label(pantalla1, text = "Registro facial: debe asignar usuario:").pack()
    # Label(pantalla1, text="").pack()    # Para dejar espacio
    Label(pantalla1, text = "Registro normal: debe asignar usuario y contraseña:").pack()
    Label(pantalla1, text="").pack()    # Para dejar espacio
    Label(pantalla1, text="Usuario *").pack()   #Mostramos en la pantalla 1 el usuario
    usuario_entrada = Entry(pantalla1, textvariable=usuario)    #Creamos un text variable para que el usuario ingrese la info
    usuario_entrada.pack()
    Label(pantalla1, text="Contraseña *").pack()    #Mostramos en la pantalla la contraseña
    contra_entrada = Entry(pantalla1, textvariable=contra)  #Creamos un text variable para que el usuario ingrese la contra
    contra_entrada.pack()
    Label(pantalla1, text="").pack()  #Djeamos un espacio para la creacion del boton
    Button(pantalla1, text ="Registro Normal", width=15, height=1, command=registrar_usuario).pack()
    # Y creamos otro botón para el registro facial
    Label(pantalla1, text="").pack()
    Button(pantalla1, text ="Registro Facial", width=15, height=1, command=registro_facial).pack()
    
def registrar_usuario():
    usuario_info = usuario.get() #Obtenemos la información almacenada del usuario
    contra_info = contra.get() #Obtenemos la información almacenada en contra

    archivo = open(usuario_info, "w")   #Abriremos la información en modo de escritura
    archivo.write(usuario_info + "\n")  #Escribimos la información
    archivo.write(contra_info)
    archivo.close()

    #Limpiamos los text variables
    usuario_entrada.delete(0, END)
    contra_entrada.delete(0, END)

    #Ahora le diremos al usuario que su registro ha sido exitoso
    Label(pantalla1, text="Registro Cnvencional Exitoso", fg="green", font=("Calibri", 11)).pack()

# Vamos a capturar el rostro
def registro_facial():
    cap = cv2.VideoCapture(0)   # Elegimos la camara con la que vamos a hacer la detección
    
    while(True):
        ret, frame = cap.read()     #Leemos el vídeo
        cv2.imshow('Registro Facial', frame)    #Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:    #Cuando oprimimos Escape rome el vídeo
            break
    
    usuario_img = usuario.get()
    cv2.imwrite(usuario_img+".jpg",frame)   # Guardamos la ultima captura del video como imagen y asignamos el nombre del usuario
    cap.release()       # Cerramos
    cv2.destroyAllWindows()
    
    usuario_entrada.delete(0, END)  #Limpiamos los text variables
    contra_entrada.delete(0, END)
    
    Label(pantalla1, text="Registro Facial Exitoso", fg= "green", font=("Calibri",11)).pack()
    
# Detectamos el rostro y exportamos los pixeles
    def reg_rostro(img, lista_resultados):

        data = pyplot.imread(img)

        for i in range(len(lista_resultados)):
            x1, y1, ancho, alto = lista_resultados[i]['box']
            x2, y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i+1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg,(150,200), interpolation=cv2.INTER_CUBIC)  #Guardamos la imagen con un tamaño de 150x200
            cv2.imwrite(usuario_img+".jpg",cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    img= usuario_img+".jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    reg_rostro(img, caras)

def login():
    global pantalla2
    global verificacion_usuario
    global verificacion_contra
    global usuario_entrada2
    global contra_entrada2

    pantalla2 = Toplevel(pantalla)
    pantalla2.title("Login")
    pantalla2.geometry("300x250")   #Creamos la ventana
    Label(pantalla2, text="Login facial: Debe de asignar un usuario:").pack()
    Label(pantalla2, text="Login normal: Debe de asignar un usuario y una contraseña:").pack()
    Label(pantalla2, text="").pack()    #Dejamos un espacio
    
    verificacion_usuario = StringVar()
    verificacion_contra = StringVar()
    
    # Ingresamos los datos
    Label(pantalla2, text="Usuario *").pack()
    usuario_entrada2 = Entry(pantalla2, textvariable = verificacion_usuario)
    usuario_entrada2.pack()
    Label(pantalla2, text="Contraseña * ").pack()
    contra_entrada2 = Entry(pantalla2, textvariable = verificacion_contra)
    contra_entrada2.pack()
    Label(pantalla2, text="").pack()
    Button(pantalla2, text="Inicio de Sesion Normal", width=20, height=1,command=verificacion_login).pack()
    #Boton para login facial
    Label(pantalla2, text="").pack()
    Button(pantalla2, text="Inicio de Sesion Facial", width=20, height=1,command=login_facial).pack()

def verificacion_login():
    log_usuario = verificacion_usuario.get()
    log_contra = verificacion_contra.get()

    usuario_entrada2.delete(0, END)
    contra_entrada2.delete(0, END)

    lista_archivos = os.listdir()   #Vamos a importar la lista de archivos con la libreria os
    if log_usuario in lista_archivos:   #Comparamos los archivos con los que nos interesa
        archivo2 = open(log_usuario, "r")   #Abrimos el archivo en modo lectura
        verificacion = archivo2.read().splitlines() #llera las lineas dentro del archivo ignorando el resto
        if log_contra in verificacion:
            print("Inicio de Sesion Exitoso")
            Label(pantalla2, text="Inicio de Sesion Exitoso", fg = "green", font=("Calibri", 11)).pack()
        else:
            print("Contraseña incorrecta, Ingresar de nuevo")
            Label(pantalla2, text="Contraseña incorrecta", fg = "red", font=("Calibri", 11)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantalla2, text="Usuario no encontrado", fg = "red", font=("Calibri", 11)).pack()

# Funcion para el Login Facal
def login_facial():
    # Vamos a capturar el rostro
    cap = cv2.VideoCapture(0)   # Elegimos la camara con la que vamos a hacer la detección
    
    while(True):
        ret, frame = cap.read()     #Leemos el vídeo
        cv2.imshow('Login Facial', frame)    #Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:    #Cuando oprimimos Escape rome el vídeo
            break
    
    usuario_login = verificacion_usuario.get()  #Con esta variable vamos a guardar la foto pero con otro nombre para no sobreescribir
    cv2.imwrite(usuario_login+"LOG.jpg",frame)   # Guardamos la ultima captura del video como imagen y asignamos el nombre del usuario
    cap.release()       # Cerramos
    cv2.destroyAllWindows()
    
    usuario_entrada2.delete(0, END)  #Limpiamos los text variables
    contra_entrada2.delete(0, END)
    
# Funcion para guardar el rostro
    def log_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1, y1, ancho, alto = lista_resultados[i]['box']
            x2, y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i+1)
            pyplot.axis('off')
            cara_reg=data[y1:y2, x1:x2]
            cara_reg=cv2.resize(cara_reg,(150,200), interpolation=cv2.INTER_CUBIC)  #Guardamos la imagen 150x200
            cv2.imwrite(usuario_login+"LOG.jpg",cara_reg)
            return pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    # Detectamos el rostro
    img = usuario_login+"LOG.jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    log_rostro(img, caras)

# Funcion para comparar los rostros
    def orb_sim(img1, img2):
        orb = cv2.ORB_create()

        kpa, descr_a = orb.detectAndCompute(img1, None)  # Creamos descriptor 1 y extraemos puntos clave
        kpb, descr_b = orb.detectAndCompute(img2, None)  # Creamos descriptor 1 y extraemos puntos clave

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)   #Creamos comparador de fuerza

        matches = comp.match(descr_a, descr_b)  #Aplicamos el comparador a los descriptores

        regiones_similares = [i for i in matches if i.distance < 70]    #Extraemos las regiones similares con base a los puntos clave
        if len(matches) == 0:
            return 0
        return len(regiones_similares)/len(matches)    #Exportamos el porcentaje de similitud

    # Se importan las imagenes y llamaos a la función de comparación
    im_archivos = os.listdir()  # Se importa la lista de archivos con la libreria os
    if usuario_login+".jpg" in im_archivos:     # Comparamos los archivos con el que nos interesa
        rostro_reg = cv2.imread(usuario_login+".jpg",0)     #Importamos el rostro del registro
        rostro_log = cv2.imread(usuario_login+"LOG.jpg",0)     #Importamos el rostro de inicio de sesión
        similitud = orb_sim(rostro_reg, rostro_log)
        if similitud >= 0.7:
            Label(pantalla2, text="Inicio de Sesión Exitoso", fg ="green", font = ("Calibri", 11)).pack()
            print("Bienvenido al sistema usuario: ", usuario_login)
            print("Compatibilidad con la foto del registro: ", similitud)
        else:
            print("Rostro invalido, Vuelva a intentarlo: ")
            print("Compatibilidad con la foto del registro: ", similitud)
            Label(pantalla2, text= "Incompatibilidad de rostro", fg="red", font=("Calibri", 11)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantalla2, text= "Usuario no encontrado", fg="red", font=("Calibri", 11)).pack()

pantalla_principal()
