from Alan import *
from DictHash import *
from ArrayQfile import *

Map = MapEdges()    #The class from the main code

#I will begin with the first city, find all the neighbors, place them into a vector.
#Next step is then to then remove the first city in the vector and create its children and add into the vector
#For every child created, the program needs to check if the child (neighbor) has already been created, this is done with the help of a dictionary.
#Once the list/que is empty, it means that there are no more neighbors and therefor it is a complete island!

Dictionary = DictHash() #Dictionary that will keep tabs on the children that were created
Que = ArrayQ()  #My queue of children


final = []      #Every element in this list should be a vector containing an island

for i in range(len(Map.cities)):    #For every city index

    if i not in Dictionary:   #  If the city hasnt already been looked at
        Que.enqueue(i)  #Entering my city into the queue
        Dictionary.store(i,True)    #Save it in the dictionary
        Result = [] # Vector that groups all the neighbours together, forming an island

        while not Que.isEmpty():    #While the queue isnt empty
            Spotlight = Que.dequeue()   #First element in the que
            children = Map.getNeighborsTo(Spotlight)    #A vector of all the neighboring cities
    
            for child in children:  #Look at every neighbor
        
                if child not in Dictionary:   #If it is a unique neighbor
                    Dictionary.store(child,True)    #Enter them into a dictionary, to keep memory
                    Que.enqueue(child)  #Add them into the que

            Result.append(Spotlight)    #group all the neighbors together
        
        final.append(Result)    #Add the island into final vector

if __name__ == '__main__':   
    print("There are",len(final),"islands") #Explain how many islands there are


    for i,vector in enumerate(final):   #Give the list of all the cities in the island
        vector.sort()
        print("\nIsland number",i+1,"consists of",len(vector),"cities, which are the following",vector)






