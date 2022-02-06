import math


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
        
def a_star(start, end):
    allStraightLines = all_straight_lines(end)
    print(allStraightLines)
    print()
    coordinates = get_coordinates()
    map = get_map()
    print(map)
    print()

    # cityRoute = []
    # totalDistance = 0 

    currentCity = start
    route = []
    routeDistances = []

    while currentCity != end:
        connectedCities = map[currentCity]
        cityNames = []
        cityDistances = []
        cityPlusStraightLine = []

        for city in connectedCities:
            cityNames.append(city[0])
            cityDistances.append(city[1])
        
        print(cityDistances)
        print(cityNames)
        for i in range(len(cityNames)):
            cityPlusStraightLine.append(allStraightLines[cityNames[i]] + cityDistances[i])
            if cityPlusStraightLine[i] == cityDistances[i]:
                cityPlusStraightLine[i] = 0
            # write an if statement about how if the new city chosen is the last city then we recalculate
            # also the second output, make sure mine matches that one as well
        print(cityPlusStraightLine)
        
        
        route.append(cityNames[cityPlusStraightLine.index(min(cityPlusStraightLine))])
        routeDistances.append(cityDistances[cityPlusStraightLine.index(min(cityPlusStraightLine))])
        print(route)
        print(routeDistances)
        print()

        currentCity = route[-1]

    print()
    return (route, routeDistances)




if __name__ == "__main__":

    # allLines = all_straight_lines("SantaCruz")
    # print(allLines)

    # coordinates = get_coordinates()
    # print()
    # print(coordinates)
    # print()
    # print(get_map())

    print()
    print(a_star("LongBeach", "SanFrancisco"))
