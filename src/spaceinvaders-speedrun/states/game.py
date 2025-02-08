import pathlib, os, sys
from abc import abstractmethod, ABC
from typing import Never
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

from lib import GameState, object


class Game(GameState):
    bg: Surface

    def __init__(self) -> None:
        from main import App

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
