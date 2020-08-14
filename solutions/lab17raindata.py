import requests
from datetime import datetime

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/cottrell_school.rain')
response.encoding = 'utf-8'
rain_list = response.text.split()
appen_rain_list = []
for i in range(len(rain_list)):
    if len(rain_list[i]) > 3:
        appen_rain_list.append((rain_list[i], rain_list[i+1]))
# print(appen_rain_list[39:])
fixed_list = []
for i in range(39, len(appen_rain_list)):
    # date = datetime.strptime(appen_rain_list[i][0], '%d-%b-%Y')
    fixed_list.append({'date':appen_rain_list[i][0], 'rain':appen_rain_list[i][1]})
total_days = len(fixed_list)
all_rain = 0
for j in range(len(fixed_list)):
    day_rain = fixed_list[j]['rain']
    if day_rain != '-':
        num_day_rain = int(day_rain)
    all_rain += num_day_rain
average_daily_rain = all_rain/total_days
print(f'The average daily rainfall in the Portland area is {average_daily_rain} inches.')




