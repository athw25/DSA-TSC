# -*- coding: utf-8 -*-
"""
CLI Skeleton – chạy demo để xác nhận cấu trúc dự án.
Lệnh:
    python scripts/run_sim.py --scenario data/scenarios/sample.yaml --ascii
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Chạy demo skeleton (không mô phỏng).")
    parser.add_argument("--scenario", required=True, help="Đường dẫn file YAML mô tả kịch bản (demo).")
    parser.add_argument("--ascii", action="store_true", help="Bật in ASCII (demo).")
    args = parser.parse_args()

    print("✅ Đây là bộ khung (skeleton) của dự án Traffic Sim City.")
    print("ℹ️  Chưa có mô phỏng thật. Bạn có thể mở các file trong src/traffic_sim/ để cài đặt dần.")
    print(f"📄 Scenario demo: {args.scenario}")
    if args.ascii:
        print("🖥️  (ASCII) Ví dụ: sẽ in trạng thái mô phỏng tại đây sau khi triển khai thật.")
    sys.exit(0)

if __name__ == "__main__":
    main()
