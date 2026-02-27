# **Slot 10 - Chapter 3 (Part 8): Mining Spatiotemporal and Trajectory Patterns**

**Ngày học: 06/02/2026** 

**Nội dung chương học:**

* Slide 3.10: Mining Spatiotemporal and Trajectory Patterns

---

## 1. Khai phá mẫu không gian (Spatial Patterns)

*Nguồn tham khảo: Slide 3.10*

### 1.1. Khái niệm cốt lõi

* **Spatiotemporal Patterns (Mẫu không gian - thời gian):** Là các mẫu dữ liệu có chứa cả thông tin về vị trí địa lý (Không gian - Spatial) và thời gian xảy ra (Thời gian - Temporal).
* **Spatial Frequent Patterns:** Khai phá các quy luật thường xuyên xảy ra ở các vị trí địa lý.
* *Ví dụ:* $is\_a(x, large\_town) \land intersect(x, highway) \to adjacent\_to(x, water)$ [Support: 7%, Confidence: 85%]. (Một thị trấn lớn nằm cắt ngang đường cao tốc thì 85% khả năng là nó nằm cạnh nguồn nước).


* **Spatial Autocorrelation (Tự tương quan không gian):** Nguyên lý cơ bản trong địa lý: "Những thứ ở gần nhau thì có xu hướng giống nhau/liên quan đến nhau nhiều hơn là những thứ ở xa nhau" (Ví dụ: Nhiệt độ, giá nhà khu vực lân cận).

### 1.2. Mối quan hệ không gian (Spatial Relationships)

Trong khai phá không gian, các thuộc tính được phân cấp (Hierarchy) tương tự như phân cấp hàng hóa:

* **Topological relations (Quan hệ topo):** `intersects` (cắt), `overlaps` (chồng lấn), `disjoint` (tách rời).
* **Spatial orientations (Hướng):** `left_of`, `west_of`, `under`.
* **Distance information (Khoảng cách):** `close_to`, `within_distance`.
* *Ví dụ phân cấp:* Thuộc tính `close_to` là cha (tổng quát) của các thuộc tính con như `near_by`, `touch`, `intersect`.

---

## 2. Khai phá mẫu quỹ đạo di chuyển (Trajectory Patterns)

*Nguồn tham khảo: Slide 3.10*

### 2.1. Khái niệm và Bài toán

* **Trajectory Data (Dữ liệu quỹ đạo):** Chuỗi các tọa độ $(x, y, t)$ ghi lại sự di chuyển của một đối tượng theo thời gian (Ví dụ: Dữ liệu GPS của xe taxi, quỹ đạo bay của chim di cư).
* **Semantics-Rich Movement Patterns (Mẫu di chuyển giàu ngữ nghĩa):** Khác với tọa độ GPS thô, ta muốn khai phá quỹ đạo dưới dạng ngữ nghĩa.
* *Ví dụ:* Thay vì tọa độ $(X1, Y1) \to (X2, Y2)$, ta muốn mẫu: `Home -> Office -> Restaurant -> Home`.



### 2.2. Các bước xử lý quỹ đạo ngữ nghĩa

Để tìm ra các mẫu di chuyển thông minh, thuật toán thường qua 2 bước:

1. **Bước 1 (Chuyển đổi):** Chuyển dữ liệu di chuyển thô thành chuỗi các địa điểm có ngữ nghĩa (Semantic trajectories) thông qua việc phân tích điểm dừng (stop points).
2. **Bước 2 (Phân chia & Nhóm):** Chia các mẫu di chuyển thô (coarse patterns) thành nhiều đoạn di chuyển chi tiết hơn (fine-grained) bằng cách gom nhóm (grouping) các đoạn cắt quỹ đạo (movement snippets) có sự tương đồng.

---

## 3. Khai phá tính chu kỳ trong dữ liệu thưa thớt (Periodicity in Sparse Data)

*Nguồn tham khảo: Slide 3.10*

### 3.1. Vấn đề của Dữ liệu thưa thớt (Sparse Data)

* **Bối cảnh:** Dữ liệu di chuyển trong không gian - thời gian đôi khi rất phân tán và thưa thớt (Ví dụ: Cuộc gọi điện thoại tại các trạm phát sóng khác nhau, quỹ đạo của một loài chim chỉ được ghi nhận vài lần trong tháng).
* **Thử thách:** Làm sao để tìm ra **tính chu kỳ (Periodicity)** khi dữ liệu không liên tục?

### 3.2. Giải pháp phát hiện chu kỳ

1. **Tìm điểm tham chiếu (Reference Spots):** Phân cụm (Cluster) dữ liệu để tìm ra các vị trí quan trọng/thường xuyên lui tới. Các vị trí này đóng vai trò là "điểm neo" để phân tích.
2. **Phân tích toán học:** Tại mỗi "điểm tham chiếu", sử dụng các công cụ toán học mạnh mẽ như **Fourier Transform (Biến đổi Fourier)** và **Auto-correlation (Tự tương quan)** để phát hiện ra các chu kỳ bị xen kẽ (interleaved periods).
3. **Tổng hợp:** Từ các điểm và chu kỳ rời rạc, thuật toán tóm tắt lại thành một mẫu chu kỳ hoàn chỉnh (Periodic patterns).

---

## 4. Tổng kết & Tra cứu nhanh (Cheatsheet)

### Bảng phân biệt các loại mẫu

| Loại mẫu | Dữ liệu đầu vào | Ví dụ thực tế |
| --- | --- | --- |
| **Spatial Pattern** | Tọa độ địa lý tĩnh, khoảng cách. | Vị trí trạm xăng thường đặt cạnh trạm dừng nghỉ trên cao tốc. |
| **Spatiotemporal** | Tọa độ thay đổi theo thời gian. | Sự lây lan của dịch bệnh qua các tỉnh thành theo từng tháng. |
| **Trajectory Pattern** | Chuỗi di chuyển liên tục (GPS). | Tuyến đường tài xế công nghệ thường đi vào giờ cao điểm. |

### Từ khóa quan trọng

* **Spatial Autocorrelation:** Sự tương quan không gian (Gần nhau thì giống nhau).
* **Semantic Trajectory:** Quỹ đạo mang ý nghĩa con người hiểu được (ví dụ: Nhà $\to$ Trường học), thay vì chỉ là kinh độ/vĩ độ.
* **Fourier Transform:** Công cụ toán học chuyển đổi tín hiệu từ miền thời gian sang miền tần số, dùng để dò tìm chu kỳ ẩn trong dữ liệu thưa thớt.

---

*Ghi chú: Nội dung được tổng hợp từ tệp: 3.10 Mining Spatiotemporal and Trajectory Patterns.pptx.*

---
