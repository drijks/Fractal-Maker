import pygame
import colors
import fractals2d
import fractals3d
from fractalsDict import alphabet, wordParser, wordNest, drawWordPoints
from tree3d import treethang
from operator import eq



ps = 'PRESET'
cs = 'CUSTOM'
funcs = 0
sc = 'SAME'
uc = 'UNIQ'
scl = 'SCL'
rot = 'ROT'
ref = 'REF'
trn = 'TRN'
mat = 'MAT'
skw = 'SKW'
mult = 'MULT'


print("Welcome to the fractal maker! This version uses affine transformations.")
wordFrac = False
twoD = False
aTree = False
fractype = input("preset or custom?")
if eq(fractype.upper(), ps):
    funclist = []
    translist = []
    collist = [] 
    print("enter 'SPK' for a Sierpinski's Triangle, 'SPK3D' for a 3d Sierpinski's Triangle, ")
    presetype = input("'TREE' for a 3d tree, or 'WORD' to make a fractal out of a word: ")
    if eq(presetype.upper(), 'SPK'):
        funclist.append(fractals3d.uniformScaling(.5))
        translist.append([100,0,0])
        collist.append(colors.pink)
        funclist.append(fractals3d.uniformScaling(.5))
        translist.append([-100,0,0])
        collist.append(colors.yellow)
        funclist.append(fractals3d.uniformScaling(.5))
        translist.append([0,100,0])
        collist.append(colors.aqua)
    elif eq(presetype.upper(), 'SPK3D'):
        funclist.append(fractals3d.uniformScaling(.5))
        translist.append([0,0,0])
        collist.append(colors.pink)
        funclist.append(fractals3d.uniformScaling(.5))
        translist.append([100,0,0])
        collist.append(colors.yellow)
        funclist.append(fractals3d.uniformScaling(.5))
        translist.append([0,100,0])
        collist.append(colors.aqua)
        funclist.append(fractals3d.uniformScaling(.5))
        translist.append([0,0,100])
        collist.append(colors.aqua)
    elif eq(presetype.upper(), 'TREE'):
        theTreeThang = treethang()
        aTree = True
    elif eq(presetype.upper(), 'WORD'):
        testWord = input("enter your word: ")
        wordFrac = True
