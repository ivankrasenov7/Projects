import matplotlib.pyplot as plt

def plot_stock_prices():

    dates = ['2023-12-11', '2023-01-07', '2023-11-08', '2023-11-01', '2023-15-11']
    prices = [100, 105, 98, 120, 103]

    plt.plot(dates, prices, marker = 'o')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title("Stock Price Trend")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def get_population_growth():

    years = [2010, 2012, 2014, 2016, 2018]
    population = [7, 7.5, 8, 9, 9.5]

    plt.bar(years, population)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('World Population Growth')
    plt.grid(True)
    plt.show()

plot_stock_prices()
get_population_growth()
