import pygame

pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((480,700))
# 加载图形数据
bg = pygame.image.load('./images/background.png')
# 绘制图像
screen.blit(bg,(0,0))

# 英雄飞机
hero_rect = pygame.Rect(100,500,120,125)







pygame.quit()
