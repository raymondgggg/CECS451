# Raymond Guevara Lozano
# 018504731
# CECS 451 Sec 01
import math
import sys

def get_coordinates():
    coordinates = {}
    with open('coordinates.txt') as file:
        for line in file.readlines():
            city, colon, coordinatesNotFormat = line.partition(":")
            coordinatesFormatted = coordinatesNotFormat.replace(
                "(", "").replace(")", "").replace("\n", "").split(",")
            coordinates[city] = [
                float(coordinatesFormatted[0]), float(coordinatesFormatted[1])]
    return coordinates # Dictionary 

def get_map(): 
    map = {}
    with open('map.txt') as file:
        for line in file.readlines():
            mainCity, hypen, tailCities = line.partition("-")
            getTailCityNames = tailCities.replace("\n", "").split(
                ",")  # List of the tail cities with the distance
            tailCityDistance = []
            for tailCity in getTailCityNames:
                cityData = tailCity.replace(")", "").split("(")
                tailCityDistance.append(cityData)

            # print(mainCity, tailCityDistance)
            tailCitiesFormatted = []
            for tailCity in tailCityDistance:
                tailCitiesFormatted.append((tailCity[0], float(tailCity[1])))
            map[mainCity] = tailCitiesFormatted
    return map # Dictionary 

def straight_line_distance(start, end):
    coordinates = get_coordinates()

    startCoordinatesRad = list(map(math.radians, coordinates[start]))
    endCoordinatesRad = list(map(math.radians, coordinates[end]))

    r = 3958.8 #mile
    changeLatitude = (math.sin((endCoordinatesRad[0] - startCoordinatesRad[0])/2))**2
    cosProduct = math.cos(
        startCoordinatesRad[0]) * math.cos(endCoordinatesRad[0])
    ChangeLongitude = (
        math.sin((endCoordinatesRad[1] - startCoordinatesRad[1])/2))**2

    d = 2 * r * math.asin(math.sqrt(changeLatitude + cosProduct * ChangeLongitude))
    return d

def all_straight_lines(end):
    coordinates = get_coordinates()
    allStraightLines = {}
    for c in coordinates:
        straightLineDistance = straight_line_distance(c, end)
        allStraightLines[c]= straightLineDistance
    return allStraightLines

def unpack(city, end):
    map = get_map()
    allStraightLines = all_straight_lines(end)
    connectedCities = map[city]
    connectedCitiesStraightLines = []
    for city in connectedCities:
        connectedCitiesStraightLines.append(allStraightLines[city[0]])
    return min(connectedCitiesStraightLines)

def a_star(start, end):
    allStraightLines = all_straight_lines(end)
    map = get_map() 

    currentCity = start
    routes = []
    routeDistances = []

    while currentCity != end:
        connectedCities = map[currentCity]
        cityNames = []
        cityDistances = []
        cityPlusStraightLine = []

        for city in connectedCities:
            cityNames.append(city[0])
            cityDistances.append(city[1])

        for i in range(len(cityNames)):
            if allStraightLines[cityNames[i]] == 0:
                cityPlusStraightLine.append(cityDistances[i])
                break

            cityPlusStraightLine.append(allStraightLines[cityNames[i]] + cityDistances[i] + unpack(cityNames[i], end))
        
        routes.append(cityNames[cityPlusStraightLine.index(min(cityPlusStraightLine))])
        routeDistances.append(cityDistances[cityPlusStraightLine.index(min(cityPlusStraightLine))])
        currentCity = routes[-1]
    return (routes, routeDistances)

if __name__ == "__main__":
    print(f'From city: {sys.argv[1]}')
    print(f'To city: {sys.argv[2]}')

    route, distance = a_star(sys.argv[1], sys.argv[2])
    print(f"Best Route: {sys.argv[1]} - ", end='')
    print(*route, sep=" - ")  
    print(f'Total distance: {sum(distance):.2f} mi') 