from Alan   import * 
from Islands import *
from DictHash import * 


#I know that this map is a map of the 5th island
Cities_5 = final[4]  # Get all the city index in the island

Map = MapEdges()  # Your map
Dictionary = DictHash() # A ditionary to store coordinates as key and city name as value, this is to get the city name once i have gotten the coordinated for all the cities
for city in Cities_5:   # Enter every city into the dictionary along with its coordinates
   Dictionary.store( Map.getCityCoord(city), Map.getCityName(city) )
       
       

island_map="""
---------------------------------------------------------------------------------------------------------------------------
      🏨 .                                         .  .  . 🏣 . 🏘                                                   
             .  .                       . 🏭 .  .  .  .  .  .  .  .  .                                                 
                   .             🏥 .  .  .           .     .     . 🏫 .  .  . 🏗                                    
                      .  .     .        .     .  .  .        .  .        .        .                                     
                            . 🏰 .  .  .  . 🏣 .              .  .     .        .                                     
                               .  .     .  .  .     .  .  .     .           .  .  .                                     
                               .  .  .  .  .  .  .           . 🏙 .  .        .  .                                     
                               .  .  .     .  .  .              .     .  .  . 🏙 .  .                                  
                              🏰 .     .  . 🏥 .        .        .     .     .  .  .                                  
                               .     . 🏪 .  .  .  .  .     .  . 🏨 .  .        .  .                                  
                                  .           .  . 🏢 .  .        .        .  . 🌆 .                                  
                                  .  .  .     .  .     .     .  .     .           .  .                                  
                                  .  .        .  .       🏙 .        .     .  .  .  .                                  
                                     .  .  .  .     .  .  .     .  .     .  .  .     .                                  
                                    🏯 .     .  .  .        .     .  . 🏢 .  .     .  .                               
                                        . 🏭 .  .  .  .  . 🏟 .  .        . 🏪    .  .                               
                                                                .  .  .  .  .     .     .                               
                                                                   . 🏥 .  .  .     .  .                               
                                                                      .        .  .  . 🏣                              
                                                                     🏦                                                
---------------------------------------------------------------------------------------------------------------------------
"""


x = 0 # Begining coordinates
y = 0
coordinates = []  # Will store city name and coordinates in here
useless = "- .\n" # If it is one of these symbols, i will not save the coordinates
for symbol in island_map:  # Go through every symbol in the string
   
   if symbol not in useless:  # Means that the program has arrived at a utf symbol
      vec = (x, y)   # Create coordinates
      name = Dictionary[vec]  # Get the name of the city with the help of the coordinates and knowing which island we are on
      coordinates.append( (name, vec) )   # Enter name and coordinates

   
   x += 1   #Increase your x    
   if symbol == "\n":      # Means that we have arrived at the end of a line
      x = 0       # Reset your back to zero
      y += 1      # Increase your y by 1

for element in coordinates:
   city = element[0]
   place = element[1]
   print( '{0:20} {1}'.format(city, place))


test = Map.getCityIndex("Strong Oak")
nei = Map.getNeighborsTo(test)
print('\n \n')
for i in nei:
       print('{0:20} {1}'.format(Map.getCityName(i), Map.getCityCoord(i)), Map.getCostBetween(test,i))

test = Map.getCityIndex("Gandahar")
nei = Map.getNeighborsTo(test)
print('\n \n')
for i in nei:
       print('{0:20} {1}'.format(Map.getCityName(i), Map.getCityCoord(i)), Map.getCostBetween(test,i))

       
test = Map.getCityIndex("Arlan's Way")
nei = Map.getNeighborsTo(test)
print('\n \n')
for i in nei:
       print('{0:20} {1}'.format(Map.getCityName(i), Map.getCityCoord(i)), Map.getCostBetween(test,i))