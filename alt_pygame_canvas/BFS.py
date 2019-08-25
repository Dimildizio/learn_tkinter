
import queue
from random import choice


'''   
27. Terrain class:
     27.1 attributes
         27.1.1 terrain difficulty
         27.1.2 terrain danger
     27.2 terrain_effect()
'''

class Terrain:
    def __init__(self, name, speed_penalty = 1, penalty = 1, effects = []):
        self.name = name
        self.speed_penalty = speed_penalty
        self.penalty = penalty
        self.effects = effects

    def terrain_effect(self):
        return self.effects

class Node:
    def __init__(self, pos, t_type = Terrain('stone')):
        self.pos = pos
        self.inside = []
        self.occupied = False
        self.neighbours = []
        self.t_type = t_type
        self.sprite = 'g.png'

    def __repr__(self):
        if self.inside: return str(self.inside[0])
        elif self.occupied: return str(self.occupied)
        return '.'

                   
class Field:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.cells = {}
        self.create_nodes()
        self.creatures = []

    def __repr__(self):
        return str(type(self.cells[0, 0]))

    def bounds(self, cell):
        x,y = cell
        mx,my = self.maxsize
        return 0 <= x < mx and 0 <= y < my

    def create_nodes(self):
        mx, my = self.maxsize
        for x in range(mx):
            for y in range(my):
                self.cells[x, y] = Node((x,y))             
                #creating neighbours
                directions = [(x+1,y), (x, y+1), (x-1,y), (x,y-1), (x-1,y-1),
                              (x-1,y+1), (x+1,y+1), (x+1, y-1)]
                for n in directions:
                    if self.bounds(n):
                        self.cells[x, y].neighbours.append(n)

    def add_in(self, pos, obj):
        if self.bounds(pos):
            cell = self.cells[pos]
            if obj.passable:
                cell.inside.append(obj)
            else:
                cell.occupied = obj
            return True

    def remove(self, obj):
        cell = self.cells[obj.pos]
        if obj.passable:
            cell.inside.remove(obj)
        else:
            cell.occupied = False

    def reposition(self, obj, pos):
        if self.bounds(pos):
            self.remove(obj)
            self.add_in(pos, obj)
            return True
        
    def port_object(self, pos, obj):
        if obj.passable:
            self.add_in(pos, obj)
        elif not self.cells[pos].occupied:
            self.add_in(pos,obj)
        else:
            pos = self.port_object(choice(self.cells[pos].neighbours), obj)
        return pos
    
    def create_obj(self, position, obj):
        self.creatures.append(obj)
        return self.port_object(position, obj)
    
    def destroy_obj(self, obj):
        self.remove(obj)
        self.creatures.remove(obj)
        
    def draw_y0(self):
        for x in range(self.maxsize[1]):
            if x == 0: print('.', end = '  ')
            myend = ' ' if len(str(x)) > 1 else '  '
            print(x, end = myend)         
        print()
        
    def show(self):
        self.draw_y0()
        mx,my = self.maxsize
        for x in range(mx):
            for y in range(my):
                if y == 0:
                    myend = ' ' if len(str(x)) > 1 else '  '
                    print (x, end = myend)
                myend = ' ' if len(str(self.cells[x,y])) > 1 else '  '
                print(self.cells[x,y], end = myend)
            print()

    def bfs(self, start, goal):
        my_q = queue.Queue()
        my_q.put(start)
        came = {start:None}
        while not my_q.empty():
            current = my_q.get()
            if self.cells[current] == self.cells[goal]:
                return came
            for n in self.cells[current].neighbours:
                if not (n in came or self.cells[n].occupied):
                    my_q.put(n)
                    came[n] = current

    def find_path(self, start, goal):
        if self.cells[goal].occupied:               
            occs = [x for x in self.cells[goal].neighbours if not self.cells[
                x].occupied]
            goal = min(occs) if goal > start else max(occs)   
        current = goal
        path = []
        came = self.bfs(start, goal)
        while current != start:
            path.append(current)
            current = came[current]
        path.append(start)
        path.reverse()
        if self.cells[path[-1]].occupied:
            del path[-1]
        return path
        
    def build_rect(self, x, xm, y, ym, no = []):
        for i in range(x, xm+1):
            self.cells[i, y].occupied = '#'
            self.cells[i, ym].occupied = '#'
        for j in range(y, ym+1):
            self.cells[x,j].occupied = '#'
            self.cells[xm,j].occupied = '#'
        if no:
            for x in no:
                self.cells[x].occupied = False


    
class Object:
    def __init__(self, pic, x, y, passable = False):
        self.passable = passable
        self.pic = pic
        self.reach = 1
        self.pos = self.appear((x,y))

    def __repr__(self):
        return str(self.pic)

    def appear(self, position):
        return current_location.port_object(position, self)
            
    def step(self, position):
        if current_location.reposition(self, position):
            self.pos = position
            return True

    def goto(self, position):
        if current_location.bounds(position):
                
            mygoal = current_location.find_path(self.pos, position)
            for x in mygoal:
                if not self.step(x):
                    #current_location.show()
                    return False
            #current_location.show()
            return True
current_location = Field((16, 12))  
if __name__ == '__main__':

    
    class Object:
        def __init__(self, pic, x, y, passable = False):
            self.passable = passable
            self.pic = pic
            self.reach = 1
            self.pos = self.appear((x,y))

        def appear(self, position):
            return current_location.port_object(position, self)
                
        def step(self, position):
            if current_location.reposition(self, position):
                self.pos = position
                return True
    
        def goto(self, position):
            mygoal = current_location.find_path(self.pos, position)
            for x in mygoal:
                if not self.step(x):
                    #current_location.show()
                    return False
            #current_location.show()
            return True
            
    def generate_location(x = 20, y = 20):
        return Field((x,y))
        
    current_location = generate_location(15, 15)
    current_location.build_rect(5,9, 8,14, [(9, 12)])
    a = Object('Y', 0,0)
    b = Object('W', 6,9)
    current_location.show()

