class BaseState:
    def __init__(self, game):
        self.game = game

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def cleanup(self):
        pass