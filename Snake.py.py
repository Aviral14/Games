import os,sys
import pygame
from pygame.locals import*
import time
import random


def text_display(size,caption,posix,posiy,k):
	font= pygame.font.Font('freesansbold.ttf', size)
	text = font.render(caption, True, (255,0,0)) 
	textRect = text.get_rect()
	textRect.center = (posix, posiy)
	screen.blit(text,textRect) 
	if k:
		time.sleep(5)
	

def load_image(name):
	image=pygame.image.load(name)
	image=image.convert()
	return image,image.get_rect()

def handle_eat():
	boolean=True
	global food
	global score
	score+=10
	global snake_parts
	global new_next
	global h
	
	x,y=find_random()
	food.rect.centerx=x
	food.rect.centery=y
	while boolean:
		x,y=find_random()
		food.rect.centerx=x
		food.rect.centery=y
		for obj in snake_parts.sprites():
			if (obj.rect.centerx>food.rect.centerx+20 or obj.rect.centerx<food.rect.centerx-20) and (obj.rect.centery>food.rect.centery+20 or obj.rect.centery<food.rect.centery-20):
				boolean=False
		
	global tail
	if tail.speedx==0 and tail.speedy>0:
		new_part=Snake('snake.png',tail.speedx,tail.speedy,tail.rect.centerx,tail.rect.centery-45)
		new_part.action=tail.action.copy()
		snake_parts.add(new_part)
		tail=new_part
		if h==0:
			new_next=tail
			h+=1
	if tail.speedx==0 and tail.speedy<0:
		new_part=Snake('snake.png',tail.speedx,tail.speedy,tail.rect.centerx,tail.rect.centery+45)
		new_part.action=tail.action.copy()
		snake_parts.add(new_part)
		tail=new_part
		if h==0:
			new_next=tail
			h+=1
	if tail.speedy==0 and tail.speedx>0:
		new_part=Snake('snake.png',tail.speedx,tail.speedy,tail.rect.centerx-45,tail.rect.centery)
		new_part.action=tail.action.copy()
		snake_parts.add(new_part)
		tail=new_part
		if h==0:
			new_next=tail
			h+=1
	if tail.speedy==0 and tail.speedx<0:
		new_part=Snake('snake.png',tail.speedx,tail.speedy,tail.rect.centerx+45,tail.rect.centery)
		new_part.action=tail.action.copy()
		snake_parts.add(new_part)
		tail=new_part
		if h==0:
			new_next=tail
			h+=1
	
		
def find_random():
	x=random.randint(97,1107)
	y=random.randint(78,523)	
	return x,y

class Snake(pygame.sprite.Sprite):
	
	def __init__(self,name,speedx,speedy,x,y):
		super(Snake,self).__init__()
		self.image,self.rect=load_image(name)
		self.speedx=speedx
		self.speedy=speedy
		self.rect.centerx=x
		self.rect.centery=y
		self.action=[]

		
	def handle_turn():
		
		
		for obj in snake_parts.sprites():	

			if len(obj.action):
				if obj.action[0][2]=='u':
					if obj.rect.centerx==obj.action[0][0] and obj.rect.centery==obj.action[0][1]:
						obj.speedx=0
						obj.speedy=-gspeed
						obj.action.pop(0)
			
				elif obj.action[0][2]=='d':
					if obj.rect.centerx==obj.action[0][0] and obj.rect.centery==obj.action[0][1]:
						obj.speedx=0
						obj.speedy=gspeed
						obj.action.pop(0)
				elif obj.action[0][2]=='l':
					if obj.rect.centerx==obj.action[0][0] and obj.rect.centery==obj.action[0][1]:
						obj.speedx=-gspeed
						obj.speedy=0
						obj.action.pop(0)
				elif obj.action[0][2]=='r':
					if obj.rect.centerx==obj.action[0][0] and obj.rect.centery==obj.action[0][1]:
						obj.speedx=gspeed
						obj.speedy=0
						obj.action.pop(0)
			
		
	def update(self):
		if self.rect.centerx<77 or self.rect.centerx>1127:
			text_display(512,'Game Over',600,300,1)
			sys.exit()
		if self.rect.centery<58 or self.rect.centery>543:
			text_display(512,'Game Over',600,300,1)
			sys.exit()
		self.rect.centerx+=self.speedx
		self.rect.centery+=self.speedy
		if not (self.rect.centerx==face.rect.centerx) and (self.rect.centery==face.rect.centery):
			snake_parts.remove(face,new_next)
			list=pygame.sprite.spritecollide(face,snake_parts,True)
			if len(list):
				text_display(512,'Game Over',600,300,1)
				sys.exit()	
			snake_parts.add(face,new_next)		
		
		list2=pygame.sprite.spritecollide(food,snake_parts,False)
		if len(list2):
		#if (food.rect.centerx<=self.rect.centerx+20 and food.rect.centerx>=face.rect.centerx-20) and (food.rect.centery>=self.rect.centery-20 and food.rect.centery<=self.rect.centery+20):
			handle_eat()
		
	
	
		

		
pygame.init()


screen=pygame.display.set_mode((1200,600))
pygame.display.set_caption('Snake')

background=pygame.image.load('background.png')
background=background.convert()
screen.blit(background,(0,0))

posx=None
posy=None
ch=None

score=0

gspeed=1

face=Snake('snake.png',gspeed,0,600,300)
tail=face

clock=pygame.time.Clock()

snake_parts=pygame.sprite.Group()
snake_parts.add(face)

food=pygame.sprite.Sprite()
food.image,food.rect=load_image('food.png')
food.rect.centerx=290
food.rect.centery=290

k=0

new_next=None
h=0

while 1:

	clock.tick()

	for event in pygame.event.get():

		if event.type==QUIT:
			sys.exit()

		if event.type==KEYDOWN and event.key==K_ESCAPE:
			sys.exit()
		
		if event.type==KEYDOWN and event.key==K_UP and face.speedx!=0:
			posx=face.rect.centerx
			posy=face.rect.centery
			ch='u'
			k=1

		if event.type==KEYDOWN and event.key==K_DOWN and face.speedx!=0:
			posx=face.rect.centerx
			posy=face.rect.centery
			ch='d'
			k=1


		if event.type==KEYDOWN and event.key==K_LEFT and face.speedy!=0:
			posx=face.rect.centerx
			posy=face.rect.centery
			ch='l'
			k=1
	
		if event.type==KEYDOWN and event.key==K_RIGHT and face.speedy!=0:
			posx=face.rect.centerx
			posy=face.rect.centery
			ch='r'
			k=1

		if k:
			for obj in snake_parts.sprites():
				obj.action.append([posx,posy,ch])
				k=0

	Snake.handle_turn()

	screen.blit(background,(0,0))

	snake_parts.draw(screen)
	snake_parts.update()	
	screen.blit(food.image,(food.rect.centerx,food.rect.centery))	
	text_display(42,'Score: '+str(score),1030,81,0)		
	pygame.display.flip()

		
