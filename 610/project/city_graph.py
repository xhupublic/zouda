"""
Arthor: Xinran Hu

Graph ADT implementation
"""
from queue import Queue 
import copy
import raw_data

class City:
    def __init__(self, name):
        self.name = name
        self.neighbor = {}

class Path:
    def __init__(self):
        self.dist = 0
        self.visited = []

class CityGraph:
    def __init__(self):
        self.cities = {}
        for city in raw_data.cities:
            self.add_city(city)

        for road in raw_data.roads:
            self.add_road(road[0], road[1], road[2])

    def add_city(self, name):
        if name in self.cities:
            return False
        else:
            self.cities[name] = City(name)
            return True

    def add_road(self, fr, to, distance):
        if fr in self.cities and to in self.cities:
            self.cities[fr].neighbor[to] = distance
            self.cities[to].neighbor[fr] = distance
            return True
        else:            
            return False

    def get_cities(self):
        return list(self.cities.keys())


    def bfs(self, origin, max_dist):
        result = {}
        if origin not in self.cities:
            return result

        q = Queue()
        path = Path()
        path.visited.append(origin)
        q.put(path)
        while q.qsize() > 0:
            path = q.get()
            if path.dist >= max_dist:
                continue
            
            # last visited city name
            last = path.visited[-1]
            
            # update min distance 
            if last not in result:
                result[last] = path.dist
            else:
                result[last] = min(result[last], path.dist)
                
            for city, dist in self.cities[last].neighbor.items():
                if city not in path.visited:
                    # visit next city if haven't visited
                    new_path = copy.deepcopy(path)
                    new_path.visited.append(city)
                    new_path.dist += dist
                    q.put(new_path)        
        
        result.pop(origin)
        return list(result.items())