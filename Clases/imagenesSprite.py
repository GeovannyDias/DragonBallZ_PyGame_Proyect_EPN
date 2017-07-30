import pygame
import sys
from pygame.locals import *




class CargarImagenJugador():
	ImagenGohanMystic = pygame.image.load("Imagenes\Sprite\DBZ\gohanMystic.gif")
	arrayAnim=[]
	listaDeArrayAnim=[]
	def __init__(self):
		self.transparente = self.ImagenGohanMystic.get_at((0, 0))
		self.ImagenGohanMystic.set_colorkey(self.transparente)

	def ImagenGohanMystic_All(self):
		self.ImagenGohanMystic1()
		self.ImagenGohanMystic2()
		self.ImagenGohanMystic3()
		self.ImagenGohanMystic4()

		return self.listaDeArrayAnim


	def ImagenGohanMystic1(self):#Estado Estatico
		self.arrayAnim=[]
		imgX = [20,58,102,145] 
		recX = [32,32,32,32]
		for i in range (len(imgX)):
			#subsurface((posicion en la imagen.gif x,y),(dimension del rectangulo x,y))	
			self.arrayAnim.append(self.ImagenGohanMystic.subsurface((imgX[i],11,recX[i],66)))
		#subsurface((posicion en la imagen.gif x,y),(dimension del rectangulo x,y))
		#self.arrayAnim.append(self.ImagenGohanMystic.subsurface(( (imgX[0],368),(30,136) )))#((imgX,imgY),(recX,recY))
		self.listaDeArrayAnim.append(self.arrayAnim)
		return self.listaDeArrayAnim

	def ImagenGohanMystic2(self):#Poder al aire
		self.arrayAnim=[]
		imgX = [20,64,112,159,213,274]
		recX = [30,38,38,41,48,50]

		for i in range (len(imgX)):
			self.arrayAnim.append(self.ImagenGohanMystic.subsurface((imgX[i],368,recX[i],136)))#((imgX,imgY),(recX,recY))
		
		self.listaDeArrayAnim.append(self.arrayAnim)
		return self.listaDeArrayAnim

	def ImagenGohanMystic3(self):
		self.arrayAnim=[]
		imgX = [333,271,210,122,58,17]
		recX = [48,48,49,74,50,30]
		for i in range (len(imgX)):			
			self.arrayAnim.append(self.ImagenGohanMystic.subsurface((imgX[i],2156,recX[i],67)))

		self.listaDeArrayAnim.append(self.arrayAnim)
		return self.listaDeArrayAnim

	def ImagenGohanMystic4(self):
		self.arrayAnim=[]
		imgX = [21,60,129,212,281]
		recX = [35,59,77,60,35]
		for i in range (len(imgX)):			
			self.arrayAnim.append(self.ImagenGohanMystic.subsurface((imgX[i],2339,recX[i],63)))

		self.listaDeArrayAnim.append(self.arrayAnim)
		return self.listaDeArrayAnim




	
class CargarImagenEnemigo():
	ImagenCellPerfect = pygame.image.load("Imagenes\Sprite\DBZ\cellperfect.gif")
	arrayAnim=[]
	def __init__(self):
		self.transparente = self.ImagenCellPerfect.get_at((0, 0))
		self.ImagenCellPerfect.set_colorkey(self.transparente)

	
	def ImagenCellPerfect1(self):#Estado Estatico
		imgX = [30,85,137,190] 
		recX = [40,40,40,40]
		for i in range (len(imgX)):
			self.arrayAnim.append(self.ImagenCellPerfect.subsurface((imgX[i],10,recX[i],84)))
		
		return self.arrayAnim

	def ImagenCellPerfect2(self):#Poder al aire
		imgX = [6,60,117,187,251]
		recX = [34,48,57,47,54]

		for i in range (len(imgX)):
			self.arrayAnim.append(self.ImagenCellPerfect.subsurface((imgX[i],192,recX[i],88)))#((imgX,imgY),(recX,recY))
		
		return self.arrayAnim

	def ImagenCellPerfect3(self):		
		imgX = [27,93,162,225]
		recX = [52,63,46,62]
		for i in range (len(imgX)):			
			self.arrayAnim.append(self.ImagenCellPerfect.subsurface((imgX[i],1060,recX[i],84)))

		return self.arrayAnim

	def ImagenCellPerfect4(self):		
		imgX = [36,94,157,227,301]
		recX = [45,49,68,65,61,]
		for i in range (len(imgX)):			
			self.arrayAnim.append(self.ImagenCellPerfect.subsurface((imgX[i],216,recX[i],76)))

		return self.arrayAnim


	








