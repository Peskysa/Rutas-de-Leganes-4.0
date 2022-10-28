
class Grafico:
    def __init__(self,df,nº_camiones):
        self.nº_camiones = nº_camiones
        self.df = df
        dis1=None
        self.dis1=dis1

    def grafi(self):
        import matplotlib.pyplot as plt
        from sklearn.preprocessing import MinMaxScaler
        from sklearn.cluster import KMeans
        import pandas as pd
        
        self.df.plot.scatter(x='Longitud',  y='Latitud', c='DarkGreen')
        plt.grid("--")
        plt.title("Todos los puntos")
        #plt.show()
        plt.savefig('src\static\grafico.png')
        #......................................................................
        # Normalizamos los datos
        min_max_scaler = MinMaxScaler() 
        self.df = min_max_scaler.fit_transform(self.df)
        self.df = pd.DataFrame(self.df) # Convertimos a Dataframe
        #print(df.head())
        # Aplicamos k-means a nuestro dataset
        km = KMeans(n_clusters=self.nº_camiones, init='random', 
                    max_iter=200, random_state=0)
        y_km = km.fit_predict(self.df)
        # Gráfico con los puntos y su cluster y los centroides
        plt.figure(figsize=(9,9))
        plt.scatter(self.df[y_km == 0][0], self.df[y_km == 0][1], 
                    s=50, c='green', marker='o', 
                    edgecolor='black', label='ruta 1')
        plt.scatter(self.df[y_km == 1][0], self.df[y_km == 1][1],  
                    s=50, c='orange', marker='s', 
                    edgecolor='black', label='ruta 2')
        plt.scatter(self.df[y_km == 2][0], self.df[y_km == 2][1], 
                    s=50, c='lightblue', marker='v', 
                    edgecolor='black', label='ruta 3')
        plt.scatter(self.df[y_km == 3][0], self.df[y_km == 3][1], 
                    s=50, c='purple', marker='d', 
                    edgecolor='black', label='ruta 4')
        plt.scatter(self.df[y_km == 4][0], self.df[y_km == 4][1], 
                    s=50, c='blue', marker='o', 
                    edgecolor='black', label='ruta 5')
        plt.scatter(self.df[y_km == 5][0], self.df[y_km == 5][1], 
                    s=50, c='pink', marker='s', 
                    edgecolor='black', label='ruta 6')
        plt.scatter(self.df[y_km == 6][0], self.df[y_km == 6][1], 
                    s=50, c='yellow', marker='v', 
                    edgecolor='black', label='ruta 7')
        plt.scatter(self.df[y_km == 7][0], self.df[y_km == 7][1], 
                    s=50, c='black', marker='d', 
                    edgecolor='black', label='ruta 8')
        plt.scatter(km.cluster_centers_[:, 0], 
                    km.cluster_centers_[:, 1], s=400, 
                    marker='*', c='red', 
                    edgecolor='black', label='centros')
        plt.legend(loc="best")
        plt.grid("--")
        plt.title("Los puntos separados por rutas")
        plt.savefig('src\static\cluster.png')


    
        if self.nº_camiones == 1:
            primer_cluster = self.df[y_km == 0]
            primer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(primer_cluster)
        elif self.nº_camiones == 2:
            primer_cluster = self.df[y_km == 0]
            primer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(primer_cluster)
            segundo_cluster = self.df[y_km == 1]
            segundo_cluster_lista_coordenadas = min_max_scaler.inverse_transform(segundo_cluster)
        elif self.nº_camiones == 3:
            primer_cluster = self.df[y_km == 0]
            primer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(primer_cluster)
            segundo_cluster = self.df[y_km == 1]
            segundo_cluster_lista_coordenadas = min_max_scaler.inverse_transform(segundo_cluster)
            tercer_cluster = self.df[y_km == 2]
            tercer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(tercer_cluster)
        elif self.nº_camiones == 4:
            primer_cluster = self.df[y_km == 0]
            primer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(primer_cluster)
            segundo_cluster = self.df[y_km == 1]
            segundo_cluster_lista_coordenadas = min_max_scaler.inverse_transform(segundo_cluster)
            tercer_cluster = self.df[y_km == 2]
            tercer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(tercer_cluster)
            cuarto_cluster = self.df[y_km == 3]
            cuarto_cluster_lista_coordenadas = min_max_scaler.inverse_transform(cuarto_cluster)
        elif self.nº_camiones == 5:
            primer_cluster = self.df[y_km == 0]
            primer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(primer_cluster)
            segundo_cluster = self.df[y_km == 1]
            segundo_cluster_lista_coordenadas = min_max_scaler.inverse_transform(segundo_cluster)
            tercer_cluster = self.df[y_km == 2]
            tercer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(tercer_cluster)
            cuarto_cluster = self.df[y_km == 3]
            cuarto_cluster_lista_coordenadas = min_max_scaler.inverse_transform(cuarto_cluster)
            quinto_cluster = self.df[y_km == 4]
            quinto_cluster_lista_coordenadas = min_max_scaler.inverse_transform(quinto_cluster)
        elif self.nº_camiones == 6:
            primer_cluster = self.df[y_km == 0]
            primer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(primer_cluster)
            segundo_cluster = self.df[y_km == 1]
            segundo_cluster_lista_coordenadas = min_max_scaler.inverse_transform(segundo_cluster)
            tercer_cluster = self.df[y_km == 2]
            tercer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(tercer_cluster)
            cuarto_cluster = self.df[y_km == 3]
            cuarto_cluster_lista_coordenadas = min_max_scaler.inverse_transform(cuarto_cluster)
            quinto_cluster = self.df[y_km == 4]
            quinto_cluster_lista_coordenadas = min_max_scaler.inverse_transform(quinto_cluster)
            sexto_cluster = self.df[y_km == 5]
            sexto_cluster_lista_coordenadas = min_max_scaler.inverse_transform(sexto_cluster)
        elif self.nº_camiones == 7:
            primer_cluster = self.df[y_km == 0]
            primer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(primer_cluster)
            segundo_cluster = self.df[y_km == 1]
            segundo_cluster_lista_coordenadas = min_max_scaler.inverse_transform(segundo_cluster)
            tercer_cluster = self.df[y_km == 2]
            tercer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(tercer_cluster)
            cuarto_cluster = self.df[y_km == 3]
            cuarto_cluster_lista_coordenadas = min_max_scaler.inverse_transform(cuarto_cluster)
            quinto_cluster = self.df[y_km == 4]
            quinto_cluster_lista_coordenadas = min_max_scaler.inverse_transform(quinto_cluster)
            sexto_cluster = self.df[y_km == 5]
            sexto_cluster_lista_coordenadas = min_max_scaler.inverse_transform(sexto_cluster)
            septimo_cluster = self.df[y_km == 6]
            septimo_cluster_lista_coordenadas = min_max_scaler.inverse_transform(septimo_cluster)
        elif self.nº_camiones == 8:
            primer_cluster = self.df[y_km == 0]
            primer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(primer_cluster)
            segundo_cluster = self.df[y_km == 1]
            segundo_cluster_lista_coordenadas = min_max_scaler.inverse_transform(segundo_cluster)
            tercer_cluster = self.df[y_km == 2]
            tercer_cluster_lista_coordenadas = min_max_scaler.inverse_transform(tercer_cluster)
            cuarto_cluster = self.df[y_km == 3]
            cuarto_cluster_lista_coordenadas = min_max_scaler.inverse_transform(cuarto_cluster)
            quinto_cluster = self.df[y_km == 4]
            quinto_cluster_lista_coordenadas = min_max_scaler.inverse_transform(quinto_cluster)
            sexto_cluster = self.df[y_km == 5]
            sexto_cluster_lista_coordenadas = min_max_scaler.inverse_transform(sexto_cluster)
            septimo_cluster = self.df[y_km == 6]
            septimo_cluster_lista_coordenadas = min_max_scaler.inverse_transform(septimo_cluster)
            octavo_cluster = self.df[y_km == 7]
            octavo_cluster_lista_coordenadas = min_max_scaler.inverse_transform(octavo_cluster)

        clave_google = 'api'
        origin = "Av. de Fuenlabrada, 2, 28912 Leganés, Madrid"   
        destination = "Av. de Fuenlabrada, 2, 28912 Leganés, Madrid"
        center = "Poligono 5 de Rustica, 95, 28918 Leganés, Madrid"

        def imprime_r(cluster,lista):
                        gmaps = googlemaps.Client(key=clave_google)
                        for i in cluster:
                            i.pop(0)    
                        pp=[]
                        for i in cluster:
                            for j in i:
                                pp.append(str(j))
                        hhh=[]
                        par=0
                        impar=1
                        contador =(len(pp))
                        contador = int(contador/2)
                        for i in range(contador):
                            hhh.append(pp[par]+","+pp[impar])  
                            par = par+2
                            impar = impar+2
                        lista_coordenadas= []
                        lista_tiempo = []
                        lista_distancia = []
                        for i in hhh:
                            geocode_result = gmaps.geocode(i)
                            lista_coordenadas.append(geocode_result[0]["formatted_address"]) 
                            
                        results = gmaps.directions(
                                                origin = "Av. de Fuenlabrada, 2, 28912 Leganés, Madrid",    
                                                destination = "Av. de Fuenlabrada, 2, 28912 Leganés, Madrid",              
                                                                                                    
                                                waypoints = lista_coordenadas,
                                                optimize_waypoints = True,
                                                departure_time=datetime.now() + timedelta(hours=1))
                        ruta_total_str=[]           
                        for i, leg in enumerate(results[0]["legs"]):
                                            lista_tiempo.append(leg["duration"]["text"]) 
                                            lista_distancia.append(leg["distance"]["text"])                  
                                            ruta_total_str.append(
                                            "Parada: {0} || {1} ==> {2} || Distancia: {3} || Tiempo: {4}".format(                
                                                str(i),leg["start_address"],leg["end_address"],leg["distance"]["text"],leg["duration"]["text"]))
                        #l_ruta_total.clear()
                        for i in ruta_total_str:
                            lista.append(i)            
                            #print(i)
                        return [lista_tiempo,lista_distancia]
        from datetime import datetime, timedelta 
        datos_excel = pd.read_excel('src\static\dire_25.xlsx')            
        wp = datos_excel["direcciones"].tolist()
        import googlemaps
        def pinta_mapa(wp):
                            wpy=[]
                            for i in wp:
                                wpy.append(i[1:3])    
                            gmaps = googlemaps.Client(key=clave_google)

                            results = gmaps.directions(
                                                    origin = origin,
                                                    destination = destination,                                     
                                                    waypoints = wpy,
                                                    optimize_waypoints = True,
                                                    departure_time=datetime.now() + timedelta(hours=1))
                            marker_points = []
                            waypoints = []
                            for leg in  results[0]["legs"]:
                                            leg_start_loc = leg["start_location"]
                                            marker_points.append(f'{leg_start_loc["lat"]},{leg_start_loc["lng"]}')
                                            for step in leg["steps"]:
                                                    end_loc = step["end_location"]
                                                    waypoints.append(f'{end_loc["lat"]},{end_loc["lng"]}')
                            last_stop =   results[0]["legs"][-1]["end_location"]
                            marker_points.append(f'{last_stop["lat"]},{last_stop["lng"]}')                        
                            markers = [ "color:red|size:mid|label:" + chr(65+i) + "|" 
                                                    + r for i, r in enumerate(marker_points)]
                            result_map = gmaps.static_map(
                                                    center = center,
                                                    scale=2, 
                                                    zoom=14,
                                                    size=[640, 640], 
                                                    format="jpg", 
                                                    maptype="roadmap",
                                                    markers=markers,
                                                    path="color:0xFF0000|weight:2|" + "|".join(waypoints))   
                            return result_map                                  

        def saca_jpj():
            if self.nº_camiones == 1:
                with open('src\static\primeraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(primer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
            elif self.nº_camiones == 2:
                with open('src\static\primeraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(primer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\segundaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(segundo_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
            elif self.nº_camiones == 3:
                with open('src\static\primeraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(primer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\segundaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(segundo_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\\terceraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(tercer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
            elif self.nº_camiones == 4:
                with open('src\static\primeraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(primer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\segundaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(segundo_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\\terceraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(tercer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\cuartaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(cuarto_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)         
            elif self.nº_camiones == 5:
                with open('src\static\primeraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(primer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\segundaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(segundo_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\\terceraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(tercer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\cuartaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(cuarto_cluster_lista_coordenadas.tolist()):
                        img.write(chunk) 
                with open('src\static\quintaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(quinto_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)  
            elif self.nº_camiones == 6:
                with open('src\static\primeraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(primer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\segundaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(segundo_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\\terceraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(tercer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\cuartaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(cuarto_cluster_lista_coordenadas.tolist()):
                        img.write(chunk) 
                with open('src\static\quintaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(quinto_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)         
                with open('src\static\sextaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(sexto_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
            elif self.nº_camiones == 7:
                with open('src\static\primeraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(primer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\segundaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(segundo_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\\terceraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(tercer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\cuartaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(cuarto_cluster_lista_coordenadas.tolist()):
                        img.write(chunk) 
                with open('src\static\quintaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(quinto_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)         
                with open('src\static\sextaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(sexto_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\septimaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(septimo_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
            elif self.nº_camiones == 8:
                with open('src\static\primeraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(primer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\segundaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(segundo_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\\terceraruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(tercer_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\cuartaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(cuarto_cluster_lista_coordenadas.tolist()):
                        img.write(chunk) 
                with open('src\static\quintaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(quinto_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)         
                with open('src\static\sextaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(sexto_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\septimaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(septimo_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)
                with open('src\static\octabaruta.jpg', 'wb') as img:
                    for chunk in pinta_mapa(octavo_cluster_lista_coordenadas.tolist()):
                        img.write(chunk)

        saca_jpj() 

        def suma_tiempo(cluster):
            suma_t = [] 
            for i in cluster[0]:
                suma_t.append(int(i[0]))  
            suma_tiempos = 0
            for i in suma_t:
                suma_tiempos  += i
            return suma_tiempos 

        def suma_distancia(cluster):
            suma_d = [] 
            for i in cluster[1]:
                suma_d.append(float(i[0:3]))  
            suma_distancias = 0
            for i in suma_d:
                suma_distancias  += i
            return suma_distancias 

        if self.nº_camiones == 1:
            l_ruta_total1=[]
            uno = imprime_r(primer_cluster_lista_coordenadas.tolist(),l_ruta_total1) 
            self.dis1 = round(suma_distancia(uno),2)
            self.tie1 = suma_tiempo(uno)
            self.rut1 = l_ruta_total1
            return  self.dis1 ,self.tie1 ,self.rut1
        elif self.nº_camiones == 2:
            l_ruta_total1=[]
            uno = imprime_r(primer_cluster_lista_coordenadas.tolist(),l_ruta_total1)   
            l_ruta_total2=[]
            dos = imprime_r(segundo_cluster_lista_coordenadas.tolist(),l_ruta_total2)
            self.dis1 = round(suma_distancia(uno),2)
            self.tie1 = suma_tiempo(uno)
            self.rut1 = l_ruta_total1
            self.dis2 = round(suma_distancia(dos),2)
            self.tie2 = suma_tiempo(dos)
            self.rut2 = l_ruta_total2




            return  self.dis1 ,self.tie1 ,self.rut1, self.dis2 ,self.tie2 ,self.rut2 
        elif self.nº_camiones == 3:
            l_ruta_total1=[]
            uno = imprime_r(primer_cluster_lista_coordenadas.tolist(),l_ruta_total1)   
            l_ruta_total2=[]
            dos = imprime_r(segundo_cluster_lista_coordenadas.tolist(),l_ruta_total2)  
            l_ruta_total3=[]
        elif self.nº_camiones == 4:
            l_ruta_total1=[]
            uno = imprime_r(primer_cluster_lista_coordenadas.tolist(),l_ruta_total1)  
            l_ruta_total2=[]
            dos = imprime_r(segundo_cluster_lista_coordenadas.tolist(),l_ruta_total2)    
            l_ruta_total3=[]
            tres = imprime_r(tercer_cluster_lista_coordenadas.tolist(),l_ruta_total3)   
            l_ruta_total4=[]
            cuatro = imprime_r(cuarto_cluster_lista_coordenadas.tolist(),l_ruta_total4) 
        elif self.nº_camiones == 5:
            l_ruta_total1=[]
            uno = imprime_r(primer_cluster_lista_coordenadas.tolist(),l_ruta_total1)   
            l_ruta_total2=[]
            dos = imprime_r(segundo_cluster_lista_coordenadas.tolist(),l_ruta_total2)  
            l_ruta_total3=[]
            tres = imprime_r(tercer_cluster_lista_coordenadas.tolist(),l_ruta_total3)  
            l_ruta_total4=[]
            cuatro = imprime_r(cuarto_cluster_lista_coordenadas.tolist(),l_ruta_total4)  
            l_ruta_total5=[]
            cinco = imprime_r(quinto_cluster_lista_coordenadas.tolist(),l_ruta_total5)    
        elif self.nº_camiones == 6:
            l_ruta_total1=[]
            uno = imprime_r(primer_cluster_lista_coordenadas.tolist(),l_ruta_total1)
            l_ruta_total2=[]
            dos = imprime_r(segundo_cluster_lista_coordenadas.tolist(),l_ruta_total2) 
            l_ruta_total3=[]
            tres = imprime_r(tercer_cluster_lista_coordenadas.tolist(),l_ruta_total3)   
            l_ruta_total4=[]
            cuatro = imprime_r(cuarto_cluster_lista_coordenadas.tolist(),l_ruta_total4)
            l_ruta_total5=[]
            cinco = imprime_r(quinto_cluster_lista_coordenadas.tolist(),l_ruta_total5)  
            l_ruta_total6=[]
            seis = imprime_r(sexto_cluster_lista_coordenadas.tolist(),l_ruta_total6)  
        elif self.nº_camiones == 7:
            l_ruta_total1=[]
            uno = imprime_r(primer_cluster_lista_coordenadas.tolist(),l_ruta_total1)  
            l_ruta_total2=[]
            dos = imprime_r(segundo_cluster_lista_coordenadas.tolist(),l_ruta_total2)  
            l_ruta_total3=[]
            tres = imprime_r(tercer_cluster_lista_coordenadas.tolist(),l_ruta_total3) 
            l_ruta_total4=[]
            cuatro = imprime_r(cuarto_cluster_lista_coordenadas.tolist(),l_ruta_total4)    
            l_ruta_total5=[]
            cinco = imprime_r(quinto_cluster_lista_coordenadas.tolist(),l_ruta_total5)   
            l_ruta_total6=[]
            seis = imprime_r(sexto_cluster_lista_coordenadas.tolist(),l_ruta_total6)    
            l_ruta_total7=[]
            siete = imprime_r(septimo_cluster_lista_coordenadas.tolist(),l_ruta_total7)   
        elif self.nº_camiones == 8:
            l_ruta_total1=[]
            uno = imprime_r(primer_cluster_lista_coordenadas.tolist(),l_ruta_total1)  
            l_ruta_total2=[]
            dos = imprime_r(segundo_cluster_lista_coordenadas.tolist(),l_ruta_total2)
            l_ruta_total3=[]
            tres = imprime_r(tercer_cluster_lista_coordenadas.tolist(),l_ruta_total3)   
            l_ruta_total4=[]
            cuatro = imprime_r(cuarto_cluster_lista_coordenadas.tolist(),l_ruta_total4)   
            l_ruta_total5=[]
            cinco = imprime_r(quinto_cluster_lista_coordenadas.tolist(),l_ruta_total5)  
            l_ruta_total6=[]
            seis = imprime_r(sexto_cluster_lista_coordenadas.tolist(),l_ruta_total6)  
            l_ruta_total7=[]
            siete = imprime_r(septimo_cluster_lista_coordenadas.tolist(),l_ruta_total7)    
            l_ruta_total8=[]
            ocho = imprime_r(octavo_cluster_lista_coordenadas.tolist(),l_ruta_total8)    


                 
  


            

