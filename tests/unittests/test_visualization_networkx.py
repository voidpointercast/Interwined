import json
import unittest

import networkx as nx

from interwined.adapters.visualization_networkx import NetworkxVisualizationPort
from interwined.entities import Choice, Scene, Story


class VisualizationNetworkxTests(unittest.TestCase):
    def test_convert_story_returns_gml_graph(self) -> None:
        story = Story(title="Adventure", start_scene="start")
        start_scene = Scene(
            scene_id="start",
            name="Start",
            text="You wake up.",
            choices=[Choice(text="Go", target_scene_id="end")],
        )
        end_scene = Scene(
            scene_id="end",
            name="End",
            text="The end.",
            choices=[],
        )
        story.add_scene(start_scene)
        story.add_scene(end_scene)

        adapter = NetworkxVisualizationPort()

        response = adapter.convert_story(story)

        self.assertEqual(response.mimetype, "text/gml")

        graph = nx.parse_gml(response.content.decode("utf-8").splitlines())

        self.assertIn("start", graph.nodes)
        self.assertIn("end", graph.nodes)
        self.assertTrue(graph.nodes["start"]["is_start"])
        self.assertEqual(graph.nodes["start"]["name"], "Start")
        self.assertTrue(graph.has_edge("start", "end"))
        self.assertEqual(graph.edges["start", "end"]["text"], "Go")
        constraints_value = graph.edges["start", "end"]["constraints"]
        constraints = (
            constraints_value
            if isinstance(constraints_value, list)
            else json.loads(constraints_value)
        )
        self.assertEqual(constraints, [])


if __name__ == "__main__":
    unittest.main()
