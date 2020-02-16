
import pygame as pg
import numpy as np
from libs.pooling.dop_pool import StaticListPool
from libs.utility.classes import Position, Color
from libs.gui.base_classes import GUI_STATIC


class Bullets():
    """Class that holds all default bullets"""
    def __init__(self, max_bullets: int):
        self.pool = StaticListPool()
        self.max_bullets = max_bullets
        self.objects = np.zeros((max_bullets, 4), dtype=float)
        self.active = np.zeros(max_bullets, dtype=bool)

        # Track amount of bullets in list
        self._bullets_created = 0

    def add(self, x, y, angle, speed):
        pooled_index = self.pool.get_object()
        if pooled_index is not None:
            index = pooled_index
        else:
            index = self._bullets_created
        
            # Add one to bullet counter
            self._bullets_created += 1

        if index >= self.max_bullets:
            raise Exception("Lol maximum reached, wat nao?")

        self.active[index] = True
        self.objects[index] = x, y, angle, speed

    def remove(self, index):
        self.pool.add(index)
        self.active[index] = False

    def _check_out_of_bounds(self, x, y):
        # Get playing area size, screen pixels(???)
        # Check if bullet is out of screen
        # Return True if bullet still on screen
        return True

    def update_bullet(self, x, y, angle, speed):
        # Do movement calculations for each bullet
        pos = Position(x, y).get_coords_to_distance_and_angle(speed, angle)
        return pos.x, pos.y, angle, speed

    def update(self):
        for i in range(0, self._bullets_created):
            if not self.active[i]:
                continue

            # Get bullet details
            x, y, x_spd, y_spd = self.update_bullet(*self.objects[i])

            # Check if bullet should exist
            if not self._check_out_of_bounds(x, y):
                return self.remove(i)

            # Set values updated values back to array
            self.objects[i] = x, y, x_spd, y_spd

            # Draw bullet
            pg.draw.rect(
                GUI_STATIC.active_screen,
                Color.red.as_tuple,
                (int(x), int(y), 5, 5)
            )


class HomingBullets(Bullets):
    def __init__(self, target: object, turning_rate: float, max_bullets: int):
        self.target = target
        self.turning_rate = turning_rate
        self.super().__init__(max_bullets)

    def update_bullet(self, x, y, angle, speed):
        # Calculate angle to target
        angle_to_target = 123  # TODO

        if angle_to_target != angle:
            # Turn bullet towards target by amount of turning rate
            angle += self.turning_rate

        # Run basic movement logic from parent class
        return super().update_bullet(x, y, angle, speed)
