# Hướng dẫn cho thư mục src/** (TIẾNG VIỆT)

## Mục tiêu
- Module nhỏ, ghép được; **tái sử dụng API sẵn có**.

## Bắt buộc/Kiêng kỵ
- **Bắt buộc**: dùng `Graph.neighbors`, các API `loaders`, `get_logger`.
- **Bắt buộc**: type hints & docstring cho public API.
- **Kiêng**: I/O file trong core (trừ `viz`), side-effect ở import time.

## Hiệu năng & đúng đắn
- Ưu tiên O(E log V) cho đường đi; tránh quét bậc hai trên adjacency.
- Tie-breaking tất định.

## Lỗi & thông báo
- Ném `ValueError` có ngữ cảnh (cột/dòng/giá trị mong đợi…).

## Test
- Mỗi hàm mới: **ít nhất 1** happy-path + **1** edge case trong `tests/`.
- Giữ test **nhanh** và **độc lập**.
