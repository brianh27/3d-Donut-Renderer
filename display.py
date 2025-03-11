from Points import points
import pygame
import math


pygame.init()


screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3d Donut")
clock = pygame.time.Clock()


rX, rY = 0.01, -0.01
d = 0.0002
thres = 80
light = [0.57672, 0.577350269, -0.577350269]




def convert(a):
    point = [0, 0, 0]
    for i in range(len(a)):
        point[0] += a[i][0]
        point[1] += a[i][1]
        point[2] += a[i][2]
    mag = math.sqrt(point[0] ** 2 + point[1] ** 2 + point[2] ** 2)
    point[0] /= mag
    point[1] /= mag
    point[2] /= mag

    return point[0] * light[0] + point[1] * light[1] + point[2] * light[2]

def draw():
    global points
    screen.fill((255, 255, 255))

    
    for i in range(len(points)):
        for g in range(4):
            
            points[i][g][0] = points[i][g][0] * math.cos(rY) + (
                points[i][g][1] * math.sin(rX) + points[i][g][2] * math.cos(rX)
            ) * math.sin(rY)
            points[i][g][1] = points[i][g][1] * math.cos(rX) - points[i][g][2] * math.sin(rX)
            points[i][g][2] = -points[i][g][0] * math.sin(rY) + (
                points[i][g][1] * math.sin(rX) + points[i][g][2] * math.cos(rX)
            ) * math.cos(rY)

    points.sort(key=lambda a: a[0][0])

    # shading
    for a in range(len(points)):
        temp = []
        for b in range(4):
            temp.append(points[a][b])
        points[a][4]=((-convert(temp) + 1) * 122)

    # draw
    for a in range(0, len(points), 1):
        temp = []
        if points[a][0][0] > thres * 10000:
            continue

        temp.append([points[a][0][1] * d + screen_width / 2, points[a][0][2] * d + screen_height / 2])
        temp.append([points[a][1][1] * d + screen_width / 2, points[a][1][2] * d + screen_height / 2])
        temp.append([points[a][2][1] * d + screen_width / 2, points[a][2][2] * d + screen_height / 2])
        temp.append([points[a][3][1] * d + screen_width / 2, points[a][3][2] * d + screen_height / 2])
        
        color = (points[a][4], points[a][4], points[a][4])  #shade
        pygame.draw.polygon(screen, color, temp)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw()
    print(points[0][-1])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
