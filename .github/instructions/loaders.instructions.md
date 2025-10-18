# Hướng dẫn riêng cho src/traffic_sim/loaders.py (TIẾNG VIỆT)

## Hợp đồng schema
- Tuân thủ `docs/SCHEMAS.md` nghiêm ngặt: tên cột, kiểu, ràng buộc (vd: weight >= 0, id là int).

## I/O
- CSV: `csv.DictReader` (hoặc pandas nếu đã có), trả về cấu trúc python thuần tương thích `Graph`.
- YAML: `yaml.safe_load`.

## Logging
- Dùng `utils.logging.get_logger(__name__)` và log tổng kết (số hàng đọc, số lỗi).
- Lỗi: `ValueError` nêu rõ dòng/cột và giá trị sai.
