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
from lib import GameState
from pathlib import Path


class Menu(GameState):
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

        img = image.load(self.path.joinpath("menu_bg_tex.jpg"))
        self.bg = pg.transform.scale(
            img, (self.conf["screen"]["width"], self.conf["screen"]["height"])
        )
        text_line_1 = self.fonts["72"].render(
            "The game you made me make", True, (255, 255, 255)
        )
        text_line_2 = self.fonts["24"].render(
            "<CR> to next, <ESC> to exit", True, (255, 255, 255)
        )
        text_line_3 = self.fonts["24"].render(
            "TODO: You (*･ω･)ﾉ", True, (255, 255, 255)
        )
        self.menu_text = [
            (
                text_line_1,
                text_line_1.get_rect(center=(self.conf["screen"]["width"] / 2, 100)),
            ),
            (
                text_line_2,
                text_line_2.get_rect(center=(self.conf["screen"]["width"] / 2, 175)),
            ),
            (
                text_line_3,
                text_line_3.get_rect(center=(self.conf["screen"]["width"] / 2, 250)),
            ),
        ]

    def loop(self) -> bool:
        running = True
        while running:
            self.render()
            keys = self.grab_input()

            for keypress in keys:
                if keypress.key == pg.K_RETURN:
                    return True
                elif keypress.key == pg.K_ESCAPE:
                    running = False

            display.flip()
            self.clock.tick(120)

        self.cleanup()
        return False

    # def loop(self) -> bool:
    #     quit = False
    #     while True:
    #         self.render()
    #         keys = self.grab_input()
    #         for keypress in keys:
    #             if keypress.key == pg.K_RETURN:
    #                 return True
    #             elif keypress.key == pg.K_ESCAPE:
    #                 quit = True
    #         if quit:
    #             self.cleanup()
    #             break
    #
    #         display.flip()
    #         self.clock.tick(120)
    #
    #     return False

    def cleanup(self) -> None:
        # kill all menu objects to ensure clean frame transition
        # placeholder implementation, will nuke if unnecessary
        pass

    def render(self) -> None:
        self.screen.blit(self.bg, (0, 0))
        for text in self.menu_text:
            self.screen.blit(text[0], text[1])

    def grab_input(self) -> list:
        # read key events and tell the loop to return true/false
        # nukes the other events because they're useless
        keys = event.get(pg.KEYDOWN)
        _ = event.get()
        return keys
