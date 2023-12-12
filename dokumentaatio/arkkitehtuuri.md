# Arkkitehtuurikuvaus

## Flappy Bird, alustava luokkakaavio

```mermaid
classDiagram
    GameManager --> Start
    GameManager --> Gameplay
    GameManager --> End

    Gameplay --> GroundMovement
    Gameplay --> PipeMovement
    Gameplay --> Bird
    Start --> GroundMovement

    PipeMovement --> Pipe
    GroundMovement --> Ground

    End --> TinyDB

    class GameManager {
        + start_phase: Start
        + gameplay_phase: Gameplay
        + end_phase: End
        + phase_manager: PhaseManager
        + score: Score()
        + handle_events()
        - handle_gameplay_events(event)
        - handle_start_events(event)
        - handle_gameplay_phase_events(event)
        - handle_end_events(event)
        - restart_game()
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
        + update()
        + handle_bird_fly(dx: int, dy: int)
        + handle_bird_fall()
        + handle_collision()
        + reset_bird()
    }

    class End {
        - screen_width: int
        + score: Score()
        - init_end_message()
        - init_restart_button()
        - init_statistics_button()
        - init_end_message()
        + handle_restart_click()
        + save_score_to_database()
        + get_highest_score_from_database()
    }

    class TinyDB {
        + save_score(score)
        + get_highest_score()
        + get_all_scores()
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
        - sound_manager: SoundManager()
        + pipe: pygame.sprite.Group()
        - score: Score()
        - initialize_pipes()
        - add_pipe()
        + update_pipe()
        + update_score()
        + check_collision()
        + reset_pipes()
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
        + reset_position()

    }

```

## Flappy Bird, Sekvenssikaaviot

### Pistemäärän päivittymisen logiikka

```mermaid
sequenceDiagram
    participant GameManager
    participant Gameplay
    participant PipeMovement
    participant Score

    GameManager->>Gameplay: update()
    Gameplay->>PipeMovement: update_score()
    PipeMovement->>Score: increment_score()

```

Luokka `Gamemanager` kutsuu `Gameplay`-luokan metodia `update`, joka sisällään kutsuu `PipeMovement`-luokan metodia `update_score`. Metodi käy läpi jokaisen putken sprite-objektin
ja jos putken vasemman reunan koordinaatti on yhtä suuri kuin linnun x-koordinaatti, se kutsuu `Score`-luokan metodia `increment_score`, joka lisää yhden pisteen kokonaispistemäärään. 

Pistemäärän päivittymisessä on tärkeää huomioida se, että pistemäärä päivittyy putkien liikkeeseen perustuen, eikä varsinaisesti liity lintuun vaikka se tältä vaikuttaakin.
Itse lintu ei pelissä liiku; sen x-koordinaatti pysyy vakiona. Liikkuvalla maalla ja putkilla luodaan illuusio ikään kuin lintu liikkuisi eteenpäin.

## Huomioita

Luokkakaavio on alustava hahmotelma ja se tulee vielä muuttumaan tarkemmaksi pelin edistyessä ja projektin rakenteen muuttuessa.
