import os,sys
import pygame
from pygame.locals import *
import random

def load_image(name,color_key=None):
	try:
		image=pygame.image.load(name)
	except:
		print('Cannot load image:',name)
		sys.exit()
	image=image.convert()
	if color_key is not None:
		if color_key is -1:
			color_key= image.get_at((0,0))
		image.set_colorkey(color_key,RLEACCEL)
	return image,image.get_rect()

def load_sound(name):	
	try:
		sound=pygame.mixer.Sound(name)
	except:
		print('Cannot load Sound:',name)
	return sound
	
def update_all(no):
	car.update(no)
	

class Car(pygame.sprite.Sprite):

	def __init__(self):
		super(Car,self).__init__()
		self.image,self.rect=load_image('car.png',-1)
		self.rect.centerx=401
		self.rect.centery=506
	
	def update(self,state):
		if state:
			self.rect.centerx+=8
		else:
			self.rect.centerx-=8
		if self.rect.left<54:
			self.rect.left=54
		if self.rect.right>680:
			self.rect.right=680
		list=pygame.sprite.spritecollide(car,obstacles,True)
		if len(list):
			sys.exit()

class Obstacle(pygame.sprite.Sprite):

	def __init__(self,lane,type):
		super(Obstacle,self).__init__()
		self.image=None
		self.rect=-100
		self.type=type
		if type is 0:
			self.image,self.rect=load_image('barrier.png',-1)
		if type is 1:
			self.image,self.rect=load_image('police_car.png',-1)
		if type is 2:
			self.image,self.rect=load_image('pothole.png',-1)
		if type is 3:
			self.image,self.rect=load_image('taxi.jpg',-1)
		if type is 4:
			self.image,self.rect=load_image('truck.jpg',(255,255,255))
		if lane is 0:
			self.rect.centerx=172
		if lane is 1:
			self.rect.centerx=327
		if lane is 2:
			self.rect.centerx=487
		if lane is 3:
			self.rect.centerx=645

		self.rect.bottom=0
	
	
	def update(self):
		if self.type is 0:
			self.rect.centery+=speed
		if self.type is 1:
			self.rect.centery+=(speed+speed/2)
		if self.type is 2:
			self.rect.centery+=speed
		if self.type is 3:
			self.rect.centery+=(speed+speed/3)
		if self.type is 4:
			self.rect.centery+=(speed+speed/4)

								
		

			
		
class Tree(pygame.sprite.Sprite):

	def __init__(self,no,nos):
		super(Tree,self).__init__()
		self.image=None
		self.rect=None
		if nos:
			if no:

				self.image,self.rect=load_image('tree.jpg',-1)
			else:
				self.image,self.rect=load_image('treetop.png',-1)
		
			self.rect.centerx=45
			self.rect.centery=50
		else:
			if no:

				self.image,self.rect=load_image('tree.jpg',-1)
			else:
				self.image,self.rect=load_image('treetop.png',-1)
		
			self.rect.centerx=776
			self.rect.centery=50
		
	def update(self):
		self.rect.centery+=speed
		

pygame.init()

screen=pygame.display.set_mode((830,650))
pygame.display.set_caption('Car Crash')

bgname=os.path.join('Requirements','background.png')
background=pygame.image.load(bgname)
background=background.convert()
screen.blit(background,(0,0))
pygame.display.flip()


clock=pygame.time.Clock()

car=Car()

no=-1
time=0

trees=pygame.sprite.Group()
speed=2

to=175
obstacles=pygame.sprite.Group()

while True:

	clock.tick(50)
		
	key=pygame.key.get_pressed()
	if key[K_RIGHT]:
		no=1
	if key[K_LEFT]:
		no=0;
	

	for event in pygame.event.get():
		if event.type==QUIT:
			sys.exit()
	
	if no is not -1:
		update_all(no)
		no=-1
	screen.blit(background,(0,0))

	if time%(250//speed)==0:
		k=random.randint(0,1)
		trees.add(Tree(k,0))
		trees.add(Tree(k,1))

	if time%(250//speed)==0:
		type=random.randint(0,4)
		lane=random.randint(0,3)
		obstacles.add(Obstacle(type,lane))
	screen.blit(car.image,(car.rect.centerx,car.rect.centery))
	trees.draw(screen)
	trees.update()
	obstacles.draw(screen)
	obstacles.update()
	pygame.display.flip()
	time+=1

	if time%500==0:
		speed+=1

			
			
			




