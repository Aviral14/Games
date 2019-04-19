import pygame
import livewires
from livewires import games,color
import random


games.init(screen_width=1260,screen_height=599,fps=50)

class Pizza(games.Sprite):

	images=games.load_image("pizza.png")
	speed=1
    

	def __init__(self,x,y=90):
		super(Pizza,self).__init__(image=Pizza.images,x=x,y=y,dy=Pizza.speed)

	def update(self):
		if self.bottom>games.screen.height:
			self.end_game()
			self.destroy()
		

	def handle_caught(self):
		self.destroy()
		Pizza.speed+=0.05

	def end_game(self):
		self.end_message=games.Message(value="Game Over",size=300,color=color.red,x=640,y=250,lifetime=250,after_death=games.screen.quit)
		games.screen.add(self.end_message)

class Pan(games.Sprite):

	images=games.load_image("pan.jpg")	

	def __init__(self):
		super(Pan,self).__init__(image=Pan.images,x=games.mouse.x,y=games.screen.height-15)
		self.score=games.Text(value=0,size=60,color=color.black,x=1200,y=50)
		games.screen.add(self.score)	

	def update(self):
		self.x=games.mouse.x
		if self.left<0:
			self.left=0
		if self.right>games.screen.width:
			self.right=games.screen.width
		self.check_catch()
	
	def check_catch(self):
		for pizza in self.overlapping_sprites:
			self.score.value+=10
			self.score.right=games.screen.width-10
			pizza.handle_caught()

class Chef(games.Sprite):

	images=games.load_image("chef.jpg")


       

	def __init__(self,y=50,speed=1.5,odds_change=799):
		super(Chef,self).__init__(image=Chef.images,x=games.screen.width/2,y=y,dx=speed)
		self.odds_change=odds_change
		self.time_til_drop=0
	
	def update(self):
		if self.x>games.screen.width or self.x<0:
			self.dx=-self.dx
		elif random.randrange(self.odds_change)==350:
			self.dx=-self.dx
		elif random.randrange(self.odds_change)==0:
			self.dx+=3
             	
		self.check_drop()
		

		

	def check_drop(self):
		if self.time_til_drop>0:
			self.time_til_drop-=1
		else:
			self.new_pizza=Pizza(x=self.x)
			games.screen.add(self.new_pizza)
			self.time_til_drop=int(self.new_pizza.height*2/Pizza.speed)+1

		






	
	
wall_image=games.load_image("wallimage.jpg",transparent=False)
games.screen.background=wall_image

the_chef=Chef()
games.screen.add(the_chef)

the_pan=Pan()
	
games.screen.add(the_pan)

games.mouse.is_visible=False


games.screen.event_grab=True
        
games.screen.mainloop()
