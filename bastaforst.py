from Alan import *
from DictHash import *
from minHeap import * 
import sys

Map = MapEdges()    # Map of all the cities
Dictionary = DictHash() # Dictionary to keep track of previously visited cities
PrioritetsQue = minHeap()   # Prioritets kö, which is (min heap)!


class ParentNode:
    def __init__(self, city, parent = None):
        self.city = city
        self.parent = parent

Start = "Strong Oak"    #Enter starting city    
End = "Upper Gralt"
startindex = Map.getCityIndex(Start)    # Retreive the index of the starting index
endindex = Map.getCityIndex(End)    # Retreive the index of the final index

if type(startindex) is not int or type(endindex) is not int:    #Program will not continue if real cities are not given
    print("Enter cities that exist")
    sys.exit()

Spotlight = ParentNode(startindex)
counter = 0
while Spotlight:    #As long as we have options to look at
    counter += 1
    Dictionary.store(Spotlight.city, True)   #Enter the city into the dictionary because its now been visited
    Current = Spotlight.city    # Take out the city out of the ParentNode

    if Current == endindex:   # Exit the while loop if the city has been found
        break
    
    children = Map.getNeighborsTo( Current )   # Get all the children

    
    for child in children:  # For every neighhbor
        if child not in Dictionary: # Make sure that the child hasnt been visited already
            city = ParentNode(child, Spotlight)    # Create a ParentNode
            cost = Map.getCostBetween(child, Current)  # Find the cost (used as priority)
            PrioritetsQue.insert(city, cost)    # Enter the city and its priority   
    
    Spotlight = PrioritetsQue.delFirst()    # Take out the city with the highest priority (The city with the lowest cost in this case)
    

    
def writechain(Node):
    if Node.parent == None: #The first node
        print(Map.getCityName(Node.city))
        cost = 0        #Beging counting the total cost
        cities = 1      #Begin couting the number of cities that you pass through
        return cost, cities 
        
    else:
        cost, cities = writechain(Node.parent) #Making sure that the total cost and cities isnt lost in the recursive function
        city = Node.city

        cost += Map.getCostBetween(city, Node.parent.city)  #add the next cost
        cities += 1 #add the city

        print('{0:20} {2}'.format(Map.getCityName(city),"\t \t Which will cost you: ", Map.getCostBetween(city, Node.parent.city)))
        return cost,cities  



if Spotlight:   # If we found a path, this variable will not be equale to None
    print("This is how you get to your destination: ")
    print('{0:20} {1}'.format("City","Cost"),'\n')
    cost, cities = writechain(Spotlight)
    print("\nThe total cost comes out to: ", cost)
    print("\nYou passed",cities,"cities (Including your starting and final city!)")
    print("\nWhen the program is finished, there are",PrioritetsQue.getSize(),"nodes in the que")

else:   # If no path was found
    print("No path was found")
    print("\nWhen the program is finished, there are",PrioritetsQue.getSize(),"nodes in the que")

print("The program looped",counter,"times")