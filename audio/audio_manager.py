import pygame
from config.settings import AUDIO_VOLUME


class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.wall_hit_sound = pygame.mixer.Sound("music.wav")
        self.wall_hit_sound.set_volume(AUDIO_VOLUME)
        self.playing_now = False
        self.PAUSE_SOUND_EVENT = pygame.USEREVENT + 1

        # Start playing the sound and immediately pause it
        self.wall_hit_sound.play(loops=-1)  # Loop indefinitely
        pygame.mixer.pause()

    def play_sound_for_duration(self, duration):
        if not self.playing_now:
            pygame.mixer.unpause()
            self.playing_now = True
            pygame.time.set_timer(self.PAUSE_SOUND_EVENT, int(duration))

    def pause_sound(self):
        if self.playing_now:
            pygame.mixer.pause()
            self.playing_now = False

    def set_volume(self, volume):
        self.wall_hit_sound.set_volume(volume)

    def handle_events(self, event):
        if event.type == self.PAUSE_SOUND_EVENT:
            self.pause_sound()
            pygame.time.set_timer(self.PAUSE_SOUND_EVENT,
                                  0)  # Cancel the timer
