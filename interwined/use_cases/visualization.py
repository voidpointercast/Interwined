"""Use case for visualizing stories."""

from dataclasses import dataclass

from interwined.entities.story import Story
from interwined.use_cases.base import Command
from interwined.use_cases.ports.visualization import (
    VisualizationPort,
    VisualizationResponse,
)


@dataclass(frozen=True)
class VisualizationCommand(Command):
    story: Story


class VisualizationUseCase:
    """Convert a story into a visualization via the configured port."""

    def __init__(self, visualization_port: VisualizationPort) -> None:
        self._visualization_port = visualization_port

    def execute(self, command: VisualizationCommand) -> VisualizationResponse:
        return self._visualization_port.convert_story(command.story)
