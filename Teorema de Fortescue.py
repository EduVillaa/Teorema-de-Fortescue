#Teorema de Fortescue: Cualquier sistema desequilibrado puede ser representado como superposición de tres sistemas equilibrados,
#uno de secuencia directa, uno de secuencia inversa, y uno de secuencia homopolar
import matplotlib.pyplot as plt
import numpy as np
import cmath as cmath

Alpha_real=np.cos(120*np.pi/180)
Alpha_im=np.sin(120*np.pi/180)
Alpha=complex(Alpha_real, Alpha_im)

Vfase=[8+6j, 8j, -2-8j]
T=[[1, 1, 1,],
   [1, Alpha**2, Alpha],
   [1, Alpha, Alpha**2]]

Vsecuencia_fase_a=np.linalg.inv(T)@Vfase



Vsecuencias=[[Vsecuencia_fase_a[0], Vsecuencia_fase_a[1], Vsecuencia_fase_a[2]], #Secuencia homopolar (azul)
             [Vsecuencia_fase_a[0], Vsecuencia_fase_a[1]*Alpha**2, Vsecuencia_fase_a[2]*Alpha], #Secuencia directa (verde)
             [Vsecuencia_fase_a[0],Vsecuencia_fase_a[1]*Alpha, Vsecuencia_fase_a[2]*Alpha**2]] #Secuencia inversa (rojo)

Vsec=["Secuencia homopolar:", "Secuencia directa:", "Secuencia inversa:"]
fase=["A", "B", "C"]

for i in range(3):
    print("")
    print(Vsec[i])
    print("")
    for c in range(3):
        mag=abs(Vsecuencias[c][i])
        arg_grados = cmath.phase(Vsecuencias[c][i])*180/np.pi
        print("Fase", fase[c], ":", round(mag, 2),"∠",round(arg_grados, 2))
    

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color="k", lw=0.2)
plt.axvline(0, color="k", lw=0.2)
plt.grid()

colores=["blue", "green", "red", "orange", "purple", "navy"]

for i in Vsecuencias:
    xorigen=0
    yorigen=0
    c=0
    for x in i:
        r=np.real(x)
        im=np.imag(x)
        plt.quiver(xorigen, yorigen, r, im, angles="xy", scale_units="xy", scale=1, color=colores[c], width=0.004)
        xorigen+=r
        yorigen+=im
        c+=1

c=3   
for i in Vfase:
    r=np.real(i)
    im=np.imag(i)
    plt.quiver(0, 0, r, im, angles="xy", scale_units="xy", scale=1, color=colores[c])
    c+=1

plt.show()



