empty_list = []

city_list = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(city_list)
city_list[0] = "San Francisco"
city_list[2] = "Brooklyn"
city_list[7] = "Hollywood"
city_list[5] = "Tampa"
print(city_list)

sports_list = ["Basketball", "Soccer", "Football", "Hockey", "Track and Field", "Baseball", "Tennis",]
print(sports_list)
print(sports_list[5])
print(sports_list[0])

city_list.sort(key=len)
print(city_list)