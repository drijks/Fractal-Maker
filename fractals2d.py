import pygame
import math
import random
#pygame.init()


#colors
RED = (255,0,0)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
LIMEGREEN =(50,205,50)
GREEN = (0,128,0)
BLUE = (0,0,255)
SKYBLUE = (135,206,235)
LIGHTBLUE =(173,216,230)
INDIGO = (75,0,130)
PURPLE = (128,0,128)
WHITE = (255,255,255)
BLACK = (0,0,0) 

#window properties
#size = [1100, 700]
#screen = pygame.display.set_mode(size)
#pygame.display.set_caption("FRACTALS!!!!!!!!!!!!!!!!")
#screen.fill(WHITE)
#clock = pygame.time.Clock()


def translate(pt, a, b):
    return [pt[0] + a, pt[1]+b]

def multiTranslate(pt, aff):
    ptNew = []
    for i in range(len(pt)):
        ptNew.append([pt[i][0]+aff[0], pt[i][1]+aff[1]])
    return ptNew
    
def customMatrix(a, b, c, d):
    return [[a,b],[c,d]]

def dotProduct(row, column):
    val = 0
    for i in range(len(row)):
        val = val + row[i]*column[i]
    return val

#takes a matrix pt1 and a point pt2 and does the matrix multiplication
def oneByFour(pt1, pt2):
    ptNew = []
    for i in range(len(pt1)):
        ptNew.append(dotProduct(pt1[i], pt2))
    return ptNew

def multiPointTransform(pt1, pt2):
    newPt = []
    for i in range(len(pt2)):
        newPt.append(oneByFour(pt1, pt2[i]))
    return newPt

#scaling matrices
def uniformScaling(s):
    return [[s,0],[0,s]]

def customScaling(x, y):
    return [[x,0],[0,y]]


#rotationmatrices (takes an angle in degrees)
def zRotate(theta):
    t = ((theta * math.pi)/180)    
    c = round(math.cos(t), 5)
    s = round(math.sin(t), 5)
    return [[c,-s],[s,c]]


#skew/shear matrices
def skewMatrixX(a):
    return [[1,a],[0,1]]
def skewMatrixY(a):
    return [[1,0],[a,1]]
def identityMatrix():
    return [[1,0],[0,1]]

def xReflect():
    return [[-1,0],[0,1]]
def yReflect():
    return [[1,0],[0,-1]]
def xyReflect():
    return [[0,1],[1,0]]

#combines matrices
def multiMatrix(a, b):
    newPt = []
    for i in range(len(a)):
        newPt.append([])
        for j in range(len(a)):
            sum = 0
            for k in range(len(a)):
                sum = sum + (a[i][k]*b[k][j])
            newPt[i].append(sum)
    return newPt

#combines matrices entered into a list
def multiList(li):
    tr = li[0]
    for i in range(len(li)-1):
        tr = multiMatrix(identityMatrix(), tr)
        tr = multiMatrix(tr, li[i+1])
    return tr

#used to get points to show up on screen
def getItOnScreen(size, pt):
    return [pt[0]+int(size[0]/2), -pt[1]+int(size[1]/2)]

#draws lines between points in a list, requires the points to ONLY have x and y coordinates
def drawLines(pt, color, width): 
    end = len(pt)-1
    pygame.draw.line(screen, color, getItOnScreen(pt[0]), getItOnScreen(pt[end]), width)
    for i in range(len(pt)-1):
        pygame.draw.line(screen, color, getItOnScreen(pt[i]), getItOnScreen(pt[i+1]), width)

def drawXYLines(drawPt, color, width):
    end = len(drawPt)-1
    pygame.draw.line(screen, color, getItOnScreen(drawPt[0]), getItOnScreen(drawPt[end]), width)
    for i in range(len(drawPt)-1):
        pygame.draw.line(screen, color, getItOnScreen(drawPt[i]), getItOnScreen(drawPt[i+1]), width)

