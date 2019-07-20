import googlemaps
from configuracion import*
from ruta import Ruta
from trayecto import Trayecto
class gestorDeTrayectos(object):
    
    def crearTrayecto(self,origen,destino,clave):
        o1=origen
        d1=destino
        if(origen==destino):
            raise Exception("Origen y destino son iguales")
        
        print("Creando trayecto......")
        distancia = self.solicitarDistancia(o1,d1)
        tiempo = self.solicitarTiempo(o1,d1)
        
        ruta = Ruta(o1,d1,distancia,tiempo)#instancia de ruta para agregar al trayecto
        
        trayecto = Trayecto(clave)
        trayecto.agregarRuta(ruta)
        
        print("Distancia: ",distancia," km")
        print("Tiempo: ",tiempo," segundos")
        return trayecto
        
    def agregarCiudadAlFinal(self,trayecto,ciudad):
        print("Creando ruta al final....")
        origen = trayecto.obtenerUltimaCiudad()
        if(origen==ciudad):
            raise Exception("Origen y destino son iguales")   
        distancia = self.solicitarDistancia(origen,ciudad)
        tiempo = self.solicitarTiempo(origen,ciudad)
        ruta = Ruta(origen,ciudad,distancia,tiempo)#instancia de ruta para agregar al trayecto
        trayecto.agregarRuta(ruta)

    def agregarCiudadEnMedio(self,trayecto,cIn,cOut):
        print("Agregando ciudad al medio del trayecto......")
        encontrado = False
        for i in range(len(trayecto.rutas)):
            if(trayecto.rutas[i].destino==cIn):
                encontrado = True
                indice= i
                
        if(encontrado==True):
            #trayecto.rutas[indice].setDestino(cOut)
            dPre = self.solicitarDistancia(trayecto.rutas[indice].getOrigen(),cOut)
            tPre = self.solicitarTiempo(trayecto.rutas[indice].getOrigen(),cOut)
            d = self.solicitarDistancia(cOut,cIn)
            t = self.solicitarTiempo(cOut,cIn)
            trayecto.rutas[indice].setDestino(cOut)
            trayecto.rutas[indice].setDistancia(dPre)
            trayecto.rutas[indice].setTiempo(tPre)
            r = Ruta(cOut,cIn,d,t)
            if((len(trayecto.rutas)-1)==indice):
                trayecto.rutas.append(r)
            else:    
                trayecto.rutas.insert(indice+1,r)
            
        else:
            print("La ciudad: ",cIn,"No se encuentra en el trayecto")    
    def isCiudad(self,ciudad):
        print("")
            
    def concatenarTrayecto(self,trayecto1,trayecto2):
        print("Concatenando trayectos......")
        origen = trayecto1.obtenerUltimaCiudad()
        destino = trayecto2.obtenerPrimeraCiudad()
        if(origen==destino):
            raise Exception("Origen y destino son iguales")
        #dPre = self.solicitarDistancia(trayecto1.rutas[len(trayecto1.rutas)-1].getOrigen(),origen)
        #tPre = self.solicitarTiempo(trayecto1.rutas[len(trayecto1.rutas)-1].getOrigen(),origen)
        d = self.solicitarDistancia(origen,destino)
        t = self.solicitarTiempo(origen,destino)
        #trayecto1.rutas[len(trayecto1.rutas)-1].setDestino(origen)
        #trayecto1.rutas[len(trayecto1.rutas)-1].setDistancia(dPre)
        #trayecto1.rutas[len(trayecto1.rutas)-1].setTiempo(tPre)
        r = Ruta(origen,destino,d,t)
        trayecto1.rutas.append(r)
        trayecto1.rutas = trayecto1.rutas + trayecto2.rutas
        
    def compararTrayecto(self,trayecto1,trayecto2):
        #t1 = trayecto1
        #t2 = trayecto2
        print("Comparando trayectos......")  
        print("Trayecto:",trayecto1.getClave())
        print("  ",trayecto1.rutas[0].getOrigen())
        for r in trayecto1.rutas:
            print("  ",r.getDestino()) 
        t1 = trayecto1.getTiempoTotal()
        d,h,m = self.obtenerTiempo(t1)  
        print("[distancia:",trayecto1.getDistancaTotal(),"km]")    
        print("[Tiempo:",d,"dias",h,"horas",m,"min]")
        print("-------------VS---------------")
        print("Trayecto:",trayecto2.getClave())
        print("  ",trayecto2.rutas[0].getOrigen())
        for r in trayecto2.rutas:
            print("  ",r.getDestino()) 
        t1 = trayecto2.getTiempoTotal()
        d,h,m = self.obtenerTiempo(t1)  
        print("[distancia:",trayecto2.getDistancaTotal(),"km]")    
        print("[Tiempo:",d,"dias",h,"horas",m,"min]")
        
    def mostrarTrayecto(self,trayecto): 
        print("Mostrando trayecto.......")
        print("Trayecto:",trayecto.getClave())
        print("  ",trayecto.rutas[0].getOrigen())
        for r in trayecto.rutas:
            print("  ",r.getDestino()) 
        t1 = trayecto.getTiempoTotal()
        d,h,m = self.obtenerTiempo(t1)  
        print("[distancia:",trayecto.getDistancaTotal(),"km]")    
        print("[Tiempo:",d,"dias",h,"horas",m,"min]")
        print("")
        
    def mostrarRutas(self,trayecto): 
        print("Mostrando rutas.......")
        print("Trayecto:",trayecto.getClave())
        for r in trayecto.rutas:
            t1 = r.getTiempo()
            d,h,m = self.obtenerTiempo(t1)
            print("  [ruta: ",r.getOrigen(),",",r.getDestino(),"]")  
            print("  [distancia:",r.getDistancia(),"km]")    
            print("  [Tiempo:",d,"dias",h,"horas",m,"min]")
            print("")
        
    def listarTrayectosCalculados(self,trayectos): 
        print("Listado trayectos calculados.......")
        for t in trayectos:
            print(t)
            for r in t.rutas:
                print("  ",r)
    
    def obtenerTiempo(self,segundos):
        t1 = segundos
        dias=int(t1/24/60/60)
        t1=t1-(dias*24*60*60)
        horas=int(t1/60/60)
        t1=t1-horas*60*60
        min=int(t1/60)
        return dias,horas,min
        
    def existeRuta(self):
        return True
    
    def solicitarDistancia(self,origen,destino):
        gmaps=googlemaps.Client(key=KEY)
        
        ruta1 = gmaps.distance_matrix(origen,destino)
        d1 = ruta1['rows'][0]['elements'][0]['distance']['value']
        distancia=d1/1000
        return distancia
    
    def solicitarTiempo(self,origen,destino):
        gmaps=googlemaps.Client(key=KEY) 
        ruta1 = gmaps.distance_matrix(origen,destino)
        t1 = ruta1['rows'][0]['elements'][0]['duration']['value']
        
        return t1