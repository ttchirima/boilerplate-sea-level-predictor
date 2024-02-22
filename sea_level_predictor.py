import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line_A = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    x_values = np.arange(data['Year'].min(), 2051, 1)
    y_values = line_A.slope * x_values + line_A.intercept
    plt.plot(x_values, y_values, label='Line of Best Fit')

    # Create second line of best fit
    data2000 = data[data['Year'] >= 2000]
    line_B = linregress(data2000['Year'], data2000['CSIRO Adjusted Sea Level'])
    x_values_2000 = np.arange(2000, 2051, 1)
    y_values_2000 = line_B.slope * x_values_2000 + line_B.intercept
    plt.plot(x_values_2000, y_values_2000, label='Line of Best Fit (2000-2021)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()