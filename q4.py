import pandas as pd
import matplotlib.pyplot as plt
import pygame.math as gamemath
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# import necessary libraries

df = pd.read_excel('CAMP2.xlsx')
df_birthdays = df['Date']
# import excel file and needed libraries (and pygame)
years = list(df['Years'])
dob = list(df['Date'])

sections = ['RO', 'FR', 'RA', 'VO']
# define sections to search
avg_retirement_age = {}
age_year_amt = {}

for index, attendence in enumerate(years):
    for s in sections:
        split_history = attendence.split(' ')
        year = int(split_history[0])
        # get the last year of camp
        date_of_birth = int(dob[index].split("/")[2])
        age = int(year) - date_of_birth
        # get the date of birth and use that and the last day of camp to calculate the age
        if s in split_history[1] and 9 < age < 18:
            avg_retirement_age[year] = avg_retirement_age.get(year, gamemath.Vector2(0, 0)) + gamemath.Vector2(age, 1)
            age_and_years = gamemath.Vector2(age, year)
            # use pygame math vectors to store information and calculate the average age of retirement over the years
            # access the years and ages to plot retirement ages over the years

            two_datas = str(age_and_years.x) + "-" + str(age_and_years.y)
            age_year_amt[two_datas] = age_year_amt.get(two_datas, 0) + 1
            # define the ages, years, and amounts of retirement

grad_ages = []
grad_years = []
grad_amts = []

for key, value in age_year_amt.items():
    age_year = key.split('-')
    grad_ages.append(float(age_year[0]))
    grad_years.append(float(age_year[1]))
    grad_amts.append(value)

# organize data

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
# define graph
dx = np.ones(len(grad_ages))
dy = np.ones(len(grad_ages))
z = np.zeros(len(grad_ages))

# define additional values needed for graph (delta versions needed from graph to work-empty parameters)
plt.xlabel("Ages")
plt.ylabel("Years")
ax1.set_zlabel("Amount")
plt.title("Age of Retirement and Number of Campers who Retire from Years 1990 to 2015")
# define labels and title
colors = {
    10:'k',
    11:'darkgoldenrod',
    12:'mediumaquamarine',
    13:'lightsalmon',
    14:'palevioletred',
    15:'darkolivegreen',
    16:'cornflowerblue',
    17:'firebrick',
    18:'indianred'
}
# define the colours

print((grad_ages), (grad_years), (grad_amts))

for index, g in enumerate(grad_ages):
    ax1.bar3d(grad_ages[index], grad_years[index], z[index], dx[index], dy[index], grad_amts[index], color=colors[grad_ages[index]])
    # graph all the values with different colours on different axes

plt.show()
# show graph