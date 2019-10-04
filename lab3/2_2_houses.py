from graph import*
from math import*

windowSize(800, 700)
canvasSize(800, 700)
width, height = windowSize()
c = canvas()
penColor('#32CD32')
brushColor('#32CD32')
rectangle(0, 400, width, height)
c.configure(background = "#87CEEB")

def ellips_rot(x1, y1, a, b, phi):
    a=int(a)
##    penColor(235, 235, 235)
##    brushColor(235, 235, 235)
    p=[]
    for x in range(-a, a, 1):
        y = b * (1 - x * x / (a * a))**0.5
        x, y = x * cos(radians(phi)) - y * sin(radians(phi)), \
                x * sin(radians(phi)) + y * cos(radians(phi))
        xe = x + x1
        ye = y + y1
        p.append((xe, ye))
    for x in range(a, -a, -1):
        y = -b * (1 - x * x / (a * a))**0.5
        x, y = x * cos(radians(phi)) - y * sin(radians(phi)), \
                x * sin(radians(phi)) + y * cos(radians(phi))
        xe = x + x1
        ye = y + y1
        p.append((xe, ye))
    polygon(p)

##домики
penColor('black')
def house (x, y, s):
    brushColor('#D2691E')
    rectangle(x, y, x + 200 * s, y + 150 * s)
    brushColor('#B22222')
    rectangle(x + 150*s , y - 100*s, x + 170 * s, y - 5 * s)
    polygon([(x, y), (x + 100 * s, y - 100*s), (x + 200*s, y), (x, y)])
    brushColor('#1E90FF')
    rectangle(x + 50*s , y + 30 * s, x + 150 * s, y + 120 * s)
    brushColor('#CDB79E')
    c.create_oval(x+63*s, y + 50 * s, x + 80 * s, y + 95 * s, fill = '#458B00', \
                    outline = 'black')
    polygon([(x + 60 * s, y + 90 * s), (x + 90 * s, y + 90 * s), \
            (x + 85 * s, y + 120 * s), (x + 60 * s, y + 120 * s), \
            (x + 55 * s, y + 90 * s)])
    brushColor('#D2691E')
    rectangle(x + 100*s , y + 30 * s, x + 110 * s, y + 120 * s)
house (90, 350, 1)
house (500, 310, 0.8)

##деревья
def trees (x, y, s):
    r=30
    brushColor(130, 100, 10)
    polygon([(x + 0.5 * r * s, y + 2 * r * s), (x + 1.5 * r * s, y + 2 * r * s), \
            (x + 1.5 * r * s, y + 5 * r * s), (x + 0.5 * r * s, y + 5 * r * s), \
            (x + 0.5 * r * s, y + 2 * r * s)])
    brushColor('green')
    circle(x + r * s, y - r * s, r * s)
    circle(x, y, r * s)
    circle(x + 2 * r * s, y, r * s)
    circle(x + r * s, y + r * s - 10, r * s)
    circle(x + r * s / 6, y + 2 * r * s - 10, r * s)
    circle(x + 2 * r * s - 5, y + 2 * r * s - 10, r * s)
trees(340,350,1)
trees(700,310,0.8)


##забор
def fence (x, y, s):
    brushColor(240, 204, 80)
    polygon([(x, y), (x, y - 70 * s), (x + 9 * s, y - 75 * s), \
            (x + 18 * s, y - 70 * s), (x + 18 * s, y),(x, y)])
    brushColor('black')
    circle(x + 9 * s, y - 50 * s, 2 * s)
x=5
for i in range (15):
    fence(x, 580, 1)
    x += 30
x=450
for i in range (14):
    fence(x, 500, 0.8)
    x += 25

##котики
def cat (x, y, s):
    r=15
    penSize (1)
    brushColor(182, 177, 159)
    polygon([(x-r*s, y+1*s),(x-1.2*r*s, y-1.3*r*s),(x-0.3*r*s, y-0.5*r*s),\
            (x-r*s, y+1*s)])
    polygon([(x-0.3*r*s, y-0.5*r*s),(x-0.2*r*s, y-1.7*r*s),\
            (x+0.8*r*s, y-0.5*r*s),(x-0.3*r*s, y-0.5*r*s)])
    circle(x, y, r*s)
    penColor('black')
    brushColor('#b6b19f')
    ellips_rot (x+0.5*r*s, y+2.2*r*s, r*s, 0.25*r*s, -50)
    ellips_rot (x+4*r*s, y+2.5*r*s, r*s, 0.25*r*s, -60)
    c.create_oval(x+1.5*r*s, y+1.5*r*s, x+2*r*s, y+3.5*r*s, fill='#b6b19f')
    c.create_oval(x+5.3*r*s, y+1.5*r*s, x+5.8*r*s, y+3.5*r*s, fill='#b6b19f')
    c.create_oval(x+5.3*r*s, y-3*r*s, x+6.3*r*s, y+0.3*r*s, fill='#b6b19f')      #хвост
    c.create_oval(x+0.7*r*s, y-0.4*r*s, x+6*r*s, y+2*r*s, fill='#b6b19f')        #тело
    brushColor('green')
    circle(x-0.53*r*s, y+0.1*r, 0.2*r*s)
    circle(x+0.25*r*s, y-0.35*r*s, 0.2*r*s)
    penColor('black')
    penSize (2)
    moveTo(x-0.1*r*s, y+0.65*r*s)
    lineTo(x+0.11*r*s, y+0.25*r*s)
    lineTo(x+0.6*r*s, y+0.3*r*s)

cat(570, 510, 1)
cat(150, 600, 1.5)

##облака
def clouds (x, y, s):
    brushColor('white')
    penSize (1)
    r=32
    circle(x, y, r*s)
    circle(x+1.2*r*s, y, r*s)
    circle(x+2.4*r*s, y, r*s)
    circle(x+3.6*r*s, y, r*s)
    circle(x+1.2*r*s, y-1.5*r*s, r*s)
    circle(x+2.4*r*s, y-1.5*r*s, r*s)

clouds(250, 150, 1)
clouds(500, 120, 0.8)
clouds(700, 100, 0.5)

##клумба
penSize (1)
brushColor(182, 177, 159)
c.create_oval(450, 590, 750, 680, fill='#57f014', outline='black')

def flower (x, y):
    brushColor('red')
    circle(x+10, y, 6)
    circle(x-10, y, 6)
    circle(x, y-10, 6)
    circle(x, y+10, 6)
    brushColor('yellow')
    circle(x,y, 5)

flower (500, 635)
flower (550, 625)
flower (600, 640)
flower (650, 620)
flower (700, 635)

##солнце
N=12
x=100
y=100
r=90
c=200
hc=10
h=5

for i in range(N):
    penColor (240, c, 20)
    brushColor (240, c, 20)
    circle (x, y, r-h)
    r-=h
    c-=hc



run()




