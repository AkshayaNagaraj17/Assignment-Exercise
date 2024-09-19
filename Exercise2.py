dist = {'a': 100, 'b': 200, 'c': 300}
print(f"Distance in miles: {dist}")

dist_km={key :value*1.6 for key,value in dist.items()}
print(dist_km)
