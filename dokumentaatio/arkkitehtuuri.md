# Arkkitehtuurikuvaus

## Flappy Bird, alustava luokkakaavio

```mermaid
classDiagram
    GameManager --> Start
    GameManager --> Gameplay
    GameManager --> GroundMovement
    GameManager --> PipeMovement

    Gameplay --> GroundMovement
    Gameplay --> PipeMovement
    Gameplay --> Bird
    Start --> GroundMovement

    PipeMovement --> Pipe
    GroundMovement --> Ground

    class GameManager {
        screen_width: int
        screen_height: int
        start_phase: Start
        gameplay_phase: Gameplay
        ground_movement: GroundMovement
        pipe_movement: PipeMovement
        hover_speed: float
        hover_range: int
        hover_direction: int
        current_hover: int
        handle_events()
        handle_game_state()
    }

    class Start {
        screen_width: int
        screen_height: int
        start_message: image
        start_message_x: int
        start_message_y: int
        ground_movement: GroundMovement
        update()
    }

    class Gameplay {
        start_phase: Start
        screen_width: int
        screen_height: int
        bird: sprite
        wing_sound: sound
        ground_movement: GroundMovement
        pipe_movement: PipeMovement
        update()
        handle_bird_fly(dx: int, dy: int)
        handle_bird_fall()
    }

    class GroundMovement {
        screen_width: int
        screen_height: int
        ground_initial_x: int
        ground_initial_y: int
        speed: float
        ground: sprite
        update_ground()
    }

    class PipeMovement {
        screen_width: int
        screen_height: int
        pipe_initial_x: int
        speed: float
        pipe_difference: int
        top_pipe_y: int
        bottom_pipe_y: int
        pipe: sprite
        update_pipe()
    }

    class Pipe {
        image: image
        rect: rect
        speed: float
        screen_width: int
        screen_height: int
        update()
    }

    class Ground {
        image: image
        rect: rect
        speed: float
        screen_height: int
        update()
    }

    class Bird {
        sprites: list
        current_sprite: float
        image: image
        rect: rect
        velocity: float
        gravity: float
        angle: int
        update()
        _apply_gravity()
        fly(dx: int, dy: int)
        fall()
    }

```

## Huomioita

Luokkakaavio on alustava hahmotelma ja se tulee vielä muuttumaan tarkemmaksi pelin edistyessä ja projektin rakenteen muuttuessa.
