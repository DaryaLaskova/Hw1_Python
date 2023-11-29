postcards = {
    "Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"
}


new_postcard = {"Petra": "Paris", "Ivan": "Moscow"}
postcards.update(new_postcard)
postcards["Oleg"] = "Sidney"
print(len(set(dict.values(postcards))))