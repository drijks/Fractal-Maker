import pygame
import math
import random
import colors
#pygame.init()

#purples = [colors.lavender, colors.thistle, colors.plum, colors.orchid, colors.violet, colors.fuchsia, colors.magenta, colors.mediumorchid, colors.darkorchid, colors.darkviolet, colors.blueviolet, colors.darkmagenta, colors.purple, colors.mediumpurple, colors.mediumslateblue, colors.slateblue, colors.darkslateblue, colors.rebeccapurple, colors.indigo]

##window properties
#size = [1100, 700]
#screen = pygame.display.set_mode(size)
#pygame.display.set_caption("FRACTALS!!!!!!!!!!!!!!!!")
#screen.fill(colors.WHITE)
#clock = pygame.time.Clock()





def translate(pt, a, b, c):
    return [pt[0] + a, pt[1]+b, pt[2]+c]

def multiTranslate(pt, aff):
    ptNew = []
    for i in range(len(pt)):
        ptNew.append([pt[i][0]+aff[0], pt[i][1]+aff[1], pt[i][2]+aff[2]])
    return ptNew
    
def customMatrix(a, b, c, d, e, f, g, h, i):
    return [[a,b,c],[d,e,f],[g,h,i]]

def dotProduct(row, column):
    val = 0
    for i in range(len(row)):
        val = val + (row[i]*column[i])
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
    return [[s,0,0],[0,s,0],[0,0,s]]

def customScaling(x, y, z):
    return [[x,0,0],[0,y,0],[0,0,z]]


#rotationmatrices (takes an angle in degrees)
def xRotate(theta):
    t = ((theta * math.pi)/180)    
    c = round(math.cos(t), 5)
    s = round(math.sin(t), 5)
    return [[1,0,0],[0,c,-s],[0,s,c]]

def yRotate(theta):
    t = ((theta * math.pi)/180)    
    c = round(math.cos(t), 5)
    s = round(math.sin(t), 5)
    return [[c,0,s],[0,1,0],[-s,0,c]]

def zRotate(theta):
    t = ((theta * math.pi)/180)    
    c = round(math.cos(t), 5)
    s = round(math.sin(t), 5)
    return [[c,-s,0],[s,c,0],[0,0,1]]


#skew/shear matrices
def skewMatrix1(a):
    t = round(math.tan(a), 5)
    return [[1,0,0],[t,1,0],[0,0,1]]
def skewMatrix2(a):
    t = round(math.tan(a), 5)    
    return [[1,0,0],[0,1,0],[t,0,1]]
def skewMatrix3(a):
    t = round(math.tan(a), 5)
    return [[1,t,0],[0,1,0],[0,0,1]]
def skewMatrix4(a):
    t = round(math.tan(a), 5)
    return [[1,t,0],[0,1,0],[0,0,1]] 
def skewMatrix5(a):
    t = round(math.tan(a), 5)
    return [[1,0,0],[0,1,0],[0,t,1]]
def skewMatrix6(a):
    t = round(math.tan(a), 5)
    return [[1,0,t],[0,1,0],[0,0,1]]  
def identityMatrix():
    return [[1,0,0],[0,1,0],[0,0,1]]


def xReflect():
    return [[1,0,0],[0,-1,0],[0,0,-1]]
def yReflect():
    return [[-1,0,0],[0,1,0],[0,0,-1]]
def zReflect():
    return [[-1,0,0],[0,-1,0],[0,0,1]]


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
#def getItOnScreen(pt):
    #if pt[2] != 0:
        #x = pt[0]/pt[2]
        #y = pt[1]/pt[2]
    #else:
        #x = pt[0]
        #y = pt[1]
    #return [x+400, -y+size[1]-200]

def getItOnScreen(size, pt):
    x = pt[0]
    y = pt[1]
    return [int(x+(size[0]/2)), int(-y+(size[1]/2))]


#draws lines between points in a list, requires the points to ONLY have x and y coordinates
def drawLines(screen, pt, color, width): 
    end = len(pt)-1
    pygame.draw.line(screen, color, getItOnScreen(pt[0]), getItOnScreen(pt[end]), width)
    for i in range(len(pt)-1):
        pygame.draw.line(screen, color, getItOnScreen(pt[i]), getItOnScreen(pt[i+1]), width)

def drawXYLines(screen, drawPt, width):
    end = len(drawPt)-1
    pygame.draw.line(screen, drawPt[end][1], getItOnScreen(drawPt[0][0]), getItOnScreen(drawPt[end][0]), width)
    for i in range(len(drawPt)-1):
        pygame.draw.line(screen, drawPt[i][1], getItOnScreen(drawPt[i][0]), getItOnScreen(drawPt[i+1][0]), width)

def drawPoints(size, screen, drawPts, color):
    for i in range(len(drawPts)):
        pygame.draw.line(screen, color, getItOnScreen(size, drawPts[i]), getItOnScreen(size, drawPts[i]), 1)

def randomMultiColorDrawPoints(screen, drawPts, colors):
    for i in range(len(drawPts)):
        r = random.randint(0,len(colors)-1)
        pygame.draw.line(screen, colors[r], getItOnScreen(drawPts[i]), getItOnScreen(drawPts[i]), 1)
  
def multiColorDrawPoints(screen, drawPts, colors):
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
    ptNew = [ptNew[0]+aff[0], ptNew[1]+aff[1], ptNew[2]+aff[2]]
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
    pt1 = translate(pt,aff1[0],aff1[1],aff1[2])
    ptNew = (oneByFour(f, pt1))
    ptNew1 = translate(ptNew, aff2[0],aff2[1],aff2[2])
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


