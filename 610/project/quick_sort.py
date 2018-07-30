from functools import cmp_to_key

class QuickSort:
    def sort(self, data, func):
        print("called")
        print(data)
        sorted_data = sorted(data, key=cmp_to_key(func))
        print(sorted_data)
        return sorted_data