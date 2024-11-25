from enum import (Enum)
import random as rd
class TipoAtributo (Enum):
  OSCURIDAD = 1
  LUZ = 2
  TIERRA = 3
  AGUA = 4
  FUEGO = 5
  VIENTO = 6

class TipoCarta (Enum):
  MONSTRUO = 1
  MAGICA = 2
  TRAMPA = 3

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
  def __init__(self, nombre, descripcion, posicion,orientacion): #jdas
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
    self._defensa = defensa
    self._ataque = ataque

  def getTipo (self):
      return self.__tipo
  def setTipo (self, tipo):
      self.__tipo = tipo
  def getAtributo (self):
      return self.__atributo
  def setAtributo (self,atributo):
      self.__atributo = atributo
  def getAtaque (self):
      return self._ataque
  def setAtaque (self, ataque):
      self._ataque = ataque
  def getDefena (self):
      return self._defensa
  def setDefensa (self, defensa):
      self._defensa = defensa
    
  def cambiarPosicion(self,posicion):
      if self.__orientacion == Orientacion.ARRIBA:
        self.__posicion = posicion
  def modoAtaque(self):
      self.__orientacion = Orientacion.ARRIBA
  def modoDefensa(self):
      self.__orientacion = Orientacion.ABAJO

class CartaMagica (Carta):
  def __init__(self, nombre, descripcion, posicion, orientacion, ataque, defensa):
    super().__init__(nombre, descripcion, posicion, orientacion)
    self._defensa = defensa
    self._ataque = ataque

  def getAtaque (self):
    return self._ataque
  def setAtaque (self, ataque):
    self._ataque = ataque
  def getDefena (self):
    return self._defensa
  def setDefensa (self, defensa):
    self._defensa = defensa
    
  def incrementaAtaque (self, carta):
    nuevo_ataque = carta.getAtaque + self._ataque
    carta.setAtaque(nuevo_ataque)
      
  def incrementaDef (self, carta):
    nueva_defensa = carta.getDefensa() + self._defensa
    carta.setDefensa(nueva_defensa)

class CartaTrampa (Carta):
  def __init__(self, nombre, descripcion, posicion, orientacion,atributo):
    super().__init__(nombre, descripcion, posicion, orientacion)
    self.__atributo = atributo
  def getAtributo (self):
      return self.__atributo
  def setAtributo (self,atributo):
      self.__atributo = atributo

from cartasCreadas import listaCartasCreadas
class Deck:
  def crearDeck(self):#crea lista de cartas
    l_mons=[]
    l_mag=[]
    l_tram=[]
    for c in listaCartasCreadas:
      if isinstance(c,CartaMonstruo):
        l_mons.append(c)
      if isinstance(c,CartaMagica):
        l_mag.append(c)
      if isinstance(c,CartaTrampa):
        l_tram.append(c)
      deck= rd.sample(l_mons,20)+rd.sample(l_mag,5)+rd.sample(l_tram,5)
    return deck

   
class Tablero:
  def _init_(self):
    self.cartas= []



class Jugador:
  def __init__(self,nombre,deck,tablero,mano):
    self.__nombre = nombre
    self.__deck = Deck.crearDeck(self)
    self.__puntos = 4000
    self.__tablero = Tablero()
    self.__mano= [deck.pop(),deck.pop(),deck.pop(),deck.pop(),deck.pop()]
  def getNombre(self):
    return self.__nombre
  def setNombre (self, nombre):
    self.__nombre = nombre
  def getDeck (self):
    return self.__deck
  def getPuntos (self):
    return self.__puntos
  def setPuntos (self, puntos):
    self.__puntos = puntos
  def tomarCarta(self):
    return self.__deck.pop()
  def contar_cartas_tipo(self, tipo):
    for carta in self.__mano:
      return sum(isinstance(carta, tipo))
  def agregarCartaTablero(self,carta):
    if (len(self.__tablero)<=6):
      if isinstance(carta,CartaMonstruo):
        if self.contar_cartas_tipo(CartaMonstruo) < 3:
          self.__tablero.append(carta)
          self.__mano.remove(carta)
        elif isinstance(carta, (CartaMagica, CartaTrampa)):
          if self.contar_cartas_tipo(CartaMagica) + self.contar_cartas_tipo(CartaTrampa) < 3:
            self.__tablero.append(carta)
            self.__mano.remove(carta)
  def seleccionarCartaTablero(self,nombre):
    for c in self.__tablero:
      if (c.getNombre()==nombre):
        return c
