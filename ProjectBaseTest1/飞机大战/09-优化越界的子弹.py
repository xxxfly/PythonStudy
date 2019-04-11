#coding=utf-8
import pygame
from pygame.locals import *
import time


"""玩家飞机类"""
class HeroPlan(object):
    def __init__(self,screen_temp):
        self.hero_x=210
        self.hero_y=720
        self.image=pygame.image.load("./feiji/hero1.png")
        self.screen=screen_temp
        self.bullet_list=[] #存储发射出去的子弹 引用
    def display(self):
        self.screen.blit(self.image,(self.hero_x,self.hero_y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge(): #判断子弹是否越界
                self.bullet_list.remove(bullet)

    def move_left(self):
        self.hero_x-=6
    def move_right(self):
        self.hero_x+=6
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.hero_x,self.hero_y))

"""子弹类"""
class Bullet(object):
    def __init__(self,screen_temp,bullet_x,bullet_y):
        self.bullet_x=bullet_x+40
        self.bullet_y=bullet_y-20
        self.image=pygame.image.load("./feiji/bullet.png")
        self.screen=screen_temp
    def display(self):
        self.screen.blit(self.image,(self.bullet_x,self.bullet_y))
    def move(self):
        self.bullet_y-=8
    def judge(self):
        if self.bullet_y<0:
            return True
        else:
            return False
                        

"""敌机类"""
class EnemyPlan(object):
    def __init__(self,screen_temp):
        self.enemy_x=0
        self.enemy_y=0
        self.image=pygame.image.load("./feiji/enemy0.png")
        self.screen=screen_temp
        #self.bullet_list=[] #存储发射出去的子弹 引用
        self.direction='right'

    def display(self):
        self.screen.blit(self.image,(self.enemy_x,self.enemy_y))

        # for bullet in self.bullet_list:
        #     bullet.display()
        #     bullet.move()

    #敌机左右移动
    def move(self):
        if self.direction=='right':
            self.enemy_x+=2
        if self.direction=='left':
            self.enemy_x-=2

        if self.enemy_x>430:
            self.direction='left'
        elif self.enemy_x<0:
            self.direction='right'

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.enemy_x,self.enemy_y))

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
        key_control(hero)
       
        #更新需要显示的内容
        pygame.display.update()

        time.sleep(0.01)


if __name__ == '__main__':
    main()