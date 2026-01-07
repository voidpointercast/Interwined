"""Entities for interactive stories."""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class VariableType(str, Enum):
    NUMBER = "number"
    BOOLEAN = "boolean"
    TEXT = "text"


@dataclass(frozen=True)
class VariableDefinition:
    name: str
    variable_type: VariableType
    default: int | float | bool | str | None = None


class ComparisonOperator(str, Enum):
    EQUAL = "=="
    NOT_EQUAL = "!="
    GREATER = ">"
    GREATER_EQUAL = ">="
    LESS = "<"
    LESS_EQUAL = "<="
    CONTAINS = "contains"


@dataclass(frozen=True)
class Constraint:
    variable_name: str
    operator: ComparisonOperator
    value: Any


class Effect(ABC):
    """Base class for choice effects."""


@dataclass
class Choice:
    text: str
    target_scene_id: str
    constraints: list[Constraint] = field(default_factory=list)
    effects: list[Effect] = field(default_factory=list)


@dataclass
class Scene:
    scene_id: str
    name: str
    text: str
    choices: list[Choice] = field(default_factory=list)


@dataclass
class Story:
    title: str
    variables: dict[str, VariableDefinition] = field(default_factory=dict)
    scenes: dict[str, Scene] = field(default_factory=dict)

    def add_scene(self, scene: Scene) -> None:
        self.scenes[scene.scene_id] = scene

    def add_variable(self, variable: VariableDefinition) -> None:
        self.variables[variable.name] = variable
