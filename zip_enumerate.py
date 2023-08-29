# Quiz: Zip Coordinates
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points_list = list(zip(labels, list(zip(x_coord, y_coord, z_coord))))
points = []
for a, (b, c, d) in points_list:
    points.append("{}: {}, {}, {}".format(a, b, c, d))

# Quiz: Zip Lists to a Dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

dict = {}
cast = None # replace with your code
for (key,value) in list(zip(cast_names,cast_heights)):
    dict[key]=value
print(dict)


# Quiz: Unzip Tuples
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
# define names and heights here
names, heights = tuple(zip(*cast))


# transpose

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
((a,b,c)) = zip(*data)
result = (a,b,c)
print(result)

#data_transpose = zip(a,b,c,d)
#print(data_transpose)



# Quiz Solution: Enumerate

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
# write your for loop here


cast_new = []
for name,height in list(zip(cast,heights)): # replace with your code
    cast_new.append("{} {}".format(name,height))
cast = cast_new

print(cast)

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)
