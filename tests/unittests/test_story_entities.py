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


def test_variable_definition_holds_defaults() -> None:
    variable = VariableDefinition(
        name="health",
        variable_type=VariableType.NUMBER,
        default=10,
    )

    assert variable.name == "health"
    assert variable.variable_type is VariableType.NUMBER
    assert variable.default == 10


def test_choice_can_hold_constraints_and_effects() -> None:
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

    assert choice.constraints == [constraint]
    assert choice.effects == [effect]


def test_scene_includes_text_and_choices() -> None:
    scene = Scene(
        scene_id="intro",
        name="Introduction",
        text="You wake up in a quiet room.",
        choices=[],
    )

    assert scene.text == "You wake up in a quiet room."
    assert scene.choices == []


def test_story_can_add_variables_and_scenes() -> None:
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

    assert story.variables["gold"] == variable
    assert story.scenes["start"] == scene