else:
    dimens = input("2D or 3D?")
    if eq(dimens, "3D"):
        funcs = int(input("please enter the number of functions you want your fractal to be drawn from"))
        
        funclist = []
        translist = []
        collist = []    
        for i in range(int(funcs)):
            print('')
            print('')
            print("function " + str(i+1) + ": ")
            print("To add a scaling matrix, enter 'SCL'. To add a rotation matrix, enter 'ROT'.")
            print("For a reflection matrix, enter 'REF'.")
            print("To add a skew matrix, enter 'SKW'. To enter your own matrix, enter 'MAT'. ")
            thing = input("To do multiple matrix transformations in one function, enter 'MULT'.")
            if eq(thing.upper(), scl):
                sc1 = input("enter x scaling: ")
                sc2 = input("enter y scaling: ")
                sc3 = input("enter z scaling: ")
                funclist.append(fractals3d.customScaling(float(sc1), float(sc2), float(sc3)))
                print('') 
                trns1 = input("enter x translation (in PIXELS): ")
                trns2 = input("enter y translation (in PIXELS): ")
                trns3 = input("enter z translation (in PIXELS): ")
                translist.append([int(trns1), int(trns2), int(trns3)])
                col = input("enter a color: ")
                collist.append(colors.parseColor(col))    
                print('')
                print('')                
            elif eq(thing.upper(), rot):
                rotype = input("x, y, or z rotation?")
                theta = input("enter your angle (in degrees): ")
                if eq(rotype.upper(), 'X'):
                    funclist.append(fractals3d.xRotate(int(theta)))
                elif eq(rotype.upper(), 'Y'):
                    funclist.append(fractals3d.yRotate(int(theta)))
                else:     
                    funclist.append(fractals3d.zRotate(int(theta)))
                print('')
                trns1 = input("enter x translation (in PIXELS): ")
                trns2 = input("enter y translation (in PIXELS): ")
                trns3 = input("enter z translation (in PIXELS): ")
                translist.append([int(trns1), int(trns2), int(trns3)])
                print('') 
                col = input("enter a color: ")
                collist.append(colors.parseColor(col))
                print('')
                print('')                
            elif eq(thing.upper(), skw):
                rotype = input("x, y, z, xy, xz, or yz skew?")
                theta = input("skew by how much?")
                if eq(rotype.upper(), 'X'):
                    funclist.append(fractals3d.skewMatrix1(int(theta)))
                elif eq(rotype.upper(), 'Y'):
                    funclist.append(fractals3d.skewMatrix2(int(theta)))
                elif eq(rotype.upper(), 'Z'):
                    funclist.append(fractals3d.skewMatrix3(int(theta)))
                elif eq(rotype.upper(), 'XY'):
                    funclist.append(fractals3d.skewMatrix4(int(theta)))
                elif eq(rotype.upper(), 'XZ'):
                    funclist.append(fractals3d.skewMatrix5(int(theta)))
                else:
                    funclist.append(fractals3d.skewMatrix6(int(theta)))
                print('')
                trns1 = input("enter x translation (in PIXELS): ")
                trns2 = input("enter y translation (in PIXELS): ")
                trns3 = input("enter z translation (in PIXELS): ")
                translist.append([int(trns1), int(trns2), int(trns3)])
                print('')
                col = input("enter a color: ")
                collist.append(colors.parseColor(col))  
                print('')
                print('')  
            elif eq(thing.upper(), ref):
                rotype = input("x, y, or z reflection?")
                if eq(rotype.upper(), 'X'):
                    funclist.append(fractals3d.xReflect())
                elif eq(rotype.upper(), 'Y'):
                    funclist.append(fractals3d.yReflect())
                else:
                    funclist.append(fractals3d.zReflect())
                print('')
                trns1 = input("enter x translation (in PIXELS): ")
                trns2 = input("enter y translation (in PIXELS): ")
                trns3 = input("enter z translation (in PIXELS): ")
                translist.append([int(trns1), int(trns2), int(trns3)])
                print('')
                col = input("enter a color: ")
                collist.append(colors.parseColor(col))
                print('')
                print('')
            elif eq(thing.upper(), mat):
                m1 = input("row 1, column 1: ")
                m2 = input("row 1, column 2: ")
                m3 = input("row 1, column 3: ")
                m4 = input("row 2, column 1: ")
                m5 = input("row 2, column 2: ")
                m6 = input("row 2, column 3: ")
                m7 = input("row 3, column 1: ")
                m8 = input("row 3, column 2: ")
                m9 = input("row 3, column 3: ")
                funclist.append(fractals3d.customMatrix(float(m1), float(m2), float(m3), float(m4), float(m5), float(m6), float(m7), float(m8), float(m9)))
                print('')
                trns1 = input("enter x translation (in PIXELS): ")
                trns2 = input("enter y translation (in PIXELS): ")
                trns3 = input("enter z translation (in PIXELS): ")
                translist.append([int(trns1), int(trns2), int(trns3)])
                print('')
                col = input("enter a color: ")
                collist.append(colors.parseColor(col))
                print('')
                print('')
            elif eq(thing.upper(), mult):
                numby = input("how many matrices do you want to multiply?")
                bleah = []
                for i in range(int(numby)):
                    print('')            
                    fnc = input('SCL, ROT, REF, SKW, MAT?')
                    if eq(fnc.upper(), scl):
                        sc1 = input("enter x scaling: ")
                        sc2 = input("enter y scaling: ")
                        sc3 = input("enter z scaling: ")
                        bleah.append(fractals3d.customScaling(float(sc1), float(sc2), float(sc3)))
                    elif eq(fnc.upper(), rot):
                        rotype = input("x, y, or z rotation?")
                        theta = input("enter your angle (in degrees): ")
                        if eq(rotype.upper(), 'X'):
                            bleah.append(fractals3d.xRotate(int(theta)))
                        elif eq(rotype.upper(), 'Y'):
                            bleah.append(fractals3d.yRotate(int(theta)))
                        else:
                            bleah.append(fractals3d.zRotate(int(theta)))
                    elif eq(fnc.upper(), ref):
                        rotype = input("x, y, or z reflection?")
                        if eq(rotype.upper(), 'X'):
                            bleah.append(fractals3d.xReflect())
                        elif eq(rotype.upper(), 'Y'):
                            bleah.append(fractals3d.yReflect())
                        else:
                            bleah.append(fractals3d.zReflect())   
                    elif eq(fnc.upper(), skw):
                        rotype = input("x, y, z, xy, xz, or yz skew?")
                        t = input("skew by how much?")
                        if eq(rotype.upper(), 'X'):
                            bleah.append(fractals3d.skewMatrix1(int(t)))
                        elif eq(rotype.upper(), 'Y'):
                            bleah.append(fractals3d.skewMatrix2(int(t)))
                        elif eq(rotype.upper(), 'Z'):
                            bleah.append(fractals3d.skewMatrix3(int(t)))
                        elif eq(rotype.upper(), 'XY'):
                            bleah.append(fractals3d.skewMatrix4(int(t)))
                        elif eq(rotype.upper(), 'XZ'):
                            bleah.append(fractals3d.skewMatrix5(int(t)))
                        else:
                            bleah.append(fractals3d.skewMatrix6(int(t)))            
                    elif eq(fnc.upper(), mat):
                        m1 = input("row 1, column 1: ")
                        m2 = input("row 1, column 2: ")
                        m3 = input("row 1, column 3: ")
                        m4 = input("row 2, column 1: ")
                        m5 = input("row 2, column 2: ")
                        m6 = input("row 2, column 3: ")
                        m7 = input("row 3, column 1: ")
                        m8 = input("row 3, column 2: ")
                        m9 = input("row 3, column 3: ")
                        bleah.append(fractals3d.customMatrix(float(m1), float(m2), float(m3), float(m4), float(m5), float(m6), float(m7), float(m8), float(m9)))
                funclist.append(fractals3d.multiList(bleah))
                print('')
                print('')
                trns1 = input("enter x translation (in PIXELS): ")
                trns2 = input("enter y translation (in PIXELS): ")
                trns3 = input("enter z translation (in PIXELS): ")
                translist.append([int(trns1), int(trns2), int(trns3)])
                print('')
                col = input("enter a color: ")
                collist.append(colors.parseColor(col))
                print('')
                print('')

    else:
        funcs = int(input("please enter the number of functions you want your fractal to be drawn from"))
        twoD = True
        funclist = []
        translist = []
        collist = []    
        for i in range(int(funcs)):
            print("function " + str(i+1) + ": ")
            print('')
            print('')
            print("To add a scaling matrix, enter 'SCL'. To add a rotation matrix, enter 'ROT'.")
            print("For a reflection matrix, enter 'REF'.")
            print("To add a skew matrix, enter 'SKW'. To enter your own matrix, enter 'MAT'. ")
            thing = input("To do multiple matrix transformations in one function, enter 'MULT'.")
            if eq(thing.upper(), scl):
                sc1 = input("enter x scaling: ")
                sc2 = input("enter y scaling: ")
                funclist.append(fractals2d.customScaling(float(sc1), float(sc2)))
                print('') 
                trns1 = input("enter x translation (in PIXELS): ")
                trns2 = input("enter y translation (in PIXELS): ")
                translist.append([int(trns1), int(trns2)])
                col = input("enter a color: ")
                collist.append(colors.parseColor(col))    
                print('')
                print('')                
            elif eq(thing.upper(), rot):
                theta = input("enter your angle (in degrees): ")
                funclist.append(fractals2d.zRotate(int(theta)))
                
                print('')
                trns1 = input("enter x translation (in PIXELS): ")
                trns2 = input("enter y translation (in PIXELS): ")
                translist.append([int(trns1), int(trns2)])
                print('') 
                col = input("enter a color: ")
                collist.append(colors.parseColor(col))
                print('')
                print('')                
            elif eq(thing.upper(), skw):
                rotype = input("x or y skew?")
                theta = input("skew by how much?")
                if eq(rotype.upper(), 'X'):
                    funclist.append(fractals2d.skewMatrixX(int(theta)))
                else:
                    funclist.append(fractals2d.skewMatrixY(int(theta)))
                print('')
                trns1 = input("enter x translation (in PIXELS): ")
                trns2 = input("enter y translation (in PIXELS): ")
                translist.append([int(trns1), int(trns2)])
                print('')
                col = input("enter a color: ")
                collist.append(colors.parseColor(col))    
                print('')
                print('')                
            elif eq(thing.upper(), ref):
                rotype = input("x, y, or xy reflection?")
                if eq(rotype.upper(), 'X'):
                    funclist.append(fractals2d.xReflect())
                elif eq(rotype.upper(), 'Y'):
                    funclist.append(fractals2d.yReflect())
                else:
                    funclist.append(fractals2d.xyReflect())
                print('')
                trns1 = input("enter x translation (in PIXELS): ")
                trns2 = input("enter y translation (in PIXELS): ")
                translist.append([int(trns1), int(trns2)])
                print('')
                col = input("enter a color: ")
                collist.append(colors.parseColor(col))
                print('')
                print('')                
            elif eq(thing.upper(), mat):
                m1 = input("row 1, column 1: ")
                m2 = input("row 1, column 2: ")
                m3 = input("row 2, column 1: ")
                m4 = input("row 2, column 2: ")
                funclist.append(fractals2d.customMatrix(float(m1), float(m2), float(m3), float(m4)))
                print('')
                trns1 = input("enter x translation (in PIXELS): ")
                trns2 = input("enter y translation (in PIXELS): ")
                translist.append([int(trns1), int(trns2)])
                print('')
                col = input("enter a color: ")
                collist.append(colors.parseColor(col))       
                print('')
                print('')                
            elif eq(thing.upper(), mult):
                numby = input("how many matrices do you want to multiply?")
                bleah = []
                for i in range(int(numby)):
                    print('')            
                    fnc = input('SCL, ROT, REF, SKW, MAT?')
                    if eq(fnc.upper(), scl):
                        sc1 = input("enter x scaling: ")
                        sc2 = input("enter y scaling: ")
                        bleah.append(fractals2d.customScaling(float(sc1), float(sc2)))
                    elif eq(fnc.upper(), rot):
                        theta = input("enter your angle (in degrees): ")
                        bleah.append(fractals2d.zRotate(int(theta)))
                    elif eq(fnc.upper(), ref):
                        rotype = input("x, y, or xy reflection?")
                        if eq(rotype.upper(), 'X'):
                            bleah.append(fractals2d.xReflect())
                        elif eq(rotype.upper(), 'Y'):
                            bleah.append(fractals2d.yReflect())
                        else:
                            bleah.append(fractals2d.xyReflect())   
                    elif eq(fnc.upper(), skw):
                        rotype = input("x or y skew?")
                        t = input("skew by how much?")
                        if eq(rotype.upper(), 'X'):
                            bleah.append(fractals2d.skewMatrixX(int(t)))
                        else:
                            bleah.append(fractals2d.skewMatrixY(int(t)))            
                    elif eq(fnc.upper(), mat):
                        m1 = input("row 1, column 1: ")
                        m2 = input("row 1, column 2: ")
                        m3 = input("row 2, column 1: ")
                        m4 = input("row 2, column 2: ")
                        bleah.append(fractals2d.customMatrix(float(m1), float(m2), float(m3), float(m4)))
                funclist.append(fractals2d.multiList(bleah))
                print('')
                print('')
                trns1 = input("enter x translation (in PIXELS): ")
                trns2 = input("enter y translation (in PIXELS): ")
                translist.append([int(trns1), int(trns2)])
                print('')
                col = input("enter a color: ")
                collist.append(colors.parseColor(col))
                print('')
                print('')                
        


