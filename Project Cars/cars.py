"""
Author:     Ivan Kirov
Date:       12.06.23
Description: Json Car Reader
Version:     1.0
"""

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
        """

        :return:
            non unique cars
        """
        unique_cars = self.data["Name"].nunique()
        return unique_cars

    def average_number(self):
        """

        :return:
            average horsepower
        """
        average_horsepower = self.data["Horsepower"].mean()
        return average_horsepower

    def heaviеst_cars(self):
        """

        :return:
            five heaviest cars
        """
        heaviest_five_car = self.data.nlargest(5, "Weight_in_lbs")
        return heaviest_five_car

    def manufacturer(self):
        """

        :return:
            produced cars by manufaturer
        """
        cars_manufacturer = self.data["Origin"].value_counts()
        return cars_manufacturer

    def year(self):
        """

        :return:
            produced cars by year
        """
        cars_by_year = self.data["Year"].value_counts()
        return cars_by_year

    def save_csv(self, output_file):
        """

        :param output_file:
        :return:
            csv data file
        """
        self.data.to_csv(output_file, index=False)

    @staticmethod
    def create_graphs(data):
        '''

        :param data: int
        :return: return graphs for HP vs Weight and Year vs HP
        '''
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
        '''

        :return: return pie chart for manufacturer cars by origin
        '''
        manufacturer_counts = self.data["Origin"].value_counts()
        plt.pie(manufacturer_counts, labels=manufacturer_counts.index, autopct='%1.1f%%')
        plt.title("Cars by Manufacturer")
        plt.show()

    def create_bar_chart(self):
        '''

        :return: return cars count by manufacturer
        '''
        manufacturer_counts = self.data["Origin"].value_counts()
        plt.bar(manufacturer_counts.index, manufacturer_counts.values)
        plt.xlabel("Manufacturer")
        plt.ylabel("Count")
        plt.title("Cars Count by Manufacturer")
        plt.show()

    def create_line_chart(self):
        '''

        :return: return line chart for cars count by year
        '''
        cars_by_year = self.data["Year"].value_counts().sort_index()
        plt.plot(cars_by_year.index, cars_by_year.values)
        plt.xlabel("Year")
        plt.ylabel("Count")
        plt.title("Cars Count by Year")
        plt.show()



def main():
    try:
        df = pd.read_json("cars.json")
        print("Data has been succesfully uploaded")
    except FileNotFoundError:
        print("Fila was not found. Pleave provide valid information")
        return

    analysis = Cars(df)

    unique_cars = analysis.car_counts()
    print(f"The number of unique cars is relevant to {unique_cars}")

    average_horsepower = analysis.average_number()
    print(f"The average horsepower of the cars is {average_horsepower}")

    heaviest_five_car = analysis.heaviеst_cars()
    print(f"The five heaviest cars are: {heaviest_five_car}")

    cars_manufacturer = analysis.manufacturer()
    print("Number of cars produced by each manufacturer:" ,cars_manufacturer)

    cars_by_year = analysis.year()
    print(f"Number of cars produced by each year: {cars_by_year}")

    analysis.save_csv("Cars_output.csv")
    print("Data has been sucessfully upoloaded in Cars_output.csv")

    analysis.create_graphs(df)
    analysis.create_pie_chart()
    analysis.create_bar_chart()
    analysis.create_line_chart()


if __name__ == "__main__":
    main()
