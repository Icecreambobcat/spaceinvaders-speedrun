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


class GameState(ABC):
    @abstractmethod
    def loop(self) -> bool:
        pass

    @abstractmethod
    def cleanup(self) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass


class GameSprite(ABC, sprite.Sprite):
    """
    Defines the basic structure of ingame sprite objects
    """

    @property
    @abstractmethod
    def position(self) -> tuple[int, int]:
        pass

    @property
    @abstractmethod
    def image(self) -> Surface:
        pass

    @property
    @abstractmethod
    def rect(self) -> Rect:
        pass

    @property
    @abstractmethod
    def health(self) -> int:
        pass