def drawXYPoints(screen, pts, color):
    drawPts = getXY2(pts)
    for i in range(len(drawPts)):
        pygame.draw.line(screen, color, getItOnScreen(drawPts[i]), getItOnScreen(drawPts[i]), 1)
        
        
def getXY2(pt):
    newPt = []
    for i in range(len(pt)):
        newPt.append([int(pt[i][0]/pt[i][2]),int(pt[i][1]/pt[i][2])])
    return newPt


#box = [[0,0],[100,0],[100,150],[0,150]]

def affineNestColor(pt, fs, affs, col, num):
    pts = []
    pts.append([pt,col[0]])
    for i in range(1,num):
        j = random.randint(0,len(fs)-1)
        f = fs[j]
        aff = affs[j]
        pts.append([affine(pts[i-1][0],f,aff),col[j]])
    return pts

def affineNestColor2(pt, fs, affs, col, num):
    pts = []
    pts.append([pt,col[0],[0,0,0]])
    for i in range(1,num):
        j = random.randint(0,len(fs)-1)        
        f = fs[j]
        aff = affs[j]
        a,b,c = aff
        aff2 = [int(a/2),int(b/2),int(c/2)]
        aff3 = [int(a/4),int(b/4),int(c/4)]
        aff4 = [0,0,0]
        pts.append([affine(pts[i-1][0],f,aff),col[j],aff4,f])
    return pts

def affineNestColor3(pt, fs, affs, col, num):
    pts = []
    pts.append([pt,col[0],[0,0,0]])
    for i in range(1,num):
        for j in range(len(fs)):
            f = fs[j]
            aff = affs[j]
            a,b,c = aff
            aff2 = [int(a/2),int(b/2),int(c/2)]
            aff3 = [int(a/4),int(b/4),int(c/4)]
            aff4 = [0,0,0]
            pts.append([affine(pts[i-1][0],f,aff),col[j],aff4,f])
    return pts

def drawPointsColor(size, screen, drawPts):
    for i in range(len(drawPts)):
        pygame.draw.line(screen, drawPts[i][1], getItOnScreen(size, drawPts[i][0]), getItOnScreen(size, drawPts[i][0]), 1)
        
def affItUp(pts,f):
    newPts = []
    for i in range(len(pts)):
        a,b,c = pts[i][2]
        aff1 = [-a,-b,-c]
        aff2 = [a,b,c]
        newPts.append([transFirst(pts[i][0],f,aff1,aff2),pts[i][1]])
    return newPts


def halfwayPoint(pt1,pt2):
    a, b, c = pt1
    d, e, f = pt2
    g = int(a+((d-a)/2))
    h = int(b+((e-b)/2))
    i = int(c+((f-c)/2))
    return [g,h,i]

def chaosGame(pt, v1, v2, v3, v4, num):
    p = pt
    pts = []
    for i in range(num):
        r = random.randint(0,4)
        if r == 0:
            nv = halfwayPoint(p, v1)
            col = colors.red
            v = v1
        elif r == 1:
            nv = halfwayPoint(p, v2)
            col = colors.blue
            v = v2
        elif r == 2:
            nv = halfwayPoint(p, v3)
            col = colors.limegreen
            v = v3
        else:
            nv = halfwayPoint(p, v4)
            col = colors.yellow
            v = v4
        pts.append([nv,col,v])
        p = nv
    return pts

def chaosGame2(pt, vs, colors, num):
    p = pt
    pts = []
    for i in range(num):
        r = random.randint(0, len(vs)-1)
        #nv = halfwayPoint(halfwayPoint(p, vs[r]),vs[r])
        nv = halfwayPoint(p, vs[r])
        pts.append([nv, colors[r], vs[r]])
        p = nv
    return pts

def chaosGame3(pt, vs, colors, num):
    p = pt
    pts = []
    aaa = [0,0,0]
    for i in range(num):
        r = random.randint(0, len(vs)-1)
        nv = onethird(p, vs[r])
        pts.append([nv, colors[r], aaa])
        p = nv
    return pts

def onethird(pt1,pt2):
    a, b, c = pt1
    d, e, f = pt2
    g = int(a+(2*(d-a)/3))
    h = int(b+(2*(e-b)/3))
    i = int(c+(2*(f-c)/3))
    return [g,h,i]

def affineNestColor3(pt, fs, affs, col, num):
    pts = []
    pts.append([pt,col[0],[0,0,0]])
    for i in range(1,num):
        for j in range(len(fs)):
            f = fs[j]
            aff = affs[j]
            a,b,c = aff
            aff2 = [int(a/2),int(b/2),int(c/2)]
            aff3 = [int(a/4),int(b/4),int(c/4)]
            aff4 = [0,0,0]
            pts.append([affine(pts[i-1][0],f,aff),col[j],aff4,f])
    return pts



##MAIN
#done = False
#while not done:
    #clock.tick(25)
    #screen.fill(colors.WHITE)
    #for event in pygame.event.get(): 
        #if event.type == pygame.QUIT:
            #done=True
            
    #pygame.draw.line(screen, colors.GREEN, [0,size[1]/2], [size[0],size[1]/2], 1)
    #pygame.draw.line(screen, colors.GREEN, [size[0]/2,0], [size[0]/2,size[1]], 1)
    
    
    #pygame.display.flip()
#pygame.quit()

