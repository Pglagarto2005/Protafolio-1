import streamlit as st


st.set_page_config(
    page_title="Portafolio Interfaces Multimodales",
    page_icon="",
    layout="centered"
)



st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #ff4b1f, #ff9068, #36d1dc, #5b86e5);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.stApp::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
    background-size: 40px 40px;
    animation: moveParticles 20s linear infinite;
    z-index: 0;
}

@keyframes moveParticles {
    from {transform: translate(0, 0);}
    to {transform: translate(-50px, -50px);}
}

h1, h2, h3, p {
    color: white;
}
</style>
""", unsafe_allow_html=True)


st.title("💻 Portafolio de Proyectos")
st.write("Bienvenido a mi colección de trabajos de Interfaces Multimodales 🚀")


proyectos = [
    {
        "Nombre":"Primera pagina Streamlit",
        "Descripcion": "Utilizar textos, botones, marcas, listas, etc",
        "link": "https://bananarotate.streamlit.app/"
    },
    {
        "Nombre": "Conversión de texto a audio",
        "Descripcion": "Pasar un texto a un audio",
        "link": "https://ejemplottssantiagobotero.streamlit.app/"
    },
    {
        "Nombre": "TF-IDF",
        "Descripcion": "Es una métrica numérica que evalúa la importancia de un término",
        "link": "https://tfxidfenesp.streamlit.app/"
    },
    {
        "Nombre": "Natural Language Toolkit",
        "Descripcion": "Una biblioteca de Python para trabajar con lenguaje humano",
        "link": "https://lenguajenatural.streamlit.app/"
    },
    {
        "Nombre": "Análisis de sentimientos",
        "Descripcion": "Escribe algo y sabremos que emocion quieres reflejar",
        "link": "https://whatisyouremotion.streamlit.app/"
    },
    {
        "Nombre": "Traductor de voz",
        "Descripcion": "Dia algo y lo traduciremos",
        "link": "https://traductor-etbhn56yutwgjgxmvgkcek.streamlit.app/"
    },
]


for proyecto in proyectos:
    with st.container():
        st.markdown(f"### {proyecto['Nombre']}")
        st.write(proyecto["Descripcion"])
        st.link_button("Ver proyecto", proyecto["link"])
        st.write("")
