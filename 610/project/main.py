#! python


from city_data_set import CityDataSet




def show_neighbour(data):
    
    try:
        listCities(data)
        print("Enter Origin Id:")
        origin_id = int(input())

        print("Enter Max Distance:")
        max_dist = float(input())
    
        print("Sorted by (1) Name or (2) Distance?")
        sort_option = int(input())
    except:
        print("Invalid Input, please retry...")
        return



    cities = data.list_cities()
    if origin_id < 0 or origin_id >= len(cities):
        print("origin is not a valid id")
        return

    if max_dist <= 0:
        print("max distance can not be negative or zero")
        return

    if sort_option not in [1, 2]:
        print("invalid sort option")
        return

    origin = cities[origin_id]
    res = data.search_within_dist(origin, max_dist)
    print("\n")
    print("Found {} Cities within {} miles from {}:".format(len(res), max_dist, origin))
    
    print("=============================")
    for city in res:
        print(city[0], city[1])
    
    pass

def listCities(data):
    cities = data.list_cities()
    print("=====================")
    print("{:<3s} | {:>12s}".format("Id", "Name"))
    print("---------------------")
    for idx, name in enumerate(cities):
        print("{:<3d} | {:>12s}".format(idx, name))
    print("=====================")
def show_menu(data):
    s = """
=============================
Press Command... 

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
        listCities(data)
        return True
    elif cmd == "2":
        print("Searching Neighbors...")
        show_neighbour(data)
        return True
    elif cmd == "3":
        return False
    else:
        print("Invalid cmd: '{}', choose again".format(cmd))
        return True

def main():
    dataset = CityDataSet()
    run = True
    while run:
        run = show_menu(dataset)


if __name__ == "__main__":
    main()