import numpy as np  
import matplotlib.pyplot as plt
import numpy.random as alea

def visu_point(matPoint,style):
    # matPoint contient les coordonnées des points 
    x = matPoint[0, :]
    y = matPoint[1, :]
    plt.plot(x, y, style)
    
def visu_segment(P1,P2,style):
    # attention P1 et P2 sont des tableaux (2,1)
    matP = np.concatenate((P1,P2),1)
    visu_point(matP,style)

def visu_BezierQuad(matPointControl,str):
    
    n=50
    mt = np.linspace(0,1.,n)  
    matt = np.ones((3,n))  # que des 1
    matt[1,:] = mt  # ligne avec les t
    matt[2,:] = mt*mt  # ligne avec les t*t

    matBezier3 = np.array([[1, 0, 0], 
                           [-2, 2, 0], 
                           [1, -2, 1]])

    matPointligne = np.dot(np.dot(matt.T,matBezier3),matPointControl.T)
    matPoint=matPointligne.T  # on transpose

    visu_point(matPoint,str)
    
def visu_BezierCubic(matPointControl,str):
    n=50
    mt = np.linspace(0,1.,n)  
    matt = np.ones((4,n))  # que des 1
    matt[1,:] = mt  # ligne avec les t
    matt[2,:] = mt*mt  # ligne avec les t*t
    matt[3,:] = mt*mt*mt
    matBezier4 = np.array([[1,0,0, 0],
                          [-3,3,0, 0],
                          [3, -6, 3, 0],
                          [-1,3,-3,1]])
    
    matPointligne = np.dot(np.dot(matt.T,matBezier4),matPointControl.T)
    matPoint=matPointligne.T  # on transpose

    visu_point(matPoint,str)

# *********************************************************

plt.axis('scaled') # la position est importante
taille=25
plt.xlim(-taille-1, taille+1+5)  
plt.ylim(-taille-1, taille+1)

matPointControl3 = np.array([[7,-20,25,-5],
                             [8,5,-1,-5]])
matPointControl4 = np.array([[-5, -15, -10],
                             [-5, -5, 0]])


matPointControl10 = np.zeros((2,4))
matPointControl11 = np.zeros((2,3));
   
over = 0.2
for nbCoubre in  range (20) :     
    over +=0.2
    for i in range(2):
        for j in range(4) : 
            if (i == 1) : 
                if (matPointControl3[i][j]) < 0 : 
                    matPointControl10[i][j] = matPointControl3[i][j]-over
                else : 
                    matPointControl10[i][j] = matPointControl3[i][j]+over
            else :
                matPointControl10[i][j] = matPointControl3[i][j]
        
    visu_BezierCubic(matPointControl10, "k")
    
over = 0.2

for nbCoubre in range (20) : 
    over +=0.2
    for i in range (2) : 
        for  j in range(3) : 
            if (i == 1) : 
                if (matPointControl4[i][j] < 0) : 
                    matPointControl11[i][j] = matPointControl4[i][j]-over
                else : 
                    matPointControl11[i][j] = matPointControl4[i][j]+over
            else : 
                matPointControl11[i][j] = matPointControl4[i][j]
    visu_BezierQuad(matPointControl11, "k")         
    

matPointControlTriangle = np.array([[-9,-7, -4],
                                    [-15, -5, -15]])
    

tab_angle = np.linspace(0, np.pi*2, 30)
rayon = 1.5
for i in range(20) : 
    x = 0 + np.cos(tab_angle)*rayon
    y = -12 + np.sin(tab_angle)*rayon
    plt.plot(x,y,'k')    
    rayon-=0.1
    
rayon = 1.5
for i in range(20) : 
    x = -3.5 + np.cos(tab_angle)*rayon
    y = -12 + np.sin(tab_angle)*rayon
    plt.plot(x,y,'k')    
    rayon-=0.1    
    
