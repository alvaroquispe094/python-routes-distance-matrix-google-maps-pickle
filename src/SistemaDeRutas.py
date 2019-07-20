from gestorOperaciones import gestorDeTrayectos
import pickle

def obtenerTrayectos():
        listado = pickle.load( open( "lista_trayectos.p", "rb" ) )
        return listado 
    
def guardarTrayectos(lista):        
        pickle.dump( lista, open( "lista_trayectos.p", "wb" ) )   
        print("Se han guardado los datos en Disco") 

class SistemaDeRutas(object):
    def __init__(self):
        self.trayectos =[]
    
    def agregarTrayecto(self,trayecto):
        self.trayectos.append(trayecto)
        
    def buscarTrayecto(self,clave):
        if(type(clave)!=int):
            raise Exception("Id de trayecto invalido")
        trayecto = False   
        for t in self.trayectos:
            if(t.id==clave):
                trayecto = t
                return trayecto
        return trayecto    
            
    def guardarTrayectos(self,lista):        
        pickle.dump( lista, open( "lista_trayectos.p", "wb" ) )
    
    def getListado(self):
        return self.trayectos
    def setListado(self,lista):
        self.trayectos = lista
        
    def listarTrayectos(self):
        for t in self.trayectos:
            print(t)
            for r in t.rutas:
                print("  ",r)   
        
if __name__ == '__main__':
    sistema = SistemaDeRutas()
    gestor = gestorDeTrayectos()
    '''Carga en el sistema la lista de trayectos y toma excetion si es la primera vez en el sistema'''
    try:
        lista = obtenerTrayectos()
        sistema.setListado(lista)
    except Exception as e:
        print("En el sistema por primera vez")
    
    while True:
        try:
            print("*******************************")
            print("*Selecciona una opcion:       *")
            print("*1.Crear un trayecto          *")
            print("*2.Agregar ciudad al final    *")
            print("*3.Agregar ciudad intermedia  *")
            print("*4.Concatenar dos trayectos   *")
            print("*5.Comparar dos trayects      *")
            print("*6.Mostrar trayecto           *")
            print("*7.Mostrar rutas              *")
            print("*8.Listar trayectos calculados*")
            print("*9.Salir                      *")
            print("*******************************")
        
            opcionMenu = int(input("inserta un numero valor: "))
            if opcionMenu==1:
                try:
                    print("Crear trayecto.....")  
                    
                    ori = input("Ingrese la ciudad origen: ")
                    desti = input("Ingrese la ciudad destino: ")
                    trayecto = gestor.crearTrayecto(ori,desti,len(sistema.trayectos)+1)
                    sistema.agregarTrayecto(trayecto)
                    
                except KeyError:
                    print("Error al crear trayecto,no existe una ruta")     
                except Exception as e:
                    print("error:",e) 
                
            elif opcionMenu==2:
                try:
                    print ("agregar ciudad  al final.....")
                    print("Ingrese id de trayecto para agregar ruta al final")
                    clave = int(input())
                    t1 = sistema.buscarTrayecto(clave)
                    if(t1!=False):
                        ciudad = input("Ingrese la ciudad a agregar: ")
                        gestor.agregarCiudadAlFinal(t1, ciudad)
                    else:
                        print("No se encontro el trayecto buscado") 
                except ValueError:
                    print("Id Invalido,ingrese nuevamente")
                except KeyError:
                    print("Error al agregar ruta al trayecto,no existe una ruta")              
                except Exception as e:
                    print("Error: ",e)  
                
            elif opcionMenu==3:
                try:
                    print ("agregar ciudad al medio.....")
                    clave = int(input("Ingrese id del trayecto para agregar ciudad intermedia: "))
                    cIn = input("Ingrese ciudad del trayecto: ")
                    cOut = input("Ingrese ciudad a agregar al trayecto")
                    t1 = sistema.buscarTrayecto(clave)
                    if(t1!=False):
                        gestor.agregarCiudadEnMedio(t1,cIn,cOut)
                    else:
                        print("No se encontro el trayecto buscado")
                except ValueError:
                    print("Id Invalido,ingrese nuevamente")  
                except KeyError:
                    print("Error al agregar ruta al trayecto,no existe una ruta")          
                except Exception as e:
                    print("Se ha producido un error: ",e)
            elif opcionMenu==4:
                try:
                    print("concatenar trayectos.....")
                    print("Ingrese id de trayecto al que se concatenara")
                    clave1 = int(input())
                    print("Ingrese id de trayecto a concatenar")
                    clave2 = int(input())
                    t1 = sistema.buscarTrayecto(clave1)
                    t2 = sistema.buscarTrayecto(clave2)
                    if((t1!=False) and (t2!=False)):
                        gestor.concatenarTrayecto(t1, t2)
                        index = sistema.trayectos.index(t2)
                        del sistema.trayectos[index]
                    else:
                        print("No se encontro uno o ambos trayectos") 
                except KeyError:
                    print("Error al concatenar trayectos,no existe una ruta")        
                except ValueError:
                    print("Id Invalido,ingrese nuevamente")
                except Exception as e:
                    print("Error: ",e)             
                    
            elif opcionMenu==5:
                try:
                    print ("Compara trayectos.....")
                    print("Ingrese id de trayecto a comparar")
                    clave1 = int(input())
                    print("Ingrese id de trayecto a comparar")
                    clave2 = int(input())
                    t1 = sistema.buscarTrayecto(clave1)
                    t2 = sistema.buscarTrayecto(clave2)
                    if((t1!=False) and (t2!=False)):
                        gestor.compararTrayecto(t1, t2)
                    else:
                        print("No se encontro uno o ambos trayectos")  
                except ValueError:
                    print("Id Invalido,ingrese nuevamente")
                except Exception:
                    print("Error",e)    
            elif opcionMenu==6:
                try:
                    print ("Mostrando trayectos.....")
                    #sistema.listarTrayectos()
                    print("Ingrese id de trayecto")
                    clave = int(input())
                    t1 = sistema.buscarTrayecto(clave)
                    if(t1!=False):
                        gestor.mostrarTrayecto(t1)
                    else:
                        print("No se encontro el trayecto buscado")
                except Exception as e:
                    print("Error: ",e) 
            elif opcionMenu==7:
                try:
                    print ("Mostrando rutas.....")
                    #sistema.listarTrayectos()
                    print("Ingrese id de trayecto")
                    clave = int(input())
                    t1 = sistema.buscarTrayecto(clave)
                    if(t1!=False):
                        gestor.mostrarRutas(t1)
                    else:
                        print("No se encontro el trayecto buscado")
                except ValueError:
                    print("Id trayecto Invalido,ingrese nuevamente")        
                except Exception as e:
                    print("Error: ",e) 
            elif opcionMenu==8:
                print ("Listando trayectos calculados.....")
                #sistema.listarTrayectos()
                gestor.listarTrayectosCalculados(sistema.trayectos)
            elif opcionMenu==9:
                lista = sistema.getListado()
                guardarTrayectos(lista)
                #print("Se han guardado los datos en disco")
                break    
        except Exception:
            print("Se produjo un error,elija nuevamente")