def drawPoints(size, screen, drawPts, color):
    for i in range(len(drawPts)):
        pygame.draw.line(screen, color, getItOnScreen(drawPts[i]), getItOnScreen(drawPts[i]), 1)
        
def drawPointsColor(size, screen, drawPts):
    for i in range(len(drawPts)):
        pygame.draw.line(screen, drawPts[i][1], getItOnScreen(size, drawPts[i][0]), getItOnScreen(size, drawPts[i][0]), 1)
        
def randomMultiColorDrawPoints(drawPts, colors):
    for i in range(len(drawPts)):
        r = random.randint(0,len(colors)-1)
        pygame.draw.line(screen, colors[r], getItOnScreen(drawPts[i]), getItOnScreen(drawPts[i]), 1)
  
def multiColorDrawPoints(drawPts, colors):
    a = int(len(drawPts)/len(colors))
    for i in range(1,len(colors)):
        for j in range(a*i-1,a*i):
            pygame.draw.line(screen, colors[i], getItOnScreen(drawPts[j]), getItOnScreen(drawPts[i]), 1)

#make a nested list of points
def nestList(pt, f, num):
    pts = []
    pts.append(pt)
    for i in range(1,num):
        pts.append(oneByFour(f,pts[i-1]))
    return pts

def nestedList(pt, f, num):
    pts = []
    pts.append(pt)
    for i in range(1,num):
        j = random.randint(0,len(f)-1)
        func = f[j]
        pts.append(oneByFour(func,pts[i-1]))
    return pts

def affine(pt, f, aff):
    ptNew = (oneByFour(f, pt))
    ptNew = [ptNew[0]+aff[0], ptNew[1]+aff[1]]
    return ptNew

def affineMulti(pt, f, aff):
    ptNew = multiPointTransform(f, pt)
    for i in range(len(ptNew)):
        ptNew[i] = [ptNew[i][0]+aff[0], ptNew[i][1]+aff[1]]
    return ptNew

def affineNest(pt, fs, affs, num):
    pts = []
    pts.append(pt)
    for i in range(1,num):
        j = random.randint(0,len(fs)-1)
        f = fs[j]
        aff = affs[j]
        pts.append(affine(pts[i-1],f,aff))
    return pts

def transFirst(pt,f,aff1,aff2):
    pt1 = translate(pt,aff1[0],aff1[1])
    ptNew = (oneByFour(f, pt1))
    ptNew1 = translate(ptNew, aff2[0],aff2[1])
    return ptNew1

def transFirstMulti(pt,f,aff1,aff2):
    pts = []
    for i in range(len(pt)):
        pts.append(transFirst(pt[i],f,aff1,aff2))
    return pts

def transAffineNest(pt, fs, aff1,affs2, num):
    pts = []
    pts.append(pt)
    for i in range(1,num):
        j = random.randint(0,len(fs)-1)
        f = fs[j]
        aff = affs2[j]
        pts.append(transFirst(pts[i-1],f,aff1,aff))
    return pts

def affineNestColor(pt, fs, affs, col, num):
    pts = []
    pts.append([pt,col[0]])
    for i in range(1,num):
        j = random.randint(0,len(fs)-1)
        f = fs[j]
        aff = affs[j]
        pts.append([affine(pts[i-1][0],f,aff),col[j]])
    return pts

