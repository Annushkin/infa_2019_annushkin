from graph import*
from math import*

windowSize(500, 700)
canvasSize(500, 700)
width, height = windowSize()
c = canvas()
penColor('black')
brushColor('black')
rectangle(0, 300, width, height)
c.configure(background = "#666666")

##луна,облака
penColor('#e6e6e6')
brushColor('#e6e6e6')
circle(445, 60, 40)
c.create_oval(200, 150, 500, 200, fill = '#1a1a1a', outline = '#1a1a1a')
brushColor('#e6e6e6')
circle(445, 60, 40)
c.create_oval(300, 100, 900, 140, fill = '#4d4d4d', outline = '#4d4d4d')
c.create_oval(30, 59, 440, 110, fill = '#333333', outline = '#333333')
c.create_oval(180, 35, 500, 75, fill = '#4d4d4d', outline = '#4d4d4d')
c.create_oval(100, 350, 400, 390, fill = '#4d4d4d', outline = '#4d4d4d')

def ellips_rot(x1, y1, a, b, phi):
    a = int(a)
    p = []
    for x in range(-a, a, 1):
        y = b * (1 - x * x / (a * a))**0.5
        x, y = x * cos(radians(phi)) - y * sin(radians(phi)), \
                x * sin(radians(phi)) + y * cos(radians(phi))
        xe = x + x1
        ye = y + y1
        p.append((xe, ye))

    for x in range(a, -a, -1):
        y =-b * (1 - x * x / (a * a))**0.5
        x, y = x * cos(radians(phi)) - y * sin(radians(phi)), \
                x * sin(radians(phi)) + y * cos(radians(phi))
        xe = x + x1
        ye = y + y1
        p.append((xe, ye))
    polygon(p)


##домики
def gost_houses (x, y):
    penColor('#28220b')
    brushColor('#28220b')
    rectangle(x, y, x + 130, y + 180)
    penColor('#2b1100')
    brushColor('#2b1100')
    rectangle(x + 15, y + 130, x + 40, y + 160)
    rectangle(x + 53, y + 130, x + 78, y + 160)
    penColor('#d4aa00')
    brushColor('#d4aa00')
    rectangle(x + 91, y + 130, x + 116, y + 160)
    penColor('#483e37')
    brushColor('#483e37')
    rectangle(x + 10, y, x + 22, y + 60)
    rectangle(x + 35, y, x + 47, y + 60)
    rectangle(x + 67, y, x + 79, y + 60)
    rectangle(x + 99, y, x + 111, y + 60)
    penColor('#1a1a1a')
    brushColor('#1a1a1a')
    rectangle(x - 10, y + 60, x + 140, y + 80)
    rectangle(x + 9, y + 40, x + 15, y + 60)
    rectangle(x + 33, y + 40, x + 39, y + 60)
    rectangle(x + 55, y + 40, x + 61, y + 60)
    rectangle(x + 82, y + 40, x + 88, y + 60)
    rectangle(x + 112, y + 40, x + 118, y + 60)
    rectangle(x - 5, y + 37, x + 135, y + 44)
    rectangle(x + 135, y + 45, x + 137, y + 60)
    rectangle(x - 8, y + 45, x - 6, y + 60)
    penColor('#0d0c0c')
    brushColor('#0d0c0c')
    polygon([(x - 10, y), (x + 10, y - 15), (x + 120, y - 15), (x + 140, y),
            (x - 10, y)])
    penColor('#282828')
    brushColor('#282828')
    rectangle(x + 15, y - 30, x + 18, y - 8)
    rectangle(x + 112, y - 30, x + 115, y - 8)
    rectangle(x + 22, y - 45, x + 29, y - 8)
    rectangle(x + 80, y - 30, x + 83, y - 15)

gost_houses(10, 320)
gost_houses(175, 260)
gost_houses(360, 160)


##привидения
def ghosts (x, y, s):
    penColor('#b3b3b3')
    brushColor('#b3b3b3')
    r = 18
    circle(x, y, r*s)
    polygon([(x - r * s, y + 0.4 * r * s), (x - 1.3 * r * s, y + 0.8 * r * s),
        (x - 1.4 * r * s, y + 1.5 * r * s), (x - 2.6 * r * s, y + 3.9 * r * s),
        (x - 2.2 * r * s, y + 4.2 * r * s), (x - 2 * r * s, y + 4.8 * r * s),
        (x - 1.1 * r * s, y + 4.4 * r * s), (x + 0.1 * r * s, y + 5.3 * r * s),
        (x + 1.1 * r * s, y + 4.3 * r * s), (x + 2.2 * r * s, y + 4.9 * r * s),
        (x + 2.2 * r * s, y + 3.9 * r * s), (x + 4.4 * r * s, y + 4.4 * r * s),
        (x + 1.7 * r * s, y + 0.3 * r * s), (x + r * s, y),
        (x - r * s, y + 0.4 * r * s)])
    penColor('#87cdde')
    brushColor('#87cdde')
    r = 5
    circle(x - 1.5 * r * s, y, r * s)
    circle(x + 1.4 * r * s, y - 0.6 * r * s, r * s)
    penColor('black')
    brushColor('black')
    r = 2
    circle(x - 4 * r * s, y + 0.7 * r * s, r * s)
    circle(x + 2.5 * r * s, y - r * s, r * s)
    penColor(235, 235, 235)
    brushColor(235, 235, 235)
    ellips_rot(x - 1.9 * r * s, y - 0.8 * r * s, 4 * s, 1 * s, - 30)
    ellips_rot(x + 4.5 * r * s, y - 2 * r * s, 4 * s, 1 * s, - 30)

ghosts(400, 500, 1)
ghosts(430, 380, 0.3)
ghosts(330, 450, 0.5)
ghosts(150, 550, 1.2)

##label("6", 230, 345, font = ("Calibry", 20), bg = "#584911", bd = 2)
##label("МФТИ", 200, 345, font = ("Calibry", 20), bg = "#584911", bd = 2)

run()
