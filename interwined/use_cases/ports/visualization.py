"""Ports for visualizing stories."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from interwined.entities.story import Story
from interwined.use_cases.base import Response


@dataclass(frozen=True)
class VisualizationResponse(Response):
    content: bytes
    mimetype: str


class VisualizationPort(ABC):
    """Port for converting stories into visual assets."""

    @abstractmethod
    def convert_story(self, story: Story) -> VisualizationResponse:
        """Convert a story into visual content."""
        raise NotImplementedError
