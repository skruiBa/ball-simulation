import pygame


class BounceAudioManager:
    def __init__(self, audio_volume, audio_type, audio_name, audio_name_2):
        pygame.mixer.init()
        if audio_type == "music":
            self.bounce_sound = pygame.mixer.Sound(audio_name)
            self.PAUSE_SOUND_EVENT = pygame.USEREVENT + 1
            self.bounce_sound.play(loops=-1)  # Loop indefinitely
            pygame.mixer.pause()
        elif audio_type == "effect":
            self.bounce_sound = pygame.mixer.Sound(audio_name)
            self.bounce_sound_2 = pygame.mixer.Sound(audio_name_2)
            self.bounce_sound_2.set_volume(audio_volume)
            self.bounce_sound_switcher = 0

        self.bounce_sound.set_volume(audio_volume)

    """ For sound effect """

    def play_bounce_effect(self, duration):
        # Play the bounce sound effect
        if self.bounce_sound_switcher == 0:
            self.bounce_sound.play()
            self.bounce_sound_switcher = 1
        elif self.bounce_sound_switcher == 1:
            self.bounce_sound_2.play()
            self.bounce_sound_switcher = 0

    """ For music """

    def play_bounce_music(self, duration):
        pygame.mixer.unpause()
        self.playing_now = True
        pygame.time.set_timer(self.PAUSE_SOUND_EVENT, int(duration))

    def pause_sound(self):
        pygame.mixer.pause()

    def handle_events(self, event):
        if event.type == self.PAUSE_SOUND_EVENT:
            self.pause_sound()
            pygame.time.set_timer(self.PAUSE_SOUND_EVENT,
                                  0)  # Cancel the timer

    """ Set volume """

    def set_volume(self, volume):
        self.bounce_sound.set_volume(volume)
