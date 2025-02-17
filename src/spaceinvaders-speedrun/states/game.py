import pathlib, os, sys
from random import randrange
from abc import abstractmethod, ABC
from typing import Callable, Dict, List, Never, Tuple
import pygame as pg
from pygame import (
    Color,
    display,
    event,
    font,
    image,
    key,
    mouse,
    mixer,
    Rect,
    sprite,
    Surface,
    time,
)

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))
from lib import GameState, GameSprite
from pathlib import Path


class Player(GameSprite):
    x: int
    y: int
    hp: int

    @property
    def position(self) -> tuple[int, int]:
        return (0, 0)

    @property
    def image(self) -> Surface:
        return Surface((0, 0))

    @property
    def rect(self) -> Rect:
        return Rect(0, 0, 0, 0)

    @property
    def health(self) -> int:
        return self.hp


class Enemy(GameSprite):
    x: int
    y: int
    row: int
    kind: int
    hp: int

    def __init__(self, row: int) -> None:
        self.row = row
        self.kind = randrange(3)

    @property
    def position(self) -> tuple[int, int]:
        return (0, 0)

    @property
    def image(self) -> Surface:
        return Surface((0, 0))

    @property
    def rect(self) -> Rect:
        return Rect(0, 0, 0, 0)

    @property
    def health(self) -> int:
        return self.hp


class Game(GameState):
    bg: Surface
    screen: Surface
    menu_text: List[Tuple[Surface, Rect]]
    clock: time.Clock
    quit_call: Callable
    conf: Dict
    path: Path
    fonts: Dict
    player: Player
    enemies: List[Enemy]
    groups: Dict[str, sprite.Group]

    def __init__(
        self,
        screen: Surface,
        clock: time.Clock,
        path: Path,
        conf: Dict,
        fonts: Dict[str, font.Font],
    ) -> None:
        from main import App

        self.path = path
        self.screen = screen
        self.clock = clock
        self.conf = conf
        self.fonts = fonts
        self.quit_call = App.quit_app
        self.player = Player()
        self.groups = {
            "enemy_0": sprite.Group(),
            "enemy_1": sprite.Group(),
            "enemy_2": sprite.Group(),
            "player": sprite.Group(),
            "player_bullets": sprite.Group(),
            "enemy_bullets": sprite.Group(),
        }

        tmp = image.load(App.asset_path.joinpath("ingame_bg_tex.jpg"))
        self.bg = pg.transform.scale(
            tmp, (App.conf["screen"]["width"], App.conf["screen"]["height"])
        )
        del tmp

    def loop(self) -> bool:
        self.enemy_gen()

        running = True
        while running:
            self.render()
            display.flip()
            self.clock.tick(120)

        self.cleanup()
        return False

    def cleanup(self) -> None:
        for e in self.enemies:
            e.kill()
        self.enemies = []
        self.screen.fill((0, 0, 0))
        display.flip()

    def render(self) -> None:
        self.screen.blit(self.bg, (0, 0))

    def enemy_gen(self) -> None:
        """
        Generates 3 rows of enemies of a random type
        """
        for i in range(3):
            for j in range(10):
                _ = j
                self.enemies.append(Enemy(i))

        for e in self.enemies:
            self.groups[f"enemy_{e.row}"].add(e)

    def get_keys(self) -> list:
        # this needs a different implementation than the menu; we need to detectect held keys
        return []
