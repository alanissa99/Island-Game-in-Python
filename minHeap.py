
class Node:
    def __init__(self, city, cost):
        self.city = city    #The city name
        self.cost = cost    #The priority

# A min heap will be used. Lower costs are prioritized

class minHeap:
    def __init__(self):
        self.maxsize = 210      # Will never be reached, however set to 210 because thats how many cities i have
        self.slots = (self.maxsize + 1)*[None]  # The min heap will be written in vector form
        self.size = 0

    def isEmpty(self):  # Will return true if the size of the min heap is 0
        return self.size == 0
    
    def isFull(self):   # Will return true if the size of the min heap is the size of the max size
        return self.size == self.maxsize
    
    def insert(self, city, cost):
        if not self.isFull():   # Only insert if the min heap isnt full
            self.size += 1  # Once you insert, the size will increase by one
            self.slots[self.size] = Node(city, cost)    # Enter the node at the next slot available 
            i = self.size   # This is used to keep tabs on the reshuffling process

            while i > 1 and self.slots[i//2].cost > self.slots[i].cost: # Move the Node upwards as long as it has a  lower cost than its parent
                self.slots[i//2], self.slots[i] = self.slots[i], self.slots[i//2]   # Switcch positions
                i = i//2    #Next step
    
    def delFirst(self): # Remove the first node in the min heap
        if not self.isEmpty():  #Check first that the min Heap is not empty
            data = self.slots[1] # Retreive the first node in the min heap
            self.slots[1] = self.slots[self.size]   # Let the first slot point at the node in the last slot
            self.size -= 1  # By removing the first node, the size decreases by one
            i = 1 # Begin from the first node in the 

            while i <= self.size//2:   #As long as there is more than 1 Node in the min heap
                minChild = self.minindex(i) # Return the child with the lowest cost
                
                if self.slots[i].cost > self.slots[minChild].cost:  # If the parent has a cost greater than the child
                    self.slots[i], self.slots[minChild] = self.slots[minChild], self.slots[i]
                i = minChild    # Start moving down the min Heap and continue switching places if it is needed

            return data.city    #Return the city with the lowest cost

        else:   #If the min heap is empty, return nothing
            return None    

    def minindex(self, i): # A helping function that gives you the index of the child with the lowest cost
        if 2*i+1 > self.size:   # If there is only one child
            return 2*i
        
        if self.slots[2*i].cost < self.slots[2*i+1].cost:   #If the first child has a lower cost
            return 2*i

        else:   # Otherwise it means that the second child has a higher cost
            return 2*i+1
    
    def getSize(self):
        return self.size
    
    # This function is made quite terribly as it only works for how i have implemented it ( The function is expecting that i use the class ParentNode in a different file )
    def getNode(self,name): # Function to return the node associated with a city index ( Used in billigastevagen.py )
        for slot in self.slots:
            if slot and slot.city.city == name:
                return slot.city    # Return the ParentNode (OBS IT IS NOT THE SAME AS "Node" IN THIS FILE)
        
        return None
    
    def updateNode(self,node):
        i = 0   # The index
        for slot in self.slots: # find which index the node we want to update is at
            if slot and slot.city == node:
                break
            i += 1
        
        self.slots[i].cost = self.slots[i].city.cost # There are two nodes, make sure they both have some cost
        
        if i > 1 and self.slots[i//2].cost > self.slots[i].cost:  # If the parent is larger than the node
            while i > 1 and self.slots[i//2].cost > self.slots[i].cost: # Move the Node upwards as long as it has a  lower cost than its parent
                self.slots[i//2], self.slots[i] = self.slots[i], self.slots[i//2]   # Switcch positions
                i = i//2    #Next step
        
        minChild = self.minindex(i) # get the child with highest priority
        if i<= self.size//2 and self.slots[i].cost > self.slots[minChild].cost:    # if the child has a higher priority than the node
            while i <= self.size//2:   #As long as there is more than 1 Node in the min heap
                minChild = self.minindex(i) # Return the child with the lowest cost
                
                if self.slots[i].cost > self.slots[minChild].cost:  # If the parent has a cost greater than the child
                    self.slots[i], self.slots[minChild] = self.slots[minChild], self.slots[i]
                i = minChild    # Start moving down the min Heap and continue switching places if it is needed
        
            




