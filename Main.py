import streamlit as st
st.title("Um presente especial para você")

st.write("Olá, meu amor!")
st.write("Toque o som e veja o que eu te preparei!")
st.audio("You-and-Me.mp3", format="audio/mpeg", loop=True)

st.markdown("### 20 de outubro de 2019")
Tab1, Tab2, Tab3 = st.tabs(["TAB1", "TAB2", "TAB3"])
Tab1.image("Photos/43.jpg")
Tab2.image("Photos/44.jpg")
Tab3.image("Photos/45.jpg")

st.markdown("### 15 de novembro de 2019")
Tab1, Tab2,  = st.tabs(["TAB1", "TAB2"])
Tab1.image("Photos/41.jpg")
Tab2.image("Photos/42.jpg")

st.markdown("### 16 de fevereiro de 2020")
st.image("Photos/39.jpg")

st.markdown("### 2 de março de 2020")
Tab1, Tab2,  = st.tabs(["TAB1", "TAB2"])
Tab1.image("Photos/37.jpg")
Tab2.image("Photos/40.jpg")

st.markdown("### 14 de março de 2020")
Tab1, Tab2, Tab3 = st.tabs(["TAB1", "TAB2", "TAB3"])
Tab1.image("Photos/46.jpg")
Tab2.image("Photos/47.jpg")
Tab3.image("Photos/48.jpg")

st.markdown("### 03 de maio de 2020")
Tab1, Tab2, Tab3 = st.tabs(["TAB1", "TAB2", "TAB3"])
Tab1.image("Photos/49.jpg")
Tab2.image("Photos/50.jpg")
Tab3.image("Photos/51.jpg")

st.markdown("### 12 de julho de 2020")
Tab1, Tab2,  = st.tabs(["TAB1", "TAB2"])
Tab1.image("Photos/52.jpg")
Tab2.image("Photos/53.jpg")

st.markdown("### outras de 2020")
Tab1, Tab2, Tab3 = st.tabs(["TAB1", "TAB2", "TAB3"])
Tab1.image("Photos/54.jpg")
Tab2.image("Photos/55.jpg")
Tab3.image("Photos/56.jpg")

with st.expander("2021"):
    st.image("Photos/57.jpg")

st.markdown("### 20 de Março de 2022")
Tab1, Tab2, Tab3 = st.tabs(["TAB1", "TAB2", "TAB3"])
Tab1.image("Photos/1.jpg")
Tab2.image("Photos/2.jpg")
Tab3.image("Photos/3.jpg")

st.markdown("### 19 de Fevereiro de 2023")
Tab1, Tab2, Tab3, Tab4 = st.tabs(["TAB1", "TAB2", "TAB3", "TAB4"])
Tab1.image("Photos/4.jpg")
Tab2.image("Photos/5.jpg")
Tab3.image("Photos/6.jpg")
Tab4.image("Photos/7.jpg")

st.markdown("### 30 de Abril de 2023")
Tab1, Tab2, Tab3, Tab4, Tab5 = st.tabs(["TAB1", "TAB2", "TAB3", "TAB4", "TAB5"])
Tab1.image("Photos/8.jpg")
Tab2.image("Photos/9.jpg")
Tab3.image("Photos/10.jpg")
Tab4.image("Photos/11.jpg")
Tab5.image("Photos/12.jpg")

st.markdown("### 20 de Agosto de 2023")
Tab1, Tab2 = st.tabs(["TAB1", "TAB2"])
Tab1.image("Photos/13.jpg")
Tab2.image("Photos/14.jpg")

st.markdown("### 03 de Setembro de 2023")
Tab1, Tab2, Tab3, Tab4 = st.tabs(["TAB1", "TAB2", "TAB3", "TAB4"])
Tab1.image("Photos/15.jpg")
Tab2.image("Photos/16.jpg")
Tab3.image("Photos/17.jpg")
Tab4.image("Photos/18.jpg")

st.markdown("### 17 de Dezembro de 2023")
st.image("Photos/19.jpg")

st.markdown("### 08 de fevereiro de 2024")
Tab1, Tab2, Tab3 = st.tabs(["TAB1", "TAB2", "TAB3"])
Tab1.image("Photos/20.jpg")
Tab2.image("Photos/21.jpg")
Tab3.image("Photos/22.jpg")

st.markdown("### 10 de fevereiro de 2024")
st.image("Photos/23.jpg")

st.markdown("### 23 de fevereiro de 2024")
st.image("Photos/24.jpg")

st.markdown("### 22 de setembro de 2024")
Tab1, Tab2, Tab3 = st.tabs(["TAB1", "TAB2", "TAB3"])
Tab1.image("Photos/25.jpg")
Tab2.image("Photos/26.jpg")
Tab3.image("Photos/27.jpg")

st.markdown("### 18 de dezembro de 2024")
Tab1, Tab2, Tab3 = st.tabs(["TAB1", "TAB2", "TAB3"])
Tab1.image("Photos/28.jpg")
Tab2.image("Photos/29.jpg")
Tab3.image("Photos/30.jpg")

st.markdown("### 02 de janeiro de 2025")
st.image("Photos/31.jpg")

st.markdown("### 8 de fevereiro de 2025")
st.image("Photos/32.jpg")

st.markdown("### 28 de Março de 2025")
Tab1, Tab2, Tab3, Tab4 = st.tabs(["TAB1", "TAB2", "TAB3", "TAB4"])
Tab1.image("Photos/33.jpg")
Tab2.image("Photos/34.jpg")
Tab3.image("Photos/35.jpg")
Tab4.image("Photos/36.jpg")

st.markdown("### 19 de Abril de 2025")
Tab1, Tab2= st.tabs(["TAB1", "TAB2"])
Tab1.image("Photos/36-1.jpg")
Tab2.image("Photos/36-2.jpg")

if st.button("Click me"):
    st.markdown("#  :red[Obrigado por estar aqui comigo, meu amor!]")
    st.text("Eu te amo!")
    st.markdown("### ❤️ ")
    st.balloons()