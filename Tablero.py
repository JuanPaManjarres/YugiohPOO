from Carta import *
from Jugador import *
class Tablero:
  def init(self):
    self.__cartasjugador = [[None, None, None], [None, None, None]] 
  def _str_(self):
    print(f"Tablero
            \nMonstruo: [{self.__cartasjugador[0][0]}] [{self.__cartasjugador[0][1]}] [{self.__cartasjugador[0][2]}]
            \nMagicas: [{self.__cartasjugador[1][0]}] [{self.__cartasjugador[1][1]}] [{self.__cartasjugador[1][2]}]
            ")
  def seleccionarCarta(self,indice):
    print(self._str_())
    return self.__cartasjugador[1,indice]#Retorna la Carta del indice indicado
  def agregarCartaTablero(self,carta):
      if isinstance(carta,CartaMonstruo):
        if None in self.__cartasjugador[0]:
          indice= self.__cartasjugador[0].index(None)
          self.__cartasjugador[0][indice]= carta
        else:
          print("Espacio para carta tipo Monstruo lleno en el tablero")
      elif isinstance(carta,CartaMagica) or isinstance(carta,CartaMonstruo):
        if None in self.__cartasjugador[1]:
          indice= self.__cartasjugador[1].index(None)
          self.__cartasjugador[1][indice]= carta
        else:
          print("Espacio para cartas tipo Magica o Trampa lleno en el tablero")