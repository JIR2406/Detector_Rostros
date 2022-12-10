import cv2
path=r'C:\Users\jairg\PycharmProjects\VisionArtificial\venv\contorno\contorno.jpg';
imagen=cv2.imread(path) #Se crea la imagen
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,umbrall=cv2.threshold(grises,100,255,cv2.THRESH_BINARY)#Tomamos y convertimos en colores fuertes
contorno,jerarquia=cv2.findContours(umbrall,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contorno,-1,(0, 0, 255),3); 
#Mostrar
cv2.imshow("Original", imagen)  # Mostramos la imagen
cv2.imshow("Grises", grises) 
cv2.imshow("Umbrall", umbrall)  # Mostramos la imagen
cv2.waitKey(0)  # Esperamos cierto tiempo
cv2.destroyAllWindows()