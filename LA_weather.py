#This assignment focuses on counting types of weather in Los Angeles during an year using Dictionaries
#We need to know how many days were Sunny, Rain, Fog etc. We make use of dictionaries to achieve this goal

f = open("la_weather.csv")
r = f.read()
#Split on the newline character to return list
rows = r.split('\n')
weather_list = []
for row in rows:
    splitr = row.split(',')
    weather_list.append(splitr)
#create a list only containing weather types
weather = []
for i in weather_list:
    type = i[1]
    weather.append(type)

#Remove header
new_weather = weather[1:len(weather)]

#Counting types of weather
wtype = {}

for item in new_weather:
    if item not in wtype:
        wtype[item] = 1
    else:
        wtype[item] += 1

print (wtype)


#Output: {'Fog': 125, 'Sunny': 210, 'Thunderstorm': 1, 'Rain': 25, 'Fog-Rain': 4}





