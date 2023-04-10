#Matrix
#Which is a 2D list or array, a array inside of a array
#Remeber to count from starting from 0 not 1

matrix = [ 
  [1,2,3],
  [2,4,6],
  [7,8,9]
]

print(matrix)

print('--------------------')
#the first [] means which array to look at, and the second [] means which number or letter you want

print(matrix[0][1]) # [0] means the first array [1,2,3], [1] means the answer is 2

print(matrix[2][2]) #the answer should be 9 due to the rules on line 14

print('--------------------')
#Matrix Assignment
# access "Oranges" and print it:

basket = ["Banana",["Apples", ["Oranges"], "Blueberries"]]

print(basket[1])
print(basket[1][1])
print(basket[1][1][0]) # final answer

# the first [1] means to access the second array ["Apples", , "Blueberries"]]
# the next [1] also means to select the second array,["Oranges"]
# the [0] means to select the first option in the array, Oranges
