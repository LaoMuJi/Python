import pygame

pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((480,700))
# 加载图形数据
bg = pygame.image.load('./images/background.png')
# 绘制图像
screen.blit(bg,(0,0))


# 英雄飞机
hero = pygame.image.load('./images/me1.png')
screen.blit(hero,(200,500))



# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(100,500,102,126)





# 创建时钟对象
clock = pygame.time.Clock()

while True:
    clock.tick(60)

    # 捕获 事件监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    hero_rect.y -= 1
    if hero_rect.y < -126:
        hero_rect.y = 700
    #调用blit方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    # 更新屏幕显示
    pygame.display.update()

