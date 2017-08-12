import pygame
import math
import random
#pygame.init()

##ENTER TEST WORD AROUND LINE 680


##colors
#RED = (255,0,0)
#ORANGE = (255,165,0)
#YELLOW = (255,255,0)
#GREEN = (0,128,0)
#BLUE = (0,0,255)
#SKYBLUE = (135,206,235)
#LIGHTBLUE =(173,216,230)
#INDIGO = (75,0,130)
#PURPLE = (128,0,128)
#WHITE = (255,255,255)
#BLACK = (0,0,0) 

##window properties
#size = [1100, 700]
#screen = pygame.display.set_mode(size)
#pygame.display.set_caption("FRACTALS!!!!!!!!!!!!!!!!")
#screen.fill(WHITE)
#clock = pygame.time.Clock()




def alphabet():
    global wlength
    global lsize
    #GOOD
    A1 = []
    A2 = []
    #A1.append(multiList([customScaling(1/wlength, 1),customMatrix(.5,0,1.1,.2667)]))
    A1.append(multiList([customScaling(1/wlength, 1),customMatrix(.5,0,1.1/wlength,.2667)]))
    A2.append([0*lsize,0*lsize])
    #A1.append(multiList([customMatrix(-1,0,0,1),customScaling(1/wlength, 1),customMatrix(.5,0,1.1,.2667)]))
    A1.append(multiList([customMatrix(-1,0,0,1),customScaling(1/wlength, 1),customMatrix(.5,0,1.1/wlength,.2667)]))
    A2.append([1*lsize,0*lsize])
    #A1.append(multiList([customScaling(1/wlength, 1),customMatrix(.4,0,0,.133)]))
    A1.append(multiList([customScaling(1/wlength, 1),customMatrix(.4,0,0,.133)]))
    A2.append([.3*lsize,.8*lsize])
    A = ['A',A1,A2]
    
    #GOOD
    B1 = []
    B2 = []
    B1.append(multiList([customScaling(1/wlength, 1),customMatrix(1,1*wlength,0,1),customMatrix(.85,0,0,2/15)]))
    B2.append([-.1*lsize,1.3*lsize])
    B1.append(multiList([zRotate(90),customScaling(1/wlength, 1),customScaling(1.25, 2.0/15)]))
    B2.append([.4*lsize, .0*lsize])
    B1.append(multiList([customScaling(1/wlength, 1),customMatrix(1,0,0,-1),customMatrix(1,1*wlength,0,1),customMatrix(.85,0,0,2.0/15)]))
    B2.append([-.1*lsize, .2*lsize])
    B1.append(multiList([customScaling(1/wlength, 1),customMatrix(2.5/5,0,0,2.0/15)]))
    B2.append([.3*lsize, .65*lsize])
    B1.append(multiList([zRotate(90),customScaling(1/wlength, 1),customMatrix(1,0,0,-1),customMatrix(1,1*wlength,0,1),customMatrix(3.5/5,0,0,2.0/15)]))
    B2.append([.8*lsize, .55*lsize])
    B1.append(multiList([zRotate(90),customScaling(1/wlength, 1),customMatrix(1,1*wlength,0,1),customMatrix(3.5/5,0,0,2.0/15)]))
    B2.append([1*lsize,-.15*lsize])
    B = ['B',B1,B2]
    
    #GOOD
    C1 = []
    C2 = []
    C1.append(multiList([zRotate(-90),customScaling(1/wlength, 1),customMatrix(.5,0,0,.2)]))
    C2.append([.7*lsize,1.5*lsize])
    C1.append(multiList([customScaling(1/wlength,1),customMatrix(.7,0,0,.2)]))
    C2.append([0*lsize,1.2*lsize])
    C1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(.9,0,0,.2)]))
    C2.append([.3*lsize, .3*lsize])
    C1.append(multiList([customScaling(1/wlength,1),customMatrix(.7,0,0,.2)]))
    C2.append([0,0])
    C1.append(multiList([zRotate(-90),customScaling(1/wlength,1),customMatrix(.5,0,0,.2)]))
    C2.append([.7*lsize,.5*lsize])
    C = ['C',C1,C2]
    
    D1 = []
    D2 = []
    D = ['D',D1,D2]
    
    E1 = []
    E2 = []
    E1.append(multiList([customScaling(1/wlength,1),customMatrix(1.0/3,0,0,1)]))
    E2.append([0*lsize,0*lsize])
    E1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(1/3,0,0,1/3)]))
    E2.append([(2/3)*lsize,.6*lsize])
    E1.append(multiList([customScaling(1/wlength,1),customMatrix(.95,0,0,.2)]))
    E2.append([0*lsize,0*lsize])
    E1.append(multiList([customScaling(1/wlength,1),customMatrix(.95,0,0,.2)]))
    E2.append([0*lsize,1.2*lsize])
    E = ['E',E1,E2]
    
    F1 = []
    F2 = []
    F1.append(multiList([zRotate(-90),customScaling(1/wlength,1),customMatrix(.25,0,0,1.0/3)]))
    F2.append([0*lsize,.25*lsize])
    F1.append(multiList([customScaling(1/wlength,1),customMatrix(.25,0,0,2.0/3)]))
    F2.append([.125*lsize,.25*lsize])
    F1.append(multiList([customScaling(1/wlength,1),customMatrix(.25,0,0,1.0/6)]))
    F2.append([.375*lsize,.625*lsize])
    F1.append(multiList([customScaling(1/wlength,1),customMatrix(.125,0,0,1.0/3)]))
    F2.append([.625*lsize,.5*lsize])
    F1.append(multiList([zRotate(-90),customScaling(1/wlength,1),customMatrix(.25,0,0,.5)]))
    F2.append([0*lsize,1.5*lsize])
    F1.append(multiList([customScaling(1/wlength,1),customMatrix(.25,0,0,1.25/6)]))
    F2.append([.75*lsize,1.1875*lsize])
    F = ['F',F1,F2]
    
    G1 = []
    G2 = []
    G1.append(multiList([customScaling(1/wlength,1),customMatrix(.7,0,0,.2)]))
    G2.append([.3*lsize,1.2*lsize])
    G1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(1.2,0,0,.2)]))
    G2.append([.3*lsize,.3*lsize])
    G1.append(multiList([customScaling(1/wlength,1),customMatrix(.7,0,0,.2)]))
    G2.append([0*lsize,0*lsize])
    G1.append(multiList([zRotate(-90),customScaling(1/wlength,1),customMatrix(.6,0,0,.2)]))
    G2.append([0.7*lsize,0.6*lsize])
    G1.append(multiList([customScaling(1/wlength,1),customMatrix(.5,0,0,.2)]))
    G2.append([0.5*lsize,0.6*lsize])    
    G = ['G',G1,G2]
    
    H1 = []
    H2 = []
    H1.append(multiList([customScaling(1/wlength,1),customMatrix(1.0/4,0,0,1.0/12)]))
    H2.append([0*lsize,0*lsize])
    H1.append(multiList([customScaling(1/wlength,1),customMatrix(1.0/4,0,0,1.0/12)]))
    H2.append([(9.0/16)*lsize,0*lsize])
    H1.append(multiList([customScaling(1/wlength,1),customMatrix(3.0/8,0,0,1.0/6)]))
    H2.append([(5.0/16)*lsize,.625*lsize])
    H1.append(multiList([customScaling(1/wlength,1),customMatrix(1.0/8,1.0/8,0,10/12)]))
    H2.append([(1.0/16)*lsize,.125*lsize])
    H1.append(multiList([customScaling(1/wlength,1),customMatrix(1.0/8,1.0/8,0,10/12)]))
    H2.append([(5.0/8)*lsize,.125*lsize])
    H1.append(multiList([customScaling(1/wlength,1),customMatrix(1.0/4,0,0,1.0/12)]))
    H2.append([(3.0/16)*lsize,1.375*lsize])
    H1.append(multiList([customScaling(1/wlength,1),customMatrix(1.0/4,0,0,1.0/12)]))
    H2.append([(3.0/4)*lsize,1.375*lsize])
    H = ['H',H1,H2]
    
    I1 = []
    I2 = []
    I1.append(multiList([customScaling(1/wlength,1),customMatrix(1.0,0,0,.25/1.5)]))
    I2.append([0*lsize,1.5*lsize])
    I1.append(multiList([customScaling(1/wlength,1),customMatrix(1.0,0,0,.25/1.5)]))
    I2.append([0*lsize,0*lsize])
    I1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(1.25,0,0,.25/1.5)]))
    I2.append([.62*lsize,.25*lsize])
    I = ['I',I1,I2]
    
    
    #GOOD
    J1 = []
    J2 = []
    J1.append(multiList([customScaling(1/wlength,1),customMatrix(.5,0,0,.2/1.5)]))
    J2.append([.0*lsize,1.3*lsize])
    J1.append(multiList([customScaling(1/wlength,1),customMatrix(-1,0,0,1),customMatrix(.5,0,0,.2/1.5)]))
    J2.append([1*lsize,1.3*lsize])
    J1.append(multiList([zRotate(-90),customScaling(1/wlength,1),customMatrix(1,0,0,.3/1.5)]))
    J2.append([.4*lsize,1.3*lsize])
    J1.append(multiList([customMatrix(1,.1/.3,0,1),zRotate(-90),customScaling(1/wlength,1),customMatrix(.3,0,0,.3/1.5)]))
    J2.append([.4*lsize,.3*lsize])
    J1.append(multiList([customMatrix(1,-.1/.3,0,1),customMatrix(-1,0,0,1),zRotate(90),customScaling(1/wlength,1),customMatrix(.3,0,0,.3/1.5)]))
    J2.append([.1*lsize,0*lsize])
    J1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(.3,0,0,.05/1.5)]))
    J2.append([.05*lsize,1.2*lsize])
    J1.append(multiList([customMatrix(-1,0,0,1),zRotate(90),customScaling(1/wlength,1),customMatrix(.3,0,0,.05/1.5)]))
    J2.append([.95*lsize,1.2*lsize])
    J = ['J',J1,J2]
    
    K1 = []
    K2 = []
    K1.append(multiList([zRotate(45),customScaling(1/wlength,1),customScaling(0.6, 2.0/15)]))
    K2.append([.5*lsize,.8*lsize])
    K1.append(multiList([zRotate(-45),customScaling(1/wlength,1),customScaling(0.6, 2.0/15)]))
    K2.append([.4*lsize,.6*lsize])
    K1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(1.5,2.0/15)]))
    K2.append([.35*lsize,0*lsize])    
    K = ['K',K1,K2]
    
    
    #OKAY
    L1 = []
    L2 = []
    theta1 = 90
    tee1 = ((theta1 * math.pi)/180)    
    cee1 = round(math.cos(tee1), 5)
    see1 = round(math.sin(tee1), 5)
    L1.append(multiList([customMatrix(1,0,0,-1),customMatrix(cee1,see1,-see1,cee1),customScaling(1/wlength,1),customMatrix(.63,0,0,.2/1.5)]))
    L2.append([0*lsize,.99*lsize])
    L1.append(multiList([customMatrix(1,0,0,-1),customMatrix(cee1,see1,-see1,cee1),customScaling(1/wlength,1),customMatrix(.63,0,0,.2/1.5)]))
    L2.append([0*lsize,.36*lsize])
    L1.append(multiList([customScaling(1/wlength,1),customMatrix(.3,0,0,.12)]))
    L2.append([.4*lsize,0*lsize])
    L1.append(multiList([customScaling(1/wlength,1),customMatrix(.3,0,0,.12)]))
    L2.append([0.7*lsize,0*lsize])
    L1.append(multiList([customScaling(1/wlength,1),customMatrix(.3,0,0,.12)]))
    L2.append([0.4*lsize,0.18*lsize])
    L1.append(multiList([customScaling(1/wlength,1),customMatrix(.3,0,0,.12)]))
    L2.append([0.7*lsize,0.18*lsize])
    L1.append(multiList([customScaling(1/wlength,1),customMatrix(.4,0,0,.24)]))
    L2.append([0*lsize,0*lsize])
    L1.append(multiList([customMatrix(1,0,0,-1),customMatrix(cee1,see1,-see1,cee1),customScaling(1/wlength,1),customMatrix(.63,0,0,.2/1.5)]))
    L2.append([.2*lsize,.99*lsize])
    L1.append(multiList([customMatrix(1,0,0,-1),customMatrix(cee1,see1,-see1,cee1),customScaling(1/wlength,1),customMatrix(.63,0,0,.2/1.5)]))
    L2.append([.2*lsize,.36*lsize])
    L = ['L',L1,L2]
    
    
    #OKAY
    M1 = []
    M2 = []
    M1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(1.5,0,0,1.0/6)]))
    M2.append([.25*lsize,0*lsize])
    M1.append(multiList([zRotate(-45),customScaling(1/wlength,1),customMatrix(1,-1*wlength,0,1),customMatrix(.353553,0,0,1/6)]))
    M2.append([.25*lsize,1.145*lsize])
    M1.append(multiList([zRotate(45),customScaling(1/wlength,1),customMatrix(1,1*wlength,0,1),customMatrix(.353553,0,0,1/6)]))
    M2.append([.5*lsize,.9*lsize])
    M1.append(multiList([zRotate(-90),customScaling(1/wlength,1),customMatrix(1.5,0,0,1/6)]))
    M2.append([.75*lsize,1.6*lsize])
    M = ['M',M1,M2] #ADJUSTED FROM ORIGINAL
    
    
    #NEEDS WORK
    N1 = []
    N2 = []
    N1.append(multiList([customScaling(1/wlength,1),customMatrix(1/3,0,0,1)]))
    N2.append([0*lsize,0*lsize])
    N1.append(multiList([customScaling(1/wlength,1),customMatrix(1/3,0,0,1),customMatrix(1,-1*wlength,0,1)]))
    N2.append([1.5/3*lsize,0*lsize])
    N1.append(multiList([customScaling(1/wlength,1),customMatrix(1/3,0,0,1)]))
    N2.append([1.85/3*lsize,0*lsize])
    N = ['N',N1,N2]
    
    
    #GOOD ENOUGH
    O1 = []
    O2 = []
    O1.append(multiList([customScaling(1/wlength,1),customMatrix(.9,0,0,.25/1.5)]))#(1,0,0,.25/1.5)
    O2.append([.05*lsize, 1.5*lsize])
    O1.append(multiList([customScaling(1/wlength,1),customMatrix(.9,0,0,.25/1.5)]))#(1,0,0,.25/1.5)
    O2.append([.05*lsize, 0*lsize])
    O1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(1.25,0,0,.25/1.5)]))
    O2.append([.3*lsize, .25*lsize])
    O1.append(multiList([zRotate(-90),customScaling(1/wlength,1),customMatrix(1.25,0,0,.25/1.5)]))
    O2.append([.7*lsize, 1.5*lsize])    
    O = ['O',O1,O2]#ADJUSTED FROM ORIGINAL
    
    
    #OKAY
    P1 = []
    P2 = []
    P1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(1.5,0,0,1/6)]))
    P2.append([.25*lsize,0*lsize])
    P1.append(multiList([customScaling(1/wlength,1),customMatrix(.75,0,0,1/6)]))
    P2.append([.25*lsize,1.25*lsize])
    P1.append(multiList([customScaling(1/wlength,1),customMatrix(.75,0,0,1/6)]))
    P2.append([.25*lsize,.75*lsize])
    P1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(.5,0,0,1/6)]))
    P2.append([1*lsize,1*lsize])
    P = ['P',P1,P2]#ADJUSTED FROM ORIGINAL
    
    Q1 = []
    Q2 = []
    Q1.append(multiList([customScaling(1/wlength, 1),customScaling(0.5,2.0/15)]))
    Q2.append([.2*lsize,0])
    Q1.append(multiList([customScaling(1/wlength, 1),customScaling(0.65,2.0/15)]))
    Q2.append([.2*lsize,1.25*lsize])    
    Q1.append(multiList([zRotate(90),customScaling(1/wlength, 1),customScaling(1.1,2.0/15)]))
    Q2.append([.2*lsize,.2*lsize])
    Q1.append(multiList([zRotate(90),customScaling(1/wlength, 1),customScaling(1,2.0/15)]))
    Q2.append([.99*lsize,.35*lsize])
    Q1.append(multiList([zRotate(-45),customScaling(1/wlength, 1),customScaling(0.5, 2.0/15)]))
    Q2.append([.5*lsize,.35*lsize])
    Q = ['Q',Q1,Q2]
    
    R1 = []
    R2 = []
    R = ['R',R1,R2]
    
    S1 = []
    S2 = []
    S1.append(multiList([zRotate(30),customScaling(1/wlength,1),customScaling(.99, 2.0/15)]))
    S2.append([.075*lsize,.99*lsize])
    S1.append(multiList([zRotate(-25),customScaling(1/wlength,1),customScaling(0.85, 2.0/15)]))
    S2.append([.05*lsize,.9*lsize])
    S1.append(multiList([zRotate(25),customScaling(1/wlength,1),customScaling(0.95, 2.0/15)]))
    S2.append([.1*lsize,0*lsize])
    S = ['S',S1,S2]
    
    T1 = []
    T2 = []
    T1.append(multiList([customScaling(1/wlength,1),customScaling(0.5,2.0/15)]))
    T2.append([0,1.3*lsize])
    T1.append(multiList([xReflect(),customScaling(1/wlength,1),customScaling(0.5,2.0/15)]))
    T2.append([.99*lsize,1.3*lsize])
    T1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(1.3,2.0/15)]))
    T2.append([.6*lsize,0])
    T = ['T',T1,T2]
    
    
    
    
    #GOOD
    U1 = []
    U2 = [] 
    U1.append(multiList([customMatrix(cee1,see1,-see1,cee1),customScaling(1/wlength,1),customMatrix(1.15,0,0,.25/1.5)]))
    U2.append([0*lsize,1.5*lsize])
    U1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(1.15,0,0,.25/1.5)]))
    U2.append([1*lsize,.35*lsize])
    U1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(.35,0,.25/wlength,.25/1.5)]))
    U2.append([.503*lsize,0*lsize])
    U1.append(multiList([customMatrix(-1,0,0,1),zRotate(90),customScaling(1/wlength,1),customMatrix(.35,0,.25/wlength,.25/1.5)]))
    U2.append([.503*lsize,0*lsize])
    U = ['U',U1,U2]#ADJUSTED FROM ORIGINAL
    
    V1 = []
    V2 = []
    V = ['V',V1,V2]
    
    W1 = []
    W2 = []
    W = ['W',W1,W2]
    
    X1 = []
    X2 = []
    X1.append(multiList([customScaling(1/wlength,1),customMatrix(.2,.2*wlength,0,.5)]))
    X2.append([0*lsize,0*lsize])
    X1.append(multiList([customScaling(1/wlength,1),customMatrix(-1,0,0,-1),customMatrix(.2,.2*wlength,0,.5)]))
    X2.append([1*lsize,1.5*lsize])
    X1.append(multiList([customScaling(1/wlength,1),xReflect(),customMatrix(.2,.2*wlength,0,.5)]))
    X2.append([1*lsize,0*lsize])
    X1.append(multiList([customScaling(1/wlength,1),yReflect(),customMatrix(.2,.2*wlength,0,.5)]))
    X2.append([0*lsize,1.5*lsize])
    X = ['X',X1,X2]
    
    
    Y1 = []
    Y2 = []
    Y = ['Y',Y1,Y2]
    
    
    Z1 = []
    Z2 = []
    Z1.append(multiList([customScaling(1/wlength,1),customMatrix(1,0,0,1/6)]))
    Z2.append([0*lsize,1.25*lsize])
    Z1.append(multiList([zRotate((.975*180/math.pi)),customScaling(1/wlength,1),customMatrix(1,-.69*wlength,0,1),customMatrix(1.21,0,0,1/6)]))
    Z2.append([.305*lsize,.25*lsize])
    Z1.append(multiList([customScaling(1/wlength,1),customMatrix(1,0,0,1/6)]))
    Z2.append([0*lsize,0*lsize])
    Z = ['Z',Z1,Z2]
    
    a1 = []
    a2 = []
    a1.append(multiList([customScaling(1/wlength,1),customScaling(0.5, 2.0/15)]))
    a2.append([.2*lsize,.8*lsize])
    a1.append(multiList([customScaling(1/wlength,1),customScaling(0.6,2.0/15)]))
    a2.append([.1*lsize,.5*lsize])
    a1.append(multiList([customScaling(1/wlength,1),customScaling(0.6,2.0/15)]))
    a2.append([.1*lsize,0*lsize])    
    a1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.7,2.0/15)]))
    a2.append([.2*lsize,0*lsize])
    a1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(1.2,2.0/15)]))
    a2.append([.7*lsize,-.1*lsize])
    a = ['a',a1,a2]
    
    b1 = []
    b2 = []
    b1.append(multiList([customScaling(1/wlength,1),customScaling(0.6, 2.0/15)]))
    b2.append([.2*lsize,.6*lsize])
    b1.append(multiList([customScaling(1/wlength,1),customScaling(0.6,2.0/15)]))
    b2.append([.2*lsize,0*lsize])
    b1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(1.4,2.0/15)]))
    b2.append([.2*lsize,.1*lsize])    
    b1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.6,2.0/15)]))
    b2.append([.9*lsize,.1*lsize])
    b = ['b',b1,b2]
    
    c1 = []
    c2 = []
    c1.append(multiList([customScaling(1/wlength,1),customScaling(0.6, 2.0/15)]))
    c2.append([.2*lsize,.7*lsize])
    c1.append(multiList([customScaling(1/wlength,1),customScaling(0.6,2.0/15)]))
    c2.append([.2*lsize,0*lsize])
    c1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.5,2.0/15)]))
    c2.append([.3*lsize,.2*lsize])  
    c = ['c',c1,c2]
    
    d1 = []
    d2 = []
    d1.append(multiList([zRotate(40),customScaling(1/wlength,1),customScaling(0.5, 2.0/15)]))
    d2.append([.3*lsize,.4*lsize])
    d1.append(multiList([zRotate(135),customScaling(1/wlength,1),customScaling(0.5, 2.0/15)]))
    d2.append([.7*lsize,.1*lsize])
    d1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(1.4,2.0/15)]))
    d2.append([.9*lsize,0*lsize])    
    d = ['d',d1,d2]
    
    e1 = []
    e2 = []
    e1.append(multiList([customScaling(1/wlength,1),customScaling(0.4, 2.0/15)]))
    e2.append([.2*lsize,.8*lsize])
    e1.append(multiList([customScaling(1/wlength,1),customScaling(0.4,2.0/15)]))
    e2.append([.2*lsize,.35*lsize])
    e1.append(multiList([customScaling(1/wlength,1),customScaling(0.5,2.0/15)]))
    e2.append([.2*lsize,0*lsize])    
    e1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.7,2.0/15)]))
    e2.append([.2*lsize,.1*lsize])
    e1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.5,2.0/15)]))
    e2.append([.8*lsize,.4*lsize])
    e = ['e',e1,e2]
    
    f1 = []
    f2 = []
    f1.append(multiList([zRotate(40),customScaling(1/wlength,1),customScaling(0.35, 2.0/15)]))
    f2.append([.3*lsize,1.1*lsize])
    f1.append(multiList([zRotate(-40),customScaling(1/wlength,1),customScaling(0.35, 2.0/15)]))
    f2.append([.55*lsize,1.3*lsize])
    f1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.6,2.0/15)]))
    f2.append([.4*lsize,0*lsize])
    f1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.3,2.0/15)]))
    f2.append([.4*lsize,.8*lsize])
    f1.append(multiList([customScaling(1/wlength,1),customScaling(0.7, 2.0/15)]))
    f2.append([0*lsize,.6*lsize])
    f = ['f',f1,f2]
    
    g1 = []
    g2 = []
    g1.append(multiList([customScaling(1/wlength,1),customScaling(0.6, 2.0/15)]))
    g2.append([.2*lsize,.5*lsize])
    g1.append(multiList([customScaling(1/wlength,1),customScaling(0.6,2.0/15)]))
    g2.append([.1*lsize,.0*lsize])
    g1.append(multiList([customScaling(1/wlength,1),customScaling(0.6,2.0/15)]))
    g2.append([.2*lsize,-.5*lsize])    
    g1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.5,2.0/15)]))
    g2.append([.2*lsize,0*lsize])
    g1.append(multiList([zRotate(-90),customScaling(1/wlength,1),customScaling(1,2.0/15)]))
    g2.append([.8*lsize,.6*lsize])
    g = ['g',g1,g2]
    
    h1 = []
    h2 = []
    h1.append(multiList([customScaling(1/wlength,1),customScaling(0.4,2.0/15)]))
    h2.append([.2*lsize,.5*lsize])    
    h1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(1.4,2.0/15)]))
    h2.append([.2*lsize,0*lsize])
    h1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.6,2.0/15)]))
    h2.append([.8*lsize,0*lsize])
    h = ['h',h1,h2]
    
    i1 = []
    i2 = []
    i1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.7,2.0/15)]))
    i2.append([.6*lsize,0*lsize])
    i1.append(multiList([zRotate(45),customScaling(1/wlength,1),customScaling(.2,2.0/15)]))
    i2.append([.475*lsize,.9*lsize])    
    i = ['i',i1,i2]
    
    j1 = []
    j2 = []
    j1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.9,2.0/15)]))
    j2.append([.9*lsize,-.4*lsize])
    j1.append(multiList([zRotate(45),customScaling(1/wlength,1),customScaling(.2,2.0/15)]))
    j2.append([.8*lsize,.7*lsize])
    j1.append(multiList([zRotate(-15),customScaling(1/wlength,1),customScaling(0.6,2.0/15)]))
    j2.append([0*lsize,-.3*lsize])
    j = ['j',j1,j2]
    
    
    
    #GOOD
    k1 = []
    k2 = []
    k1.append(multiList([zRotate(45),customScaling(1/wlength,1),customScaling(0.5, 2.0/15)]))
    k2.append([.5*lsize,.6*lsize])
    k1.append(multiList([zRotate(-45),customScaling(1/wlength,1),customScaling(0.5, 2.0/15)]))
    k2.append([.4*lsize,.4*lsize])
    k1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(1.4,2.0/15)]))
    k2.append([.35*lsize,0*lsize])
    k = ['k',k1,k2]
    
    
    #GOOD
    l1 = []
    l2 = []
    l1.append(multiList([customScaling(1/wlength,1),customScaling(0.4,2.0/15)]))
    l2.append([.4*lsize,0*lsize])    
    l1.append(multiList([zRotate(-90),customScaling(1/wlength,1),customScaling(1.3,2.0/15)]))
    l2.append([0.2*lsize,1.5*lsize])
    l = ['l',l1,l2]
    
    
    #GOOD
    m1 = []
    m2 = []
    m1.append(multiList([zRotate(80),customScaling(1/wlength,1),customScaling(0.7, 1.5/15)]))
    m2.append([.2*lsize,0*lsize])
    m1.append(multiList([zRotate(-80),customScaling(1/wlength,1),customScaling(0.7, 1.5/15)]))
    m2.append([.3*lsize,0.75*lsize])
    m1.append(multiList([zRotate(80),customScaling(1/wlength,1),customScaling(0.7, 1.5/15)]))
    m2.append([.65*lsize,0*lsize])
    m1.append(multiList([zRotate(-80),customScaling(1/wlength,1),customScaling(0.7, 1.5/15)]))
    m2.append([.75*lsize,0.75*lsize])
    m = ['m',m1,m2]
    
    n1 = []
    n2 = []
    n1.append(multiList([customScaling(1/wlength,1),customScaling(0.4,2.0/15)]))
    n2.append([.2*lsize,.5*lsize])    
    n1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.4,2.0/15)]))
    n2.append([.2*lsize,0*lsize])
    n1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.4,2.0/15)]))
    n2.append([.8*lsize,0*lsize])
    n = ['n',n1,n2]
    
    o1 = []
    o2 = []
    o1.append(multiList([customScaling(1/wlength,1),customScaling(0.6, 2.0/15,)]))
    o2.append([.2*lsize,.6*lsize])
    o1.append(multiList([customScaling(1/wlength,1),customScaling(0.6,2.0/15)]))
    o2.append([.2*lsize,0*lsize])
    o1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.4,2.0/15)]))
    o2.append([.2*lsize,.1*lsize])    
    o1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.4,2.0/15)]))
    o2.append([.9*lsize,.1*lsize])
    o = ['o',o1,o2]
    
    
    #NEEDS WORK
    p1 = []
    p2 = []
    p1.append(multiList([zRotate(40),customScaling(1/wlength,1),customScaling(0.5, 2.0/15)]))
    p2.append([.25*lsize,0*lsize])
    p1.append(multiList([zRotate(-40),customScaling(1/wlength,1),customScaling(0.5, 2.0/15)]))
    p2.append([.2*lsize,.7*lsize])
    p1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(1.2,2.0/15)]))
    p2.append([.1*lsize,-.4*lsize])  
    p = ['p',p1,p2]
    
    q1 = []
    q2 = []
    q1.append(multiList([customScaling(1/wlength,1),customScaling(0.6, 2.0/15)]))
    q2.append([.2*lsize,.5*lsize])
    q1.append(multiList([customScaling(1/wlength,1),customScaling(0.6,2.0/15)]))
    q2.append([.1*lsize,.0*lsize])
    q1.append(multiList([customScaling(1/wlength,1),customScaling(0.3,2.0/15)]))
    q2.append([.7*lsize,-.5*lsize])    
    q1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.5,2.0/15)]))
    q2.append([.2*lsize,0*lsize])
    q1.append(multiList([zRotate(-90),customScaling(1/wlength,1),customScaling(.9,2.0/15)]))
    q2.append([.8*lsize,.6*lsize])
    q = ['q',q1,q2]
    
    
    #OKAY
    r1 = []
    r2 = []
    r1.append(multiList([customScaling(1/wlength,1),customScaling(0.35,2.0/15)]))
    r2.append([.4*lsize,.5*lsize])
    r1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.7,2.0/15)]))
    r2.append([.4*lsize,0*lsize])
    r = ['r',r1,r2]
    
    
    #OKAY
    s1 = []
    s2 = []
    s1.append(multiList([zRotate(20),customScaling(1/wlength,1),customScaling(0.7, 2.0/15)]))
    s2.append([.175*lsize,.7*lsize])
    s1.append(multiList([zRotate(-20),customScaling(1/wlength,1),customScaling(0.6, 2.0/15)]))
    s2.append([.15*lsize,.575*lsize])
    s1.append(multiList([zRotate(20),customScaling(1/wlength,1),customScaling(0.7, 2.0/15)]))
    s2.append([.2*lsize,0*lsize])
    s = ['s',s1,s2]
    
    
    #GOOD
    t1 = []
    t2 = []
    t1.append(multiList([customScaling(1/wlength,1),customScaling(0.3,2.0/15)]))
    t2.append([.1*lsize,.8*lsize])
    t1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(1.3,2.0/15)]))
    t2.append([.6*lsize,0*lsize])
    t1.append(multiList([customScaling(1/wlength,1),customScaling(0.3,2.0/15)]))
    t2.append([.6*lsize,.8*lsize])
    t1.append(multiList([customScaling(1/wlength,1),customScaling(0.2,2.0/15)]))
    t2.append([.6*lsize,0*lsize])
    t = ['t',t1,t2]
    
    
    #GOOD
    u1 = []
    u2 = []
    u1.append(multiList([customScaling(1/wlength,1),customScaling(0.6,2.0/15)]))
    u2.append([.1*lsize,0*lsize])
    u1.append(multiList([zRotate(-90),customScaling(1/wlength,1),customScaling(.6,2.0/15)]))
    u2.append([0*lsize,.85*lsize])
    u1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.8,2.0/15)]))
    u2.append([.9*lsize,0*lsize])
    u = ['u',u1,u2]
    
    
    #GOOD
    v1 = []
    v2 = []
    v1.append(multiList([zRotate(60),customScaling(1/wlength,1),customScaling(0.65, 2.0/15)]))
    v2.append([.6*lsize,0*lsize])
    v1.append(multiList([zRotate(-60),customScaling(1/wlength,1),customScaling(0.65, 2.0/15)]))
    v2.append([0*lsize,.6*lsize])

    v = ['v',v1,v2]
    
    
    #GOOD
    w1 = []
    w2 = []
    w1.append(multiList([zRotate(80),customScaling(1/wlength,1),customScaling(0.7, 1.5/15)]))
    w2.append([.9*lsize,0*lsize])
    w1.append(multiList([zRotate(80),customScaling(1/wlength,1),customScaling(0.7, 1.5/15)]))
    w2.append([.4*lsize,0*lsize])
    w1.append(multiList([zRotate(-80),customScaling(1/wlength, 1),customScaling(0.7, 1.5/15)]))
    w2.append([.5*lsize,.75*lsize])
    w1.append(multiList([zRotate(-80),customScaling(1/wlength, 1),customScaling(0.7, 1.5/15)]))
    w2.append([0*lsize,.75*lsize])    
    w = ['w',w1,w2]
    
    
    #GOOD
    x1 = []
    x2 = []
    x1.append(multiList([zRotate(45),customScaling(1/wlength, 1),customScaling(0.5, 2.0/15)]))
    x2.append([.51*lsize,.46*lsize])
    x1.append(multiList([zRotate(135),customScaling(1/wlength, 1),customScaling(0.5, 2.0/15)]))
    x2.append([.45*lsize,.55*lsize])
    x1.append(multiList([zRotate(220),customScaling(1/wlength, 1),customScaling(0.5, 2.0/15)]))
    x2.append([.36*lsize,.48*lsize])
    x1.append(multiList([zRotate(-45),customScaling(1/wlength, 1),customScaling(0.5, 2.0/15)]))
    x2.append([.42*lsize,.38*lsize])
    x = ['x',x1,x2]
    
    
    #GOOD
    y1 = []
    y2 = []
    y1.append(multiList([zRotate(120),customScaling(1/wlength, 1),customScaling(0.6, 2.0/15)]))
    y2.append([.5*lsize,.2*lsize])
    y1.append(multiList([zRotate(60),customScaling(1/wlength, 1),customScaling(1.2, 2.0/15)]))
    y2.append([.35*lsize,-.5*lsize])
    y = ['y',y1,y2]
    
    
    #GOOD
    z1 = []
    z2 = []
    z1.append(multiList([customScaling(1/wlength,1),customScaling(.9, 2.0/15)]))
    z2.append([0*lsize,.8*lsize])
    z1.append(multiList([zRotate(45),customScaling(1/wlength,1),customScaling(1.1, 2.0/15)]))
    z2.append([0*lsize,0*lsize])
    z1.append(multiList([customScaling(1/wlength,1),customScaling(.9, 2.0/15)]))
    z2.append([0*lsize,0*lsize])
    z = ['z',z1,z2]
    
    
    #GOOD
    exc1 = []
    exc2 = []
    exc1.append(multiList([customMatrix(0,-1,1,0),customScaling(1/wlength,1),customMatrix(1,0,0,.25/1.6)]))
    exc2.append([(.25+(1/8))*lsize,.5*lsize])
    exc1.append(multiList([customMatrix(0,-1,1,0),customScaling(1/wlength,1),customMatrix(.25,0,0,.25/1.6)]))
    exc2.append([(.25+(1/8))*lsize,0*lsize])
    exc = ['!',exc1,exc2]#ADJUSTED FROM ORIGINAL
    
    #GOOD
    qmark1 = []
    qmark2 = []   
    qmark1.append(multiList([zRotate(40),customScaling(1/wlength,1),customScaling(0.5, 2.0/15)]))
    qmark2.append([.15*lsize,1*lsize])
    qmark1.append(multiList([zRotate(40),customScaling(1/wlength,1),customScaling(0.5, 2.0/15)]))
    qmark2.append([.6*lsize,.7*lsize])
    qmark1.append(multiList([zRotate(-45),customScaling(1/wlength,1),customScaling(0.4, 2.0/15)]))
    qmark2.append([.5*lsize,1.4*lsize])
    qmark1.append(multiList([zRotate(90),customScaling(1/wlength,1),customScaling(.35,2.0/15)]))
    qmark2.append([.7*lsize,.35*lsize])
    qmark1.append(multiList([zRotate(45),customScaling(1/wlength,1),customScaling(.2,2.0/15)]))
    qmark2.append([.575*lsize,0*lsize])    
    qmark = ['?',qmark1,qmark2]
    
    #GOOD
    per1 = []
    per2 = []
    per1.append(multiList([zRotate(45),customScaling(1/wlength,1),customScaling(.2,2.0/15)]))
    per2.append([.475*lsize,0*lsize])
    per = ['.',per1,per2]
    
    one1 = []
    one2 = []
    one1.append(multiList([customScaling(1/wlength,1),customMatrix(.5,0,0,1/8)]))
    one2.append([.25*lsize,0*lsize])
    one1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(1.25,0,0,1/8)]))
    one2.append([.6*lsize,.1875*lsize])
    one1.append(multiList([zRotate(45),customScaling(1/wlength,1),customMatrix(1,1,0,1),customMatrix(.3,0,0,1/10)]))
    one2.append([.2*lsize,1*lsize])
    one = ['1', one1, one2]
    
    two1 = []
    two2 = []
    two = ['2',two1,two2]
    
    three1 = []
    three2 = []
    three = ['3',three1, three2]
    
    four1 = []
    four2 = []
    four1.append(multiList([customMatrix(0,-1,1,0),customScaling(1/wlength,1),customMatrix(1.6,0,0,.25/1.6)]))
    four2.append([1*lsize,0*lsize])
    four1.append(multiList([customMatrix(1,0,.6,1),customScaling(1/wlength,1),customMatrix(3/4,0,0,.25/1.6)]))
    four2.append([0*lsize,.9*lsize])
    four1.append(multiList([customScaling(1/wlength,1),customMatrix(3/4,0,0,.25/1.6)]))
    four2.append([0*lsize,.65*lsize])
    four = ['4',four1,four2]
    
    five1 = []
    five2 = []
    five = ['5',five1,five2]
    
    six1 = []
    six2 = []
    six = ['6',six1,six2]
    
    seven1 = []
    seven2 = []
    seven1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(.15,0,0,.5)]))
    seven2.append([1*lsize,1.1*lsize])
    seven1.append(multiList([customScaling(1/wlength,1),customMatrix(1,.8*wlength,0,1),customMatrix(.25,0,0,.5)]))
    seven2.append([.25*lsize,.5*lsize])
    seven1.append(multiList([customScaling(1/wlength,1),customMatrix(1,.75*wlength,0,1),customMatrix(.25,0,0,.25)]))
    seven2.append([.065*lsize,.25*lsize])
    seven = ['7',seven1,seven2]
    
    eight1 = []
    eight2 = []
    eight1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(3/5,0,0,1/5)]))
    eight2.append([.3*lsize,0*lsize])
    eight1.append(multiList([customScaling(1/wlength,1),customMatrix(2/5,0,0,2/15)]))
    eight2.append([.3*lsize,0*lsize])
    eight1.append(multiList([customScaling(1/wlength,1),customMatrix(1,1*wlength,0,1),customMatrix(7/10,0,0,1/5)]))
    eight2.append([0*lsize,.6*lsize])
    eight1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(3/5,0,0,1/5)]))
    eight2.append([1*lsize,.9*lsize])
    eight1.append(multiList([customScaling(1/wlength,1),customMatrix(2/5,0,0,2/15)]))
    eight2.append([.3*lsize,1.3*lsize])
    eight1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(1,0,0,-1),customMatrix(1,1*wlength,0,1),customMatrix(3/5,0,0,1/5)]))
    eight2.append([0*lsize,.6*lsize])
    eight1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(1,0,0,-1),customMatrix(1,1*wlength,0,1),customMatrix(3/5,0,0,1/5)]))
    eight2.append([.7*lsize,0*lsize])
    eight = ['8', eight1, eight2]
    
    nine1 = []
    nine2 = []
    nine1.append(multiList([customScaling(1/wlength,1),customMatrix(.25,0,0,.5)]))
    nine2.append([.75*lsize,0*lsize])
    nine1.append(multiList([customScaling(1/wlength,1),customMatrix(.25,0,0,.5)]))
    nine2.append([.75*lsize,.5*lsize])
    nine1.append(multiList([customScaling(1/wlength,1),customMatrix(.25,0,0,.5)]))
    nine2.append([0*lsize,.5*lsize])
    nine1.append(multiList([customScaling(1/wlength,1),customMatrix(.25,0,0,.5)]))
    nine2.append([.75*lsize,0*lsize])
    nine1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(.25,0,0,.5)]))
    nine2.append([1*lsize,.5*lsize])
    nine1.append(multiList([zRotate(90),customScaling(1/wlength,1),customMatrix(.25,0,0,.5)]))
    nine2.append([1*lsize,1*lsize])
    nine = ['9', nine1, nine2]
    
    zero1 = []
    zero2 = []
    zero1.append(multiList([customMatrix(1,(.2/.3),0,1),zRotate(90),customScaling(1/wlength,1),customMatrix(.3,0,0,.3/1.5)]))
    zero2.append([.3*lsize,1.2*lsize])
    zero1.append(multiList([zRotate(-90),customScaling(1/wlength,1),customMatrix(1,0,0,.3/1.5)]))
    zero2.append([0*lsize,1.2*lsize])
    zero1.append(multiList([customMatrix(-1,0,0,1),customMatrix(1,1,0,1),zRotate(90),customScaling(1/wlength,1),customScaling(.2,.3/1.5)]))
    zero2.append([.2*lsize,0*lsize])
    zero1.append(multiList([customMatrix(1,1,0,1),zRotate(90),customScaling(1/wlength,1),customMatrix(.2,0,0,.3/1.5)]))
    zero2.append([.8*lsize,0*lsize])
    zero1.append(multiList([customMatrix(-1,0,0,1),zRotate(-90),customScaling(1/wlength,1),customMatrix(1,0,0,.3/1.5)]))
    zero2.append([1*lsize,1.2*lsize])
    zero1.append(multiList([customMatrix(-1,0,0,1),customMatrix(1,(.2/.3),0,1),zRotate(90),customScaling(1/wlength,1),customMatrix(.3,0,0,.3/1.5)]))
    zero2.append([.7*lsize,1.2*lsize])    
    zero = ['0', zero1, zero2]
    
    space1 = []
    space2 = []
    space = [' ',space1,space2]
    
    return [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,exc,qmark,per,one,two,three,four,five,six,seven,eight,nine,zero]


