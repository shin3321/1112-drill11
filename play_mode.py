import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


    global  balls
    balls = [Ball(random.randint(100, 1600-100), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)
    game_world.add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)

    global zombie
    zombie = Zombie()
    game_world.add_object(zombie, 1)
    game_world.add_collision_pair('boy:zombie', boy, None)
    game_world.add_collision_pair('boy:zombie', None, zombie)

    game_world.add_collision_pair('ball:zombie', zombie, None)
    for ball in balls:
        game_world.add_collision_pair('ball:zombie', None, ball)

def finish():
    game_world.clear()
    pass

def handle_collisions():
    for group, pairs in game_world.collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if game_world.collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)

def update():
    game_world.update()
    handle_collisions()
    # for ball in balls:
    #     if game_world.collide(boy, ball):
    #         print('COLLISION boy:ball')
    #         boy.ball_count += 1
    #         game_world.remove_object(ball)
    #         balls.remove(ball)
    # fill here



def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

