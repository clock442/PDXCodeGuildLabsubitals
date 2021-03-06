import requests
import math
from datetime import datetime
import matplotlib.pyplot as plt


response = requests.get('https://or.water.usgs.gov/non-usgs/bes/cottrell_school.rain')
response.encoding = 'utf-8'
rain_list = response.text.split()
appen_rain_list = []
for i in range(len(rain_list)):
    if len(rain_list[i]) > 3:
        appen_rain_list.append((rain_list[i], rain_list[i+1]))

# make a list of dictionaries with date as the first key and rain as the second each dictionary represents one day
fixed_list = []
for i in range(39, len(appen_rain_list)):
    fixed_list.append({'date':appen_rain_list[i][0], 'rain':appen_rain_list[i][1]})

# removing '-' from the list and changing 'rain': strings into 'rain': integers
for i in range(len(fixed_list)):
    if fixed_list[i]['rain'] == '-':
        fixed_list[i]['rain'] = 0
    else:
        fixed_list[i]['rain'] = int(fixed_list[i]['rain'])

# finding the average daily rain
total_days = len(fixed_list)
all_rain = 0
for j in range(len(fixed_list)):
    all_rain += fixed_list[j]['rain']
average_daily_rain = all_rain/total_days
print(f'The average daily rainfall in the Cottrell School area is {average_daily_rain*.01} inches.')

# finding the variance and standard deviation
root_list = []
for i in range(len(fixed_list)):
    zut = (fixed_list[i]['rain'] - average_daily_rain)**2
    root_list.append(zut)
root_sum = 0
for elem in root_list:
    root_sum += elem
variance = root_sum/len(root_list)
standard_deviation = math.sqrt(variance)
print(f'The variance is {variance*.01} inches. The standard deviation is {standard_deviation*.01} inches.')

# finding the date with the most rainfall
most_rain_in_day = 0
most_rain_date = ''
for k in range(len(fixed_list)):
    num_day_rain = int(fixed_list[k]['rain'])
    if fixed_list[k]['rain'] > most_rain_in_day:
        most_rain_in_day = fixed_list[k]['rain']
        most_rain_date = fixed_list[k]['date']
print(f'The date of the the day with the most rainfall in one day is {most_rain_date} on which {most_rain_in_day*.01} inches of rain fell.')

# plot a graph with dates as the x axis and rain levels as the y axis
all_dates = []
rain_data_day = []
for i in range(len(fixed_list)):
    n_date = datetime.strptime(fixed_list[i]['date'],'%d-%b-%Y')
    all_dates.append(n_date)
    rain_data_day.append(fixed_list[i]['rain'])
plt.plot(all_dates, rain_data_day)
plt.show()

