import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")
print(data.head()) #Take a look and see the information about the data

# Declaring a new variable that equals to life expectancy dataset
life_expectancy = data['Life Expectancy']
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])
# print(life_expectancy_quartiles) #Uncomment this to see the quartiles of Life Expectancy

# This line of codes is assigning new variables, low_gdp and high_gdp, to get the data where GDP is 
# whether high or low relatives to the mean/average of the dataset
gdp = data['GDP']
gdp_median = np.quantile(gdp, 0.5)
low_gdp = data[data['GDP'] <= gdp_median]
high_gdp = data[data['GDP'] >= gdp_median]
low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'], [0.25, 0.5, 0.75])


# print(low_gdp) #Uncomment to see the dataset of low GDP countries
# print(high_gdp) #Uncomment to see the dataset of low GDP countries

# This line of codes is showing us the distribution, mean, q1, and q2 from the Life Expectancy data

plt.hist(life_expectancy, bins=10, edgecolor='black')
plt.title('Life Expectancy')
plt.xlabel('Age')
plt.ylabel('Count')
plt.axvline(62.325, color='b', linestyle='-', label="Q1")
plt.axvline(72.525, color='y', linestyle='--', label="Q2/Median")
plt.axvline(75.4421875, color='r', linestyle='-', label="Q3")
plt.legend()
plt.show()

# This line of codes is showing the relationship between GDP and Life Expectancy using quartiles data

plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()
plt.show()