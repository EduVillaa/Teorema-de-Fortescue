import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

polar2cart = lambda mod, ang: (mod*np.cos(np.pi/180*ang), mod*np.sin(np.pi/180*ang))

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
    angulofa = st.slider("Arg fase A", 0.0, 360.0, 30.0, 1.0)
    modulofb = st.slider("Módulo fase B", 0.0, 10.0, 5.0, 0.1)
    angulofb = st.slider("Arg fase B", 0.0, 360.0, 150.0, 1.0)
    modulofc = st.slider("Módulo fase C", 0.0, 10.0, 5.0, 0.1)
    angulofc = st.slider("Arg fase C", 0.0, 360.0, 90.0, 1.0)
    
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
    faseA = ax.quiver(0, 0, faX, faY, angles="xy", scale_units="xy", scale=1, color="blue", label="Fase A")
    faseB = ax.quiver(0, 0, fbX, fbY, angles="xy", scale_units="xy", scale=1, color="green", label="Fase B")
    faseC = ax.quiver(0, 0, fcX, fcY, angles="xy", scale_units="xy", scale=1, color="red", label="Fase C")
    ax.legend()
    fig.tight_layout()
    st.pyplot(fig, clear_figure=True)
    

