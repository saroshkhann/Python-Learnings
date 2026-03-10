# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }
#
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }
#
# print(travel_log["France"][1])
#
# for key in travel_log:
#     print(travel_log[key][1])
#     break
#
#
# nested_list = ["A","B", ["C", "D"]]
#
# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 32
    },
    "Germany": {
        "cities_visited": ["Berlin","Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}


print(travel_log["Germany"]["cities_visited"][2])

