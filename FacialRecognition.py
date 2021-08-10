import cv2

#Hacemos referencia al archivo que se descargo el cual es haarcascade_frontalface_default.xml
#No hace falta que se agreguen mas especificaciones al directorio porque se guardó al mismo nivel
#que este archivo
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)  #Probar cambiando el parametro 0 por 1

#Se crea un ciclo infinito para leer los fotogramas de la camara
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #Convertimos esos fotogramas a un tono grisaseo para que OpenCV los pueda detectar más facilmente, sino lo convertimos a la escala de grises puede fallar
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)     #Almacenamos las caras que detecta, si hubiera error checar documentación de la función para cambiar paremtros

    #Con este ciclo solo dibujamos los rectangulos o cuadrados 
    #X Y W H son los vertices de la figura
    #(255, 0, 0) el color del rectangulo
    #2 este es el grosor de la linea de la figura 
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    #Aqui mostramos el fotograma ya modificado
    cv2.imshow('img', img )

    #Se verifica si se está presionando la tecla ESC para terminar el programa
    k= cv2.waitKey(30)

    if k == 27:     #27 es ESCAPE en ASCI
        break

cap.release()