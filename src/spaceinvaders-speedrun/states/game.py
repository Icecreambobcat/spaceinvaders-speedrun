import pathlib, os, sys, asyncio
from abc import abstractmethod, ABC
from typing import Never
import pygame as pg
from pygame import (
    color,
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
    font72: font.Font
    font32: font.Font
    font24: font.Font
    font12: font.Font
    bg: Surface

    def __init__(self) -> None:
        from main import App

        self.font72 = App.font72
        self.font32 = App.font32
        self.font24 = App.font24
        self.font12 = App.font12

        tmp = image.load(App.asset_path.joinpath("ingame_bg_tex.jpg"))
        self.bg = pg.transform.scale(
            tmp, (App.conf["screen"]["width"], App.conf["screen"]["height"])
        )
        del tmp

    def loop(self) -> bool:
        return False

    async def cleanup(self) -> None:
        pass

    def render(self) -> None:
        pass

    def enemy_gen(self) -> None:
        pass


class Player(object):
    pass


class Enemy(object):
    pass
