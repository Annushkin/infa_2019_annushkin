from graph import *

brushColor(0,255,255)
rectangle(0, 0, 600, 300)
brushColor(20,255,0)
rectangle(0, 250, 600, 600)

penColor(250,200,0)
brushColor("yellow")
circle(450, 50, 30)


def trees (x, y, r):
    penColor("white")
    brushColor("white")
    rectangle(x-10, y+r-10, x+10, y+r*2)

    penSize(1)
    penColor(200,255,0)
    brushColor("green")
    circle(x, y, r)

    penColor("yellow")
    brushColor("white")
    circle(x+r*3/4, y+r*1/2, r/6)

x=120
y=220
r=50
for i in range(3):
    trees(x, y, r)
    x=x+100
    y=y-10
    r=r+3

def sheeps (x1, y1, r1):
    penColor("black")
    brushColor("black")
    rectangle(x1-15, y1+r1-10, x1-10, y1+r1*1.8)
    rectangle(x1+15, y1+r1-10, x1+10, y1+r1*1.8)
    brushColor("white")
    circle(x1, y1, r1)
    circle(x1-r1, y1+3/4*r1, r1/2)
    polygon([(x1+r1,y1), (x1+r1+15,y1-5),
         (x1+r1+15,y1+5), (x1+r1,y1)])
    polygon([(x1-r1*1.5,y1+3/4*r1), (x1-r1*1.5-10,y1+3/4*r1-5),
         (x1-r1*1.5-10,y1+3/4*r1+5), (x1-r1*1.5,y1+3/4*r1)])
    polygon([(x1-r1*1.5+3,y1+3/4*r1-5), (x1-r1*1.5-5,y1+3/4*r1-15),
         (x1-r1*1.5-10,y1+3/4*r1-5), (x1-r1*1.5+3,y1+3/4*r1-5)])

x1=100
y1=400
r1=30
sheeps (x1, y1, r1)

x1=200
y1=450
r1=30
sheeps (x1, y1, r1)

x1=300
y1=390
r1=30
sheeps (x1, y1, r1)

x1=400
y1=460
r1=30
sheeps (x1, y1, r1)

run()
