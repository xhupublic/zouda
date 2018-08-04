#! python
"""
main driver class 
"""

import time
from city_graph import CityGraph
from quick_sort import QuickSort
from merge_sort import MergeSort
import copy

class Driver:
    def __init__(self):
        self.graph = CityGraph()
        self.quick_sort = QuickSort()
        self.merge_sort = MergeSort()

    def get_input(self):
        # get user input for search nearby city
        self.list_cities()
        try:
            origin = int(input("Enter Origin City Id:"))
            radius = float(input("Enter Search Radius:"))
            sort_option = int(input("Sorted by 1) Name or 2) Distance?"))
        except:
            print("Invalid Input, please try again")
            return

        cities = self.graph.get_cities()
        if origin < 0 or origin >= len(cities):
            print("origin is not a valid id")
            return

        if radius <= 0:
            print("max distance can not be negative or zero")
            return

        if sort_option not in [1, 2]:
            print("invalid sort option")
            return
        
        return (origin, radius, sort_option)

    def search(self, origin, radius):
        cities = self.graph.get_cities()
        origin_city = cities[origin]
        res = self.graph.bfs(origin_city, radius)
        print("Found {} Cities within {} miles from {}:".format(len(res), radius, origin_city))
        return res

    def sort(self, data, sort_option, algo):

        # create compare function
        if sort_option is 1:
            cmp = lambda x, y : x[0] < y[0]
            sort_by = "name"
        else:
            cmp = lambda x, y : x[1] < y[1]
            sort_by = "distance"

        n = 1000
        total_time = 0
        for i in range(n):
            data_copy = copy.deepcopy(data)
            s = time.time()
            sorted_data = algo.sort(data_copy, cmp)
            total_time += (time.time() - s)
         
        print("{} took {:4.4f} ms and {} comparisons".format(algo.name, total_time * 1e3, algo.compare))
        print("Sorted by {}".format(sort_by))
        for i, city in enumerate(sorted_data):
            print("{:<2d} | {:<12s} | {}".format(i, city[0], city[1]))
        print("\n")

    def search_neighbour(self):
        user_input = self.get_input()
        if user_input is None:
            return

        origin, radius, sort_option = user_input
        # res is unsorted nearby cities
        res = self.search(origin, radius)
        self.sort(res, sort_option, self.quick_sort)
        self.sort(res, sort_option, self.merge_sort)
        
    def list_cities(self):
        cities = self.graph.get_cities()
        print("=" * 40)
        print("{:<3s} | {:>20s}".format("Id", "Name"))
        print("-" * 40)
        for idx, name in enumerate(cities):
            print("{:<3d} | {:>20s}".format(idx, name))
        print("=" * 40)
    
    def add_city(self):
        name = input("New City Name:")
        self.graph.add_city(name)
    
    def add_road(self):
        from_city = input("From City:")
        to_city = input("To City:")
        distance = int(input("Distance:"))
        self.graph.add_road(from_city, to_city, distance)

    def show_menu(self):
        s = """
=============================
Choose Command... 

1) List Cities
2) Add City
3) Add Road
4) Search Nearby Cities 
5) Exit
=============================
    """
        print(s)
        g = None
        cmd = input()
        if cmd == "1":
            self.list_cities()
            return True
        elif cmd == "2":
            self.add_city()
            return True
        elif cmd == "3":
            self.add_road()
            return True
        elif cmd == "4":
            self.search_neighbour()
            return True
        elif cmd == "5":
            return False
        else:
            print("Invalid cmd: '{}', choose again".format(cmd))
            return True

    def run(self):
        run = True
        while run:
            # run forever until 5 is pressed
            run = self.show_menu()

    
def main():
    driver = Driver()
    driver.run()


if __name__ == "__main__":
    main()