"""NetworkX-based visualization adapter."""

from __future__ import annotations

import json

import networkx as nx

from interwined.entities.story import Choice, Constraint, Scene, Story
from interwined.use_cases.ports.visualization import (
    VisualizationPort,
    VisualizationResponse,
)


class NetworkxVisualizationPort(VisualizationPort):
    """Convert stories into a NetworkX graph representation."""

    def convert_story(self, story: Story) -> VisualizationResponse:
        """Convert a story into a GML-encoded NetworkX graph."""
        graph = self._build_graph(story)
        gml_content = "\n".join(nx.generate_gml(graph)).encode("utf-8")
        return VisualizationResponse(content=gml_content, mimetype="text/gml")

    def _build_graph(self, story: Story) -> nx.DiGraph:
        graph: nx.DiGraph = nx.DiGraph(title=story.title)
        for scene in story.scenes.values():
            self._add_scene_node(graph, story, scene)
            for choice in scene.choices:
                self._add_choice_edge(graph, scene.scene_id, choice)
        return graph

    def _add_scene_node(self, graph: nx.DiGraph, story: Story, scene: Scene) -> None:
        graph.add_node(
            scene.scene_id,
            name=scene.name,
            text=scene.text,
            is_start=scene.scene_id == story.start_scene,
        )

    def _add_choice_edge(
        self,
        graph: nx.DiGraph,
        scene_id: str,
        choice: Choice,
    ) -> None:
        constraints_payload = [
            self._serialize_constraint(constraint) for constraint in choice.constraints
        ]
        graph.add_edge(
            scene_id,
            choice.target_scene_id,
            text=choice.text,
            constraints=json.dumps(constraints_payload),
        )

    def _serialize_constraint(self, constraint: Constraint) -> dict[str, str]:
        return {
            "variable_name": constraint.variable_name,
            "operator": constraint.operator.value,
            "value": str(constraint.value),
        }
