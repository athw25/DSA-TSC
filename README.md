<<<<<<< HEAD
# DSA-TSC
Mô phỏng hệ thống giao thông với đèn xanh – đỏ, các tuyến đường.
=======
# Traffic Sim City – Python Traffic Simulation (BFS/DFS, Dijkstra/A*)

Mô phỏng hệ thống giao thông thành phố với **đèn xanh–đỏ**, **luồng xe**, và **tuyến đường tối ưu**.
Dành cho bài tập Case Study CTDL & GT: dùng **Graph**, **Queue/Priority Queue**, **BFS/DFS**, **Dijkstra** (có thể mở rộng **A\***).

---

## 1) Tính năng chính

- **Đồ thị thành phố (Graph)**: danh sách kề, cạnh có trọng số (thời gian/quãng đường).
- **Luồng xe**: mô phỏng theo **tick thời gian** với hàng chờ tại nút (Queue).
- **Đèn giao thông**: chu kỳ **green/red** có `offset`, đồng bộ tại nút.
- **Đường đi tối ưu**: **Dijkstra** (mặc định), tùy chọn **A\*** với heuristic Euclid.
- **Thống kê (KPIs)**: tổng thời gian, độ trễ trung bình, độ dài hàng chờ, throughput.
- **Trình diễn**: renderer ASCII (nhẹ); có `matplotlib` để vẽ biểu đồ theo tick.

---

## 2) Cài đặt nhanh

### Yêu cầu
- Python 3.10+
- (Tuỳ chọn) virtualenv/venv

### Bắt đầu
```bash
git clone <your-repo-url> traffic-sim-city
cd traffic-sim-city

python -m venv .venv
# Windows: .\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
>>>>>>> b46317e (Khởi tạo project TSC)
