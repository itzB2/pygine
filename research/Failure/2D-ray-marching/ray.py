import pygame
import numpy as np
from math import cos , sin, radians, sqrt
from Functions import normalize, signedDistance, offScreen

class Ray:
	def __init__(self, x, y, angle, screen, color):
		self.position = [x, y]
		self.angle = angle
		self.screen = screen
		self.color = color
		self.xPos = 0
		self.yPos = 0
		self.collisions = []
		self.collisionDistance = 20
	def March(self, objects):
		counter = 0
		current_position = self.position
		# pygame.draw.circle(self.screen, (255, 41, 120), self.position, 5)
		while counter < 100:
			record = 2000
			closest = None
			for obj in objects:
				distance = signedDistance(current_position, obj, obj.radius)
				if distance < record:
					record = distance
					closest = obj

			if record < 1:
				break

			self.xPos = current_position[0] + cos(self.angle) * record
			self.yPos = current_position[1] + sin(self.angle) * record
			a_X = current_position[0] + sin(self.angle) * record
			a_Y = current_position[1] + cos(self.angle) * record
			# pygame.draw.circle(self.screen, (0, 204, 37), (int(current_position[0]), int(current_position[1])), abs(int(record)), 1)

			pygame.draw.line(self.screen, self.color, (self.position[0], self.position[1]), (normalize(self.xPos) * a_X, normalize(self.yPos) * a_Y))
			current_position[0] = normalize(self.xPos) * a_X
			current_position[1] = normalize(self.xPos) * a_Y
			# pygame.draw.circle(self.screen, self.color, (int(self.xPos), int( self.yPos)), 5)
			# closest.draw(self.screen, (130, 190, 41))
			print(int(signedDistance(current_position, obj, obj.radius)))
			if int(signedDistance(current_position, obj, obj.radius)) <= int(self.collisionDistance):
				self.collisions.append((current_position[0], current_position[1]))

			if offScreen([self.xPos, self.yPos], 1280, 720):
				break
			if offScreen(current_position, 1280, 720):
				break
			counter += 1
		pygame.display.update()