from math import sqrt
import numpy as np

def signedDistance(a, b, r):
	d = sqrt((a[0] - b.position[0])**2+(a[1]-b.position[1])**2)
	return d - r

def normalize(v):
	n = np.linalg.norm(v)
	if n == 0:
		return v
	return v/n

def offScreen(vec, hei, wid):
	x = int(vec[0])
	y = int(vec[1])

	if x < 0 or x > wid or y < 0 or y > hei:
		return True
	else:
		return False

def rotate(point, degree):
	point.angle+=degree