import random
def get_smallest_number(list_1, list_2):
    if len(list_1) == 0 or len(list_2) == 0:
        return "List is empty"

    # smallest_number_of_list1 = min(list_1)
    # smallest_number_of_list2 = min(list_2)
    smallest_number_of_list1 = min(num for num in list_1)
    smallest_number_of_list2 = min(num for num in list_2)

    return smallest_number_of_list1 + smallest_number_of_list2

list_1 = [random.randint(1, 100)for _ in range(1, 10)]
list_2 = [random.randint(1,100)for _ in range(1, 8)]
result = get_smallest_number(list_1, list_2)
print(f"The computer has chosen the following numbers from a list: {list_1}")
print(f"The computer has chosen the following numbers from a list: {list_2}")
print(f"The sum of minimum numbers from both lists is equal to {result}")

