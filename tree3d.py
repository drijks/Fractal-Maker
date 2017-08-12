import pygame
import math
import random
import colors
#pygame.init()

purples = [colors.lavender, colors.thistle, colors.plum, colors.orchid, colors.violet, colors.fuchsia, colors.magenta, colors.mediumorchid, colors.darkorchid, colors.darkviolet, colors.blueviolet, colors.darkmagenta, colors.purple, colors.mediumpurple, colors.mediumslateblue, colors.slateblue, colors.darkslateblue, colors.rebeccapurple, colors.indigo]

#window properties
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

def getItOnScreen(pt):
    x = pt[0]
    y = pt[1]
    return [x+(size[0]/2), -y+(size[1]/2)]


#draws lines between points in a list, requires the points to ONLY have x and y coordinates
def drawLines(pt, color, width): 
    end = len(pt)-1
    pygame.draw.line(screen, color, getItOnScreen(pt[0]), getItOnScreen(pt[end]), width)
    for i in range(len(pt)-1):
        pygame.draw.line(screen, color, getItOnScreen(pt[i]), getItOnScreen(pt[i+1]), width)

def drawXYLines(drawPt, width):
    end = len(drawPt)-1
    pygame.draw.line(screen, drawPt[end][1], getItOnScreen(drawPt[0][0]), getItOnScreen(drawPt[end][0]), width)
    for i in range(len(drawPt)-1):
        pygame.draw.line(screen, drawPt[i][1], getItOnScreen(drawPt[i][0]), getItOnScreen(drawPt[i+1][0]), width)

def drawPoints(drawPts, color):
    for i in range(len(drawPts)):
        pygame.draw.line(screen, color, getItOnScreen(drawPts[i]), getItOnScreen(drawPts[i]), 1)

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
    ptNew = [ptNew[0]+aff[0], ptNew[1]+aff[1], ptNew[2]+aff[2]]
    return ptNew

def affineMulti(pt, f, aff):
    ptNew = multiPointTransform(f, pt)
    for i in range(len(ptNew)):
        ptNew[i] = [ptNew[i][0]+aff[0], ptNew[i][1]+aff[1], ptNew[i][2]+aff[2]]
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


def drawXYPoints(pts, color):
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


def drawPointsColor(drawPts):
    for i in range(len(drawPts)):
        pygame.draw.line(screen, drawPts[i][1], getItOnScreen(drawPts[i][0]), getItOnScreen(drawPts[i][0]), 1)
        
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
            aff4 = [a*2,b*2,c*2]
            pts.append([affine(pts[i-1][0],f,aff),col[j],aff4,f])
    return pts


def absYZ(pt):
    return [pt[0], abs(pt[0]), abs(pt[0])]

def absXY(pt):
    return [abs(pt[2]), abs(pt[2]), pt[2]]

def absYnZ(pt):
    return [pt[0], abs(pt[0]), -abs(pt[0])]

def posXabsoval(pt):
    return ([int(abs(pt[0])), int(abs(pt[0])), int(abs(pt[0]))])

def negXabsoval(pt):
    return ([int(-abs(pt[0])), int(abs(pt[0])), int(abs(pt[0]))])

def vertline(pt):
    return ([int(pt[0]*0), int(abs(pt[0])), int(abs(pt[0]))])

def parabolic(pt):
    return ([int(pt[0]), int((.1*pt[0])*(.1*pt[0])), int((.1*pt[0])*(.1*pt[0]))])


