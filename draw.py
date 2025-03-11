import math
r=open('out.txt','w')
points = []
circle = []
s = 500

# x, y, z
for a in range(0, 360, 10):
    circle.append([math.cos(math.radians(a)) * s, math.sin(math.radians(a)) * s,0])

d=1000
for a in range(0, 360, 10):
    layer=[]
    for b in range(len(circle)):
        layer.append([
            (math.cos(math.radians(a))*s-d)*circle[b][0],
            (math.cos(math.radians(a))*s-d)*circle[b][1],
            math.sin(math.radians(a))*s*s
        ])
    points.append(layer)
light=[-0.577350269,-0.577350269,-0.577350269]
def convert(a):
    point=[0,0,0]
    for b in a:
        point[0]+=b[0]
        point[1]+=b[1]
        point[2]+=b[2]
    mag=(point[0]**2+point[1]**2+point[2]**2)**0.5
    point[0]/=mag
    point[1]/=mag
    point[2]/=mag
    
    return point[0]*light[0]+point[1]*light[1]+point[2]*light[2]

    
    #returns x rot, y rot,

quads=[]
for a in range(len(points)):
    for b in range(len(points[a])):
        temp=[points[a][b],points[a][b-1],points[a-1][b-1],points[a-1][b]]
        temp.append((-convert(temp)+1)*255/2)
        quads.append(temp)

quads.sort(key=lambda x:x[0][0])
r.write(str(quads))