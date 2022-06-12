import matplotlib.pyplot as plt
import math
import random

## square marching


# on prend en argument une fonction f(x,y), et onn cherche à tracer la courbe f(x,y) = 0

def configuration (carré) :
    [[a,b],[c,d]] = carré
    tab = [0,0,0,0]
    if a > 0 : tab[0] = 1
    if b > 0 : tab[1] = 1
    if c > 0 : tab[2] = 1
    if d > 0 : tab[3] = 1
    return tab[3]+tab[2]*2 + tab[1]*4 + tab[0]*8

def dessin (f,config,bg,dx):
    x,y = bg
    if config == 1 : plt.plot ([x+dx/2,x+dx],[y,y+dx/2],'r')
    elif config == 2 : plt.plot ([x,x+dx/2],[y+dx/2,y],'r')
    elif config == 3 : plt.plot ([x,x+dx],[y+dx/2,y+dx/2],'r')
    elif config == 4 : plt.plot ([x+dx/2,x+dx],[y+dx,y+dx/2],'r')
    elif config == 5 : plt.plot ([x+dx/2,x+dx/2],[y,y+dx],'r')
    elif config == 6 :
        fm = f(x+dx/2,y+dx/2)
        if fm > 0 :
            plt.plot ([x,x+dx/2],[y+dx/2,y+dx],'r')
            plt.plot ([x+dx/2,x+dx],[y,y+dx/2],'r')
        else :
            plt.plot ([x,x+dx/2],[y+dx/2,y],'r')
            plt.plot ([x+dx/2,x+dx],[y+dx,y+dx/2],'r')
    elif config == 7 : plt.plot ([x,x+dx/2],[y+dx/2,y+dx],'r')
    elif config == 8 : plt.plot ([x,x+dx/2],[y+dx/2,y+dx],'r')
    elif config == 9 :
        fm = f(x+dx/2,y+dx/2)
        if fm > 0 :
            plt.plot ([x,x+dx/2],[y+dx/2,y],'r')
            plt.plot ([x+dx/2,x+dx],[y+dx,y+dx/2],'r')
        else :
            plt.plot ([x,x+dx/2],[y+dx/2,y+dx],'r')
            plt.plot ([x+dx/2,x+dx],[y,y+dx/2],'r')
    elif config == 10 : plt.plot ([x+dx/2,x+dx/2],[y,y+dx],'r')
    elif config == 11 : plt.plot ([x+dx/2,x+dx],[y+dx,y+dx/2],'r')
    elif config == 12 : plt.plot ([x,x+dx],[y+dx/2,y+dx/2],'r')
    elif config == 13 : plt.plot ([x,x+dx/2],[y+dx/2,y],'r')
    elif config == 14 : plt.plot ([x+dx/2,x+dx],[y,y+dx/2],'r')
    # 0 et 15 correspondent à des fills

