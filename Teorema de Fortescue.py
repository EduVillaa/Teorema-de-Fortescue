#Teorema de Fortescue: Cualquier sistema desequilibrado puede ser representado como superposición de tres sistemas equilibrados,
#uno de secuencia directa, uno de secuencia inversa, y uno de secuencia homopolar
from matplotlib.widgets import Slider, Button, CheckButtons
import matplotlib.pyplot as plt
import numpy as np
#Definimos en coordenadas polares el sistema trifásico desequilibrado
modulofa, modulofb, modulofc, angulofa, angulofb, angulofc = 5, 5, 5, 90, -30, -150
#Definimos una función para pasar de coordenadas polares a coordenadas cartesianas
def polar2cart(modulo, angulo):
    x=modulo*np.cos(angulo*np.pi/180)
    y=modulo*np.sin(angulo*np.pi/180)
    return x, y
#Definimos una función para pasar de coordenadas cartesianas a coordenadas polares
def cart2polar(x, y):
    modulo = np.sqrt(x**2+y**2)
    arg = np.arctan2(y, x)
    return modulo, arg
#Dedinimos una función que nos permite obtener en grados el argumento de un número complejo
def argZ(z):
    theta_rad = np.angle(z)          
    theta_deg = np.degrees(theta_rad)
    return theta_deg
#Definimos las características de la imagen
fig, ax = plt.subplots()
plt.subplots_adjust(right=0.7, left=0.2)
#fig, (ax, ax_time) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(8, 8))



plt.xlim(-10,10)
plt.ylim(-10,10)
plt.axvline(0, color="k", lw=0.5)
plt.axhline(0, color="k", lw=0.5)
ax.set_title("Teorema de Fortescue", pad=30, fontdict={"fontsize":25, "fontweight":"bold", "color":"black"})
ax.set_facecolor("whitesmoke")
ax.tick_params(colors="dimgray")
ax.set_aspect("equal")
plt.grid()
#Representamos los fasores del sistema trifásico desequilibrado
dxA, dyA = polar2cart(modulofa, angulofa)
quiver_faseA = ax.quiver(0, 0, dxA, dyA, angles="xy", scale_units="xy", scale=1, color="cornflowerblue", label = "A")
dxB, dyB = polar2cart(modulofb, angulofb)
quiver_faseB = ax.quiver(0, 0, dxB, dyB, angles="xy", scale_units="xy", scale=1, color="tomato", label = "B")
dxC, dyC = polar2cart(modulofc, angulofc)
quiver_faseC = ax.quiver(0, 0, dxC, dyC, angles="xy", scale_units="xy", scale=1, color="mediumseagreen", label = "C")
ax.legend(fontsize=15)
#Calculamos y representamos los fasores de secuencia homopolar
sec_homopolar_x = 1/3*(dxA+dxB+dxC)
sec_homopolar_y = 1/3*(dyA+dyB+dyC)
quiver_sec_homopolar = ax.quiver(0, 0, sec_homopolar_x, sec_homopolar_y, 
                                 angles="xy", scale_units="xy", scale=1, color="k") #En la secuencia homopolar las tres fases valen lo mismo

#Calculamos y representamos los fasores de secuencia directa
#Para facilitarnos la vida pasamos a polares los fasores del sistema trifásico desequilibrado
zfaseA, zfaseB, zfaseC = complex(dxA, dyA), complex(dxB, dyB), complex(dxC, dyC)
#Definimos alpha como 1∠120° en polares, que equivale a -0.5+sqrt(3)j/2 en cartesianas
Alpha= -0.5+(np.sqrt(3)/2)*1j
#Calculamos los fasores de secuencia directa
Zsec_directa_fa=1/3*(zfaseA+zfaseB*Alpha+zfaseC*Alpha**2)
Zsec_directa_fb=(Zsec_directa_fa*Alpha**2)
Zsec_directa_fc=(Zsec_directa_fa*Alpha)
#Representamos los fasores de secuencia directa
quiver_sec_directa_fa = ax.quiver(sec_homopolar_x, sec_homopolar_y, np.real(Zsec_directa_fa),
                                  np.imag(Zsec_directa_fa), angles="xy", scale_units="xy", scale=1, color="lightcoral")
