import random

class List:

    def __init__(self, list1, list2):

        self.list1 = list1
        self.list2 = list2

    def get_smallest_number(self):

        if len(self.list1) == 0 or len(self.list2) == 0:
            return "List is empty"

        smallest_num1 = min(self.list1)
        smallest_num2 = min(self.list2)

        return smallest_num1 + smallest_num2

    def implement(self):
        result = self.get_smallest_number()
        print(f"The computer has chosen the following numbers from a list: {self.list1}")
        print(f"The computer has chosen the following numbers from a list: {self.list2}")
        print(f"The sum of minimum numbers from both lists is equal to {result}")

list_of_int1 = [random.randint(1, 100) for _ in range(1, 10)]
list_of_int2 = [random.randint(1, 100) for _ in range(1, 8)]


if __name__ == '__main__':
    common_list = List(list_of_int1, list_of_int2)
    common_list.implement()


