import pygame
import random
import math
from config.settings import *  # Import everything from settings.py


class Shape:
    def __init__(self, x, y, radius, color, cooldown, gravity):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.hits = 1
        self.vx = SPEED
        self.vy = SPEED
        self.cooldown = cooldown
        self.gravity = gravity

    def update_position(self):
        raise NotImplementedError(
            "The method must be implemented by subclasses")

    def check_collision_with_circle(self):
        raise NotImplementedError(
            "The method must be implemented by subclasses")

    def check_collision_with_line(self, line_start, line_end, line_width):
        raise NotImplementedError(
            "The method must be implemented by subclasses")

    def draw_ball(self, screen):
        raise NotImplementedError(
            "The method must be implemented by subclasses")

    def draw_circle(self, screen, radius, color):
        raise NotImplementedError(
            "The method must be implemented by subclasses")

    def draw_ball_ghost(self, screen):
        raise NotImplementedError(
            "The method must be implemented by subclasses")
