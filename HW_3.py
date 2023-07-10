MAX_WEIGHT = 8
all_items = {"Фонарь" : 2, "Вода" : 3, "Палатка" : 5, "Еда" : 3, "Спальник" : 4, "Аптечка" : 2}

items = []

for all_items,weight in all_items.items():
    if weight <= MAX_WEIGHT:
        items.append(all_items)
        MAX_WEIGHT -= weight

print(items)