import math
from this import d

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
    coordinates = get_coordinates()
    map = get_map()

    cityRoute = []
    totalDistance = 0 

    currentCity = start
    route = []
    routeDistances = []

    while currentCity != end:
        connectedCities = map[start]
        cityNames = []
        cityDistances = []

        for city in connectedCities:
            cityNames.append(city[0])
            cityDistances.append(city[1])
        
        for i in range(len(cityNames)):
            cityDistances[i] += all_straight_lines[cityNames[i]]
        
        route.append(cityNames[cityDistances.index(min(cityDistances))])
        routeDistances.append()




    

    

    


    # for c in coordinates:

    return 



if __name__ == "__main__":
    allLines = all_straight_lines("SantaCruz")
    print(allLines)

    # coordinates = get_coordinates()
    # print(coordinates)
    print()
    print(get_map())

    # print(straight_line_distance("SanJose", "SantaCruz"))
    
    # map = get_map()
    # print(len(map))

