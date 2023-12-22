# Arkkitehtuurikuvaus

## Rakenne

Ohjelman yleinen rakenne käy ilmi alla olevasta pakkauskaaviosta:

<img src="kuvat/pakkauskaavio.png" width='500'>


Huomaa, että pakkauskaaviosta puuttuu sovelluksen kannalta keskeiset luokat, kuten `EventHandler` ja `GameManager`. Tarkemman kuvauksen pelilogiikasta löydät alempaa dokumentista.

## Pisteiden tallennus tietokantaan

```mermaid
sequenceDiagram
    participant Gameplay
    participant Score
    participant db

    Gameplay->>Gameplay: _handle_collision_environment()
    Gameplay->>Score: save_score_to_database()
    Score->>db: save_score(score)

```

Pelin pisteiden pysyväistallennuspaikkana käytetään `TinyDB` tietokantaa. Kun lintu törmää __maahan__ tai __putkiin__, kutsuu `Gameplay` luokka sisäisesti metodia `_handle_collision_environment`, jonka sisällä kutsutaan luokan `Score` metodia `save_score_to_database`. Kyseinen metodi taas kutsuu sisällään tietokannan funktiota `save_score`, joka tallentaa saadun pistemäärän tietokantaan.

`TinyDB`:n sijasta olisi tietokantana voinut käyttää esimerkiksi `SQLite` tietokantaa. `TinyDB` eroaa `SQLite`:stä siinä, että se on dokumenttitietokanta, kuten `MongoDB`, kun taas `SQLite` on relaatiotietokanta. `TinyDB` valittiin tähän projektiin `SQLite`:n sijaan sen vuoksi, koska se on erityisen yksinkertainen ottaa käyttöön ja sopii paremmin sovelluksiin, jotka eivät vaadi monimutkaista tiedon käsittelyä. Lisää `TinyDB`:stä voi lukea esimerkiksi [täältä](https://tinydb.readthedocs.io/en/latest/).

## Pelilogiikka
```mermaid
classDiagram
    GameManager --> Start
    GameManager --> Gameplay
    GameManager --> End
    GameManager --> EventHandler
    GameManager --> PhaseManager

    EventHandler --> Gameplay
    EventHandler --> End
    EventHandler --> Stats
    EventHandler --> PhaseManager
    EventHandler --> Score
    
    Gameplay --> GroundMovement
    Gameplay --> PipeMovement
    Gameplay --> Bird
    Gameplay --> PhaseManager
    Gameplay --> Score

    Start --> GroundMovement
    Stats --> TinyDB

    PipeMovement --> Pipe
    PipeMovement --> Score

    GroundMovement --> Ground

    Score --> TinyDB

    class GameManager {
        + start_phase: Start
        - gameplay_phase: Gameplay
        - end_phase: End
        - stats_phase: Stats
        - phase_manager: PhaseManager
        - score: Score
        - event_handler: EventHandler
        + score: Score
        + handle_events()
        + handle_game_state()
        - update_gameplay()
        + get_pipes()
        + get_ground()
        + get_bird()
        + get_end_message()
        + get_start_message()
    }

    class EventHandler {
        - phase_manager: PhaseManager
        - gameplay_phase: Gameplay
        - end_phase: End
        - stats_phase: Stats
        - score: Score
        + handle_events()
        - handle_quit_event(event)
        - handle_quit()
        - handle_game_events(event)
        - handle_start_events(event)
        - handle_gameplay_events(event)
        - handle_end_events(event)
        - restart_game()
    }

    class PhaseManager {
        - instance: PhaseManager
        - _phase: str
        + __new__()
        + set_phase(phase: str)
        + game_in_start()
        + game_in_gameplay()
        + game_in_end()
        + game_in_stats()
    }

    class Start {
        - screen_width: int
        - screen_height: int
        + ground_movement: GroundMovement
        + start_message: img
        + start_message_x: int
        + start_message_y: int
        + hover_direction: int
        + current_hover: int
        - init_start_message()
        - init_hover_attributes()
        + update()
        + handle_text_hover()
    }

    class Gameplay {
        - screen_height: int
        - screen_width: int
        + bird: pygame.sprite.Group
        - sound_manager: SoundManager
        + ground_movement: GroundMovement
        + pipe_movement: PipeMovement
        + phase_manager: PhaseManager
        - init_bird()
        - init_game_elements()
        + update()
        - update_ground()
        - update_pipes()
        + handle_bird_fly(dx: int, dy: int)
        + handle_bird_fall()
        + handle_collision()
        - handle_collision_environment
        + reset_bird()
    }

    class End {
        - screen_width: int
        + text: Text
        + restart_text
        + stats_text
        + end_message: img
        + end_message_x: int
        + end_message_y: int
        - init_end_message()
        + handle_restart_click(mouse_pos)
        + handle_statistics_click(mouse_pos)
    }

    class TinyDB {
        + save_score(score)
        + get_highest_score()
        + get_all_scores()
        + get_number_of_items()
        + get_list_of_scores()      
    }

    class Score {
        - score: int
        + increment_score()
        + get_score(): int
        + reset_score()
        + save_score_to_database()
    }

    class GroundMovement {
        - screen_width: int
        - ground_initial_x: int
        - ground_initial_y: int
        - speed: float
        + ground: sprite
        + update_ground()
        + check_collision(bird_group)
    }

    class PipeMovement {
        - screen_width: int
        - pipe_initial_x: int
        - speed: float
        - pipe_difference: int
        - top_pipe_y: int
        - bottom_pipe_y: int
        + pipe: pygame.sprite.Group()
        - score: Score
        - initialize_pipes()
        - add_pipe(x, y, is_top)
        + update_pipe()
        + update_score(sound_manager)
        + check_collision(bird_group)
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

    class Stats {
        + text: Text
        + handle_back_click(mouse_pos)
        - initialize_graph()
        - set_graph_properties(ax)
        - set_ticks(ax, ticks)
        - render_graph(fig)
        + draw_graph()
    }

```

Pelissä on karkeasti jaoteltuna __neljä__ eri vaihetta:

- __Aloitusvaihe__: Aloitusvaiheesta vastaa luokka `Start`.
- __Pelivaihe__: Pelin keskeisin vaihe, josta vastaa `Gameplay`-luokka. Tässä vaiheessa tapahtuu itse pelaaminen.
- __Loppuvaihe__: `End`-luokka vastaa pelin loppuvaiheesta, kun peli päättyy.
- __Tilastovaihe__: Tilastovaiheesta vastaa `Stats`-luokka.

`GameManager`-luokka toimii keskeisenä komponenttina, joka hallitsee pelin etenemistä ja vaiheiden välisiä siirtymiä. `EventHandler` taas vastaa pelin tapahtumien käsittelystä ja reagoi pelaajan toimiin. Myös __utils__-hakemistossa sijaitsevalla luokalla `PhaseManager` on tärkeä rooli, koska sen avulla voidaan tarkistaa missä vaiheessa peli on ja asettaa uusi vaihe tarvittaessa.

## Toiminnallisuudet

### Pistemäärän päivittyminen

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

## Kuvaajan luominen

```mermaid
sequenceDiagram
    participant StatsRenderer
    participant Stats
    participant db

    StatsRenderer->>Stats: draw_graph()
    Stats->>db: get_list_of_scores()
    Stats->>db: get_highest_score()
    Stats->>db: get_number_of_items()
    db-->>Stats: Scores data
    Stats->>Stats: _initialize_graph()_
    Stats->>Stats: _set_graph_properties()
    Stats->>Stats: _set_ticks()
    Stats->>Stats: _render_graph()
    Stats-->>StatsRenderer: Return rendered graph surface

```

`Stats`-luokka kommunikoi tietokannan kanssa saadakseen tarvittavat pistetiedot, jonka jälkeen se alustaa, asettaa ominaisuudet ja piirtää graafin Matplotlib-kirjaston avulla. Lopuksi se palauttaa piirretävän pinnan StatsRenderer-luokalle, joka piirtää graafin näytölle.

## Huomioita heikkouksista

Tällä hetkellä ohjelman rakenne vaikuttaa hieman monimutkaiselta. Vaikka tapahtumien käsittelyn erottaminen `GameManager`-luokasta oli askel oikeaan suuntaan – koska aiemmin kyseinen luokka oli hyvin massiivinen ja sisälsi paljon toiminnallisuuksia – tämä muutos teki rakenteesta hieman monimutkaisemman. Jatkokehityksen kannalta olisi hyödyllistä harkita luokkien vastuiden tarkempaa eriyttämistä ja riippuvuuksien hallintaa. Ainakin `PhaseManager`-luokan roolia voisi harkita tarkemmin, jotta se ei olisi niin vahvasti kytköksissä muihin luokkiin, mikä mahdollistaisi joustavamman ja paremmin hallitun pelivaiheiden käsittelyn


