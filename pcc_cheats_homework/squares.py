squares = []
for x in range(1, 11):
    square = x**2
    squares.append(square)
print(squares)

#another version
squares = [x**2 for x in range(1, 11)]
print(squares)