quiver_sec_directa_fb = ax.quiver(sec_homopolar_x, sec_homopolar_y, np.real(Zsec_directa_fb),
                                  np.imag(Zsec_directa_fb), angles="xy", scale_units="xy", scale=1, color="lightcoral")
quiver_sec_directa_fc = ax.quiver(sec_homopolar_x, sec_homopolar_y, np.real(Zsec_directa_fc),
                                  np.imag(Zsec_directa_fc), angles="xy", scale_units="xy", scale=1, color="lightcoral")

#Calculamos los fasores de secuencia inversa
Zsec_inversa_fa=1/3*(zfaseA+zfaseB*Alpha**2+zfaseC*Alpha)
Zsec_inversa_fb=(Zsec_inversa_fa*Alpha)
Zsec_inversa_fc=(Zsec_inversa_fa*Alpha**2)
#Representamos los fasores de secuencia inversa
quiver_sec_inversa_fa = ax.quiver(np.real(Zsec_directa_fa)+sec_homopolar_x, np.imag(Zsec_directa_fa)+sec_homopolar_y,
                                  np.real(Zsec_inversa_fa), np.imag(Zsec_inversa_fa), angles="xy", scale_units="xy", scale=1, color="khaki")
quiver_sec_inversa_fb = ax.quiver(np.real(Zsec_directa_fb)+sec_homopolar_x, np.imag(Zsec_directa_fb)+sec_homopolar_y,
                                  np.real(Zsec_inversa_fb), np.imag(Zsec_inversa_fb), angles="xy", scale_units="xy", scale=1, color="khaki")
quiver_sec_inversa_fc = ax.quiver(np.real(Zsec_directa_fb)+sec_homopolar_x, np.imag(Zsec_directa_fb)+sec_homopolar_y,
                                  np.real(Zsec_inversa_fb), np.imag(Zsec_inversa_fb), angles="xy", scale_units="xy", scale=1, color="khaki")

#Escribimos texto con los valores de cada secuencia
#Secuencia homopolar
mod_homopolar, arg_homopolar = cart2polar(sec_homopolar_x, sec_homopolar_y)
texto_sec_homopolar=ax.text(14, 5, f"$U_{{a_0}}=U_{{b_0}}=U_{{c_0}}=${mod_homopolar:.2f}∠{arg_homopolar*180/np.pi:.2f}", 
        fontsize=13, color="k")
#Secuencia directa
mod_directa = abs(Zsec_directa_fa)
arg_directa_fa = argZ(Zsec_directa_fa)
arg_directa_fb = argZ(Zsec_directa_fb)
arg_directa_fc = argZ(Zsec_directa_fc)
texto_sec_directa_fa=ax.text(15, 0, f"$U_{{a_1}}=${mod_directa:.2f}∠{arg_directa_fa:.2f}", 
        fontsize=13, color="k")
texto_sec_directa_fb=ax.text(15, -1, f"$U_{{b_1}}=${mod_directa:.2f}∠{arg_directa_fb:.2f}", 
        fontsize=13, color="k")
texto_sec_directa_fc=ax.text(15, -2, f"$U_{{c_1}}=${mod_directa:.2f}∠{arg_directa_fc:.2f}", 
        fontsize=13, color="k")
#Secuencia inversa
mod_inversa = abs(Zsec_inversa_fa)
arg_inversa_fa = argZ(Zsec_inversa_fa)
arg_inversa_fb = argZ(Zsec_inversa_fb)
arg_inversa_fc = argZ(Zsec_inversa_fc)
texto_sec_inversa_fa=ax.text(15, -7, f"$U_{{a_2}}=${mod_inversa:.2f}∠{arg_inversa_fa:.2f}", 
        fontsize=13, color="k")
texto_sec_inversa_fb=ax.text(15, -8, f"$U_{{b_2}}=${mod_inversa:.2f}∠{arg_inversa_fb:.2f}", 
        fontsize=13, color="k")
texto_sec_inversa_fc=ax.text(15, -9, f"$U_{{c_2}}=${mod_inversa:.2f}∠{arg_inversa_fc:.2f}", 
        fontsize=13, color="k")

