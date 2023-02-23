objects = [1, 2, 1, 2, 3]
result = set()
for obj in objects:  # variable 'objects' is available.
    result.add(id(obj))
print(len(result))

# print(len(set(map(id, objects))))
