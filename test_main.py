#import pygame
from main import Pong


def test_main():
    for (width, height) in [(600, 400), (800, 600), (1200, 800)]:
        Pong(width, height)