#Definimos los ejes del slider
eje_modulofa = plt.axes([0.75, 0.8, 0.2, 0.02])
eje_angulofa = plt.axes([0.75, 0.75, 0.2, 0.02])
eje_modulofb = plt.axes([0.75, 0.6, 0.2, 0.02])
eje_angulofb = plt.axes([0.75, 0.55, 0.2, 0.02])
eje_modulofc = plt.axes([0.75, 0.35, 0.2, 0.02])
eje_angulofc = plt.axes([0.75, 0.3, 0.2, 0.02])

#Definimos los sliders
slider_modulofa = Slider(eje_modulofa, "Modulo A", 0, 10, valinit=5)
slider_angulofa = Slider(eje_angulofa, "Arg A", 0, 360, valinit=90)
slider_modulofb = Slider(eje_modulofb, "Modulo B", 0, 10, valinit=5)
slider_angulofb = Slider(eje_angulofb, "Arg B", 0, 360, valinit=330)
slider_modulofc = Slider(eje_modulofc, "Modulo C", 0, 10, valinit=5)
slider_angulofc = Slider(eje_angulofc, "Arg C", 0, 360, valinit=210)
sliders = [slider_modulofa, slider_angulofa,  slider_modulofb, slider_angulofb, slider_modulofc, slider_angulofc]
#Boton de reseteo
ax_button = plt.axes([0.8, 0.07, 0.1, 0.04])
boton = Button(ax_button, "Reset")
#Botones de CheckButtons
ax_check = plt.axes([0.02, 0.65, 0.12, 0.12])
ax_check.set_facecolor("lightgray")
checklist = CheckButtons(ax_check, ["Fase A", "Fase B", "Fase C"], [True, True, True])

#Función para actualizar checklist
def actualizar(label):
    if label == "Fase A":
        quiver_faseA.set_visible(not quiver_faseA.get_visible())
        quiver_sec_directa_fa.set_visible(not quiver_sec_directa_fa.get_visible())
        quiver_sec_inversa_fa.set_visible(not quiver_sec_inversa_fa.get_visible())
    elif label == "Fase B":
        quiver_faseB.set_visible(not quiver_faseB.get_visible())
        quiver_sec_directa_fb.set_visible(not quiver_sec_directa_fb.get_visible())
        quiver_sec_inversa_fb.set_visible(not quiver_sec_inversa_fb.get_visible())
    elif label == "Fase C":
        quiver_faseC.set_visible(not quiver_faseC.get_visible())
        quiver_sec_directa_fc.set_visible(not quiver_sec_directa_fc.get_visible())
        quiver_sec_inversa_fc.set_visible(not quiver_sec_inversa_fc.get_visible())
    plt.draw()

checklist.on_clicked(actualizar)

#Funcion que ejecuta el reset
def reset(event):
        for s in sliders:
            s.reset()
