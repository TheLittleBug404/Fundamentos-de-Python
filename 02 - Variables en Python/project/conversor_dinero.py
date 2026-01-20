# este es un conversor de dinero nos sirve para convertir dolares a euros
# 1 .- Ingresar la cantidad de dolares
# 2 .-  realizar la formula matematica para convertir dolares a euros 
# 3 .- Imprimir el resultado en la consola, se debe realizar con un boton 

import streamlit as st
#este sera nuestro titulo de nuestra pagina
st.title("Conversión de dolares a euros")
#este es nuestro input
dolares = st.number_input("Ingrese la cantidad de dolares")
#euros = dolares * 0.86
#euros = str(euros)
#st.button("Procesar",on_click = print('Aqui se imprimira el resultado:',euros))
if st.button("Procesar"):
    euros = dolares * 0.86
    st.success(f"El monto en euros es: € {euros:.2f}")
