"""
Mô-đun `viz.ascii_view` – Renderer ASCII cực nhẹ để in ra trạng thái mô phỏng theo tick.
"""

from __future__ import annotations

from typing import Any, Dict


def render_ascii(state: Dict[str, Any]) -> str:
    """Trả về chuỗi ASCII mô tả sơ lược trạng thái hiện tại."""
    lines = []
    lines.append(f"== Tick {state.get('tick', 0)} ==")
    inters = state.get("intersections", {})
    for k, inter in inters.items():
        lines.append(
            f"- Nút {k}: hàng chờ = {len(inter.queue)}; "
            f"đèn = {'XANH' if inter.light.is_green() else 'ĐỎ'}"
        )

    finished = sum(1 for v in state.get("vehicles", []) if v.finished)
    lines.append(f"Xe hoàn thành: {finished}/{len(state.get('vehicles', []))}")
    return "\n".join(lines)


def draw_tick(state: Dict[str, Any]) -> None:
    """In trạng thái ra console (tiếng Việt)."""
    print(render_ascii(state))