##MAIN
#done = False
#while not done:
    #clock.tick(25)
    #screen.fill(WHITE)
    #for event in pygame.event.get(): 
        #if event.type == pygame.QUIT:
            #done=True
    #if event.type == pygame.KEYDOWN:
        #if event.key == pygame.K_a:
            #if leafscale1 >= 1:
                #leafscale1 = 0
            #else:
                #leafscale1 += .01
        #if event.key == pygame.K_b:
            #if leafscale2 >= 1:
                #leafscale2 = 0
            #else:
                #leafscale2 += .01
        #if event.key == pygame.K_c:
            #if leafrotate1 >= 90:
                #leafrotate1 = 0
                #leafrotate2 = -1*leafrotate1
            #else:
                #leafrotate1 += 1
                #leafrotate2 = -1*leafrotate1
        #if event.key == pygame.K_d:
            #if leaftrans1 >= 100:
                #leaftrans1 = -100
            #else:
                #leaftrans1 += 10
        #if event.key == pygame.K_e:
            #if leaftrans2 >= 300:
                #leaftrans2 = 100
            #else:
                #leaftrans2 += 10
        #if event.key == pygame.K_f:
            #if leaftrans3 >= 200:
                #leaftrans3 = 0
                #leaftrans4 = -1*leaftrans3
            #else:
                #leaftrans3 += 5
                #leaftrans4 = -1*leaftrans3
        #if event.key == pygame.K_g:
            #if leaftrans5 >= 75:
                #leaftrans5 = 25
            #else:
                #leaftrans5 += 5
        #if event.key == pygame.K_r:
            #leafscale1 = 0.6
            #leafscale2 = 0.5
            #leafrotate1 = 30
            #leafrotate2 = -1*leafrotate1
            #leaftrans1 = 0  
            #leaftrans2 = 200    
            #leaftrans3 = 100 
            #leaftrans4 = -1*leaftrans3
            #leaftrans5 = 50       
    #leaf0 = [0,0]
    
    #screen.blit(instructions1, (800, 50))
    #screen.blit(instructions2, (800, 70))
    #screen.blit(instructions3, (800, 90))
    #screen.blit(instructions4, (800, 110))
    #screen.blit(instructions5, (800, 130))
    #screen.blit(instructions6, (800, 150))
    #screen.blit(instructions7, (800, 170))
    #screen.blit(instructions15, (800, 190))
    
    #varxrot = font.render("scale 1: "+str(leafscale1),1,(0,0,0))
    #varyrot = font.render("scale 2: "+str(leafscale2),1,(0,0,0))
    #varzrot = font.render("rotation: "+str(leafrotate1),1,(0,0,0))
    #varxtrans = font.render("translation 1: "+str(leaftrans1),1,(0,0,0))
    #varytrans = font.render("translation 2: "+str(leaftrans2),1,(0,0,0))
    #varztrans = font.render("translation 3: "+str(leaftrans3),1,(0,0,0))
    #varscale = font.render("translation 4: "+str(leaftrans5), 1, (0,0,0))   
    #screen.blit(varxrot, (50, 50))
    #screen.blit(varyrot, (200, 50))
    #screen.blit(varzrot, (350, 50))
    #screen.blit(varxtrans, (500, 50))
    #screen.blit(varytrans, (50, 70))
    #screen.blit(varztrans, (200, 70))
    #screen.blit(varscale, (350, 70))    
    ##pygame.draw.line(screen, GREEN, [0,size[1]-200], [size[0],size[1]-200], 1)
    ##pygame.draw.line(screen, GREEN, [400,0], [400,size[1]], 1)
    
    
    
    #leaf1 = []
    #leaf2 = []
    #leaf1.append(customScaling(leafscale1,leafscale1))
    #leaf2.append([leaftrans1,leaftrans1])
    #leaf1.append(customScaling(leafscale2,leafscale2))
    #leaf2.append([leaftrans1,leaftrans2])
    #leaf1.append(multiList([zRotate(leafrotate1),customScaling(leafscale2,leafscale2)]))
    #leaf2.append([leaftrans4,leaftrans5])
    #leaf1.append(multiList([zRotate(leafrotate2),customScaling(leafscale2,leafscale2)]))
    #leaf2.append([leaftrans3,leaftrans5])
    #leaf = transAffineNest(leaf0,leaf1,leaf0,leaf2,100000)    
    
    
    ##ADD DRAW FUNCTIONS HERE
    #randomMultiColorDrawPoints(leaf,[RED,ORANGE,YELLOW,LIMEGREEN,GREEN,BLUE,SKYBLUE,LIGHTBLUE,INDIGO,PURPLE])

    
    #pygame.display.flip()


#pygame.quit()

