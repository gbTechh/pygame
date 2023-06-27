import pygame
import pygame.mixer
from const import DEFAULT_SOUND_ENABLED, SPEED_CHARACTER


class Configuration:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Configuration, cls).__new__(cls)
            cls._instance.sound_enabled = True
            cls._instance.jump_key = pygame.K_SPACE
            cls._instance.move_key = pygame.K_RIGHT
            cls._instance.move_left = pygame.K_a
            cls._instance.move_right = pygame.K_d
            cls._instance.attack_key = pygame.MOUSEBUTTONDOWN
            cls._instance.unattack_key = pygame.MOUSEBUTTONUP
            cls._instance.fly = pygame.K_w
            cls._instance.speed_character = SPEED_CHARACTER
            cls._instance.observers = []

        return cls._instance

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.configuration_changed()

    def set_sound_enabled(self, enabled):
        self.sound_enabled = enabled
        self.notify_observers()

    def set_jump_key(self, key):
        self.jump_key = key
        self.notify_observers()

    def set_move_key(self, key):
        self.move_key = key
        self.notify_observers()



class SoundManager:

    sound = ''
    
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}

    def load_sound(self, sound_name, sound_path):
        self.sound = pygame.mixer.Sound(sound_path)        
        self.sounds[sound_name] = self.sound

    def play_sound(self, sound_name, loop = 0):
        isSounding = pygame.mixer.Channel(0).get_busy()
        sound = self.sounds.get(sound_name)
        if sound:
            sound.play(loop)
        

    def stop_sound(self, sound_name):
        sound = self.sounds.get(sound_name)
        if sound:
            sound.stop()

    def set_sound_volume(self, sound_name, volume):
        sound = self.sounds.get(sound_name)
        if sound:
            sound.set_volume(volume)
    def unload_sound(self, sound_name):
        sound = self.sounds.get(sound_name)
        if sound:
            sound.stop()
            del self.sounds[sound_name]