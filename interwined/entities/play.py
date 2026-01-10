"""Entity for playing through a story."""

from __future__ import annotations

from typing import Any

from interwined.entities.story import Choice, Story


class Play:
    """Manage the state of a story playthrough."""

    def __init__(self, story: Story) -> None:
        self.story = story
        self.variables: dict[str, Any] = {
            name: definition.default for name, definition in story.variables.items()
        }
        self.current_scene_id = story.start_scene

    def next(self) -> tuple[str, list[str]]:
        if self.current_scene_id is None:
            raise ValueError("Story does not define a start scene.")

        scene = self.story.scenes.get(self.current_scene_id)
        if scene is None:
            raise ValueError(f"Scene '{self.current_scene_id}' is not defined in the story.")

        available_choices = [
            choice.text for choice in scene.choices if self._is_applicable(choice)
        ]
        return scene.text, available_choices

    def _is_applicable(self, choice: Choice) -> bool:
        """Stub for determining whether a choice can be selected."""
        return True
