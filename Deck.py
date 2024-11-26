from CartaMonstruo import *
from CartaTrampa import *
from CartaMagica import *
from TipoAtributo import *
from TipoMonstruo import *
import random as rd

class Deck:
  @staticmethod
  def crearDeck(self):
    l_mons=[]
    l_mag=[]
    l_tram=[]
    archivo= open("cartasCreadas",'r')
    for linea in archivo.strip().split(','):
      tipodecarta,nombre,descripcion,posicion,orientacion,tipomonstruo,tipoatributo,ataque,defensa,= linea
      posicion= posicion.split('.')[-1]
      orientacion= orientacion.split('.')[-1]
      tipomonstruo= tipomonstruo.split('.')[-1]
      tipoatributo= tipoatributo.split('.')[-1]
      ataque=int(ataque)
      defensa=int(defensa)
      if(tipodecarta=="CartaMonstruo"):
        c= CartaMonstruo(nombre,descripcion,Posicion[posicion],Orientacion[orientacion],TipoMonstruo[tipomonstruo],TipoAtributo[tipoatributo],defensa,ataque)
        l_mons.append(c)
      if(tipodecarta=="CartaMagica"):
        c= CartaMagica(nombre, descripcion, Posicion[posicion], Orientacion[orientacion], ataque, defensa)
        l_mag.append(c)
      if(tipodecarta=="CartaTrampa"):
        c= CartaTrampa(nombre, descripcion, Posicion[posicion], Orientacion[orientacion],TipoAtributo[tipoatributo])
        l_tram.append(c)
      archivo.close()
      deck=rd.sample(l_mons,20)+rd.sample(l_mag,5)+rd.sample(l_tram,5)
      return deck