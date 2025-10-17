# Cẩm nang dùng Copilot (TIẾNG VIỆT)

## Mục tiêu
- Dùng Copilot để tăng tốc viết **mã + test**, **không thay thế review**.
- Luôn pass: **ruff + black + pytest**.

## Cách đặt yêu cầu (prompt)
- Nêu rõ: **Inputs/Outputs**, ràng buộc (độ phức tạp), **edge cases**.
- Gọi tên **API hiện có** để tái sử dụng (vd: `loaders.load_graph`, `Graph.neighbors`).
- Yêu cầu **docstring + type hints** và **test** kèm theo.
- Giới hạn phạm vi: “chỉ sửa hàm X”, “không đổi chữ ký Y”.

## Quy trình gợi ý
1) Tạo khung (signature + docstring + TODO) và **viết 1–2 test nhỏ** trước.
2) Nhờ Copilot “điền” code còn thiếu dựa trên khung đó.
3) Chạy `pre-commit run --all-files` và `pytest -q`, sửa đến khi **xanh**.
4) Refactor nhẹ, cập nhật doc nếu đổi hành vi.

## Không được làm
- Secrets đặt trong code/comment (dùng `.env`, đã ignore).
- Đọc file trực tiếp trong thuật toán (đi qua loader).
- Thêm phụ thuộc nặng chưa bàn bạc.

## Tài liệu tham chiếu
- `docs/ARCHITECTURE.md` — kiến trúc & flow.
- `docs/SCHEMAS.md` — schema CSV/YAML.
- `docs/SCENARIOS.md` — cách viết scenario.
- `CONTRIBUTING.md` — quy trình nhánh, PR, DoD.
