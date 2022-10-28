


import os
from flask import Flask, render_template, request
from todas_clases.clase1_direcciones import Direcciones_coordenadas_API_Google
from todas_clases.clase2_mapas import Mapa
from todas_clases.clase3_grafico import Grafico
import pandas as pd
from werkzeug.utils import secure_filename
######################################################################
UPLOAD_FOLDER = 'src\static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'csv', 'xlsx'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route ("/")
def home():           
    return render_template('hom.html')   

@app.route ("/post", methods=['GET', 'POST'])
def post():      
    if request.method == 'POST':
        #cargar archivo
        file = request.files['file']                        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)      
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename)) 
            ############
            clave_google = 'api' 
            # saca coordenadas
            datos_excel = pd.read_excel('src\static\dire_25.xlsx') 
            coordenadas = Direcciones_coordenadas_API_Google(datos_excel,clave_google)   
            resultado_apy = coordenadas.coordenadas_API_Google() 
            # crea mapa interactivo
            columnas = ['lat', 'lon'] # definimos los nombres de las columnas
            df1 = pd.DataFrame(resultado_apy, columns=columnas, index=None)
            crea_html = Mapa(df1)
            crea_html.mapa_con_puntos()
            # creamos df elquesea 
            df_segundo = pd.DataFrame(resultado_apy)
            columnas2 = ['Latitud', 'Longitud'] # definimos los nombres de las columnas
            df2 = pd.DataFrame(resultado_apy, columns=columnas2, index=None)
            # escribir el DataFrame en excel
            excel = pd.ExcelWriter('src\static\elquesea.xlsx')
            df2.to_excel(excel)
            # guardar el excel
            excel.save()
            # leer el generado
            df = pd.read_excel('src\static\elquesea.xlsx') 
            #crear grafico de cluster
            uno = int(request.form['uno'])  #numero de camiones
            grafi=Grafico(df,uno)
            d_t_r=grafi.grafi()           

            if uno == 1:
                dis1= d_t_r[0]          
                tie1= d_t_r[1]
                rut1= d_t_r[2]
                return render_template('home.html',
                         resultado = f' Con {uno} camion, la distancia total será de {dis1} km y el tiempo {tie1} minutos',
                         rut11 = rut1) 

            elif uno == 2:
                dis1= d_t_r[0]          
                tie1= d_t_r[1]
                rut1= d_t_r[2]
                dis2= d_t_r[3]          
                tie2= d_t_r[4]
                rut2= d_t_r[5]
                 

                return render_template('home2.html',
                            resultado1 = f' La distancia de la ruta es de {dis1} km y el tiempo de {tie1} minutos',
                            resultado2 = f' La distancia de la ruta es de {dis2} km y el tiempo de {tie2} minutos',
                            rut11 = rut1,
                            rut22 = rut2
                            )  



@app.route ("/mapa")
def mapa_():           
    return render_template('Mapa.html')  

    
# lo ejecutamos diciendo que se mantenga activado siempre
if __name__ == '__main__':
    app.run(debug=True)



