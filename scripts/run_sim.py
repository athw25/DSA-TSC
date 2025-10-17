# # -*- coding: utf-8 -*-
# """
# CLI Skeleton – chạy demo để xác nhận cấu trúc dự án.
# Lệnh:
#     python scripts/run_sim.py --scenario data/scenarios/sample.yaml --ascii
# """
# import argparse
# import sys

# def main():
#     parser = argparse.ArgumentParser(description="Chạy demo skeleton (không mô phỏng).")
#     parser.add_argument
# ("--scenario", required=True, help="Đường dẫn file YAML mô tả kịch bản (demo).")
#     parser.add_argument("--ascii", action="store_true", help="Bật in ASCII (demo).")
#     args = parser.parse_args()

#     print("✅ Đây là bộ khung (skeleton) của dự án Traffic Sim City.")
#     print("ℹ️  Chưa có mô phỏng thật.
# Bạn có thể mở các file trong src/traffic_sim/ để cài đặt dần.")
#     print(f"📄 Scenario demo: {args.scenario}")
#     if args.ascii:
#         print("🖥️  (ASCII) Ví dụ: sẽ in trạng thái mô phỏng tại đây sau khi triển khai thật.")
#     sys.exit(0)

# if __name__ == "__main__":
#     main()

# -*- coding: utf-8 -*-
"""
Chương trình dòng lệnh (CLI) để chạy mô phỏng giao thông.
Ví dụ:
    python scripts/run_sim.py --scenario data/scenarios/sample.yaml --ascii --ticks 200 --use-a-star
"""

import argparse
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from traffic_sim.simulation import SimulationEngine


def main():
    parser = argparse.ArgumentParser(description="Chạy mô phỏng giao thông (tiếng Việt).")
    parser.add_argument("--scenario", required=True, help="Đường dẫn file YAML mô tả kịch bản.")
    parser.add_argument("--ticks", type=int, default=None, help="Ghi đè số tick mô phỏng.")
    parser.add_argument("--ascii", dest="ascii", action="store_true", help="Bật renderer ASCII.")
    parser.add_argument("--no-viz", dest="ascii", action="store_false", help="Tắt mọi renderer.")
    parser.set_defaults(ascii=True)
    parser.add_argument("--use-a-star", action="store_true", help="Dùng A* thay vì Dijkstra.")
    parser.add_argument("--seed", type=int, default=None, help="Đặt seed ngẫu nhiên.")
    parser.add_argument("--kpi-out", default=None, help="Đường dẫn CSV để xuất KPI.")
    args = parser.parse_args()

    config = {"simulation": {}, "astar": {"use": args.use_a_star}}
    if args.ticks is not None:
        config["simulation"]["ticks"] = args.ticks
    if args.kpi_out:
        config["simulation"]["kpi_export"] = args.kpi_out

    engine = SimulationEngine(config=config)
    engine.setup_from_scenario(args.scenario)

    ticks = engine.config.get("simulation", {}).get("ticks", 200)
    if args.seed is not None:
        from traffic_sim.utils.rng import set_seed

        set_seed(args.seed)

    print("🚦 Bắt đầu mô phỏng...")
    engine.run(ticks=ticks, ascii_draw=args.ascii)
    print("✅ Kết thúc mô phỏng.")


if __name__ == "__main__":
    main()
