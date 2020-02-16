
import pygame as pg
import GameFunctions as gf
import numpy as np
from Riku.base_creatures import Creature
from libs.utility.input import Input
from Riku.bullets import Bullets


class Player(Creature):
    #MaxWalkSpeed
    MWS=3.5
    ACCEL=0.15

    def __init__(self, *args):
        super().__init__(*args)

        self.facing = [0, -1]
        self.shoot_tick_count = 0

        #tweakables
        self.shoot_speed = 2
        self.bullet_speed = 10
        self.bullets = Bullets(100, self.bullet_speed)

    def update(self):
        # Check user input
        change = [0, 0]
        shooting = 0
        if Input.key_pressed(pg.K_UP): change[1] -= 1
        if Input.key_pressed(pg.K_LEFT): change[0] -= 1
        if Input.key_pressed(pg.K_DOWN): change[1] += 1
        if Input.key_pressed(pg.K_RIGHT): change[0] += 1
        if Input.key_pressed(pg.K_SPACE): shooting = 1
                
        # Apply drag and change
        for i in [0,1]:
            if not change[i] and self.speed[i]:
                # change is zero but we still have speed
                if self.speed[i] < 0:
                    self.speed[i] += self.ACCEL
                    if self.speed[i] > 0:
                        self.speed[i] = 0
                else:
                    self.speed[i] -= self.ACCEL
                    if self.speed[i] < 0:
                        self.speed[i] = 0
            
            if change[i]:
                if abs(self.speed[i]) < self.MWS or not gf.csign(change[i], self.speed[i]):
                    # We have input and not max walk speed reached
                    if gf.csign(change[i], self.speed[i]):
                        self.speed[i] += self.ACCEL * change[i]
                        if abs(self.speed[i]) > self.MWS:
                            self.speed[i] = self.MWS * change[i]
                    else:
                        self.speed[i] += 2 * self.ACCEL * change[i]

                self.facing[i] = change[i]
            else:
                self.facing[i] = 0

        # Shoot if space pressed
        if shooting and self.shoot_tick_count <= 0:
            self.shoot(self.pos)
            self.shoot_tick_count = self.shoot_speed

        self.shoot_tick_count -= 1

        # This should be refactored somewhere else, so bullets get updated even if player dies
        # Needed if player has lives and can respawn back amongst the battle
        self.bullets.update()

        super().update()
   
    def shoot(self, pos):
        # Angle 180 because 0 is south
        self.bullets.add(pos[0], pos[1], 180)
