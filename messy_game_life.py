import time
import os
import numpy as np

def create_grid(size):
    matrix = np.zeros([size,size])
    return matrix

def print_grid(grid):
    empty_element='  '
    occupied_element='* '
    for line in grid:
        for element in line:
            if(element==0):
                print(empty_element, end = '')
            else:
                print(occupied_element, end = '')
        print()

def insert_element(grid,x,y):
    grid[(x,y)] = 1
    return grid

def starter_board(grid):
    grid = insert_element(grid,3,1)
    grid = insert_element(grid,1,2)
    grid = insert_element(grid,2,1)
    grid = insert_element(grid,3,1)
    grid = insert_element(grid,1,2)
    grid = insert_element(grid,1,3)
    return grid

def start_glider(grid):
	grid = insert_element(grid,1,2)
	grid = insert_element(grid,2,2)
	grid = insert_element(grid,3,2)
	grid = insert_element(grid,3,1)
	grid = insert_element(grid,2,0)
	return grid

def random_start(grid,elements):
	from random import randint
	counter=0
	if((len(grid)*len(grid)) >= elements):
		seen = set()
		while True:
			x, y = randint(0,len(grid)-1), randint(0,len(grid)-1)
			if((x,y) in seen):
				continue
			else:
				seen.add((x,y))
				grid = insert_element(grid,x,y)
				counter += 1
				if counter == elements:
					break

	return grid
		

def live_neighbors(grid,x,y):
    size = len(grid)
    minimum_grid = lambda x : x-1 if (x > 0) else 0
    maximum_grid = lambda x : x+2 if (x < (size+1)) else size
    min_x = minimum_grid(x)
    min_y = minimum_grid(y)
    max_x = maximum_grid(x)
    max_y = maximum_grid(y)
    subgrid = grid[min_x:max_x, min_y:max_y]
    neighbours = np.sum(subgrid)-grid[(x,y)]
    return neighbours

def step(grid):
    new_grid = create_grid(len(grid))
    for x in range(len(grid)):
        for y in range(len(grid)):
            living_neighbours = live_neighbors(grid,x,y)
            if(grid[(x,y)]==1):
                if((living_neighbours<=3) and (living_neighbours>=2)):
                    new_grid[(x,y)]=1
                else:
                    new_grid[(x,y)]=0
            else:
                if(living_neighbours==3):
                    new_grid[(x,y)]=1
                else:
                    new_grid[(x,y)]=0
    return new_grid
            
            
grid=create_grid(25)
#grid=start_glider(grid)
grid=random_start(grid,100)
time.sleep(0.5)
os.system('clear')
print_grid(grid)
new_grid=step(grid)
for i in range(80):
	time.sleep(0.5)
	os.system('clear')
	print_grid(new_grid)
	new_grid=step(new_grid)