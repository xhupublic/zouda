#! python
"""
main driver class implmenetation

"""
import time
from city_graph import CityGraph
from quick_sort import QuickSort
from merge_sort import MergeSort


class Driver:
    def __init__(self):
        self.graph = CityGraph()
        self.quick_sort = QuickSort()
        self.merge_sort = MergeSort()
        self.cmp = None

    def search_neighbour(self):
        try:
            self.list_cities()
            print("Enter Origin City Id:")
            origin_id = int(input())

            print("Enter Search Radius:")
            max_dist = float(input())
        
            print("Sorted City by (1) Name or (2) Distance?")
            sort_option = int(input())
        except:
            print("Invalid Input, please retry...")
            return

        cities = self.graph.get_cities()
        if origin_id < 0 or origin_id >= len(cities):
            print("origin is not a valid id")
            return

        if max_dist <= 0:
            print("max distance can not be negative or zero")
            return

        if sort_option not in [1, 2]:
            print("invalid sort option")
            return
        elif sort_option is 1:
            self.cmp = lambda x, y : x[0] < y[0]
        else:
            self.cmp = lambda x, y : x[1] < y[1]

        origin = cities[origin_id]
        res = self.graph.bfs(origin, max_dist)
        print("\n")
        print("Found {} Cities within {} miles from {}:".format(len(res), max_dist, origin))
        print("=" * 40)


        
        s = time.time()
        for i in range(1):
            quick_sort_res = self.quick_sort.sort(res, self.cmp)
        print("Quick sort took {} ns".format((time.time() - s) * 1e6))
        for city in quick_sort_res:
            print(city[0], city[1])
        
        print("=" * 40)
        
        s = time.time()
        for i in range(1):
            merge_sort_res = self.merge_sort.sort(res, self.cmp)
        print("Merge sort took {} ns".format((time.time() - s) * 1e6))
        for city in merge_sort_res:
            print(city[0], city[1])

        pass

    def list_cities(self):
        cities = self.graph.get_cities()
        print("=" * 40)
        print("{:<3s} | {:>12s}".format("Id", "Name"))
        print("-" * 40)
        for idx, name in enumerate(cities):
            print("{:<3d} | {:>12s}".format(idx, name))
        print("=" * 40)
    
    def show_menu(self):
        s = """
=============================
Choose Command... 

(1) List Cities
(2) Search Neighbors
(3) Exit
=============================
    """
        print(s)
        g = None
        cmd = input()
        if cmd == "1":
            print("Listing Cities...")
            self.list_cities()
            return True
        elif cmd == "2":
            print("Searching Neighbors...")
            self.search_neighbour()
            return True
        elif cmd == "3":
            return False
        else:
            print("Invalid cmd: '{}', choose again".format(cmd))
            return True

    def run(self):
        run = True
        while run:
            run = self.show_menu()

    
def main():
    driver = Driver()
    driver.run()



if __name__ == "__main__":
    main()