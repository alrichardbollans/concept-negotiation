def find_closest_cuboid(concept,point): #given a point and a concept, finds cuboid in concept which is closest to the point
    closest_points=[]
    distances=[]
    num_cuboids = len(concept._core._cuboids)
    cub = 0
    for x in range(0,num_cuboids):
        closest_points.append(concept._core._cuboids[x].find_closest_point(point))
        distances.append(space.distance(point,closest_points[x],concept._weights))

    
    for x in range(0,num_cuboids):
        if distances[cub]>distances[x]:
            cub = x

    return concept._core._cuboids[cub]



def update_concept(concept,point): # given a point to add to the concept, finds the closest cuboid in the concept and extends the cuboid with the point
    cub = find_closest_cuboid(concept,point)
    for x in range(0,len(cub._p_min)):
        if point[x]<cub._p_min[x]:
            cub._p_min[x]=point[x]
        if point[x]>cub._p_max[x]:
            cub._p_max[x]=point[x]


def com_cuboid(cuboid): #calcualtes centre of mass of a given cuboid
    com=[]
    for x in range(0,len(cuboid._p_min)):
        com.append((cuboid._p_max[x]+cuboid._p_min[x])/2)
    return com

def weight_cuboid(cuboid): #calculates the volume of a cuboid which, assuming uniform density, we can use as mass/weight
    lengths=[]
    w=1
    for x in range(0,len(cuboid._p_min)):
        lengths.append(cuboid._p_max[x]-cuboid._p_min[x])
    if len(lengths)==0:
        return 0
    else:
        for x in range(0,len(lengths)):
            w=w*lengths[x]
        return w 
     

def comconcept(concept): #calculates the total centre of mass for a concept assuming uniform density
    num_cuboids = len(concept._core._cuboids)
    
    totalweight=0
    sumofweightedcoms=[]
    totalcom=[]
    for y in range(0,len(concept._core._cuboids[0]._p_min)):
        sumofweightedcoms.append(0)
        totalcom.append(0)

    for cuboid in concept._core._cuboids:
        totalweight+=weight_cuboid(cuboid)
        for y in range(0,len(cuboid._p_min)):
  
            sumofweightedcoms[y]+=weight_cuboid(cuboid)*com_cuboid(cuboid)[y]

    for y in range(0,len(concept._core._cuboids[0]._p_min)):
        totalcom[y]=sumofweightedcoms[y]/totalweight
    return totalcom