#Función para actualizar la gráfica
def update(val):
    modulofa = slider_modulofa.val
    angulofa = slider_angulofa.val
    modulofb = slider_modulofb.val
    angulofb = slider_angulofb.val
    modulofc = slider_modulofc.val
    angulofc = slider_angulofc.val
    dxA, dyA = polar2cart(modulofa, angulofa)
    quiver_faseA.set_UVC(dxA, dyA)
    dxB, dyB = polar2cart(modulofb, angulofb)
    quiver_faseB.set_UVC(dxB, dyB)
    dxC, dyC = polar2cart(modulofc, angulofc)
    quiver_faseC.set_UVC(dxC, dyC)
    #Escribimos los fasores de secuencia homopolar
    sec_homopolar_x, sec_homopolar_y = 1/3*(dxA+dxB+dxC), 1/3*(dyA+dyB+dyC)
    quiver_sec_homopolar.set_UVC(sec_homopolar_x, sec_homopolar_y)
    mod_homopolar, arg_homopolar = cart2polar(sec_homopolar_x, sec_homopolar_y)
    texto_sec_homopolar.set_text(f"$U_{{a_0}}=U_{{b_0}}=U_{{c_0}}=${mod_homopolar:.2f}∠{arg_homopolar*180/np.pi:.2f}")
    #Escribimos los fasores de secuencia directa
    zfaseA, zfaseB, zfaseC = complex(dxA, dyA), complex(dxB, dyB), complex(dxC, dyC)
    Zsec_directa_fa=1/3*(zfaseA+zfaseB*Alpha+zfaseC*Alpha**2)
    Zsec_directa_fb=(Zsec_directa_fa*Alpha**2)
    Zsec_directa_fc=(Zsec_directa_fa*Alpha)
    sec_homopolar_x = 1/3*(dxA+dxB+dxC)
    sec_homopolar_y = 1/3*(dyA+dyB+dyC)
    quiver_sec_directa_fa.set_UVC(np.real(Zsec_directa_fa), np.imag(Zsec_directa_fa))
    quiver_sec_directa_fa.set_offsets([sec_homopolar_x, sec_homopolar_y])
    quiver_sec_directa_fb.set_UVC(np.real(Zsec_directa_fb), np.imag(Zsec_directa_fb))
    quiver_sec_directa_fb.set_offsets([sec_homopolar_x, sec_homopolar_y])
    quiver_sec_directa_fc.set_UVC(np.real(Zsec_directa_fc), np.imag(Zsec_directa_fc))
    quiver_sec_directa_fc.set_offsets([sec_homopolar_x, sec_homopolar_y])
    mod_directa = abs(Zsec_directa_fa)
    arg_directa_fa = argZ(Zsec_directa_fa)
    arg_directa_fb = argZ(Zsec_directa_fb)
    arg_directa_fc = argZ(Zsec_directa_fc)
    texto_sec_directa_fa.set_text( f"$U_{{a_1}}=${mod_directa:.2f}∠{arg_directa_fa:.2f}")
    texto_sec_directa_fb.set_text( f"$U_{{b_1}}=${mod_directa:.2f}∠{arg_directa_fb:.2f}")
    texto_sec_directa_fc.set_text( f"$U_{{c_1}}=${mod_directa:.2f}∠{arg_directa_fc:.2f}")
    #Escribimos los fasores de secuencia inversa
    Zsec_inversa_fa=1/3*(zfaseA+zfaseB*Alpha**2+zfaseC*Alpha)
    Zsec_inversa_fb=(Zsec_inversa_fa*Alpha)
    Zsec_inversa_fc=(Zsec_inversa_fa*Alpha**2)
    quiver_sec_inversa_fa.set_UVC(np.real(Zsec_inversa_fa), np.imag(Zsec_inversa_fa))
    quiver_sec_inversa_fa.set_offsets([np.real(Zsec_directa_fa)+sec_homopolar_x, np.imag(Zsec_directa_fa)+sec_homopolar_y])
    quiver_sec_inversa_fb.set_UVC(np.real(Zsec_inversa_fb), np.imag(Zsec_inversa_fb))
    quiver_sec_inversa_fb.set_offsets([np.real(Zsec_directa_fb)+sec_homopolar_x, np.imag(Zsec_directa_fb)+sec_homopolar_y])
    quiver_sec_inversa_fc.set_UVC(np.real(Zsec_inversa_fc), np.imag(Zsec_inversa_fc))
    quiver_sec_inversa_fc.set_offsets([np.real(Zsec_directa_fc)+sec_homopolar_x, np.imag(Zsec_directa_fc)+sec_homopolar_y])
    mod_inversa = abs(Zsec_inversa_fa)
    arg_inversa_fa = argZ(Zsec_inversa_fa)
    arg_inversa_fb = argZ(Zsec_inversa_fb)
    arg_inversa_fc = argZ(Zsec_inversa_fc)
    texto_sec_inversa_fa.set_text( f"$U_{{a_2}}=${mod_inversa:.2f}∠{arg_inversa_fa:.2f}")
    texto_sec_inversa_fb.set_text( f"$U_{{b_2}}=${mod_inversa:.2f}∠{arg_inversa_fb:.2f}")
    texto_sec_inversa_fc.set_text( f"$U_{{c_2}}=${mod_inversa:.2f}∠{arg_inversa_fc:.2f}")
    
    fig.canvas.draw_idle()

boton.on_clicked(reset)
#Llamamos a la función update cada vez que el slider cambie de posición
for s in sliders:
    s.on_changed(update)

plt.show()
    
    






