# test ascii visualization functions
import unittest
from io import StringIO
from unittest.mock import patch

from src.traffic_sim.viz.ascii_view import draw_tick, render_ascii


class TestAsciiView(unittest.TestCase):
    def setUp(self):
        self.sample_state = {
            "tick": 5,
            "intersections": {
                "A": type(
                    "Inter",
                    (),
                    {"queue": [1, 2], "light": type("Light", (), {"is_green": lambda: True})},
                )(),
                "B": type(
                    "Inter",
                    (),
                    {"queue": [3], "light": type("Light", (), {"is_green": lambda: False})},
                )(),
            },
            "vehicles": [
                type("Vehicle", (), {"finished": True})(),
                type("Vehicle", (), {"finished": False})(),
                type("Vehicle", (), {"finished": True})(),
            ],
        }

    def test_render_ascii(self):
        expected_output = (
            "== Tick 5 ==\n"
            "- Nút A: hàng chờ = 2; đèn = XANH\n"
            "- Nút B: hàng chờ = 1; đèn = ĐỎ\n"
            "Xe hoàn thành: 2/3"
        )
        result = render_ascii(self.sample_state)
        self.assertEqual(result, expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_draw_tick(self, mock_stdout):
        draw_tick(self.sample_state)
        expected_output = (
            "== Tick 5 ==\n"
            "- Nút A: hàng chờ = 2; đèn = XANH\n"
            "- Nút B: hàng chờ = 1; đèn = ĐỎ\n"
            "Xe hoàn thành: 2/3\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
"""Mô-đun `viz.ascii_view` – Renderer ASCII cực nhẹ để in ra trạng thái mô phỏng theo tick. """
