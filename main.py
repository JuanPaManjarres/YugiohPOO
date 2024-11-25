from enum import (Enum)
from cartasCreadas import cartas
import random as rd

class TipoAtributo (Enum):
  OSCURIDAD = 1
  LUZ = 2
  TIERRA = 3
  AGUA = 4
  FUEGO = 5
  VIENTO = 6

class TipoMonstruo (Enum):
  L = 1 #Lanazador de Conjuros
  D = 2 #Dragon
  Z = 3 #Zombi
  G = 4 #Guerrero
  B = 5 #Bestia
  O = 6 #Demonio

class Orientacion (Enum):
  ARRIBA = 1
  ABAJO = 2

class Posicion (Enum):
  VERTICAL = 1
  HORIZONTAL = 2

class Carta:
  def __init__(self, nombre, descripcion, posicion,orientacion): #Constructor
    self.__nombre = nombre #__ es para acceso privado
    self.__descripcion = descripcion
    self.__posicion = posicion
    self.__orientacion = orientacion

  #getters y setters
  def getNombre (self):
    return self.__nombre
  def setNombre (self, nombre):
    self.__nombre = nombre
  def getDescripcion (self):
    return self.__descripcion
  def setDescripcion (self, descripcion):
    self.__descripcion = descripcion
  def getOrientacion (self):
    return self.__orientacion
  def setOrientacion (self, orientacion):
    self.__orientacion = orientacion
  def getPosicion (self):
    return self.__posicion
  def setPosicion (self, posicion):
    self.__posicion = posicion
 
class CartaMonstruo(Carta):
  def __init__(self, nombre, descripcion, posicion,orientacion,tipo, atributo, defensa, ataque): #constructor
    super().__init__(nombre, descripcion, posicion,orientacion)
    self.__tipo = tipo
    self.__atributo = atributo
    self.__defensa = defensa
    self.__ataque = ataque

  def getTipo (self):
      return self.__tipo
  def setTipo (self, tipo):
      self.__tipo = tipo
  def getAtributo (self):
      return self.__atributo
  def setAtributo (self,atributo):
      self.__atributo = atributo
  def getAtaque (self):
      return self.__ataque
  def setAtaque (self, ataque):
      self.__ataque = ataque
  def getDefensa (self):
      return self.__defensa
  def setDefensa (self, defensa):
      self.__defensa = defensa
    
  def cambiarPosicion(self,posicion):
      if self.__orientacion == Orientacion.ARRIBA:
        self.__posicion = posicion
  def modoAtaque(self):
      self.__orientacion = Orientacion.ARRIBA
  def modoDefensa(self):
      self.__orientacion = Orientacion.ABAJO
  def muere(self): #NOT SURE
    return True

class CartaMagica (Carta):
  def __init__(self, nombre, descripcion, posicion, orientacion,ataque, defensa,tipo,carta_monstruo):
    super().__init__(nombre, descripcion, posicion, orientacion)
    self.__tipo = tipo
    self.__carta_montruo = carta_monstruo
    self.__defensa = defensa
    self.__ataque = ataque
  
  def getTipo (self):
    return self.__tipo
  def getAtaque (self):
    return self.__ataque
  def setAtaque (self, ataque):
    self._ataque = ataque
  def getDefena (self):
    return self.__defensa
  def setDefensa (self, defensa):
    self.__defensa = defensa
    
  def usar (self,carta_monstruo):
    if self.__tipo == carta_monstruo.getTipo():
      if self.__defensa == 0:
        nuevo_ataque = carta_monstruo.getAtaque() + self._ataque
        carta_monstruo.setAtaque(nuevo_ataque)
      if self.__ataque == 0:
        nueva_defensa = carta_monstruo.getDefensa() + self.__defensa
        carta_monstruo.setDefensa(nueva_defensa)
  
  def destruir (self,carta_monstruo):#NOT SURE
    if carta_monstruo.muere():
      return True

  def __str__(self):
    if self.__defensa == 0:
      return f"{self.__nombre} , incrementa en {self._ataque} el ataque de monstruos de tipo {self.__tipo}"
    if self.__ataque == 0:
      return f"{self.__nombre} , incrementa en {self.defensa} la defensa de monstruos de tipo {self.__tipo}"

class CartaTrampa (Carta):
  def __init__(self, nombre, descripcion, posicion, orientacion,atributo,carta_monstruo):
    super().__init__(nombre, descripcion, posicion, orientacion)
    self.__atributo = atributo

  def getAtributo (self):
      return self.__atributo
  def setAtributo (self,atributo):
      self.__atributo = atributo
from cartasCreadas import cartas
class Deck:
  def crearDeck(self,archivo):
    l_mons=[]
    l_mag=[]
    l_tram=[]
    archivo= open(archivo,'r')
    for linea in archivo.strip().split(','):
      nombre,descripcion,tipodecarta,posicion,orientacion,ataque,defensa,tipomonstruo,tipoatributo= linea
      if(tipodecarta==TipoCarta.MONSTRUO):
        c= CartaMonstruo(nombre,descripcion,posicion,orientacion,tipomonstruo,tipoatributo,defensa,ataque)
        l_mons.append(c)
      if(tipodecarta==TipoCarta.MAGICA):
        c= CartaMagica(nombre, descripcion, posicion, orientacion, ataque, defensa)
        l_mag.append(c)
      if(tipodecarta==TipoCarta.TRAMPA):
        c= CartaTrampa(nombre, descripcion, posicion, orientacion,tipoatributo)
        l_tram.append(c)
      archivo.close()
      deck=rd.sample(l_mons,20)+rd.sample(l_mag,5)+rd.sample(l_tram,5)
      return deck

class Tablero:
  def _init_(self):
    self.cartas= []
  def contar_cartas_tipo(self, tipo):
    for carta in self.cartas:
      return sum(isinstance(carta, tipo))
  def agregarCarta(self,carta):
    if (len(cartas)<=6):
      if isinstance(carta,CartaMonstruo):
        if self.contar_cartas_tipo(Monstruo) < 3:
          self.cartas.append(carta)
        elif isinstance(carta, (Magica, Trampa)):
          if self.contar_cartas_tipo(Magica) + self.contar_cartas_tipo(Trampa) < 3:
            self.cartas.append(carta)
  def seleccionarCarta(self,nombre):
    for c in self.cartas:
      if (c.getNombre()==nombre):
        return c


class Jugador:
  def __init__(self,nombre,deck):
    self.__nombre = nombre
    self.__deck = deck
    self.__puntos = 4000
  def getNombre(self):
    return self.__nombre
  def setNombre (self, nombre):
    self.__nombre = nombre
  def getDeck (self):
    return self.__deck
  def setDeck (self, deck):
    self.__deck = deck
  def getPuntos (self):
    return self.__puntos
  def setPuntos (self, puntos):
    self.__puntos = puntos



#Clase Juego 
class Juego():
  def __init__(self, Lista_tableros, Jugador): #donde las lista tableros y jugadores tienen 2 elementos
    self.__tableros = Lista_tableros
    self.__jugador = Jugador
    self.__turno = 0
  def faseDeclararBatalla(self, carta_oponente):
    if self.__turno < 2: 
      print("No se puede declarar batalla en el primer turno")
    else: #El turno es igual a 2 o mayor
      if(carta_oponente.posicion == Posicion.VERTICAL): #si es verdad, entonces quiere decir que esta en ataque
        if():    # se comparan los puntos de ataque de la carta de ataque al la carta atacada
    
      # else: #Si es falso, quiere decir que esta en defensa
