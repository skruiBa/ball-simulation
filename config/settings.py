
# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "BALL SIMULATION"

# Circle
CIRCLE_WIDTH = SCREEN_WIDTH
CIRCLE_HEIGHT = SCREEN_HEIGHT
CIRCLE_RADIUS = SCREEN_WIDTH // 2.1

# Vibrant, colorful colors
# Key Rainbow Colors (in order)
RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (148, 0, 211)


# Non-list colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (15, 11, 33)

# List of all vibrant, colorful colors
colors = [
    RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET, RED
]
# colors = [PINK]

colors_lenght = len(colors) - 1

# Physics constants
SPEED = 10  # Constant speed
REFLECTION_FACTOR = 2
COOLDOWN_TIME = 10
FPS = 80
GRAVITY = 1
FRICTION = 1
TRAIL_ALPHA = 50  # RGB alpha (max = 255, min = 0)
TRAIL_DURATION = 9999  # How many trails shown on screen at once
SOUND_DURATION = 500  # Measured in ms

# Ball
BALL_RADIUS = 30
BALL_COLOR = colors[0]

# Line coordinates
line_start = (400, 400)
line_end = (450, 450)
line_width = 10

# Audio
AUDIO_VOLUME = 0

LABEL_LOCATION_X = SCREEN_WIDTH / 3.5
LABEL_LOCATION_Y = SCREEN_HEIGHT / 3
