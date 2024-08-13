import pygame
import random
import math
from config.settings import *  # Import everything from settings.py
from shapes.shape import Shape


class Ball(Shape):
    def __init__(self, x, y, radius, color, cooldown, gravity):
        super().__init__(x, y, radius, color, cooldown, gravity)

    def update_position(self):
        # Update position
        self.x += self.vx
        self.y += self.vy

        # Apply gravity to vertical
        self.vy += self.gravity

        # Add friction
        self.vx *= FRICTION
        self.vy *= FRICTION
        # print("{:.2f}, {:.2f}".format(self.x, self.y))

        if self.cooldown > 0:
            self.cooldown -= 1

    def check_collision_with_circle(self, circle_radius):
        # Center of the circle
        center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        # Distance from ball to center of circle
        dist_to_center = math.sqrt(
            (self.x - center_x) ** 2 + (self.y - center_y) ** 2)

        # Check if the ball is inside the circle
        is_inside = dist_to_center + self.radius > circle_radius
        if is_inside:
            # Calculate angle of incidence
            angle = math.atan2(self.y - center_y, self.x - center_x)

            # Set ball's position on the edge of the circle
            self.x = center_x + math.cos(angle) * (circle_radius - self.radius)
            self.y = center_y + math.sin(angle) * (circle_radius - self.radius)
            self.x += 0.03  # For chaos theory

            # Reflect the velocity based on the angle
            normal_x = math.cos(angle)
            normal_y = math.sin(angle)
            dot_product = self.vx * normal_x + self.vy * normal_y
            self.vx -= REFLECTION_FACTOR * dot_product * normal_x
            self.vy -= REFLECTION_FACTOR * dot_product * normal_y

            # other

            # Register hit only if cooldown is complete
            if self.cooldown == 0:
                self.hits += 1
                print(f"Ball hit the wall {self.hits} times")
                self.cooldown = COOLDOWN_TIME  # Reset cooldown timer

            return True
        else:
            return False

    def draw_ball(self, screen):
        pygame.draw.circle(screen, self.color,
                           (int(self.x), int(self.y)), self.radius)

    def draw_circle(self, screen, radius, color):
        center_x, center_y = CIRCLE_WIDTH // 2, CIRCLE_HEIGHT // 2
        pygame.draw.circle(
            screen, color, (center_x, center_y), radius, width=7)

    def draw_ball_ghost(self, screen, ghost_trails, trail_alpha):
        for i, ((x, y), color) in enumerate(ghost_trails):
            # Fade out effect: older trails are more transparent
            alpha = trail_alpha - int(trail_alpha * (i / len(ghost_trails)))
            ghost_color = (color[0], color[1], color[2], alpha)
            ghost_surface = pygame.Surface(
                (2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
            pygame.draw.circle(ghost_surface, ghost_color,
                               (self.radius, self.radius), self.radius)
            screen.blit(ghost_surface, (x - self.radius, y - self.radius))
