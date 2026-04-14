import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img, True, False)#練習8
    kk_img = pg.image.load("fig/3.png")#練習３
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    screen.blit(kk_img, kk_rct)
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        a,b = 0,0
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            a,b=0,-1
        if key_lst[pg.K_DOWN]:
            a,b=0,1
        if key_lst[pg.K_LEFT]:
            a,b=-1,0
        if key_lst[pg.K_RIGHT]:
            a,b=2,0
        kk_rct.move_ip(a-1, b)

        x = tmr%3200 #練習５
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img, [-x + 1600, 0])
        screen.blit(bg_img,[-x + 3200, 0])
        screen.blit(kk_img, kk_rct)#練習４
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習６


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()