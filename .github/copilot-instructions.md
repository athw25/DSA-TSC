# Hướng dẫn Copilot — traffic-sim-city (TIẾNG VIỆT)

## Ngôn ngữ

- **Luôn trả lời và viết mã kèm chú thích bằng TIẾNG VIỆT.**
- Nếu cần trích dẫn/đặt lệnh, giữ nguyên cú pháp tiếng Anh (API, CLI, code).

## Mục tiêu & bối cảnh

- Dự án mô phỏng giao thông (skeleton) theo module nhỏ gọn.
- Input: CSV (graph/coords/lights/vehicles) + YAML scenario.
- Kết quả: CLI chạy được, test unit/integration cơ bản, KPI/ASCII viz.

## Chuẩn code & công cụ

- Python ≥ 3.10, dùng **type hints đầy đủ** (public API 100%, internal ≥ 80%).
- **Black + Ruff** (line-length = 100 nếu repo không ghi khác).
- **Không dùng `print()` trong thư viện** (chỉ dùng trong `viz`/CLI). Dùng `utils.logging.get_logger`.
- Không thêm phụ thuộc nặng nếu chưa bàn bạc.

## Sơ đồ thư mục (tạm thời)

traffic-sim-city/
├─ README.md
├─ pyproject.toml
├─ requirements.txt
├─ .gitignore
├─ .pre-commit-config.yaml
├─ .github/
│ └─ workflows/
│ └─ pytest.yml
├─ data/
│ ├─ sample_map.csv
│ ├─ sample_coords.csv
│ ├─ sample_lights.csv
│ ├─ sample_vehicles.csv
│ └─ scenarios/
│ └─ sample.yaml
├─ scripts/
│ └─ run_sim.py
├─ src/
│ └─ traffic_sim/
│ ├─ **init**.py
│ ├─ graph.py
│ ├─ loaders.py
│ ├─ traffic_light.py
│ ├─ pathfinding.py
│ ├─ simulation.py
│ ├─ metrics.py
│ ├─ models.py
│ ├─ utils/
│ │ └─ logging.py
│ └─ viz/
│ ├─ ascii_view.py
│ └─ matplotlib_view.py
└─ tests/
├─ test_graph.py
├─ test_pathfinding.py
├─ test_traffic_light.py
├─ test_simulation.py
├─ test_metrics.py
├─ test_simulation_smoke.py
└─ test_integration_cli.py

## Giao kèo (contracts) & không phá vỡ API

- **Không đổi chữ ký hàm public** ở các module trên. Nếu cần mở rộng, thêm tham số **tuỳ chọn** có giá trị mặc định.
- Pathfinding: dùng `Graph.neighbors`. Tính tất định cho trường hợp đồng chi phí.
- `SimulationEngine.step` idempotent theo tick; không được mutate input ngoài ý muốn.

## Dữ liệu & schema

- Ràng buộc CSV/YAML theo `docs/SCHEMAS.md` + `docs/SCENARIOS.md`.
- Loader phải **fail-fast**: nêu rõ dòng/cột sai, giá trị mong đợi vs thực tế.
- Bất kỳ thay đổi schema → cập nhật docs + test.

## Kiểm thử

- Test nhỏ, nhanh, mang tính minh họa; seed RNG cố định nếu dùng.
- Mỗi public function mới phải có test: happy path + ≥1 edge case.
- Integration test < 2 giây; đồ thị mẫu tối thiểu.

## Mẫu prompt nên dùng (dành cho Copilot Chat)

- “Viết `a_star(graph, src, dst, heuristic=euclid)` dùng `neighbors` + `reconstruct_path`, độ phức tạp O(E log V), thêm test giống phong cách `test_dijkstra_basic`.”
- “Cập nhật `loaders.load_graph`: validate `weight >= 0`, lỗi nêu rõ số dòng/cột; giữ chữ ký cũ.”

## Điều không được làm

- Không đọc file bên trong thuật toán (chỉ dùng `loaders`).
- Không đưa state toàn cục/singleton ẩn.
- Không thêm dependency lớn hoặc thay đổi API public mà không tương thích ngược.

## Tài liệu & chú thích

- Public API: **docstring chuẩn** (Google/Numpy) + ví dụ ngắn.
- Mô tả quyết định vi tế (tie-breaking, float weights) trong docstring + test.

## Cổng chất lượng (quality gates)

- Phải pass: **ruff + black + pytest** (unit/integration).
- PR nhỏ, có test/doc kèm theo, giữ code dễ đọc.
