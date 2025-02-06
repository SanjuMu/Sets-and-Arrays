setx = {"green","blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets: ")
setz = setx.intersection(sety)
print(setz)

setA= setx.union(sety)
print(setA)

setB = setx.difference(sety)
print(setB)

setC = setx.symmetric_difference(sety)
print(setC)