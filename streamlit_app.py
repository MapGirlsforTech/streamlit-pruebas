import streamlit as st

home = st.Page('home.py',
                       title='Home', default=True)
imageIdentifier = st.Page(
    "imageIdentifier.py", title="Identificador", icon="🔥"
)

# Funciona como router, desde aca se renderizan las paginas

# Con esto configuro a mano las paginas pudiendo customizar el titulo e icono
pg = st.navigation(
    {
        "": [home, imageIdentifier]

    }
)

pg.run()