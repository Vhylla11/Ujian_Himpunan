A = {2,4,6,8,10,12,14,16,18}
B = {3,5,7,9,11,13,15,17,19}
C = {-9,-8,-7.,-6.-5,-4,-3,-2,-1}
D = {2, 3, 5, 7, 11, 13, 17, 19}
E = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18}

A = set (A)
B = set (B)
C = set (C)
D = set (D)
E = set (E)

F = ( A | B )
G = ( D | E )
H = ( A | B | C )
I = ( A & E )

## a. A ∪ B ∪ C ∪ D ∪ E
print ( A | B | C | D | E)

## c. (A ∪ B) ∩ (D ∪ E)
print (F & G)

## d. (A ∪ B) - (D ∪ E)
print (F - G )

## e. (A ∪ B ∪ C) - (A ∩ E)
print (H - I)
