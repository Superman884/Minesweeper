import pygame
import keyboard
from random import randrange
from time import sleep
import time
import mouse
win=pygame.display.set_mode((455,600))
win.fill((80,80,80))
grid=[[0 for i in range(8)] for i in range(8)]
fake_grid=[[None for i in range(8)] for i in range(8)]
blocky=pygame.image.load('block.png')
mine=pygame.image.load('mine.png')
maybe=pygame.image.load('unknown.png')
mine_img=pygame.image.load('mine_small.png')
clock=pygame.image.load('clock.png')
side=50
run=True
neighbours=[(-1,-1),(-1,0),(-1,1,),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
mines=8
total_mines=8
pygame.font.init()
do=0
seconds=0
county=False
myfont = pygame.font.SysFont('MS Comic Sans', 50)
def draw():
	global grid
	global side
	global total_mines
	global seconds
	y=20
	for row in fake_grid:
		x=30
		for block in row:
			if block==None:
				win.blit(maybe,(x,y))
			elif block!=9:
				win.blit(blocky,(x,y))
				if block!=0 and block!=10:
					textsurface=myfont.render(str(block), True, (255, 0, 0))
					win.blit(textsurface,(x+10,y+5))
			elif block==9:
				win.blit(mine,(x,y))
			x+=side+side*0
		y+=side+side*0
	win.blit(mine_img,(20,480))
	textsurface=myfont.render(str(total_mines), True, (255, 242, 0))
	win.blit(textsurface,(130,520))
	win.blit(clock,(240,480))
	textsurface=myfont.render(str(seconds), True, (255, 242, 0))
	win.blit(textsurface,(350,515))
	pygame.display.update()
def show():
	global grid
	global fake_grid
	global neighbours
	found=True
	while found:
		found=False
		for y in range(8):
			for x in range(8):
				if fake_grid[y][x]==0:
					fake_grid[y][x]=10
					found=True
					for i in neighbours:
						try:
							if y+i[0]>=0 and x+i[1]>=0:
								if fake_grid[y+i[0]][x+i[1]]==None and grid[y+i[0]][x+i[1]]!=9:
									fake_grid[y+i[0]][x+i[1]]=grid[y+i[0]][x+i[1]]
						except:
							continue
if True:
	while mines!=0:
		x=randrange(len(grid))
		y=randrange(len(grid))
		if grid[y][x]==0:
			grid[y][x]=9
			mines-=1
for y in range(len(grid)):
	for x in range(len(grid)):
		if grid[y][x]==9:
			for move in neighbours:
				try:
					if grid[y+move[0]][x+move[1]]==9 or x+move[1]<0 or y+move[0]<0:
						continue
					grid[y+move[0]][x+move[1]]+=1
				except:
					continue
draw()
count=time.time()
while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	if time.time()-count>=1 and county:
		seconds+=1
		win.fill((80,80,80))
		draw()
		count=time.time()
	x1=pygame.mouse.get_pos()[0]
	y1=pygame.mouse.get_pos()[1]
	if x1>30:
		if y1>20:
			x=30
			y=20
			while x<x1:
				x+=side+side*0
			x=x-(side+side*0)
			x=int(str(x//(side+side*0))[::-2])
			while y<y1:
				y+=side+side*0
			y=y-(side+side*0)
			y=int(str(y//(side+side*0))[::-2])
			if x<len(grid) and y<len(grid):
				for event in pygame.event.get():
					if event.type==pygame.MOUSEBUTTONDOWN:
						fake_grid[y][x]=grid[y][x]
						won=True
						for i in fake_grid:
							for j in i:
								if j==None:
									won=False
									break
							if not won:
								break
						if not won:
							if fake_grid[y][x]==9:
								fake_grid=grid
								run=False
						win.fill((80,80,80))
						if county==False:
							county=True
						show()
						draw()
						if won:
							run=False
						if not run:
							sleep(2)