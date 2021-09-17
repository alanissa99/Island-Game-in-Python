from Alan import *
from DictHash import *
from ArrayQfile import *
import sys

Map = MapEdges()    #My map
Dictionary = DictHash() #My Dictionary to keep an eye on previously visited cities
Que = ArrayQ()  #My que

class ParentNode:
    def __init__(self, city, parent = None):
        self.city = city
        self.parent = parent

Start = "The Last Battle"    #Enter starting city    
End = "Icemeet"    #Enter final city

startindex = Map.getCityIndex(Start)    #Get the index of the starting city
endindex = Map.getCityIndex(End)    #Get the index of the final city


if type(startindex) is not int or type(endindex) is not int:    #Program will not continue if real cities are not given
    print("Enter cities that exist")
    sys.exit()

Que.enqueue(ParentNode(startindex))    #Enter the starting node into the que
finalNode = None    #If we find a way to connect to cities then this will change, otherwise its none
while not Que.isEmpty():
    Spotlight = Que.dequeue()   #Take out the first city in the que
    City = Spotlight.city  #Take the city out of the node

    if City == endindex: #If the city is the final destination, exit!
        break

    else:   
        neighbors = Map.getNeighborsTo(City)    #Find all the neighbors

        for neighbor in neighbors:  #For every neighbor
            
            if neighbor not in Dictionary:   #Otherwise  add to dictionary and add to que
                Dictionary.store(neighbor,True) 
                if neighbor == endindex:    #If it is the final city, create a pointer to keep tabs on the final node
                    finalNode = ParentNode(neighbor, Spotlight)
                    Que.enqueue(finalNode)
                
                else:
                    Que.enqueue( ParentNode(neighbor, Spotlight) )


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

        print('{0:20} {1}'.format(Map.getCityName(city), Map.getCostBetween(city, Node.parent.city)))
        return cost,cities    


if finalNode:   #If i found a way to connect the cities, this variable should not be equal to None anymore
    print("This is how you get to your destination: ")
    print('{0:20} {1}'.format("City","Cost"),'\n')
    cost, cities = writechain(finalNode)
    print("\nThe total cost comes out to: ", cost)
    print("\nYou passed",cities,"cities (Including your starting and final city!)")
    print("\nWhen the program is finished, there are",len(Que._array),"nodes in the que")

else:   #If i didnt find a way, finalNode is equal to None, so we print the following
    print("There was no way to connect the cities")
    print("\nWhen the program is finished, there are",len(Que._array),"nodes in the que")





