import pandas as pd
import matplotlib.pyplot as plt

class Cars:
    """
    Car object class

    Attributes
    ----------
    data : json string

    Methods
    -------
    car_counts()
        get unique car counts
    average_number()
        get average car numbers
    heaviest_cars()
        get 5 heaviest cars
    manufacturer()
        get number of cars of each producer
    year()
        get number of cars by each year
    save_csv
        save the file to a directory
    create_graphs
        get statistics for HP and Weight
    create_pie_chart
        get manufacturer cars by origin
    create_bar_chart
        get cars by manufacturer
    create_line_chart
        get cars by manufacturer
    """

    def __init__(self, data):
        """
        :param data: str
            json data string
        """
        self.data = data

    def car_counts(self):
        unique_cars = self.data["Name"].nunique()
        return unique_cars

    def average_number(self):
        average_horsepower = self.data["Horsepower"].mean()
        return average_horsepower

    def heaviest_cars(self):
        heaviest_five_car = self.data.nlargest(5, "Weight_in_lbs")
        return heaviest_five_car

    def manufacturer(self):
        cars_manufacturer = self.data["Origin"].value_counts()
        return cars_manufacturer

    def year(self):
        cars_by_year = self.data["Year"].value_counts()
        return cars_by_year

    def save_csv(self, output_file):
        self.data.to_csv(output_file, index=False)

    @staticmethod
    def create_graphs(data):
        plt.scatter(data["Horsepower"], data["Weight_in_lbs"])
        plt.xlabel("Horsepower")
        plt.ylabel("Weight (lbs)")
        plt.title("Horsepower vs. Weight")
        plt.show()

        plt.scatter(data["Year"], data["Horsepower"])
        plt.xlabel("Year")
        plt.ylabel("Horsepower")
        plt.title("Year vs. Horsepower")
        plt.show()

    def create_pie_chart(self):
        manufacturer_counts = self.data["Origin"].value_counts()
        plt.pie(manufacturer_counts, labels=manufacturer_counts.index, autopct='%1.1f%%')
        plt.title("Cars by Manufacturer")
        plt.show()

    def create_bar_chart(self):
        manufacturer_counts = self.data["Origin"].value_counts()
        plt.bar(manufacturer_counts.index, manufacturer_counts.values)
        plt.xlabel("Manufacturer")
        plt.ylabel("Count")
        plt.title("Cars Count by Manufacturer")
        plt.show()

    def create_line_chart(self):
        cars_by_year = self.data["Year"].value_counts().sort_index()
        plt.plot(cars_by_year.index, cars_by_year.values)
        plt.xlabel("Year")
        plt.ylabel("Count")
        plt.title("Cars Count by Year")
        plt.show()

class CarsAnalyzer:
    @staticmethod
    def analyze(data):
        cars = Cars(data)
        unique_cars = cars.car_counts()
        print(f"The number of unique cars is relevant to {unique_cars}")

        average_horsepower = cars.average_number()
        print(f"The average horsepower of the cars is {average_horsepower}")

        heaviest_five_car = cars.heaviest_cars()
        print(f"The five heaviest cars are:\n{heaviest_five_car}")

        cars_manufacturer = cars.manufacturer()
        print("Number of cars produced by each manufacturer:\n", cars_manufacturer)

        cars_by_year = cars.year()
        print(f"Number of cars produced by each year:\n{cars_by_year}")

        cars.save_csv("Cars_output.csv")
        print("Data has been successfully uploaded in Cars_output.csv")

        cars.create_graphs(data)
        cars.create_pie_chart()
        cars.create_bar_chart()
        cars.create_line_chart()

def main():
    try:
        df = pd.read_json("cars.json")
        print("Data has been successfully uploaded")
    except FileNotFoundError:
        print("File was not found. Please provide valid information")
        return

    CarsAnalyzer.analyze(df)

if __name__ == "__main__":
    main()