def affAndNonNestColor(pt,fs,affs,col,num):
    pts = []
    affe = [2,2,2]
    pts.append([pt,col[0],affs[0]])
    for i in range(1,num):
        j = random.randint(0,len(fs)-1)
        
        if fs[j][1] == 0:
            f = fs[j][0]
            aff = affs[j]
            pts.append([affine(pts[i-1][0],f,aff),col[j],affe])
        elif fs[j][1] == 1:
            f = fs[j][0]
            aff = affs[j]            
            pts.append([affine(absYZ(pts[i-1][0]),f,aff),col[j],affe])
        elif fs[j][1] == 2:
            f = fs[j][0]
            aff = affs[j]             
            pts.append([affine(vertline(pts[i-1][0]),f,aff),col[j],affe])
        elif fs[j][1] == 3:
            f = fs[j][0]
            aff = affs[j]            
            pts.append([affine(posXabsoval(pts[i-1][0]),f,aff),col[j],affe])
        elif fs[j][1] == 4:
            f = fs[j][0]
            aff = affs[j]            
            pts.append([affine(negXabsoval(pts[i-1][0]),f,aff),col[j],affe])            
        elif fs[j][1] == 5:
            f = fs[j][0]
            aff = affs[j]             
            pts.append([affine(parabolic(pts[i-1][0]),f,aff),col[j],affe])
        elif fs[j][1] == 6:
            f = fs[j][0]
            aff = affs[j]
            pts.append([affine(absXY(pts[i-1][0]),f,aff),col[j],affe])
        else:
            f = fs[j][0]
            aff = affs[j]
            pts.append([affine(absYnZ(pts[i-1][0]),f,aff),col[j],affe])        
            
    return pts



#vertices = [[0,0,0], [0,0,200], [0,200,0], [200,0,0], [200,0,200], [200,200,0], [0,200,200]]
vertices = [[1,1,1], [1,1,201], [1,201,1], [201,1,1]]
#st3d = chaosGame2([100, 50, 5], vertices, purples, 10000)
xrot = 90
yrot = 0
zrot = 0


def treethang():
    st3d1 = []
    st3d2 = []
    st3d3 = []
    st3d1.append([multiList([xRotate(-45),uniformScaling(.5)]), 0])
    st3d2.append([-100,100,-100])
    st3d3.append(colors.red)
    st3d1.append([multiList([xRotate(45),uniformScaling(.5)]), 0])
    st3d2.append([100,100,100])
    st3d3.append(colors.plum)
    st3d1.append([multiList([zRotate(45),uniformScaling(.5)]), 0])
    st3d2.append([-100,100,100])
    st3d3.append(colors.black)
    st3d1.append([multiList([zRotate(-45),uniformScaling(.5)]), 0])
    st3d2.append([100,100,-100])
    st3d3.append(colors.blue)
    st3d1.append([uniformScaling(.5), 1])
    st3d2.append([0,0,0])
    st3d3.append(colors.limegreen)
    st3d1.append([uniformScaling(.5), 7])
    st3d2.append([0,0,0])
    st3d3.append(colors.limegreen)
    return affAndNonNestColor([0,0,0],st3d1,st3d2,st3d3,10000)

##MAIN
#done = False
#while not done:
    #clock.tick(25)
    #screen.fill(colors.WHITE)
    #for event in pygame.event.get(): 
        #if event.type == pygame.QUIT:
            #done=True
    #if event.type == pygame.KEYDOWN:
        #if event.key == pygame.K_a:
            #if xrot >= 360:
                #xrot = 0
            #else:
                #xrot += 2
        #if event.key == pygame.K_b:
            #if xrot <= 0:
                #xrot = 360
            #else:
                #xrot -= 2
        #if event.key == pygame.K_c:
            #if yrot >= 360:
                #yrot = 0
            #else:
                #yrot += 2
        #if event.key == pygame.K_d:
            #if yrot <= 0:
                #yrot = 360
            #else:
                #yrot -= 2
        #if event.key == pygame.K_e:
            #if zrot >= 360:
                #zrot = 0
            #else:
                #zrot += 2
        #if event.key == pygame.K_f:
            #if zrot <= 0:
                #zrot = 360
            #else:
                #zrot -= 2
        #if event.key == pygame.K_r:
            #xrot = 0
            #yrot = 0
            #zrot = 0
            
    #pygame.draw.line(screen, colors.GREEN, [0,size[1]/2], [size[0],size[1]/2], 1)
    #pygame.draw.line(screen, colors.GREEN, [size[0]/2,0], [size[0]/2,size[1]], 1)
    
    #moveIt = multiList([xRotate(xrot),yRotate(yrot),zRotate(zrot)])
    #newst3d = affItUp(st3d, moveIt)
    #drawPointsColor(newst3d)
    ##v2 = affItUp(vertices2, moveIt)
    ##drawXYLines(v2, 1)
    ##drawPointsColor(st3d)

    
    #pygame.display.flip()
#pygame.quit()

