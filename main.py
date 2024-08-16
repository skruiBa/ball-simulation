import pygame
import sys
from config.settings import *  # Import everything from settings.py
from shapes.ball import Ball
from audio.audio_bounce_manager import BounceAudioManager
from utils.functions import *


def main():
    # Init
    pygame.init()
    pygame.font.init()
    bounce_audio_manager = BounceAudioManager(
        AUDIO_VOLUME, AUDIO_TYPE, AUDIO_NAME, AUDIO_NAME_2)

    # Init font
    font = pygame.font.Font('comfortaa.ttf', 50)

    # Setup the screen (Do this once)
    screen = pygame.display.set_mode(
        (SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.display.set_caption("Ball Simulation")

    # Create a ball instance
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                BALL_RADIUS, BALL_COLOR, COOLDOWN_TIME, GRAVITY)
    shapes = [ball]

    # List to store ghost trail positions
    ghost_trails = []

    # Generate rainbow colors
    rainbow_colors = generate_rainbow_colors()
    num_colors = len(rainbow_colors)

    # Main loop
    clock = pygame.time.Clock()
    running = True

    # Timer for color change
    color_change_timer = 0
    color_index = 0

    # Local circle radius
    circle_radius = CIRCLE_RADIUS

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the timer
        color_change_timer += clock.get_time()

        # Change the ball color every 200 ms
        if color_change_timer >= 200:
            color_change_timer = 0
            ball.color = rainbow_colors[color_index]
            color_index = (color_index + 1) % num_colors

        # Clear the screen (keep this on the original screen)
        screen.fill(BEIGE)

        # Draw circle first
        ball.draw_circle(screen, circle_radius, SAGE, CIRCLE_THICKNESS)

        # Update ball position and check for collisions
        for i in shapes:
            i.update_position()

            # Add the current position to the ghost trail
            ghost_trails.append(((i.x, i.y), i.color))

            # Limit the ghost trail length
            if len(ghost_trails) > TRAIL_DURATION:
                ghost_trails.pop(0)

            # Draw the ball ghost trail after the circle, so it appears in front
            i.draw_ball_ghost(screen, ghost_trails, TRAIL_ALPHA, TRAIL_SIZE)

            # Draw the actual ball
            i.draw_ball(screen, BALL_OUTLINE, BALL_OUTLINE_COLOR)

            # Check collision with the circle boundary
            hit_wall = i.check_collision_with_circle(circle_radius)

            # Update text
            label_text = f"Ball size: {i.radius}"
            text_surface = render_text(label_text, font, BLACK)

            if hit_wall:
                # Play sound
                bounce_audio_manager.play_bounce_effect(SOUND_DURATION)
                # Make ball bigger on hit
                i.radius += 1.5
                # Update changed text
                label_text = f"Ball size: {i.radius}"
                text_surface = render_text(label_text, font, WHITE)
                # Make the play circle smaller
                # circle_radius -= 2

        # Display text
        screen.blit(text_surface, (LABEL_LOCATION_X, LABEL_LOCATION_Y))

        # ### Rotate the screen content by 90 degrees ###
        # rotated_screen = pygame.transform.rotate(screen, 90)

        # # Clear the actual display surface before blitting the rotated content
        # screen.fill(DARK_BLUE)

        # # Blit the rotated content to the screen and flip
        # screen.blit(rotated_screen, (0, 0))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
