import unittest

from interwined.entities import (
    Choice,
    ComparisonOperator,
    Constraint,
    Effect,
    Scene,
    Story,
    VariableDefinition,
    VariableType,
)


class DummyEffect(Effect):
    pass


class StoryEntityTests(unittest.TestCase):
    def test_variable_definition_holds_defaults(self) -> None:
        variable = VariableDefinition(
            name="health",
            variable_type=VariableType.NUMBER,
            default=10,
        )

        self.assertEqual(variable.name, "health")
        self.assertEqual(variable.variable_type, VariableType.NUMBER)
        self.assertEqual(variable.default, 10)

    def test_choice_can_hold_constraints_and_effects(self) -> None:
        constraint = Constraint(
            variable_name="has_key",
            operator=ComparisonOperator.EQUAL,
            value=True,
        )
        effect = DummyEffect()

        choice = Choice(
            text="Open the door",
            target_scene_id="hallway",
            constraints=[constraint],
            effects=[effect],
        )

        self.assertEqual(choice.constraints, [constraint])
        self.assertEqual(choice.effects, [effect])

    def test_scene_includes_text_and_choices(self) -> None:
        scene = Scene(
            scene_id="intro",
            name="Introduction",
            text="You wake up in a quiet room.",
            choices=[],
        )

        self.assertEqual(scene.text, "You wake up in a quiet room.")
        self.assertEqual(scene.choices, [])

    def test_story_can_add_variables_and_scenes(self) -> None:
        story = Story(title="Test Story")
        variable = VariableDefinition(
            name="gold",
            variable_type=VariableType.NUMBER,
            default=0,
        )
        scene = Scene(
            scene_id="start",
            name="Start",
            text="Start here.",
            choices=[],
        )

        story.add_variable(variable)
        story.add_scene(scene)

        self.assertEqual(story.variables["gold"], variable)
        self.assertEqual(story.scenes["start"], scene)


if __name__ == "__main__":
    unittest.main()