def wordParser(word, letters):
    global lsize
    spacesize = .05*lsize
    wordlist = list(word)
    wlength = len(wordlist)
    wordfunc = []
    wordpos = []
    letterpos = []
    letPos = 1
    for i in wordlist:
        for j in letters:
            if j[0] == i:
                for k in j[1]:
                    wordfunc.append(k)
                for z in j[2]:
                    wordpos.append([(z[0]+((letPos-1)*lsize)+(spacesize*letPos)),z[1]])
                    letterpos.append(letPos)
        letPos += 1
    return[wlength, wordfunc, wordpos, letterpos]


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
def getItOnScreen(pt):
    return [pt[0]+100, -pt[1]+size[1]-100]

def getItOnScreen2(pt):
    return [pt[0]+100, -pt[1]+size[1]-400]


def getWordOnScreen(size, pt):
    return [pt[0]+100, -pt[1]+size[1]-100]

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

def drawPoints(drawPts, color):
    for i in range(len(drawPts)):
        pygame.draw.line(screen, color, getItOnScreen(drawPts[i]), getItOnScreen(drawPts[i]), 1)

def drawPoints2(drawPts, color):
    for i in range(len(drawPts)):
        pygame.draw.line(screen, color, getItOnScreen2(drawPts[i]), getItOnScreen2(drawPts[i]), 1)
  
