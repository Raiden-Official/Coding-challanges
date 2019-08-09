# Set of coding problems/challanges and solutions
## 1. Divisible Palindromes : Project Euler
The numbers 545, 5995 and 15151 are the three smallest palindromes divisible by 109. There are nine palindromes less than 100000 which are divisible by 109.

How many palindromes less than 1032
are divisible by 10000019 ?

## 2. Chameleon with the color change grid 
Given a 10x10 2Darray of color changing grid with possible changes in color indicated by 1 and 0 if the change is not possible, determine the minimum number of changes required from a given start color to a given end color.

Rows and Cols of the array represent color the chameleon can switch from and switch to.

For example:   
Given grid:   
| color | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-------|---|---|---|---|---|---|---|---|---|---|
| 0     | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2     | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3     | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4     | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| 5     | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 6     | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 |
| 7     | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 |
| 8     | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 9     | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
Shows that the chameleon can switch from color 0 to color 8 but not to color 1. 
Similarly, it can go from 0 to 8 and then to 3 or 6.

input : start, end, grid.
output : all possible paths and the smallest path length.
## 3. Search a key in a given sorted (asc order) shifted/rotated array
Given a sorted array shifted by any number of bits, find the index of a given key in that array.

For example:  
Test cases:  
a = [1,2,3,4,5,6,7,8,9] # key = 9  
b = [6,7,8,9,1,2,3,4,5] # key = 7  
c = [4,5,6,7,8,9,1,2,3] # key = 9  
d = [7,8,9,1,2,3,4,5,6] # key = 10  

Output:  
Key found at: 9  
Key found at: 2  
Key found at: 6  
key not found  
