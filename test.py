import math
#p1 = x ,p1[0] = x1, p1[1] = y1, p2[0] = x2 p2[1] = y2 , 
def distance(p1,p2): 
    #sqrt((x1-x2)^2+ (y1-y2)^2))
    return math.sqrt((p1[0]-p2[0]) * (p1[0]-p2[0]) + (p1[1]-p2[1]) * (p1[1]-p2[1])) 

a = [1,1]
b = [2,2]

distance1 = distance(a,b)
print(distance1)