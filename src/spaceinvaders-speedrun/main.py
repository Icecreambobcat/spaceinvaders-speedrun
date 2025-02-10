import pathlib, os, sys
from pathlib import Path
from abc import abstractmethod, ABC
from typing import Dict, Never
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

from lib import GameState


class App:
    ctx: str
    screen: Surface
    clock: time.Clock
    font72: font.Font
    font32: font.Font
    font24: font.Font
    font12: font.Font
    fonts: Dict[str, font.Font]
    conf: dict
    states: dict[str, GameState]
    asset_path: Path

    @staticmethod
    def init_game() -> None:
        """
        Initialise internal variables and pulls in configs from the config file
        """

        from conf import Conf
        from states.menu import Menu
        from states.game import Game

        pg.init()
        App.conf = Conf.configs
        App.asset_path = Path("src", "assets")
        App.screen = display.set_mode(
            size=(App.conf["screen"]["width"], App.conf["screen"]["height"]), vsync=1
        )
        App.clock = time.Clock()
        App.font72 = font.Font(
            App.asset_path.joinpath("JetBrainsMonoNerdFont-Regular.ttf"), 72
        )
        App.font32 = font.Font(
            App.asset_path.joinpath("JetBrainsMonoNerdFont-Regular.ttf"), 32
        )
        App.font24 = font.Font(
            App.asset_path.joinpath("JetBrainsMonoNerdFont-Regular.ttf"), 24
        )
        App.font12 = font.Font(
            App.asset_path.joinpath("JetBrainsMonoNerdFont-Regular.ttf"), 12
        )
        App.fonts = {
            "72": App.font72,
            "32": App.font32,
            "24": App.font24,
            "12": App.font12,
        }
        App.ctx = "Menu"
        App.states = {
            "Menu": Menu(App.screen, App.clock, App.asset_path, App.conf, App.fonts),
            # "Game": Game(),
        }

    @staticmethod
    def run_game() -> Never:
        """
        This is your game loop
        """

        ingame = True
        while ingame:
            match App.ctx:
                case "Menu":
                    out = App.states["Menu"].loop()
                    if out:
                        App.ctx = "Game"
                    else:
                        break
                case "Ingame":
                    out = App.states["Game"].loop()
                    if out:
                        App.ctx = "Game"
                    else:
                        App.ctx = "Menu"

            display.flip()
            App.clock.tick(120)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    App.quit_app()

        App.quit_app()

    @staticmethod
    def quit_app(*args) -> Never:
        """
        Calls cleanup and save functions before quitting
        if errors are passed then exit with the first error passed
        """

        if len(args) == 0:
            pg.quit()
            sys.exit(0)
        else:
            pg.quit()
            sys.exit(args[0])


def main() -> None:
    App.init_game()
    App.run_game()


if __name__ == "__main__":
    main()
