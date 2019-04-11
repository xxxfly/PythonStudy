#coding=utf-8
import pygame
from pygame.locals import *
import time
import random

"""飞机基类"""
class BasePlan(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x=x
        self.y=y
        self.image=pygame.image.load(image_name)
        self.screen=screen_temp
        self.bullet_list=[] #存储发射出去的子弹 引用
        self.exploreNum=0
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge(): #判断子弹是否越界
                self.bullet_list.remove(bullet)
            if bullet.judgeHit(self.x,self.y): #判断字段是否击中对方飞机
                self.bullet_list.remove(bullet)
            

"""子弹基类"""
class BaseBullet(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x=x
        self.y=y
        self.image=pygame.image.load(image_name)
        self.screen=screen_temp
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

"""玩家飞机类"""
class HeroPlan(BasePlan):
    def __init__(self,screen_temp):
        BasePlan.__init__(self,screen_temp,210,720,"./feiji/hero1.png")

    def move_left(self):
        self.x-=8
    def move_right(self):
        self.x+=8
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
    def explore(self):
        self.exploreNum+=1
        if self.exploreNum==2:
            self.image=pygame.image.load("./feiji/hero_blowup_n1.png")
        if self.exploreNum==3:
            self.image=pygame.image.load("./feiji/hero_blowup_n2.png")
        if self.exploreNum==4:
            self.image=pygame.image.load("./feiji/hero_blowup_n3.png")
        if self.exploreNum==5:
            self.image=pygame.image.load("./feiji/hero_blowup_n4.png")
            self.exploreNum=0

"""子弹类"""
class Bullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+40,y-20,"./feiji/bullet.png")
    def move(self):
        self.y-=8
    def judge(self):
        if self.y<0:
            return True
        else:
            return False
    def judgeHit(self,x,y):
        if self.x>x and self.x<x+51 and self.y>y and self.y<y+39:
            return True
        else:
            return False                   

"""敌机类"""
class EnemyPlan(BasePlan):
    def __init__(self,screen_temp):
        BasePlan.__init__(self,screen_temp,0,0,"./feiji/enemy0.png")#super()        
        self.direction='right'

    #敌机左右移动
    def move(self):
        if self.direction=='right':
            self.x+=2
        if self.direction=='left':
            self.x-=2

        if self.x>430:
            self.direction='left'
        elif self.x<0:
            self.direction='right'

    def fire(self):
        random_num=random.randint(1,100)
        if random_num==12 or random_num==20:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))


"""敌机子弹类"""
class EnemyBullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+25,y+40,"./feiji/bullet1.png")
    def move(self):
        self.y+=2
    def judge(self):
        if self.y>852:
            return True
        else:
            return False
    def judgeHit(self,x,y):
        if self.x>x and self.x<x+100 and self.y>y and self.y<y+124:
            return True
        else:
            return False

"""键盘事件"""
def key_control(hero_temp):
    #获取事件，比如按键等
    for event in pygame.event.get():
            
        #判断是否点击了退出按钮
        if event.type==QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()
            elif event.key==K_b:
                hero_temp.explore()

'''
    1.搭建界面，主要完成窗口和背景图片
'''
def main():

    #1.创建一个窗口，用来显示内容
    screen=pygame.display.set_mode((480,852),0,32)

    #2.创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")

    #3.创建一个飞机图图片
    hero=HeroPlan(screen)
    

    #创建一个敌机
    enemy=EnemyPlan(screen)

    #图片放到窗口中显示
    while True:
        #设定需要显示的背景图
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        key_control(hero)
       
        #更新需要显示的内容
        pygame.display.update()

        time.sleep(0.01)


if __name__ == '__main__':
    main()