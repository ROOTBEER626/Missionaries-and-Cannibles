from queue import *
from collections import deque
import heapq       
#represent a state
#a state will represent the current positions of the cannibals, missionaries and the boat
class State:
        def __init__(self, can_left, miss_left, boat, can_right, miss_right):
                self.can_left = can_left
                self.miss_left = miss_left
                self.boat = boat #true->Right, False->left
                self.can_right = can_right
                self.miss_right = miss_right
                self.action = None
        def is_valid(self):
                if self.miss_left >= 0 and self.miss_right >= 0 \
                and self.can_left >= 0 and self.can_right >= 0 \
                and (self.miss_left == 0 or self.miss_left >= self.can_left) \
                and (self.miss_right == 0 or self.miss_right >= self.can_right):
                        return True
                else:
                        return False
        def is_goal(self):
                if self.can_left == 0 and self.miss_left == 0:
                        return True
                else:
                        return False
#end of State class
#represent an action
#class Action: I don't need a class for this
        #incase I need it
       # def __init__(self, cur_state):
        #        self.cur_state = cur_state
                
poss_actions = [(2,0),(1,0),(1,1),(0,1),(0,2)]
        #                  0    1     2     3     4
        #               2can   1can  1n1   1miss 2miss
        #moves for missionaries
def move2miss(cur_state):
        if cur_state.boat == True:
                #move from right to left
                new_state = State(cur_state.can_left, cur_state.miss_left + 2, False, cur_state.can_right, cur_state.miss_right - 2)
                new_state.action = 4
                return new_state
        else: #move from left to right
                new_state = State(cur_state.can_left, cur_state.miss_left - 2, True, cur_state.can_right, cur_state.miss_right + 2)
                new_state.action = 4
                return new_state
def move1miss(cur_state):
        if cur_state.boat == True:
                #move from right to left
                new_state = State(cur_state.can_left, cur_state.miss_left + 1, False, cur_state.can_right, cur_state.miss_right - 1)
                new_state.action = 3
                return new_state
        else: #move from left to right
                new_state = State(cur_state.can_left, cur_state.miss_left - 1, True, cur_state.can_right, cur_state.miss_right + 1)
                new_state.action = 3
                return new_state
#moves for cannibals
def move2can(cur_state):
        if cur_state.boat == True:
                #move from right to left
                new_state = State(cur_state.can_left + 2, cur_state.miss_left, False, cur_state.can_right - 2, cur_state.miss_right )
                new_state.action = 0
                return new_state
        else: #move from left to right
                new_state = State(cur_state.can_left - 2, cur_state.miss_left, True, cur_state.can_right + 2, cur_state.miss_right)
                new_state.action = 0
                return new_state
def move1can(cur_state):
        if cur_state.boat == True:
                #move from right to left
                new_state = State(cur_state.can_left + 1, cur_state.miss_left, False, cur_state.can_right - 1, cur_state.miss_right)
                new_state.action = 1
                return new_state
        else: #move from left to right
                new_state = State(cur_state.can_left - 1, cur_state.miss_left, True, cur_state.can_right + 1, cur_state.miss_right)
                new_state.action = 1
                return new_state
#move for a cannibal and missionary
def move1n1(cur_state):
        if cur_state.boat == True:
                #move from right to left
                new_state = State(cur_state.can_left + 1, cur_state.miss_left + 1, False, cur_state.can_right - 1, cur_state.miss_right - 1)
                new_state.action = 2
                return new_state
        else: #move from left to right
                new_state = State(cur_state.can_left - 1, cur_state.miss_left - 1, True, cur_state.can_right + 1, cur_state.miss_right + 1)
                return new_state
#end of action class
#represent a node in the search tree
class Node:
        def __init__(self, parent_node, state, action, cost, estcost):
                self.parent_node = parent_node
                self.state = state
                self.action = action
                self.ccost = cost
                self.ecost = estcost
        
       # def gencost(self):
        #        self.ccost = self.parent_node.ccost + 1
                #return self
         #       return self.ccost
        
        #def estcost(self):
        #        self.ecost = self.ccost + self.h()
        #        #return self
        
        
        #def __repr__(self):
        #        return f'Node value: {self.ecost}'

        def __lt__(self, other):
                return self.ecost < other.ecost
        
                
#end of node class     
def h(state):
        if state.boat == False:
                if state.can_left + state.miss_left <= 2:
                        return 1
                else:
                        return (state.can_left + state.miss_left - 2) * 2 + 1
        else:
                return (state.can_left + state.miss_left + 1 - 2) * 2 +2
                                
