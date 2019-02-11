import pygame


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        #调用父类的初始方法
        super().__init__()
        #定义对象的属性
        self.image = pygame.image.load(image_name) # 读取图像地址
        self.rect = self.image.get_rect() # 图像位置、获取图像尺寸
        self.speed = speed

    def update(self):
        #在屏幕的垂直方向移动
        self.rect.y += self.speed



pygame.init()
# 创建窗口
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

