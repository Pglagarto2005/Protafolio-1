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
    {
        "Nombre": "Reconocimiento de texto en imagenes Camara",
        "Descripcion": "Reconocimiento de texto con camara",
        "link": "https://yourimagetotext.streamlit.app/"
    },
    {
        "Nombre": "Reconocimiento de texto en imagenes Upload",
        "Descripcion": "Sube una imagen para saber que dice",
        "link": "https://translateanimage.streamlit.app/"
    },
    {
        "Nombre": "Vision digital YOLO-V5",
        "Descripcion": "Reconoce que hay en la imagen",
        "link": "https://vision-digital-yolov5.streamlit.app/"
    },
    {
        "Nombre": "Piedra papel tijera",
        "Descripcion": "Juguemos piedra papel o tirjera",
        "link": "https://piedra-papel-tijera.streamlit.app/"
    },
    {
        "Nombre": "Generador de textos LSTM",
        "Descripcion": "Lenguaje al estimo chatgpt pero primitivo",
        "link": "https://nknlstmnlp.streamlit.app/"
    },
    {
        "Nombre": "Lector de PDFs",
        "Descripcion": "Es como NotebookLM",
        "link": "https://notebooklmmmt7h2vgid4d3prz73muv4h.streamlit.app/"
    },
    {
        "Nombre": "Interpretar imagenes",
        "Descripcion": "Sube una imagen y te dire que veo",
        "link": "https://lookaturimage.streamlit.app/"
    },
    {
        "Nombre": "Digitos",
        "Descripcion": "Dibuja un numero",
        "link": "https://guessyournumber.streamlit.app/"
    },
    {
        "Nombre": "Paint",
        "Descripcion": "Tablero para dibujar",
        "link": "https://drawingbord.streamlit.app/"
    },
    {
        "Nombre": "Guess the drawing",
        "Descripcion": "Te dire que dibujaste",
        "link": "https://canvasapi.streamlit.app/"
    },
    {
        "Nombre": "Consejos para dibujar",
        "Descripcion": "Te dare consejos para mejorar tu dibujo",
        "link": "https://upmydraw.streamlit.app/"
    },
    {
        "Nombre": "Receptor MQTT",
        "Descripcion": "Recibe mesajes de tu micro",
        "link": "https://connecttomymqtt.streamlit.app/"
    },
    {
        "Nombre": "Controlador MQTT",
        "Descripcion": "Control para un servo",
        "link": "https://controladormqtt-ixxpfcybpns9na2hq8vsil.streamlit.app/"
    },
    {
        "Nombre": "Controlador MQTT",
        "Descripcion": "Control para un servo",
        "link": "https://controladormqtt-ixxpfcybpns9na2hq8vsil.streamlit.app/"
    },
    {
        "Nombre": "Voz MQTT",
        "Descripcion": "Para que el micro te escuche",
        "link": "https://vozmqtt.streamlit.app/"
    }
]


for proyecto in proyectos:
    with st.container():
        st.markdown(f"### {proyecto['Nombre']}")
        st.write(proyecto["Descripcion"])
        st.link_button("Ver proyecto", proyecto["link"])
        st.write("")
