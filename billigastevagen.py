from Alan import *
from DictHash import * 
from minHeap import *
from Islands import final   # Import how the vector containing all the islands
import sys

Map = MapEdges()    # Map of all the cities
Visited = DictHash() # Dictionary to keep track of previously visited cities
PrioritetsQue = minHeap()   # Prioritets kö, which is (min heap)!


class ParentNode:
    def __init__(self, city, cost = 10000, parent = None ):
        self.city = city
        self.parent = parent
        self.cost = cost  # Begining by setting a ridiculously high price

Start = "Strong Oak"    #Enter starting city    
End = "Vale of Doom"    #Enter final city

startindex = Map.getCityIndex(Start)    # Retreive the index of the starting index
endindex = Map.getCityIndex(End)    # Retreive the index of the final index

if type(startindex) is not int or type(endindex) is not int:    #Program will not continue if real cities are not given
    print("Enter cities that exist")
    sys.exit()

for Island in final:    # Go through the Islands
    if startindex in Island:    # If the starting city is in the list ( in the island )
        theIsland = Island  # A list of all the cities in the island



startNode = ParentNode(startindex,0)  # We begin with the starting city
PrioritetsQue.insert(startNode, startNode.cost) # Add the first city into the que with its cost as its priority!
for city in theIsland:
    if city != startNode.city: # Add all cities except the starting city ( Since the cost of starting city is 0 )
        Node = ParentNode(city)
        PrioritetsQue.insert( Node, Node.cost )    # Add the city into the que

finalNode = PrioritetsQue.getNode(endindex) # Keep tabs on final destination



counter = 0
while not PrioritetsQue.isEmpty():
    counter += 1
    Spotlight = PrioritetsQue.delFirst()    # Remove the city with the shortest total distance
    City = Spotlight.city   # Get the city index
    total = Spotlight.cost # Store the total cost so far

    Visited.store(City, True) # Store the city index into a dictionary to keep track of all visited cities

    children = Map.getNeighborsTo(City) # Get all the neighbors

    for child in children:
        if child not in Visited:    # Dont check children that have already been visited
            Node = PrioritetsQue.getNode(child) # Retreive the node from the Priority Que
            newCost = total + Map.getCostBetween( City, child ) # Check the price from start to child

            if newCost < Node.cost: # If the new cost is cheaper, update!
                Node.parent = Spotlight # Cheapest way to the child is via current city
                Node.cost = newCost # Update the cost
                PrioritetsQue.updateNode(Node)





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


if finalNode: #If we established a connection
    print("This is how you get to your destination: ")
    print('{0:20} {1}'.format("City","Cost"),'\n')
    cost, cities = writechain(finalNode)
    print("\nThe total cost comes out to: ", cost)
    print("\nYou passed",cities,"cities (Including your starting and final city!)")
    print("\nWhen the program is finished, there are",PrioritetsQue.getSize(),"nodes in the que")

else:
    print("No connection possible")
    print("\nWhen the program is finished, there are",PrioritetsQue.getSize(),"nodes in the que")


print("The program looped",counter,"times")