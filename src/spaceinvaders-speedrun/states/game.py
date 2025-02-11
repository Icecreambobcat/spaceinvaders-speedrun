import pathlib, os, sys
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
from lib import GameState, object
from pathlib import Path


class Game(GameState):
    bg: Surface
    screen: Surface
    menu_text: List[Tuple[Surface, Rect]]
    clock: time.Clock
    quit_call: Callable
    conf: Dict
    path: Path
    fonts: Dict

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

        tmp = image.load(App.asset_path.joinpath("ingame_bg_tex.jpg"))
        self.bg = pg.transform.scale(
            tmp, (App.conf["screen"]["width"], App.conf["screen"]["height"])
        )
        del tmp

    def loop(self) -> bool:
        return False

    def cleanup(self) -> None:
        pass

    def render(self) -> None:
        pass

    def enemy_gen(self) -> None:
        pass


class Player(object):
    pass


class Enemy(object):
    pass
