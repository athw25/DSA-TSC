# Hướng dẫn cho src/traffic_sim/viz/\*\* (TIẾNG VIỆT)

- `ascii_view`: chỉ in ra console phục vụ demo/debug; không ảnh hưởng core state.
- `matplotlib_view`: gom dữ liệu từ `metrics`/`engine` nhưng **không** xử lý thuật toán.
- Có thể thêm tùy chọn `--no-viz` ở CLI; code viz không được chặn test (giữ test nhanh).

## Quy ước chung

- Không thay đổi trạng thái core trong module viz.
- Viết docstring đầy đủ, rõ ràng.
- Viết test riêng cho viz (không test core logic).
- Sử dụng `utils.logging.get_logger` để log thay vì `print()`.
- Giữ code đơn giản, tránh thêm phụ thuộc nặng nếu không cần thiết.
- Tuân thủ chuẩn code chung của dự án (black + ruff).
- Tham khảo tài liệu chính trong `docs/` nếu cần.
