from distutils.log import error
from operator import truediv
from this import d
import pygame
from random import randint #get random integer number to #random
import math


#define text
def create_text(string):
    font = pygame.font.SysFont('sans',40)
    return font.render(string, True, WHITE)

#define distance
#p1 = x ,p1[0] = x1, p1[1] = y1, p2[0] = x2 p2[1] = y2 , 
def distance(p1,p2): 
    #sqrt((x1-x2)^2+ (y1-y2)^2))
    return math.sqrt((p1[0]-p2[0]) * (p1[0]-p2[0]) + (p1[1]-p2[1]) * (p1[1]-p2[1])) 


#define program
pygame.init()

screen = pygame.display.set_mode((1200,700))

pygame.display.set_caption("kmeans visualization")

running = True

clock = pygame.time.Clock()

#define color
BACKGROUND = (214,214,214)
BLACK = (0,0,0)
BACKGROUND_PANEL = (249,255,230)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (147,153,35)
PURPLE = (255,0,255)
SKY = (0,255,255)
ORANGE = (255,125,25)
GRAPE = (100,25,125)
GRASS = (55,155,65)

COLOR = [RED,GREEN,BLUE,YELLOW,PURPLE,SKY,ORANGE,GRAPE,GRASS]
#insert font
font = pygame.font.SysFont('sans', 40)
font_small = pygame.font.SysFont('sans', 20)
# text_plus = font.render('+', True, WHITE) #True is anti-alisas
# insert font by function     
text_plus = create_text('+')
text_minus= create_text('-')
text_run = create_text('Run')
text_reset = create_text('Reset')
text_random = create_text('Ramdon')
text_algorithm = create_text('Algorithm')

K = 0 #set K
error = 0
points = [] #list of all points that user put in
clusters = [] #Auto set ramdom point in panel
labels = []

while running:
    clock.tick(144) #frame per second
    screen.fill(BACKGROUND) #background color
    #detect mouse direction
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Draw Interface
    # Draw Panel
    pygame.draw.rect(screen, BLACK, (50,50,700,500)) #(X,Y,width,height)
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55,55,690,490))

    #K button +
    pygame.draw.rect(screen, BLACK, (850,50,50,50))
    screen.blit(text_plus, (860,50))

    #K button -
    pygame.draw.rect(screen, BLACK, (950,50,50,50))
    screen.blit(text_minus, (960,50))

    #K value
    text_k = font.render("K = " + str(K), True, BLACK) #create 'K' value
    screen.blit(text_k, (1050,50))

    #run button 
    pygame.draw.rect(screen, BLACK, (850,150,150,50))
    screen.blit(text_run,(900,150))

    #random button
    pygame.draw.rect(screen, BLACK, (850,250,150,50))
    screen.blit(text_random,(850,250))

    #algorithm button by scikit-learn 
    pygame.draw.rect(screen, BLACK, (850,450,150,50))
    screen.blit(text_algorithm, (850,450))

    #reset button
    pygame.draw.rect(screen, BLACK, (850,550,150,50))
    screen.blit(text_reset, (850,550))

    #error text
    text_error = font.render("Error = " + str(error), True, BLACK)
    screen.blit(text_error, (850,350))

    #draw mouse position when mouse is in panel
    if 50 < mouse_x < 750 and 50 < mouse_y < 550:
        text_mouse = font_small.render("(" + str(mouse_x - 50) + "," + str(mouse_y - 50) + ")", True , BLACK)
        screen.blit(text_mouse, (mouse_x + 10,mouse_y))
        
    # End draw Interface

    
    #print(mouse_x) #show the direction num of your mouse


    #logic function

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #enable QUIT button
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: #check when mouse is clicking
            #print('click') #print 'click' when user click by mouse
            #Create point on panel
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                point = [mouse_x -50 , mouse_y -50] #start with (0,0)
                points.append(point)
                #print("in panel")
                print(points)


            #Change K button +
            if 850 < mouse_x < 900 and 50 < mouse_y < 100: #Check when mouse click into 'k +' button
                K = K + 1
                print('click K+')
                if K > 9: #Stop K at 9 points because the color list have only 9, if you want to extend please extend color list before change this line number
                    K = 9

            #Change K button - 
            if 950 < mouse_x < 1000 and 50 < mouse_y < 100: #Check when mouse click into 'k +' button
                if K > 0:
                    K = K - 1 
                    print('click K-')
                

            #Run button
            if  850 < mouse_x < 1000 and 150 < mouse_y < 200:
                labels = []

                #assign points to closet clusters
                for p in points:
                    distances_to_cluster = []
                    for c in clusters:
                        dis = distance(p,c)
                        distances_to_cluster.append(dis)
                    min_distance = min(distances_to_cluster)
                    label = distances_to_cluster.index(min_distance)
                    labels.append(label)

                #update clusters
                for i in range(K):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count += 1
                    if count !=0:
                        
                        new_cluster_x = sum_x/count
                        new_cluster_y = sum_y/count
                        clusters[i] = [new_cluster_x,new_cluster_y]
                    pass
                print("run pressed")


            #Random button
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                clusters = []
                for i in range(K):
                    random_point = [randint(0,700), randint(0,500)] #height 700px,width 500px
                    clusters.append(random_point)
                print("random pressed")

            #Algorithm button
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                print("algorithm pressed")

            #Reset button
            if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
                print("reset pressed")
            
            #error text

    #draw Clusters
    for i in range(len(clusters)):
        pygame.draw.circle(screen,COLOR[i], (clusters[i][0] +50,clusters[i][1] + 50), 10) #+50 make sure that the cluster fit in the panel not in all program
    #Draw point around by circle
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0] + 50, points[i][1] + 50), 6) #screen,color,centre of circle,radius of circle #+50 because draw in all screen not just in the panel
        if labels == []:
            pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 5)
        else:
            pygame.draw.circle(screen, COLOR[labels[i]], (points[i][0] + 50, points[i][1] + 50), 5)
    pygame.display.flip() #display all element

pygame.quit() 