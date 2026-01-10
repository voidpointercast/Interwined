"""Base types for use cases."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Command:
    """Base command for use cases."""


@dataclass(frozen=True)
class Response:
    """Base response for use cases."""
