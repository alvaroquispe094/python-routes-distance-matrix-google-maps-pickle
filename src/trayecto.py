class Trayecto(object): # una ruta generica
    def __init__(self,clave):
        '''contructor de la clase ruta.'''
        self.rutas = []
        self.id = clave
        self.tiempoTotal=0
        self.distanciaTotal=0
        
    def getClave(self):
        return self.id
        
    def getTiempoTotal(self):
        total = 0
        for ruta in self.rutas:
            total = total +  ruta.getTiempo()
            
        return total
    
    def getDistancaTotal(self):
        total = 0
        for ruta in self.rutas:
            total = total + ruta.getDistancia() 
            
        return total
    def obtenerUltimaCiudad(self):
        ultima = self.rutas[len(self.rutas)-1].getDestino()
        return ultima
    
    def obtenerPrimeraCiudad(self):
        primera = self.rutas[0].getOrigen()
        return primera
    
    def getListadoRutas(self):
        return self.rutas
    
    def agregarRuta(self,ruta):
        self.rutas.append(ruta)  
        
    def __repr__(self):
            return '[Trayecto: %s; %s km; %s seg]' %(self.id, self.getDistancaTotal(),\
                                                 self.getTiempoTotal())      
        