def drawWordPoints(size, screen, drawPts, color):
    for i in range(len(drawPts)):
        pygame.draw.line(screen, color, getWordOnScreen(size, drawPts[i]), getWordOnScreen(size, drawPts[i]), 1)

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
        if len(fs) > 1:
            j = random.randint(0,len(fs)-1)
        else:
            j = 0
        f = fs[j]
        aff = affs[j]
        pts.append(affine(pts[i-1],f,aff))
    return pts

def wordNest(pt, word, letters, num):
    parsed = wordParser(word, letters)
    return affineNest(pt, parsed[1],parsed[2],num)

















testWord = 'Niko'
wlength = len(testWord)
lsize = 250

letters = alphabet()




nest = wordNest([0,0], testWord, letters, 100000)
#print(str(nest))
box = [[0,0],[100,0],[100,150],[0,150]]

##MAIN
#done = False
#while not done:
    #clock.tick(25)
    #screen.fill(WHITE)
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #done=True
    #pygame.draw.line(screen, GREEN, [0,size[1]-100], [size[0],size[1]-100], 1)
    #pygame.draw.line(screen, GREEN, [100,0], [100,size[1]], 1)
    
    ##ADD DRAW FUNCTIONS HERE
    #drawPoints(nest, RED)
    ##drawLines(box,RED,2)
    #pygame.display.flip()


#pygame.quit()