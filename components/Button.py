
class Button:
    def __init__(self, image_path, pygame):
        self.pygame = pygame
        self.image = self.pygame.image.load(image_path)
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect = None

    def render(self, screen, x, y):
        screen.blit(self.image, (x, y))
        self.rect = self.pygame.Rect(x, y, self.width, self.height)

class HandleButton(Button):
    def __init__(self, image_path, pygame, sound_manager, path, name_sound):
        super().__init__(image_path, pygame)
        self.pygame = pygame
        self.sound_manager = sound_manager
        self.path_sound = path
        self.name_sound = name_sound

    def handle_event(self, event, isEnable = True ):
        if event.type == self.pygame.MOUSEBUTTONDOWN:
            mouse_pos = self.pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if(isEnable):
                    self.sound_manager.load_sound(self.name_sound, self.path_sound)
                    self.sound_manager.play_sound(self.name_sound)

        if event.type == self.pygame.MOUSEBUTTONUP:
            mouse_pos = self.pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                return True
        return False

