
import pygame as pg
import numpy as np
from libs.pooling.dop_pool import StaticListPool
from libs.utility.classes import Position, Color
from libs.gui.base_classes import GUI_STATIC

from Riku.game_assets import GameSettings


class Bullets():
    """Class that holds all default bullets"""
    MAX_DIST_FROM_BOUNDS = 100

    def __init__(self, max_bullets: int, speed: float):
        self.pool = StaticListPool()
        self.max_bullets = max_bullets
        self.speed = speed
        self.objects = np.zeros((max_bullets, 3), dtype=float)
        self.active = np.zeros(max_bullets, dtype=bool)

        # Track amount of bullets in list
        self._bullets_created = 0

    def add(self, x, y, angle):
        pooled_index = self.pool.get_object()
        if pooled_index is not None:
            index = pooled_index
            print("Got pooled index:", pooled_index)
        else:
            index = self._bullets_created
        
            # Add one to bullet counter
            self._bullets_created += 1

        if index >= self.max_bullets:
            # Maximum amount of bullets reached, dont create a new one
            self._bullets_created = self.max_bullets
            return

        self.active[index] = True
        self.objects[index] = x, y, angle

    def remove(self, index):
        self.pool.add(index)
        self.active[index] = False
        print("Removed index:", index)

    def _check_bullet_collision(self, x, y, angle):
        # Check if bullet collider overlaps with target colliders
        return False

    def _check_out_of_bounds(self, x, y):
        # Get screen size in pixels
        width, height = GameSettings.screen_size()

        # Check if bullet is out of screen
        if x < - self.MAX_DIST_FROM_BOUNDS or y < - self.MAX_DIST_FROM_BOUNDS:
            return True
        elif x > width + self.MAX_DIST_FROM_BOUNDS or y > height + self.MAX_DIST_FROM_BOUNDS:
            return True

        # Return False if bullet still on screen
        return False

    def check_bullet_validity(self, x, y, angle):
        if self._check_out_of_bounds(x, y):
            return False

        if self._check_bullet_collision(x, y, angle):
            return False
        return True

    def update_bullet(self, index):
        # Get bullet data
        x, y, angle = self.objects[index]

        # Do movement calculations for each bullet
        pos = Position(x, y).get_coords_to_distance_and_angle(self.speed, angle)

        return pos.x, pos.y, angle

    def set_update_data(self, index, x, y, angle):
        # Set values updated values back to array
        self.objects[index] = x, y, angle

    def update(self):
        for i in range(0, self._bullets_created):
            if not self.active[i]:
                continue

            # Update and bullet data (x, y, angle, speed [, properties of child class(es)])
            updated_data = self.update_bullet(i)

            # Check if bullet should exist
            if not self.check_bullet_validity(*updated_data):
                return self.remove(i)

            # Set bullet data
            self.set_update_data(i, *updated_data)

            # Draw bullet
            pg.draw.rect(
                GUI_STATIC.active_screen,
                Color.red.as_tuple,
                (updated_data[0], updated_data[1], 5, 5)
            )


class HomingBullets(Bullets):
    # Allow more distance out of bounds so the bullet can turn around and come back
    MAX_DIST_FROM_BOUNDS = 200

    def __init__(self, target: object, turning_rate: float, max_bullets: int):
        self.targets = np.zeros(max_bullets, dtype=int)
        self.turning_rate = turning_rate
        self.super().__init__(max_bullets)

    def update_bullet(self, index):
        # Get target position
        target_id = self.targets[i]
        if target_id == -1:
            # Current target is player, get player pos
            target_pos = (123, 321)
        else:
            # Target is enemy, fetch from enemy list with target_id
            target_pos = (321, 123)

        # Calculate angle to target
        angle_to_target = 123  # TODO

        if angle_to_target != angle:
            # Turn bullet towards target by amount of turning rate
            # TODO: This does not work at all
            angle += self.turning_rate

        # Set new angle into memory
        self.objects[index, 3] = angle

        # Run basic movement logic from parent class
        return super().update_bullet(index)
