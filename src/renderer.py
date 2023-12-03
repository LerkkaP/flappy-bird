import pygame
from utils.asset_loader import AssetLoader


class Renderer:
    def __init__(self, display, screen_width, screen_height, game_manager):
        self.display = display
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_manager = game_manager

    def render_background(self):
        background_image = AssetLoader.load_image(
            "world", "background-day.png")
        background_image = pygame.transform.scale(
            background_image, (self.screen_width, self.screen_height))

        self.display.blit(
            background_image,
            (0, 0)
        )

    def render_phase(self):
        if self.game_manager.game_phase == "start":
            self.game_manager.start_phase.ground_movement.ground.draw(
                self.display)

            hover_offset_y = self.game_manager.start_phase.start_message_y + \
                self.game_manager.start_phase.current_hover

            self.display.blit(
                self.game_manager.start_phase.start_message,
                (self.game_manager.start_phase.start_message_x, hover_offset_y)
            )

        elif self.game_manager.game_phase == "gameplay":

            self.game_manager.gameplay_phase.pipe_movement.pipe.draw(
                self.display)
            self.game_manager.gameplay_phase.ground_movement.ground.draw(
                self.display)

            self.game_manager.gameplay_phase.bird.draw(self.display)

            current_score = self.game_manager.gameplay_phase.get_current_score()
            self._render_score(current_score)

    def _render_score(self, score):
            scores = [i for i in str(score)]

            for i in range(len(scores)):
                image = AssetLoader.load_image("score", f"{scores[i]}.png")
                self.display.blit(
                image,
                ((self.screen_width - image.get_width()) // 2 + i * 21, 50))
