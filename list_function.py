friends = []
friends.append("Jack")
friends.append("Mack")
friends.insert(1, "Kevin")

print(friends,"\n")
print(friends.index("Jack"))
print(friends.count("Mack"))
print("===================")
friends.sort()
print(friends)
friends.clear()
print(friends)