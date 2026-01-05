import pygame
from src.config import ASSETS_DIR


class AssetManager:
    def __init__(self):
        self._cache_assets = {}

    def load_image(self, path):
        if path not in self._cache_assets:
            img = pygame.image.load(ASSETS_DIR / path).convert_alpha()
            self._cache_assets[path] = img
        return self._cache_assets[path]
