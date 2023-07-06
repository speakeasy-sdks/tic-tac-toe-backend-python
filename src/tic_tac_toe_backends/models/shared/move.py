"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from enum import Enum
from typing import Optional

class MoveAfterStateCurrentMark(str, Enum):
    X = 'X'
    O = 'O'



@dataclasses.dataclass
class MoveAfterStateGrid:
    cells: Optional[str] = dataclasses.field(default=None)
    




@dataclasses.dataclass
class MoveAfterStatePossibleMovesAfterStateGrid:
    cells: Optional[str] = dataclasses.field(default=None)
    


class MoveAfterStatePossibleMovesAfterStateStartingMark(str, Enum):
    X = 'X'
    O = 'O'



@dataclasses.dataclass
class MoveAfterStatePossibleMovesAfterState:
    grid: Optional[MoveAfterStatePossibleMovesAfterStateGrid] = dataclasses.field(default=None)
    starting_mark: Optional[MoveAfterStatePossibleMovesAfterStateStartingMark] = dataclasses.field(default=None)
    




@dataclasses.dataclass
class MoveAfterStatePossibleMovesBeforeStateGrid:
    cells: Optional[str] = dataclasses.field(default=None)
    


class MoveAfterStatePossibleMovesBeforeStateStartingMark(str, Enum):
    X = 'X'
    O = 'O'



@dataclasses.dataclass
class MoveAfterStatePossibleMovesBeforeState:
    grid: Optional[MoveAfterStatePossibleMovesBeforeStateGrid] = dataclasses.field(default=None)
    starting_mark: Optional[MoveAfterStatePossibleMovesBeforeStateStartingMark] = dataclasses.field(default=None)
    


class MoveAfterStatePossibleMovesMark(str, Enum):
    X = 'X'
    O = 'O'



@dataclasses.dataclass
class MoveAfterStatePossibleMoves:
    after_state: Optional[MoveAfterStatePossibleMovesAfterState] = dataclasses.field(default=None)
    before_state: Optional[MoveAfterStatePossibleMovesBeforeState] = dataclasses.field(default=None)
    cell_index: Optional[int] = dataclasses.field(default=None)
    mark: Optional[MoveAfterStatePossibleMovesMark] = dataclasses.field(default=None)
    


class MoveAfterStateStartingMark(str, Enum):
    X = 'X'
    O = 'O'

class MoveAfterStateWinner(str, Enum):
    X = 'X'
    O = 'O'



@dataclasses.dataclass
class MoveAfterState:
    current_mark: Optional[MoveAfterStateCurrentMark] = dataclasses.field(default=None)
    game_not_started: Optional[bool] = dataclasses.field(default=None)
    game_over: Optional[bool] = dataclasses.field(default=None)
    grid: Optional[MoveAfterStateGrid] = dataclasses.field(default=None)
    possible_moves: Optional[list[MoveAfterStatePossibleMoves]] = dataclasses.field(default=None)
    starting_mark: Optional[MoveAfterStateStartingMark] = dataclasses.field(default=None)
    tie: Optional[bool] = dataclasses.field(default=None)
    winner: Optional[MoveAfterStateWinner] = dataclasses.field(default=None)
    winning_cells: Optional[list[int]] = dataclasses.field(default=None)
    




@dataclasses.dataclass
class Move:
    r"""A Move containing the before and after GameStates."""
    after_state: Optional[list[MoveAfterState]] = dataclasses.field(default=None)
    
