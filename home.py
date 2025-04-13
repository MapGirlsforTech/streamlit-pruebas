import streamlit as st

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text)

# Función para añadir un enlace
def enlace(enlace, titulo):
    st.page_link(enlace, label=titulo)

# st.header("MAP Girls for Tech")

# st.markdown("<h2 style='text-align: center;'>MAP Girls for Tech</h2>", unsafe_allow_html=True)

st.markdown(
    """
    <h2 style="text-align: center; color: #4CAF50;">
        MAP Girls for TECH
    </h2>
    """, 
    unsafe_allow_html=True
)

# Texto: Presentación del equipo

st.markdown(
    "Hola, somos **Maite**, **Ana** y **Pilar** y juntas formamos el equipo MAP Girls for Tech. Participamos por tercer año consecutivo en el proyecto Technovation Girls, cuyo objetivo es acercar la tecnología a las chicas y jóvenes de 8 a 18 años, la idea es aumentar con esta iniciativa la presencia de mujeres en las carreras STEM."
)
parrafo("Debemos buscar un problema en nuestra comunidad que cumpla uno o varios de los Objetivos  de Desarrollo Sostenible 2030 de la ONU. Durante 12 semanas debemos trabajar para darle una solución a dicho problema y crear una App móvil o una Web App con dicha solución. ")

parrafo("En este programa participan y compiten equipos de chicas de todo el mundo divididas en tres categorías, Beginner, Junior y Senior. ")

parrafo("Las chicas aprendemos entre otras muchas cosas a programar, entrenar modelos de IA y a exponer nuestra idea y trabajo en público.")

parrafo("Podéis conocer más sobre este programa a través del siguiente enlace:")
# technovationchallenge.org

# enlace("https://technovationchallenge.org/", "Programa Technovation Girls")
# # st.markdown('[Programa Technovation](https://technovationchallenge.org/)')

# Crear un enlace con apariencia de botón
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
    <a href="https://technovationchallenge.org/" target="_blank">
        <button style="background-color: #4CAF50; color: white; padding: 5px 20px; font-size: 16px; border: none; cursor: pointer; border-radius: 5px;">
            Programa Technovation Girls
        </button>
    </a>
    </div>
    """, 
    unsafe_allow_html=True
)

parrafo(" ")

parrafo("Un problema que nos ha llamado la atención es que no hay calzado deportivo femenino para las jugadoras de fútbol. Es crucial utilizar un calzado adecuado al practicar deporte, ya que el uso de calzado deportivo no adecuado al pie femenino puede causar graves lesiones. Esto le ha pasado a nuestra compañera Pilar, así como dea otras muchas mujeres, que debido a la falta de calzado adaptado a su pie sufre lesiones, en ocasiones importantes, ya que se ven  obligadas a recurrir al calzado masculino. Este es el testimonio de Pilar:")

# st.caption("“He jugado al fútbol desde los 5 años y me encantan los deportes, pero nunca he encontrado botas específicamente para chicas. He sufrido de varias lesiones en los tobillos, pero mi última lesión, ha sido la más grave de todas concretamente en la rodilla, he tenido que estar 4 meses en reposo total.”")

# Centrar la cita, pero alineada a la izquierda
st.markdown(
    """
    <div style="display: flex; justify-content: center; width: 80%;">
        <blockquote style="text-align: left; font-style: italic; font-size: 1em; border-left: 5px solid #ccc; padding-left: 10px;">
            "He jugado al fútbol desde los 5 años y me encantan los deportes, pero nunca he encontrado botas diseñadas especificamente para chicas. He sufrido de varias lesiones en los tobillos, pero mi última lesión ha sido la más grave de todas, concretamente en la rodilla y he tenido que estar 4 meses en reposo total."
        </blockquote>
    </div>
    """,
    unsafe_allow_html=True
)

parrafo(" ")

parrafo("Ante esta problemática, la falta de calzado deportivo adecuado al pie de la mujer en muchos deportes femeninos, es hacia donde vamos a enfocar nuestro proyecto esta temporada.")

parrafo("Hemos creado un cuestionario con una serie de preguntas que nos ayudarán a darle forma  al proyecto y tratar de buscar una solución a este problema. ")

# parrafo("#### **¡¡¡NECESITAMOS VUESTRA AYUDA!!!**")

st.markdown("<h4 style='text-align: center;'>¡¡¡NECESITAMOS VUESTRA AYUDA!!!</h4>", unsafe_allow_html=True)

# parrafo("¿Podrías contestar nuestro cuestionario?")

st.markdown("<h5 style='text-align: center;'>¿Podrías contestar nuestro cuestionario?</h5>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>Muchas Gracias</h5>", unsafe_allow_html=True)

# enlace("https://technovationchallenge.org/", "Enlace al cuestionario")

# Crear un enlace con apariencia de botón
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
    <a href="https://technovationchallenge.org/" target="_blank">
        <button style="background-color: #4CAF50; color: white; padding: 5px 20px; font-size: 16px; border: none; cursor: pointer; border-radius: 5px;">
            Ir al Cuestionario
        </button>
    </a>
    </div>
    """, 
    unsafe_allow_html=True
)

# parrafo("__Muchas Gracias.__")

# Crear una columna para centrar la imagen
col1, col2, col3 = st.columns([1, 3, 1])  # Tres columnas, el centro tiene el triple de peso
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/Logo-Circular-WEB_OK.png", use_container_width=True)

# st.image("./images/Logo-Circular-WEB_OK.png", width=400)

# Dos columnas
col1, col2 = st.columns([1, 1])
# Usar la columna central para colocar la imagen
with col1:
    st.image("./images/ODS-03.png", use_container_width=True)
with col2:
    st.image("./images/ODS-05.png", use_container_width=True)

    # Primer fila de imágenes
col1, col2 = st.columns(2)

with col1:
    st.image("./images/ODS-03.png", caption="Imagen 1", use_container_width=True)

with col2:
    st.image("./images/ODS-05.png", caption="Imagen 2", use_container_width=True)

# Segunda fila de imágenes
col3, col4 = st.columns(2)

with col3:
    st.image("./images/ODS-09.png", caption="Imagen 3", use_container_width=True)

with col4:
    st.image("./images/ODS-10.png", caption="Imagen 4", use_container_width=True)