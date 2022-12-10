import cv2 as cv
capturaVideo=cv.VideoCapture(0) #0 para conectadas directo y 1 para remotas
if not capturaVideo.isOpened():
    print("No se encontro dispositivo de salida")
    exit()
else:
    while True:
        _,frame=capturaVideo.read() #Retorna tipo de camara, y video
        cv.imshow("En vivo",frame)
        if cv.waitKey(1)==ord("s"): #Salida codigo por medio de comparacion
            break
    capturaVideo.release()
    cv.destroyAllWindows()
