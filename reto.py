import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu



datos = pd.read_csv('base.csv' )


datos = datos[['name_employee', 'birth_date', 'age', 'gender', 'marital_status', 'hiring_date', 'position',
             'salary', 'performance_score', 'last_performance_date', 'average_work_hours', 'satisfaction_level', 'absences']]



st.set_page_config(page_title='Reto',  layout='wide')
t1, t2 = st.columns((0.35,1)) 
t1.image('1.png', width = 340)
t2.title("Socialize your Knowledge")
t2.text('El lugar donde se socializa el conocimiento')


o1,o2,o3,o4 = st.columns(4)
genero = o1.selectbox("Genero", datos['gender'].unique())
puntaje = o2.slider('Rango de puntaje', float(datos['performance_score'].min()), float(datos['performance_score'].max()), (0.0, 3.0))
estado_civil = o3.selectbox("Estado Civil", datos['marital_status'].unique())

datos_filtrados = datos[ (datos['gender'] == genero) & (datos['marital_status'] == estado_civil) & (datos['performance_score'].between(puntaje[0], puntaje[1]))]


g1, g2 = st.columns(2)
hist = px.histogram(
    datos_filtrados, x='performance_score',
    title= 'Distribución del desempeño')
g1.plotly_chart(hist, use_container_width=True)

hist2 = px.histogram(
    datos[(datos['marital_status'] == estado_civil) & (datos['performance_score'].between(puntaje[0], puntaje[1]))],
    x='average_work_hours',
    color='gender',
    opacity=0.5,
    title= 'Promedio de horas trabajadas por genero')
g2.plotly_chart(hist2, use_container_width=True)

scatter = px.scatter(
    datos_filtrados,
    x='age',
    y= 'salary',
    title= 'Edad vs Salario')
g1.plotly_chart(scatter, use_container_width=True)


scatter2 = px.scatter(
    datos_filtrados,
    x='average_work_hours',
    y= 'performance_score',
    title= 'Promedio de horas trabajadas  vs Desempeño')
g2.plotly_chart(scatter2, use_container_width=True)


st.write('Conclusión: Despues de ver lo anterior, es posible concluir que las métricas cambian respecto a las condiciones de las personas.')














