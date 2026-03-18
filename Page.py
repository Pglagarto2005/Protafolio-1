import streamlit as st


st.set_page_config(
    page_title="Mis Proyectos - Interfaces Multimodales",
    page_icon="💻",
    layout="centered"
)


st.title("💻 Portafolio de Proyectos")
st.write("Bienvenido a mi colección de trabajos de Interfaces Multimodales 🚀")


proyectos = [
    {
        "nombre": "Proyecto VR - Puerta Interactiva",
        "descripcion": "Interacción con una puerta en VR usando perilla.",
        "link": "https://tu-link-aqui.com"
    },
    {
        "nombre": "Simulación de Cocina VR",
        "descripcion": "Secuencia de interacción con ingredientes.",
        "link": "https://tu-link-aqui.com"
    },
    {
        "nombre": "Señalética en VR",
        "descripcion": "Sistema de guía visual en entorno virtual.",
        "link": "https://tu-link-aqui.com"
    }
]


for proyecto in proyectos:
    st.subheader(proyecto["nombre"])
    st.write(proyecto["descripcion"])
    st.markdown(f"[🔗 Ver proyecto]({proyecto['link']})")
    st.write("---")
