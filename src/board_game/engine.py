"""Small deterministic board-game engine with explicit domain boundaries."""

from __future__ import annotations

from dataclasses import dataclass, field
from random import Random


@dataclass
class Player:
    name: str
    position: int = 0


@dataclass
class Board:
    size: int = 30
    jumps: dict[int, int] = field(default_factory=lambda: {3: 11, 17: 8, 21: 28})

    def land(self, position: int) -> int:
        bounded = min(position, self.size)
        return self.jumps.get(bounded, bounded)


class Game:
    def __init__(self, names: list[str], seed: int = 0, board: Board | None = None):
        if not 2 <= len(names) <= 4:
            raise ValueError("Game requires two to four players")
        if len(set(names)) != len(names):
            raise ValueError("Player names must be unique")
        self.players = [Player(name) for name in names]
        self.board = board or Board()
        self.random = Random(seed)
        self.turn = 0

    def play_turn(self, roll: int | None = None) -> Player:
        player = self.players[self.turn]
        value = self.random.randint(1, 6) if roll is None else roll
        if value not in range(1, 7):
            raise ValueError("Roll must be between 1 and 6")
        player.position = self.board.land(player.position + value)
        self.turn = (self.turn + 1) % len(self.players)
        return player

    @property
    def winner(self) -> Player | None:
        return next((p for p in self.players if p.position >= self.board.size), None)