#get successors for a node
def successors(cur_node):
        children = []
        cur_state = cur_node.state
        new_state = move2miss(cur_state)
        if new_state.is_valid():
                children.append(new_state)
        new_state = move1miss(cur_state)
        if new_state.is_valid():
                children.append(new_state)
        new_state = move2can(cur_state)
        if new_state.is_valid():
                children.append(new_state)
        new_state = move1can(cur_state)
        if new_state.is_valid():
                children.append(new_state)
        new_state = move1n1(cur_state)
        if new_state.is_valid():
                children.append(new_state)
        nodes = []
        for child in children:
                new_node = Node(cur_node, child, child.action, cur_node.ccost + 1, h(child)+cur_node.ccost)
                nodes.append(new_node)
        return nodes
        
#used to print the solution      #Got from online source
def print_solution(solution):
        print("(CannibalsLeft, MissionariesLeft, boat, CannibalsRight, MissionariesRight)")
        if solution != None:
                path = []
                path.append(solution)
                parent = solution.parent_node
                while parent:
                        path.append(parent)
                        parent = parent.parent_node
                print("Length of Path is: " + str(len(path)))
                for t in range(len(path)):
                        node = path[len(path) - t - 1]
                        state = node.state
                        print( "(" + str(state.can_left) + "," + str(state.miss_left) \
                        + "," + str(state.boat) + "," + str(state.can_right) + "," + \
                        str(state.miss_right) + ")")
                        
#psuedocode for BFS 
#BFS(initial_node): #returns a solution or failure
#       initial_node = initial_node
#       if (initial_node.state.is_goal) initial_node
#       fringe = [] //empty FIFO dataStruct //used to get the next node
#       visited = set[] //an empty set //used to avoid visiting a previously visited node
#       fringe.add(initial_node)
#       while(fringe) #while we still have a possible node to visit
#               next_node = fringe.pop() //get the next node out of the fringe
#               visited.add(next_node) //so we don't search it again
#               for action in actions //for every possible action from this node
#                       child = next_action
#                       if (child not in visited) and (child not in fringe)
#                               if (child.state.is_goal) return solution
#                               fringe.add(child)
#       return failure

#answer for question a
#Length of fringe: 14595
#Length of visited: 11332
def BFS(initial_node):
        initial_node = initial_node
        #initial_state = initial_node.state#this line is not defining the initial_state
        initial_state = initial_node.state
        if initial_state.is_goal():#for some reason this line keeps returning true #ah ha initial_state is not defined # now it is defined but it still keeps returning true
                return initial_node
        fringe = Queue()
        visited = set()
        fringe.put(initial_node)
        while fringe:
                node = fringe.get()
                visited.add(node)
                #print("Length of fringe is: " + str(fringe.qsize()))
                #print("Length of visited is: " + str(len(visited)))
                if node.state.is_goal():
                        print("Length of fringe is: " + str(fringe.qsize()))
                        print("Length of visited is: " + str(len(visited)))
                        return node
                children = successors(node)
                for child in children:
                        if (child not in visited) or (child not in fringe):
                                fringe.put(child)
                                #print("Length of fringe is: " + str(fringe.qsize()))
                                #print("Length of visited is: " + str(len(visited)))
        return None

#This is a DFS algorithm that uses a deque for the stack
#It returns the same length of the fringe and visited as the BFS above it which worries me a little bit
#
#def depth_first_search(initial_node):
#        initial_node = initial_node
#        initial_state = initial_node.state
#        if initial_state.is_goal():
#                return initial_node
#        fringe = deque()
#        visited = set()
#        fringe.append(initial_node)
#        while fringe:
#                #print("Length of fringe is: " + str(len(fringe)))
#                node = fringe.popleft()
#                visited.add(node)
#                #print("Length of fringe is: " + str(len(fringe)))
#                #print("Length of visited is: " + str(len(visited)))
#                if node.state.is_goal():
#                        print("Length of fringe is: " + str(len(fringe)))
#                        print("Length of visited is: " + str(len(visited)))
#                        return node
#                #print("Length of visited is: " + str(len(visited)))
#                children = successors(node)
#                for child in children:
#                        if (child not in visited) or (child not in fringe):
#                                fringe.append(child)
#                                #print("Length of fringe is: " + str(len(fringe)))
#                                #print("Length of visited is: " + str(len(visited)))
#                                
#        return None

#PsuedoCode for A* algorithm 
#The only real difference between this and the BFS is that the fringe will be ordered so that the lowest estimated cost node will be at the front and will be visited next
#       initial_node = initial_node
#       if (initial_node.state.is_goal) initial_node
#       fringe = [] //priorityQueue dataStruct //used to keep the fringe in optimal order
#       visited = set[] //an empty set //used to avoid visiting a previously visited node
#       fringe.add(initial_node)
#       while(fringe) #while we still have a possible node to visit
#               next_node = fringe.pop() //get the next node out of the fringe //will be the one with the lowest f cost
#               visited.add(next_node) //so we don't search it again
#               for action in actions //for every possible action from this node
#                       child = next_action
#                       if (child not in visited) and (child not in fringe)
#                               if (child.state.is_goal) return solution
#                               fringe.add(child)
#       return failure

