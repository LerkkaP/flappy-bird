# Arkkitehtuurikuvaus

## Flappy Bird, alustava luokkakaavio

```mermaid
classDiagram
    GameManager --> Start
    GameManager --> Gameplay

    Gameplay --> GroundMovement
    Gameplay --> PipeMovement
    Gameplay --> Bird
    Start --> GroundMovement

    PipeMovement --> Pipe
    GroundMovement --> Ground

    class GameManager {
        + start_phase: Start
        + gameplay_phase: Gameplay
        + game_phase: start
        + handle_events()
        - handle_gameplay_events(event)
        - start_gameplay()
        + handle_game_state()
        - update_gameplay()
    }

    class Start {
        - screen_width: int
        - screen_height: int
        + ground_movement: GroundMovement
        - init_start_message()
        - init_hover_attributes()
        + updated()
        + handle_text_hover()
    }

    class Gameplay {
        - screen_height: int
        + bird: pygame.sprite.Group()
        - sound_manager: SoundManager()
        + ground_movement: GroundMovement
        + pipe_movement: PipeMovement
        + pause: bool
        + score: int
        + update()
        - get_score()
        + get_current_score()
        + handle_bird_fly(dx: int, dy: int)
        + handle_bird_fall()
        + handle_collision()
    }

    class GroundMovement {
        - screen_width: int
        - ground_initial_x: int
        - ground_initial_y: int
        - speed: float
        + ground: sprite
        + update_ground()
        + check_collision()
    }

    class PipeMovement {
        - screen_width: int
        - pipe_initial_x: int
        - speed: float
        - pipe_difference: int
        - top_pipe_y: int
        - bottom_pipe_y: int
        + pipe: pygame.sprite.Group()
        - score: int
        - initialize_pipes()
        - add_pipe()
        + update_pipe()
        + update_score()
        + return_score()
        + check_collision()
    }

    class Pipe {
        + image: image
        + rect: rect
        - speed: float
        + update()
    }

    class Ground {
        + image: image
        + rect: rect
        - speed: float
        + update()
    }

    class Bird {
        + sprites: list[image]
        + current_sprite: float
        + image: image
        + rect: rect
        + rect.x = x
        + rect.y = y
        - velocity: float
        - gravity: float
        - angle: int
        + update()
        - apply_gravity()
        - rotate_bird()
        + fly(dx: int, dy: int)
        + fall()
    }

```

## Huomioita

Luokkakaavio on alustava hahmotelma ja se tulee vielä muuttumaan tarkemmaksi pelin edistyessä ja projektin rakenteen muuttuessa.
