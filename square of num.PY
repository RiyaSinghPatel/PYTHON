#Create a list containing squares of numbers from 1 to 10 (HINT: use List Comprehension).
squares = []
for x in range(1, 11):
    squares= x * x
    print(squares, end= " ")