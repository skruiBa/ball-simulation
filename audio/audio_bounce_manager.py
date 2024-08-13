import pygame
from config.settings import AUDIO_VOLUME


class BounceAudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.bounce_sound = pygame.mixer.Sound("ball-bounce.wav")
        self.bounce_sound.set_volume(AUDIO_VOLUME)

    def play_bounce_sound(self):
        # Play the bounce sound effect
        self.bounce_sound.play()

    def set_volume(self, volume):
        self.bounce_sound.set_volume(volume)
