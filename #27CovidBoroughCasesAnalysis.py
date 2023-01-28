#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: August 28, 2021
#This program displays nyc covid cases

import matplotlib.pyplot as plt
import pandas as pd

covid_cases = pd.read_csv('covidCases.csv')
borough = input('Enter borough name: ')
output_name = input('Enter output name: ')
covid_cases['Fraction'] = covid_cases[borough] / covid_cases['Case Count']

print(f'Min: {covid_cases[borough].min()}')
print(f'Max: {covid_cases[borough].max()}')
print(f'Mean: {covid_cases[borough].mean()}')
print(f'Median: {covid_cases[borough].median()}')
print(f'Standard Deviation: {covid_cases[borough].std()}')

covid_cases.plot(x = 'Date of Interest', y = 'Fraction')
plt.gcf().savefig(output_name)

#import matplotlib.pyplot as plt
#import pandas as pd
##
#name = input('Enter borough name: ')
#output = input('Enter output name: ')
##
#pop = pd.read_csv('covidCases.csv')
#pop.plot(x="Date of Interest", y = name)
##
#print("Min:", pop[name].min())
#print("Max:", pop[name].max())
#print("Mean:", pop[name].mean())
#print("Median:", pop[name].median())
#print("Standard Deviation:", pop[name].std())
##
#plt.show()
##
#savef = plt.gcf()
#savef.savefig(output)

