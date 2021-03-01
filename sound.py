import pygame

class Sound:
    sounds = {'impact sound': pygame.mixer.Sound('resources/sounds/impact.mp3')}
    sound_on = True

    music_on = False
    pygame.mixer.music.load('resources/sounds/ambient.mp3')

    def toggle_music():
        print(Sound.music_on)
        if Sound.music_on:
            pygame.mixer.music.stop()
            Sound.music_on = False
        else:
            pygame.mixer.music.play(-1)
            Sound.music_on = True



    def play(sound_name):
        if Sound.sound_on:
            Sound.sounds[sound_name].play()
