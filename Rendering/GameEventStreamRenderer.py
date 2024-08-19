from typing import List
from pygame import Surface


class GameEventStreamRenderer:
    def __init__(self, screen: Surface):
        self.events: List[str] = []
        self.screen: Surface = screen

    def add_event_to_stream(self, event):
        self.events.append(event)

    def render_event_box(self):
        pass
