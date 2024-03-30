import streamlit as st

st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

angka_pertama =st.number_input('masukkan angka pertama')
st.write('The first number is ', angka_pertama)

angka_kedua =st.number_input('masukkan angka kedua')
st.write('The second number is ', angka_kedua)

operasi_matematika = angka_pertama * angka_kedua
st.write(f"angka pertama {angka_pertama } x angka kedua {angka_kedua} = {operasi_matematika}")