def fill (config,bg,dx):
    x,y = bg
    if config == 1 : plt.fill([x+dx/2,x+dx,x+dx],[y,y+dx/2,y],'r')
    elif config == 2 : plt.fill ([x,x+dx/2,x],[y+dx/2,y,y],'r')
    elif config == 3 : plt.fill ([x,x+dx,x,x+dx],[y+dx/2,y+dx/2,y,y],'r')
    elif config == 4 : plt.fill ([x+dx/2,x+dx,x+dx],[y+dx,y+dx/2,y+dx],'r')
    elif config == 5 : plt.fill ([x+dx/2,x+dx/2,x+dx,x+dx],[y,y+dx,y+dx,y],'r')
    elif config == 6 :
        fm = f(x+dx/2,y+dx/2)
        if fm > 0 :
            plt.fill ([x,x+dx/2,x+dx/2,x+dx],[y+dx/2,y+dx,y,y+dx/2],'r')
        else :
            plt.fill ([x,x+dx/2,x],[y+dx/2,y,y],'r')
            plt.fill ([x+dx/2,x+dx,x+dx],[y+dx,y+dx/2,y+dx],'r')
    elif config == 7 : plt.fill ([x,x+dx/2,x,x+dx,x+dx],[y+dx/2,y+dx,y,y,y+dx],'r')
    elif config == 8 : plt.fill ([x,x+dx/2,x],[y+dx/2,y+dx,y+dx],'r')
    elif config == 9 :
        fm = f(x+dx/2,y+dx/2)
        if fm > 0 :
            plt.fill ([x,x+dx/2,x+dx/2,x+dx],[y+dx/2,y+dx,y,y+dx/2],'r')
        else :
            plt.fill ([x,x+dx/2,x],[y+dx/2,y+dx,y+dx],'r')
            plt.fill([x+dx/2,x+dx,x+dx],[y,y+dx/2,y],'r')
    elif config == 10 : plt.fill ([x+dx/2,x+dx/2,x,x],[y,y+dx,y,y+dx],'r')
    elif config == 11 : plt.fill ([x+dx/2,x+dx,x,x,x+dx],[y+dx,y+dx/2,y+dx,y,y],'r')
    elif config == 12 : plt.fill ([x,x+dx,x,x+dx],[y+dx/2,y+dx/2,y+dx,y+dx],'r')
    elif config == 13 : plt.fill ([x,x+dx/2,x,x+dx,x+dx],[y+dx/2,y,y+dx,y+dx,y],'r')
    elif config == 14 : plt.fill ([x+dx/2,x+dx,x,x,x+dx],[y,y+dx/2,y,y+dx,y+dx],'r')
    elif config == 15 : plt.fill ([x,x,x+dx,x+dx],[y,y+dx,y,y+dx],'r')
    # ultra lent avec les fills et pas dingue en vrai, à améliorer

def trace_carre (f,coord_bas_gauche_carré,dx):
    x,y = coord_bas_gauche_carré
    bg = x,y
    bd = x+dx,y
    hg = x,y+dx
    hd = x+dx,y+dx
    f_carré = [[f(x,y+dx),f(x+dx,y+dx)],[f(x,y),f(x+dx,y)]]
    config = configuration(f_carré)
    dessin(f,config,bg,dx)

def trace_graphe (f,dx,xmin,ymin,xmax,ymax):
    imax = floor((xmax-xmin)/dx)
    jmax = floor((ymax-ymin)/dx)
    for i in range (imax) :
        for j in range (jmax):
            trace_carre(f,(xmin + i*dx,ymin + j*dx),dx)
    plt.axis('equal')
    plt.show()

def f_test (x,y) : return (x-3)**2 + (y-3)**2 - 9

def f_samy(x,y): return 4*x**3 - 20/(y+1) + 7

def lemniscate (x,y) :
    return (x**2+y**2)**2 - 1**2 * (x**2 - y **2)

def f_mathieu (x,y) : return (x**3 + y**4)/3

def f_joli(x,y): return tan((x)**2 + (y)**2) -1

def f_t(x,y): return ((x)**2 + (y)**2) -1

## application du square marching pour animation interaction champ elec

class corps:
    def __init__(self,coord,vitesse,masse):
        self.masse = masse
        self.coord = coord
        self.vitesse = vitesse
        self.rayon = (self.masse/3.14)**(1/3)

def potentiel (corps,x,y,coeff):
    c_x,c_y = corps.coord
    r = sqrt((x-c_x)**2 + (y-c_y)**2)
    return corps.masse*coeff*1/r

def cadre(self):
    a = self.coord
    r = self.rayon
    x,y = a
    c,b = self.vitesse

    if x > 1:
        if c > 0 :
            self.vitesse = (-0.9*c,b)
        self.coord = (x-0.01,y)
    if x < -1 :
        if c < 0 :
            self.vitesse = (-0.9*c,b)
        self.coord = (x+0.01,y)
    if y > 1 :
        if b > 0 :
            self.vitesse = (c,-0.9*b)
        self.coord = (x,y-0.01)
    if y < -1:
        if b < 0 :
            self.vitesse = (c,-0.9*b)
        self.coord = (x,y+0.01)


