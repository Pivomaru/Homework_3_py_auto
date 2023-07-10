def find_duplicates(data):

    return list(set([x for x in data if data.count(x) > 1]))

data = [1, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 7]


print(find_duplicates(data))




