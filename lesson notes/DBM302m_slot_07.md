# Slot 07 - Chapter 3 (Part 5): Advanced Mining Methods

**Ngày học: 27/01/2026** 

**Nội dung chương học:**

* Slide 3.8: Mining Methods (Multi-level & Multi-dimensional Associations)
* Slide 3.8 Mining Methods (cont.): Mining Quantitative Associations

---

## 1. Khai phá luật kết hợp đa cấp (Mining Multi-level Associations)

*Nguồn tham khảo: Slide 3.8*

### 1.1. Khái niệm cốt lõi

* **Item Hierarchies (Phân cấp mục):** Trong thực tế, hàng hóa thường được phân loại theo cấu trúc cây. Ví dụ: *Sữa Dairyland 2% $\to$ Sữa bò $\to$ Sản phẩm từ sữa*.
* **Multi-level Association:** Khai phá mối quan hệ không chỉ ở mức độ chi tiết nhất (từng sản phẩm cụ thể) mà còn ở các mức độ tổng quát hơn (nhóm sản phẩm).
* **Uniform Support (Độ hỗ trợ đồng nhất):** Áp dụng chung một ngưỡng `min_sup` cho tất cả các cấp. Dễ cài đặt nhưng thường bỏ sót các mẫu hiếm ở cấp thấp.
* **Level-reduced min-support (Độ hỗ trợ giảm theo cấp):** Các mục ở cấp càng chi tiết (thấp hơn) thì có tần suất xuất hiện tự nhiên càng nhỏ, do đó ngưỡng `min_sup` cần được giảm tương ứng.

### 1.2. Quy trình/Kiến trúc

Khai phá đa cấp thường sử dụng phương pháp chia sẻ để tối ưu hóa tính toán:

1. **Khám phá từ trên xuống (Top-down):** Bắt đầu khai phá ở cấp độ tổng quát cao nhất (Level 1).
2. **Lọc kế thừa (Shared multi-level mining):** Chỉ những nhóm sản phẩm phổ biến ở cấp trên mới được tiếp tục mở rộng để tìm kiếm ở cấp dưới chi tiết hơn.
3. Sử dụng ngưỡng `min_sup` thấp nhất để truyền xuống các tập ứng viên ở các cấp thấp hơn nhằm tiết kiệm chi phí quét dữ liệu.

---

## 2. Khai phá đa chiều và định lượng (Multi-dimensional & Quantitative Associations)

*Nguồn tham khảo: Slide 3.8 và 3.8 (cont.)*

### 2.1. Nguyên lý hoạt động

* **Tư duy (Multi-dimensional):** Thay vì chỉ tìm quan hệ trong một chiều dữ liệu (ví dụ: Mua A $\to$ Mua B), ta tìm quan hệ giữa nhiều thuộc tính khác nhau (Tuổi, Thu nhập, Nghề nghiệp $\to$ Quyết định mua hàng).
* *Ví dụ:* $age(X, "20..29") \land income(X, "52K..58K") \to buys(X, "iPad")$


* **Tư duy (Quantitative):** Làm thế nào để áp dụng luật kết hợp khi dữ liệu là số thực (Tuổi, Lương) thay vì dữ liệu phân loại (Giới tính, Nghề)?
* **Công thức/Chỉ số xử lý dữ liệu số:**
* **Static discretization:** Chia khoảng dữ liệu tĩnh dựa trên kiến thức miền (Ví dụ: Tuổi chia thành: Thanh niên, Trung niên, Người già).
* **Dynamic discretization:** Chia khoảng động dựa trên phân phối thực tế của dữ liệu.
* **Clustering-based:** Phân cụm dữ liệu số một chiều trước, sau đó tìm luật kết hợp dựa trên khoảng cách giữa các cụm.



### 2.2. Các bước thực hiện (Khai phá dữ liệu định lượng)

1. **Bước 1: Rời rạc hóa (Discretization):** Chuyển đổi các thuộc tính dạng số (Quantitative attributes) thành các khoảng giá trị phân loại (Categorical variables) thông qua chia giỏ (binning) hoặc phân cụm (clustering).
2. **Bước 2: Ánh xạ đa chiều:** Lập bản đồ các thuộc tính này vào một khối dữ liệu (Data Cube) để phân tích tổng hợp.
3. **Bước 3: Khai phá mẫu:** Áp dụng các thuật toán như Apriori hoặc FP-Growth trên các khoảng dữ liệu đã được rời rạc hóa để tìm ra các luật kết hợp.

### 2.3. Ưu và Nhược điểm

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Multi-level Mining** | Phân tích sâu hơn, phát hiện luật ở nhiều mức độ chi tiết mà phân tích đơn cấp (Single-level) bỏ qua. | Phức tạp trong việc chọn đúng ngưỡng `min_sup` cho từng cấp độ. |
| **Multi-dimensional / Quantitative** | Cung cấp ngữ cảnh rộng hơn (nhân khẩu học + hành vi), rất mạnh mẽ trong Business Intelligence (BI). | Dễ gặp hiện tượng bùng nổ chiều (Curse of dimensionality), tính toán cực kỳ nặng nề. |

---

## 3. Tổng kết & Tra cứu nhanh (Cheatsheet)

### Bảng so sánh các phương pháp khai phá

| Tiêu chí | Single-Dimensional | Multi-Dimensional | Quantitative |
| --- | --- | --- | --- |
| **Số lượng vị từ (Predicate)** | 1 (Ví dụ: `buys()`) | $\ge 2$ (Ví dụ: `age()`, `income()`, `buys()`) | Có chứa thuộc tính số |
| **Loại dữ liệu xử lý** | Dạng danh nghĩa (Categorical) | Danh nghĩa (Categorical) | Dạng số (Numerical) |
| **Kỹ thuật bổ trợ cần thiết** | Không cần | Data Cube Aggregation | Discretization (Rời rạc hóa) |

### Từ khóa quan trọng

* **Level-reduced min-support:** Kỹ thuật giảm ngưỡng độ hỗ trợ khi đi sâu xuống các nhánh chi tiết của cây phân cấp.
* **Static vs Dynamic Discretization:** Hai phương pháp rời rạc hóa dữ liệu số; tĩnh (định trước khoảng) và động (dựa vào phân phối thực tế).
* **Deviation Analysis:** Phân tích độ lệch. Ví dụ: Nữ giới có mức lương trung bình 7$/h trong khi trung bình tổng thể là 9$/h (Phát hiện sự bất thường có ý nghĩa).

---

*Ghi chú: Nội dung được tổng hợp từ các tệp: 3.8 Mining Methods.pptx, 3.8 Mining Methods( cont_).pptx.*

---
