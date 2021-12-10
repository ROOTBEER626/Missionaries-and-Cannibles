# Missionaries-and-Cannibles
Solution for Missionaries and Cannibals problem in Python.
Has a solution using BFS, DFS and A* algorithms.

#sample output
Length of fringe is: 14595
Length of visited is: 11332
BFS Missionaries and Cannibals solution:
(CannibalsLeft, MissionariesLeft, boat, CannibalsRight, MissionariesRight)
Length of Path is: 12
(3,3,False,0,0)
(1,3,True,2,0)
(2,3,False,1,0)
(0,3,True,3,0)
(1,3,False,2,0)
(1,1,True,2,2)
(2,2,False,1,1)
(2,0,True,1,3)
(3,0,False,0,3)
(1,0,True,2,3)
(1,1,False,2,2)
(0,0,True,3,3)


Length of fringe is: 16
Length of visited is: 14
A* Missionaries and Cannibals solution:
(CannibalsLeft, MissionariesLeft, boat, CannibalsRight, MissionariesRight)
Length of Path is: 12
(3,3,False,0,0)
(1,3,True,2,0)
(2,3,False,1,0)
(0,3,True,3,0)
(1,3,False,2,0)
(1,1,True,2,2)
(2,2,False,1,1)
(2,0,True,1,3)
(3,0,False,0,3)
(1,0,True,2,3)
(1,1,False,2,2)
(0,0,True,3,3)

#Notice that they both return the same path and both are optimal
#There is a very large difference in the number of searched nodes between the two searches

        
#Online sources
#https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate #helped me fix the error I was getting with the comparision in the heapq for A*
