"""
Mô-đun `viz.matplotlib_view` – Tuỳ chọn: vẽ biểu đồ bằng matplotlib.
"""

from __future__ import annotations

from typing import Any, Dict, List


def plot_queue_over_time(data: List[Dict[str, Any]]):
    try:
        import matplotlib.pyplot as plt
    except Exception:
        print("Không thể import matplotlib – bỏ qua biểu đồ.")
        return
    xs = [d["tick"] for d in data]
    ys = [d["max_queue_len"] for d in data]
    plt.figure()
    plt.title("Độ dài hàng chờ lớn nhất theo thời gian (tick)")
    plt.xlabel("Tick")
    plt.ylabel("Độ dài hàng chờ lớn nhất")
    plt.plot(xs, ys)
    plt.show()