#implementation of the A* algorithm
#in the other program this is where I was begining to have trouble
#I haven't used python in a long time and couldn't get the priorityQueue to work so lets try this again
#I am again having trouble with the priority queue
#I was able to do this by overiding the lt function in my node class
#And instead of using Python's PQ I used heapq
#when doing a comparison in heapq, Pyhton looks firsst for __lt__() if not defined it looks for __gt__(), if both are undefined it thorws the error that i kept getting
#answer for question b


#When I was sorting the PQ using just the h(n)
#Length of fringe: 16
#Length of visited: 14
#But now that I am sorting using f(n) I get:
#Fringe: 56
#Visited: 46
def A_star(initial_node):
        initial_node = initial_node
        initial_state = initial_node.state
        if initial_state.is_goal():
                return initial_node
        fringe = [initial_node]
        visited = set()
        while fringe:
                #print("Length of fringe is: " + str(len(fringe)))
                #fringe.sort(reverse=True)
                node = heapq.heappop(fringe)
                visited.add(node)
                #print("Length of fringe is: " + str(len(fringe)))
                #print("Length of visited is: " + str(len(visited)))
                if node.state.is_goal():
                        print("Length of fringe is: " + str(len(fringe)))
                        print("Length of visited is: " + str(len(visited)))
                        return node
                #print("Length of visited is: " + str(len(visited)))
                children = successors(node)
                for child in children:
                        if (child not in visited) or (child not in fringe):
                                heapq.heappush(fringe, child)
                                #print("Length of fringe is: " + str(len(fringe)))
                                #print("Length of visited is: " + str(len(visited)))
                                
        return None
#returns fringe of size 16 and visited of size 14

#Just another DFS algorithm uses a list for the stack
#this one for some reason never returns so lets just ignore it 
#def DFS(initial_node):
#        initial_node = initial_node
#        if initial_node.state.is_goal():
#                return initial_node
#        fringe = [initial_node]
#        visited = set()
#        while fringe:
#                node = fringe.pop()
#                visited.add(node)
#                print("Length of fringe is: " + str(len(fringe)))
#                print("Length of visited is: " + str(len(visited)))
#                if node.state.is_goal():
#                        print("Length of fringe is: " + str(len(fringe)))
#                        print("Length of visited is: " + str(len(visited)))
#                        return node
#                children = successors(node)
#                for child in children:
#                        if (child not in visited) or (child not in fringe):
#                                fringe.append(child)
#                                print("Length of fringe is: " + str(len(fringe)))
#                                print("Length of visited is: " + str(len(visited)))
#        return None
#

#Little space to remind myself to implement the IDS algorithm
#Just start with a max_depth of 1 and perform DFS
#if no solution found then increment the max_depth and run again

def main():
        initial_state = State(3,3,False,0,0)
        initial_node = Node(None, initial_state, None, 0, None)
        solution = BFS(initial_node)
        print("BFS Missionaries and Cannibals solution:")
        print_solution(solution)
        #solution = depth_first_search(initial_node)
        #print("DFS using deque Missionaries and Cannibals solution:")
        #print_solution(solution)
        #soulution = DFS(initial_node)
        #print("DFS using list Missionaries and Cannibals solution:")
        #print_solution(solution)
        solution = A_star(initial_node)
        print("A* Missionaries and Cannibals solution:")
        print_solution(solution)
#if called from the command line, call main
if __name__ == "__main__":
        main()
        


#sample output
#Length of fringe is: 14595
#Length of visited is: 11332
#BFS Missionaries and Cannibals solution:
#(CannibalsLeft, MissionariesLeft, boat, CannibalsRight, MissionariesRight)
#Length of Path is: 12
#(3,3,False,0,0)
#(1,3,True,2,0)
#(2,3,False,1,0)
#(0,3,True,3,0)
#(1,3,False,2,0)
#(1,1,True,2,2)
#(2,2,False,1,1)
#(2,0,True,1,3)
#(3,0,False,0,3)
#(1,0,True,2,3)
#(1,1,False,2,2)
#(0,0,True,3,3)
#Length of fringe is: 16
#Length of visited is: 14
#A* Missionaries and Cannibals solution:
#(CannibalsLeft, MissionariesLeft, boat, CannibalsRight, MissionariesRight)
#Length of Path is: 12
#(3,3,False,0,0)
#(1,3,True,2,0)
#(2,3,False,1,0)
#(0,3,True,3,0)
#(1,3,False,2,0)
#(1,1,True,2,2)
#(2,2,False,1,1)
#(2,0,True,1,3)
#(3,0,False,0,3)
#(1,0,True,2,3)
#(1,1,False,2,2)
#(0,0,True,3,3)

#Notice that they both return the same path and both are optimal
#There is a very large difference in the number of searched nodes between the two searches

        
#Online sources
#https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate #helped me fix the error I was getting with the comparision in the heapq for A*
#I accidentally lost where I got the print function from but that came from online sources to, I am sure I could've written it myself but it was there so I took it