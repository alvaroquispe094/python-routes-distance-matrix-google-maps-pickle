class Ruta(object): # una ruta generica
    def __init__(self, origen, destino, distancia, tiempo):
        '''contructor de la clase ruta.'''
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.tiempo = tiempo

    def getOrigen(self):
        return self.origen
    def setOrigen(self,origen):
        self.origen = origen
        
    def getDestino(self):
        return self.destino
    def setDestino(self,destino):
        self.destino = destino
        
    def getDistancia(self):
        return self.distancia
    def setDistancia(self,distancia):
        self.distancia = distancia
        
    def getTiempo(self):
        return self.tiempo
    def setTiempo(self,tiempo):
        self.tiempo = tiempo
        
    def isCiudad(self,ciudad):
        if(ciudad==self.getDestino()):
            return True
        else:
            return False
    '''metodo toString en python'''
    def __repr__(self):
            return '[ruta: %s; %s; %s km; %s seg]' %(self.origen, self.destino, self.distancia, self.tiempo)