def nouvelle_etape (liste_corps,dt):
    for corps in liste_corps :
        cadre(corps)
        x,y = corps.coord
        vx,vy = corps.vitesse
        corps.coord = x+vx*dt , y+vy*dt
    return liste_corps

def trace_graphe_2 (f,dx,xmin,ymin,xmax,ymax,k):
    imax = floor((xmax-xmin)/dx)
    jmax = floor((ymax-ymin)/dx)
    for i in range (imax) :
        for j in range (jmax):
            trace_carre(f,(xmin + i*dx,ymin + j*dx),dx)
    plt.axis('equal')
    plt.axis([-2,2,-2,2])
    plt.savefig("image/etape_{}.png".format(k))
    plt.close()

def affichage (liste_corps,coeff,dx,xmin,ymin,xmax,ymax,k,val):
   # for corps in liste_corps :
    #    plt.scatter(corps.coord,'r')
    def f(x,y):
        s = 0
        for corps in liste_corps :
            s+= potentiel (corps,x,y,coeff)
        return s - val
    trace_graphe_2(f,dx,xmin,ymin,xmax,ymax,k)

def animation (coeff,dx,xmin,ymin,xmax,ymax,dt,tmax,n,val):
    liste_corps = generateur_ (n)
    for k in range (floor(tmax/dt)):
        nouvelle_etape(liste_corps,dt)
        #l = [corps.coord for corps in liste_corps]
        #print(l)
        affichage (liste_corps,coeff,dx,xmin,ymin,xmax,ymax,k,val)


def generateur_ (nbr_corps):
    liste_corps = []
    for k in range (nbr_corps):
        m = random.gauss(0.5,1)
        while m <=0 :
            m = random.gauss(0.5,1)
        liste_corps.append( corps((random.uniform(-1,1),random.uniform(-1,1)),(random.uniform(0,0.1),random.uniform(0,0.1)),m) )
    return liste_corps


import imageio
def gif ():
    with imageio.get_writer('mygif3.gif', mode='I') as writer:
        filenames = ["image/etape_{}.png".format(k) for k in range (800)]
        for filename in filenames :
            image = imageio.imread(filename)
            writer.append_data(image)

## visualisation condensateur

# condensateur plan

import numpy as np
import seaborn as sns
from math import *

def dist (a,b):
    c,d = a
    e,f = b
    return sqrt ((c-e)**2 + (d-f)**2)

def f_cond (distance, longueur, n, coeff,dx,dy):
    h = longueur/n
    ny = floor(longueur/dy)
    nx = floor(distance/dx)

    positions_plus = [ (i*h + h/2,-distance/100) for i in range (n) ]
    positions_moins = [ (i*h + h/2,distance +distance/100) for i in range (n) ]

    def potentiel_force (x,y):
        s = 0
        fx = 0
        fy = 0
        for k in range(len(positions_plus)) :
            pos = (x,y)
            part = positions_plus[k]
            a,b = part
            r = dist (part,pos)
            s += 1/r
            fx -= 1/r**2 * cos( atan((a-x) /(b-y)))
            fy -= 1/r**2 * sin(atan((a-x) /(b-y)))
        for part in positions_moins :
            r = dist (part, (x,y))
            s -= 1/r
            fx += 1/r**2 * cos( atan((a-x) /(b-y)))
            fy += 1/r**2 * sin( atan((a-x) /(b-y)))
        return s,fx,fy


    carte_potentiel = np.zeros((ny,nx))
    carte_fx = np.zeros((ny,nx))
    carte_fy = np.zeros((ny,nx))
    for i in range (ny) :
        for j in range (nx) :
            carte_potentiel[i,j],carte_fx[i,j],carte_fy[i,j]  = potentiel_force(dy*i,dx*j)

    plt.figure(1)
    ax = sns.heatmap(carte_potentiel, linewidth=0.)
    ax.set_title("Carte Potentiel")

    plt.figure(2)
    ax = sns.heatmap(carte_fx, linewidth=0.)
    ax.set_title("Carte Fx")

    plt.figure(3)
    ax = sns.heatmap(carte_fy, linewidth=0.)
    ax.set_title("Carte Fy")


    plt.show()




























