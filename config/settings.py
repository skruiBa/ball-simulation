
# Screen dimensions
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "BALL SIMULATION"

# Circle
CIRCLE_WIDTH = SCREEN_WIDTH
CIRCLE_HEIGHT = SCREEN_HEIGHT
CIRCLE_RADIUS = SCREEN_WIDTH // 2.1
CIRCLE_THICKNESS = 12


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
RANDOM_BLUE = (72, 74, 107)

# Color palette
BEIGE = (254, 250, 224)
DARK_BEIGE = (250, 237, 206)
SAGE = (204, 213, 174)
LIGHT_SAGE = (224, 229, 182)

# List of all vibrant, colorful colors
colors = [
    RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET, RED
]
# colors = [PINK]

colors_lenght = len(colors) - 1

# Physics constants
SPEED = 5  # Start speed
REFLECTION_FACTOR = 2
COOLDOWN_TIME = 10
FPS = 120
GRAVITY = 0.4
FRICTION = 1.00

# Trail
TRAIL_ALPHA = 20  # RGB alpha (max = 255, min = 0)
TRAIL_DURATION = 5  # How many trails shown on screen at once
TRAIL_SIZE = 1  # Divider variable (default = 1) (half = 2)

# Audio
SOUND_DURATION = 526  # Measured in ms
AUDIO_VOLUME = 0
AUDIO_TYPE = "effect"  # music or effect
AUDIO_NAME = "goofy-bounce.wav"
AUDIO_NAME_2 = "goofy-bounce_2.wav"

# Ball
BALL_RADIUS = 5
BALL_COLOR = colors[0]
BALL_OUTLINE = 2  # outline width in pixels (no outline = 0)
BALL_OUTLINE_COLOR = SAGE


LABEL_LOCATION_X = SCREEN_WIDTH / 3
LABEL_LOCATION_Y = SCREEN_HEIGHT / 6.5
