def generate_food_list():

    filename = input("enter a name for your list: ").strip()

    with open(filename, "w") as file:

        file.write("Product's list \n")

        items = []

        while True:
            products = input("Enter your products: ").strip().lower()
            if products == "q" or products == "quit":
                break
            items.append(products)

        file.write("Products: (or q to quit")
        for item in items:
            file.write("-" + item + "\n")

    with open(filename, "r") as file:
        print("\n" + file.read())

generate_food_list()
