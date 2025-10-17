# Hướng dẫn cho src/traffic_sim/viz/** (TIẾNG VIỆT)

- `ascii_view`: chỉ in ra console phục vụ demo/debug; không ảnh hưởng core state.
- `matplotlib_view`: gom dữ liệu từ `metrics`/`engine` nhưng **không** xử lý thuật toán.
- Có thể thêm tùy chọn `--no-viz` ở CLI; code viz không được chặn test (giữ test nhanh).
