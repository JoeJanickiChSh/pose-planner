import pygame as pg
import sys
pg.init()

FONT = pg.font.Font(None, 32)

field = pg.image.load('field.png')

pg.display.set_caption('Pose Planner')
d = pg.display.set_mode(field.get_size())

robot_size = 0.6604
pixel_scale = 0.02027676595

robot_surf = pg.Surface(
    (
        int(robot_size / pixel_scale),
    )*2
    ,pg.SRCALPHA)
robot_surf.fill((255,0,255))

pg.draw.rect(robot_surf, (0,255,0), (robot_surf.get_width()//2, robot_surf.get_height()//2, robot_surf.get_width()//2, 2))

def draw_robot(x,y,angle):
    pos = (
        int(y/pixel_scale), int(x/pixel_scale)
    )
    rotated = pg.transform.rotate(robot_surf, angle)
    d.blit(rotated, (
        pos[0] - (rotated.get_width()//2),
        d.get_height() - pos[1] - (rotated.get_height()//2),
    ))

robot_x = 2
robot_y = 2
robot_angle = 0

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit(0)

    rel_x, rel_y = pg.mouse.get_rel()

    if pg.mouse.get_pressed()[0]:
        robot_y += rel_x / 100
        robot_x -= rel_y / 100
    elif pg.mouse.get_pressed()[2]:
        robot_angle -= rel_x
    d.blit(field, (0,0))

    draw_robot(robot_x, robot_y, robot_angle)

    d.blit(FONT.render(f'X: {round(robot_x,3)}, Y: {round(robot_y,3)}, ANGLE: {round(robot_angle,2)}',True, (255,255,255)), (25,10))


    pg.display.update()
