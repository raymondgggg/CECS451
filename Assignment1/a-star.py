def get_coordinates():
    coordinates = {}
    with open('coordinates.txt') as file:
        for line in file.readlines():
            city, colon, coordinatesNotFormat = line.partition(":")
            coordinatesFormatted = coordinatesNotFormat.replace(
                "(", "").replace(")", "").replace("\n", "").split(",")
            coordinates[city] = [
                float(coordinatesFormatted[0]), float(coordinatesFormatted[1])]
    return coordinates


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
            for tailCity in tailCityDistance:
                map[mainCity+hypen+tailCity[0]] = float(tailCity[1])
    return map


if __name__ == "__main__":
    coordinates = get_coordinates()
    print(coordinates)
    print()
    map = get_map()
    print(map)

