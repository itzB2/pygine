import pygame
import os
from boundary import Boundary
from random import randint
from ray import Ray

os.environ["SDL_VIDEO_CENTERED"] = '1'
width,height = 1280, 720
size = (width, height)
white, black = (255,255,255), (0,0,0)

pygame.init()
pygame.display.set_caption("2D RayMarching")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

c = 7
ia = 1

slowness = 10
collisionDistance = 50
objects = [Boundary(200, 200, 100)]
objectCount = 1
angle = 0
screen_offset = 50
iteration = 0


# for i in range(objectCount):
# 	obj = Boundary(randint(screen_offset, width-screen_offset), randint(screen_offset, height-screen_offset), randint(20, 100))
# 	objects.append(obj)

running = True
pixels = []
while running:
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	ray = Ray(width//2, height//2, 0, screen, white)
	ray.angle = angle
	ray.collisionDistance = collisionDistance

	if iteration == c*slowness:
		if int(angle) == int((ia/slowness)*(c*slowness)):	
			for pos in pixels:
				pygame.draw.circle(screen, (255, 255, 255), (max(int(pos[0]),int(pos[0]-1)),max(int(pos[1]),int(pos[1]-1))), 1, 1)
			# print("Done")
		else:
			screen.fill(black)
			angle+=1
	else:
		# font = pygame.font.Font('arial.ttf', 32)
		# text = font.render(str(iteration), True, (255,255,255), (0,0,0))
		# textRect = text.get_rect()
		# textRect.top = 100
		# textRect.right = 100
		screen.fill(black)
		# screen.blit(text, textRect)
		for obj in objects:
			obj.draw(screen, (10,10,10))
		ray.March(objects)
		angle += ia/slowness
		# print(angle)
		iteration += 1
		# screen.fill(black)
		try:
			pixels.append(ray.collisions[0])
		except:
			pass
	pygame.display.update()
	pygame.display.flip()

pygame.quit()
