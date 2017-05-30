import pygame as pg
import time as tt
import random as rnd
from pygame.locals import *

x = pg.init()

clock = pg.time.Clock()

point1 = 10
point2 = 0
    
DspH = 600
DspW = 600
gd = pg.display.set_mode((DspW,DspH))
pg.display.set_caption('PYPONG')
ico = pg.image.load('icon.png')
pg.display.set_icon(ico)
bounce = pg.mixer.Sound('g_bounce1.wav')
out = pg.mixer.Sound('test.wav')
c = []

pink=(255,0,255)
aqua = (127,224,230)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
dgreen = (0,150,0)
blue = (0,0,255)
pink = (255,105,180)
dpink = (180,0,100)
orchid = (155,50,204)
sblue=(0,191,255)
dsblue = (30,4,200)
yellow = (255,255,0)
gold = (255,215,0)
orange = (255,127,0)

def controls():
    gcont = True
    
    while gcont:
        p = pg.mouse.get_pressed()
        gd.fill(white)
        msg_to_scrn('Controls',blue,-200,Font = 'Algerian',Size= 50)
        msg_to_scrn('Player 1:           Player 2:',red,0,-40,Font='comicsansms')
        msg_to_scrn( 'UP - "W"          UP - "Arraow(UP)"  ',red,30,20,Font='comicsansms')
        msg_to_scrn('DOWN- "S"      DOWN - "Arrow(DOWN)"',red,60,50,Font='comicsansms')
        msg_to_scrn('Pause: "P"',red,140,Font='comicsansms')
        clock.tick(15)
        gcont = False
        pg.display.update()
        

def text_on_button(msg,color,rectX,rectY,rectW,rectH,Font= 'Arial',Size=25):
    font = pg.font.SysFont(Font,Size)
    textS = font.render(msg,True,color)

    textrect = textS.get_rect()
    textrect.center = (rectX + rectW/2),(rectY + rectH/2)
    gd.blit(textS,textrect)

def button(bX,bY,bW,bH,inactive_color,active_color,text,text_acolor,text_incolor,Font='Arial',Size=25,action = None):
    cur = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    
    if bX < cur[0] < bX+bW and bY < cur[1] < bY+bH:
        pg.draw.rect(gd,active_color,[bX-10,bY-10,bW+20,bH+20])
        text_on_button(text,text_acolor,bX,bY,bW,bH,Font,Size+10)
        if click[0] == 1:
            if action== 'quit':
    
                quit()
            if action == 'play':
                
                gameloop(0,0)
            if action == 'play':
                pass
                
            if action == 'controls':
                controls()
            if action == 'main':
                start()
            
    else:
        pg.draw.rect(gd,inactive_color,[bX,bY,bW,bH])
        text_on_button(text,text_incolor,bX,bY,bW,bH,Font,Size)
        
def start():
    
    intro = True
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    Exit = True
                    pg.quit()
                    quit()
        gd.fill(white)
        msg_to_scrn('PYPONG',blue,-150,Font = 'Algerian',Size= 50)
        msg_to_scrn('SCORE 10 TO WIN',red)
        

        button(50,500,130,50,pink,dpink,'Play',blue,sblue, 'comicsansms',35,'play')
        button(220,500,150,50,sblue,dsblue,'Controls',red,pink, 'comicsansms',35,'controls')
        button(400,500,130,50,yellow,orange,'Quit',green,dgreen, 'comicsansms',35,'quit')

        pg.display.update()

def won(player):
    wo  = True
    while wo:
        gd.fill(pink)
        msg_to_scrn('Congrates',red,-100,Size = 45)
        msg_to_scrn(str(player)+' won the game',blue,Size = 35)
        msg_to_scrn('Press "P" to play again',black,50,Size = 30)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    gameloop(0,0)
                    wo = False
            if event.type == pg.QUIT:
                quit()
        pg.display.update()
def msg_to_scrn(msg,color,y_disp= 0,x_disp = 0,Font= 'Arial',Size=25):
    font = pg.font.SysFont(Font,Size)
    
    textS = font.render(msg,True,color)
    textrect = textS.get_rect()
    textrect.center = ((DspW/2)+x_disp),((DspH/2)+y_disp)
    gd.blit(textS,textrect)

def pause():
    pause = True
    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    pause = False
                if event.key == pg.K_q:
                    quit()
        msg_to_scrn('Press "C" to continue and "Q" to quit',blue,200,Size = 35)
        pg.display.update()
 
def gameloop(point1,point2):
    game = True
    ya = DspH/2-50
    yb = DspH/2-50
    yachng = 0
    ybchng = 0
    speed = [1]
    spd = 10
    xc = int(DspW/2)
    yc =int(DspH/2)
    xchng = int(rnd.randint(4,10))
    ychng = int(rnd.randint(4,10))
    while game:
        gd.fill(black)
        gd.fill(white,rect=[DspW/2,0,10,DspH])
        pg.draw.rect(gd,blue,[0,ya,15,DspH/5])
        pg.draw.rect(gd,blue,[DspW-15,yb,15,DspH/5])
        pg.draw.circle(gd,red,[xc,yc],20)
        
        if ya+DspH/5 >DspH:
            ya = DspH- DspH/5-1
        if yb+DspH/5 >DspH:
            yb = DspH- DspH/5-1
        if ya<0:
            ya = 0
        if yb<0:
            yb = 0
        
        if xc+10> DspW-15:
            speed.append(1)
            spd = spd+int(len(speed)/4)
            if yc>yb-5 and yc<yb+5+DspH/10:
                xchng = -spd
                ychng = -int(rnd.randrange(5,10))
                pg.mixer.Sound.play(bounce)
            if yc>yb-5+DspH/10 and yc< yb+5+DspH/5:
                xchng = -spd
                ychng = int(rnd.randrange(5,10))
                pg.mixer.Sound.play(bounce)
            elif yc<yb-5 or yc> yb+5+DspH/10 :
                point1 +=1
                pg.mixer.Sound.play(out)
                gameloop(point1,point2)
                
        if xc<15:
            if yc>ya-5 and yc<ya+5+DspH/10:
                xchng = spd
                ychng = -int(rnd.randrange(5,10))
                pg.mixer.Sound.play(bounce)
            if yc>ya-5+DspH/10 and yc<ya+5+DspH/5:
                xchng = spd
                ychng = int(rnd.randrange(5,10))
                pg.mixer.Sound.play(bounce)
            elif  yc<ya-5 or yc> ya+5+DspH/10 :
                point2 +=1
                pg.mixer.Sound.play(out)
                gameloop(point1,point2)
                
                
        if yc<5:
            ychng = 10
        if yc+10 > DspH:
            ychng = -10

        
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key== pg.K_UP:
                    ybchng = -20
                if event.key == pg.K_DOWN:
                    ybchng = 20
                if event.key== pg.K_w:
                    yachng = -20
                if event.key == pg.K_s:
                    yachng = 20
                if event.key == pg.K_p:
                    pause()
            if event.type == pg.KEYUP:
                if event.key== pg.K_UP:
                    ybchng = 0
                if event.key == pg.K_DOWN:
                    ybchng = 0
                if event.key== pg.K_w:
                    yachng = 0
                if event.key == pg.K_s:
                    yachng = 0
                
        msg_to_scrn(str(point1),white,-200,-200,Size = 35)
        msg_to_scrn(str(point2),white,-200,200,Size = 35)
        if point1>9:
            won('player1')
        if point2>9:
            won('player2')
        ya += yachng
        yb += ybchng
        xc += xchng
        yc += ychng
        clock.tick(30)
        pg.display.update()
start()
