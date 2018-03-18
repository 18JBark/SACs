#Opens files
w = open('weather.txt', 'r')
s = open('weathersummary.txt', 'w')

#Finds the average temperature
#def avTemp():
 #       av = sum(avTemp)

#avTemp()


for line in w:
    line=line.strip('\n')
    line=line.split(' ')

#removes the first thing in the list
    day = line[0]
    date = line[1]
    dew = line[2]


    [line.extend(_.split()) for _ in w.readline(0)]
#Removes the day and date
    line.pop(0)
    line.pop(1)
    dailyTemps = (line)

#Finds max and min temp
    maxTemp = max(dailyTemps)
    minTemp = min(dailyTemps)

#Puts data into array
    #array = {dailyTemps, maxTemp, minTemp}

#Prints data
    print(day, '\n', date, '\n', maxTemp, '\n', minTemp, '\n')

    maxTemp = str(maxTemp)
    minTemp = str(minTemp)

#Writes to file
    s.write('The day was: ' + day + '\n')

    s.write('The date was: ' + date + '\n')

    s.write('The max temp was: ' + maxTemp + '\n')

    s.write('The min temp was: ' + minTemp + '\n')

    #s.write('The average temp was: ' + avTemp + '\n')
    #dew = int(dew)

    #if dew <= 16:
#        print('Dry and comfortable')

#    elif 16<dew<20:
 #       print('Muggy')

#    elif dew >= 20:
 #       print('Very sticky and oppressive')