listlength = input("how many points do you want to plot?")
if wordFrac:
    wlength = len(testWord)
    lsize = 250
    letters = alphabet()
    tester = wordNest([0,0], testWord, letters, 100000)    
elif twoD:
    tester = fractals2d.affineNestColor([0,0], funclist, translist, collist, int(listlength))
elif aTree:
    tester = theTreeThang
else:
    tester = fractals3d.affineNestColor3([0,0,0], funclist, translist, collist, int(listlength))
    
    
print(tester[20])
xrot = 0
yrot = 0
zrot = 0
pygame.init()


#window properties
size = [1100, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FRACTALS!!!!!!!!!!!!!!!!")
screen.fill(colors.WHITE)
clock = pygame.time.Clock()


#MAIN
done = False
while not done:
    clock.tick(25)
    screen.fill(colors.WHITE)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            if xrot >= 360:
                xrot = 0
            else:
                xrot += 2
        if event.key == pygame.K_b:
            if xrot <= 0:
                xrot = 360
            else:
                xrot -= 2
        if event.key == pygame.K_c:
            if yrot >= 360:
                yrot = 0
            else:
                yrot += 2
        if event.key == pygame.K_d:
            if yrot <= 0:
                yrot = 360
            else:
                yrot -= 2
        if event.key == pygame.K_e:
            if zrot >= 360:
                zrot = 0
            else:
                zrot += 2
        if event.key == pygame.K_f:
            if zrot <= 0:
                zrot = 360
            else:
                zrot -= 2
        if event.key == pygame.K_r:
            xrot = 0
            yrot = 0
            zrot = 0

    
    if wordFrac:
        pygame.draw.line(screen, colors.GREEN, [0,size[1]-100], [size[0],size[1]-100], 1)
        pygame.draw.line(screen, colors.GREEN, [100,0], [100,size[1]], 1)        
        drawWordPoints(size, screen, tester, colors.RED)
    elif twoD:
        pygame.draw.line(screen, colors.GREEN, [0,size[1]/2], [size[0],size[1]/2], 1)
        pygame.draw.line(screen, colors.GREEN, [size[0]/2,0], [size[0]/2,size[1]], 1)        
        fractals2d.drawPointsColor(size, screen, tester)
    else:
        pygame.draw.line(screen, colors.GREEN, [0,size[1]/2], [size[0],size[1]/2], 1)
        pygame.draw.line(screen, colors.GREEN, [size[0]/2,0], [size[0]/2,size[1]], 1)        
        #fractals3d.drawPointsColor(size, screen, tester)
        moveIt = fractals3d.multiList([fractals3d.xRotate(xrot),fractals3d.yRotate(yrot),fractals3d.zRotate(zrot)])
        newst3d = fractals3d.affItUp(tester, moveIt)
        fractals3d.drawPointsColor(size, screen, newst3d)
    
    pygame.display.flip()
pygame.quit()

