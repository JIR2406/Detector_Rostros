import cv2 as cv
import numpy as np
vGauss=1
vKermel=3
path=r'C:\Users\jairg\PycharmProjects\VisionArtificial\venv\contorno\monedas.jpg';
original=cv.imread(path)
gris=cv.cvtColor(original,cv.COLOR_BGR2GRAY)
gauss=cv.GaussianBlur(gris,(vGauss,vGauss),0)
canny=cv.Canny(gauss,60,100)
cv.imshow("Original2",original)
kernel=np.ones((vKermel,vKermel),np.uint8) #Modelado e importante trabajar con 8 bits
cierre=cv.morphologyEx(canny,cv.MORPH_CLOSE,kernel)#Tomamos y convertimos en colores fuertes
contornos,jerarquia=cv.findContours(cierre.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
print("monedas encontradas: {}".format(len(contornos)))
cv.drawContours(original,contornos,-1,(0,0,255))
#Mostrar resultados¿
cv.imshow("gauss",gauss)
cv.imshow("canny",canny)
cv.imshow("Cierre",cierre)
cv.imshow("Original",original)
cv.waitKey(0)