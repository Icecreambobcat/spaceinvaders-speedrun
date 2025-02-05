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


class App:
    ctx: str
    screen: Surface
    clock: time.Clock
    font72: font.Font
    font32: font.Font
    font24: font.Font
    font12: font.Font
    conf: dict
    states: dict[str, GameState]

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
        App.screen = display.set_mode(
            size=(App.conf["screen"]["width"], App.conf["screen"]["height"]), vsync=1
        )
        App.clock = time.Clock()
        menu = Menu()
        game = Game()
        App.states = {
            "Menu": menu,
            "Game": game,
        }
        App.ctx = "Menu"

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
                    pass

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
