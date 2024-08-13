from config.settings import *


# utils/functions.py

def interpolate_color(color1, color2, factor):
    """Interpolate between two colors."""
    r = round(color1[0] + (color2[0] - color1[0]) * factor)
    g = round(color1[1] + (color2[1] - color1[1]) * factor)
    b = round(color1[2] + (color2[2] - color1[2]) * factor)
    return (r, g, b)


def generate_rainbow_colors():
    key_colors = colors
    rainbow_colors = []
    colors_per_transition = 100 // (len(key_colors) - 1)

    for i in range(len(key_colors) - 1):
        for j in range(colors_per_transition):
            factor = j / colors_per_transition
            color = interpolate_color(key_colors[i], key_colors[i + 1], factor)
            rainbow_colors.append(color)

    # Ensure the last color is included
    rainbow_colors.append(key_colors[-1])

    return rainbow_colors


def render_text(text, font, color):
    return font.render(text, True, color)
