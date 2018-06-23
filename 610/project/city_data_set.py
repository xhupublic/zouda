"""
Arthor: Xinran Hu

Graph ADT implementation
"""
from queue import Queue 
import copy
import city_data as data 

class City:
    def __init__(self, name):
        self.name = name
        self.neighbor = {}

class Path:
    def __init__(self):
        self.dist = 0
        self.visited = []

class CityDataSet:
    def __init__(self):
        self.cities = {}
        self.load_data()

    def __repr__(self):
        pass    

    def load_data(self):   
        for city in data.cities:
            self.add_city(city)

        for road in data.roads:
            self.add_road(road[0], road[1], road[2])
    

    def add_city(self, name):
        if name in self.cities:
            return False
        else:
            self.cities[name] = City(name)
            return True

    def add_road(self, f, t, d):
        if f in self.cities and t in self.cities:
            self.cities[f].neighbor[t] = d
            self.cities[t].neighbor[f] = d
            return True
        else:            
            return False
    
    def list_cities(self):
        return list(self.cities.keys())


    def search_within_dist(self, origin, max_dist):
        result = {}
        if origin not in self.cities:
            return result

        path = Path()
        path.visited.append(origin)

        q = Queue()
        q.put(path)
        while q:
            path = q.get()

            if path.dist >= max_dist:
                # exceed max dist 
                break
            
            # last visited city name
            last = path.visited[-1]

            # update min distance 
            if last not in result:
                result[last] = path.dist
            else:
                result[last] = min(result[last], path.dist)
                
            for n, dist in self.cities[last].neighbor.items():
                
                # visit next city if haven't visited
                if n not in path.visited:
                    new_path = copy.deepcopy(path)
                    new_path.visited.append(n)
                    new_path.dist += dist
                    q.put(new_path)        
        
        result.pop(origin)
        return list(result.items())