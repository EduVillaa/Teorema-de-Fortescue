import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from math import atan2, degrees

polar2cart = lambda mod, ang: (mod*np.cos(np.pi/180*ang), mod*np.sin(np.pi/180*ang))
cart2polar = lambda dx, dy: (np.sqrt(dx**2+dy**2), degrees(atan2(dy, dx)))

st.set_page_config(layout="wide")
st.title("Teorema de Fortescue")
st.markdown(
    """
    <style>
    h1 {
        text-align: center;
        margin-bottom: 500px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 =st.columns([2,1,1])

with col2:
    modulofa = st.slider("Módulo fase A", 0.0, 10.0, 5.0, 0.1)
    angulofa = st.slider("Arg fase A", 0.0, 360.0, 90.0, 1.0)
    modulofb = st.slider("Módulo fase B", 0.0, 10.0, 5.0, 0.1)
    angulofb = st.slider("Arg fase B", 0.0, 360.0, 330.0, 1.0)
    modulofc = st.slider("Módulo fase C", 0.0, 10.0, 5.0, 0.1)
    angulofc = st.slider("Arg fase C", 0.0, 360.0, 210.0, 1.0)
    
with col1:
    fig, ax = plt.subplots()
    ax.set_ylabel("Eje imaginario")
    ax.set_xlabel("Eje real")
    ax.set_aspect("equal")
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.grid()
    ax.axvline(0, color="k", lw=0.5)
    ax.axhline(0, color="k", lw=0.5)
    faX, faY = polar2cart(modulofa, angulofa)
    fbX, fbY = polar2cart(modulofb, angulofb)
    fcX, fcY = polar2cart(modulofc, angulofc)
    faseA = ax.quiver(0, 0, faX, faY, angles="xy", scale_units="xy", scale=1, color="cornflowerblue", label="Fase A")
    faseB = ax.quiver(0, 0, fbX, fbY, angles="xy", scale_units="xy", scale=1, color="tomato", label="Fase B")
    faseC = ax.quiver(0, 0, fcX, fcY, angles="xy", scale_units="xy", scale=1, color="mediumseagreen", label="Fase C")
    ax.legend()
    #Fase homopolar
    zfaseA = complex(faX, faY)
    zfaseB = complex(fbX, fbY)
    zfaseC = complex(fcX, fcY)
    dxH = ((zfaseA+zfaseB+zfaseC)*1/3).real
    dyH = ((zfaseA+zfaseB+zfaseC)*1/3).imag
    secH = ax.quiver(0, 0, dxH, dyH, angles="xy", scale_units="xy", scale=1, color="k")
    #Fase directa
    alphaX, alphaY = polar2cart(1, 120)
    alpha = complex(alphaX, alphaY)
    sec_directa_faseAz = (zfaseA+zfaseB*alpha+zfaseC*alpha**2)*1/3
    sec_directa_faseBz = sec_directa_faseAz*alpha**2
    sec_directa_faseCz = sec_directa_faseAz*alpha
    secD_faseAz = ax.quiver(dxH, dyH, sec_directa_faseAz.real, sec_directa_faseAz.imag, angles="xy", scale_units="xy", scale=1, color="lightcoral")
    secD_faseBz = ax.quiver(dxH, dyH, sec_directa_faseBz.real, sec_directa_faseBz.imag, angles="xy", scale_units="xy", scale=1, color="lightcoral")
    secD_faseCz = ax.quiver(dxH, dyH, sec_directa_faseCz.real, sec_directa_faseCz.imag, angles="xy", scale_units="xy", scale=1, color="lightcoral")
    #Fase inversa
    sec_inversa_faseAz = (zfaseA+zfaseB*alpha**2+zfaseC*alpha)*1/3
    sec_inversa_faseBz = sec_inversa_faseAz*alpha
    sec_inversa_faseCz = sec_inversa_faseAz*alpha**2
    secI_faseAz = ax.quiver(sec_directa_faseAz.real+dxH, sec_directa_faseAz.imag+dyH, sec_inversa_faseAz.real, sec_inversa_faseAz.imag, angles="xy", scale_units="xy", scale=1, color="khaki")
    secI_faseBz = ax.quiver(sec_directa_faseBz.real+dxH, sec_directa_faseBz.imag+dyH, sec_inversa_faseBz.real, sec_inversa_faseBz.imag, angles="xy", scale_units="xy", scale=1, color="khaki")
    secI_faseCz = ax.quiver(sec_directa_faseCz.real+dxH, sec_directa_faseCz.imag+dyH, sec_inversa_faseCz.real, sec_inversa_faseCz.imag, angles="xy", scale_units="xy", scale=1, color="khaki") 
    fig.tight_layout()
    st.pyplot(fig, clear_figure=True)
    
with col3:
    modH, angH = cart2polar(dxH, dyH)
    st.markdown("Secuencia homopolar: ")
    st.latex(f"U_{{a0}}=U_{{b0}}=U_{{c0}}={modH:.2f}∠{angH:.2f}")
    
    modD_fa, angD_fa = cart2polar(sec_directa_faseAz.real, sec_directa_faseAz.imag)
    modD_fb, angD_fb = cart2polar(sec_directa_faseBz.real, sec_directa_faseBz.imag)
    modD_fc, angD_fc = cart2polar(sec_directa_faseCz.real, sec_directa_faseCz.imag)
    st.markdown("Secuencia directa: ")
    st.latex(f"U_{{a1}}={modD_fa:.2f}∠{angD_fa:.2f}")
    st.latex(f"U_{{b1}}={modD_fb:.2f}∠{angD_fb:.2f}")
    st.latex(f"U_{{c1}}={modD_fc:.2f}∠{angD_fc:.2f}")
    
    modI_fa, angI_fa = cart2polar(sec_inversa_faseAz.real, sec_inversa_faseAz.imag)
    modI_fb, angI_fb = cart2polar(sec_inversa_faseBz.real, sec_inversa_faseBz.imag)
    modI_fc, angI_fc = cart2polar(sec_inversa_faseCz.real, sec_inversa_faseCz.imag)
    st.markdown("Secuencia inversa: ")
    st.latex(f"U_{{a2}}={modI_fa:.2f}∠{angI_fa:.2f}")
    st.latex(f"U_{{b2}}={modI_fb:.2f}∠{angI_fb:.2f}")
    st.latex(f"U_{{c2}}={modI_fc:.2f}∠{angI_fc:.2f}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
