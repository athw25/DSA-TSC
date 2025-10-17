# Hướng dẫn cho thư mục tests/** (TIẾNG VIỆT)

## Phong cách test
- Nhỏ, tất định; ưu tiên dataset mẫu trong `data/`.
- Đặt tên dễ hiểu (BDD: `test_should_*`).

## Nội dung yêu cầu Copilot sinh
- Mỗi tính năng: 1 happy-path, 1 boundary, 1 negative case.
- Với CLI: dùng `subprocess` hoặc import trực tiếp, runtime < 2 giây.

## Không làm
- Không gọi mạng; không phụ thuộc timezone/locale máy.
