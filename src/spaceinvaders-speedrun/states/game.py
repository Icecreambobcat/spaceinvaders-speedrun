import pathlib, os, sys
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

from lib import GameState


class Game(GameState):
    def loop(self) -> bool:
        return False

    def cleanup(self) -> None:
        pass
