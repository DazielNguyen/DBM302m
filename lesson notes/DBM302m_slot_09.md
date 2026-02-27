# **Slot 09 - Chapter 3 (Part 7): Mining Sequential Patterns (Continuation)**

**Ngày học: 03/02/2026** 

**Nội dung chương học:**

* Slide 3.9 (cont.): Mining Sequential Patterns - GSP Algorithm

---

## 1. Khai phá mẫu tuần tự và Ứng dụng

*Nguồn tham khảo: Slide 3.9 (cont_)*

### 1.1. Khái niệm cốt lõi

* **Sequential Patterns (Mẫu tuần tự):** Là các mẫu nắm bắt **thứ tự thời gian** (temporal order) của các sự kiện hoặc các mục trong một chuỗi. Chúng đại diện cho các chuỗi con hoặc chuỗi sự kiện xuất hiện thường xuyên trong dữ liệu.
* **Tầm quan trọng:** Giúp khám phá các mối phụ thuộc theo thời gian (temporal dependencies). Khác với luật kết hợp thông thường (chỉ biết A và B được mua cùng nhau), mẫu tuần tự cho biết A xảy ra *trước* B.

### 1.2. Ứng dụng thực tế

* **Market Basket Analysis (Phân tích giỏ hàng):** Xác định các chuỗi mua hàng thường xuyên. *Ví dụ: Khách hàng mua điện thoại $\to$ 1 tuần sau mua ốp lưng $\to$ 1 tháng sau mua tai nghe.*
* **Web Log Analysis (Phân tích log trang web):** Phân tích luồng click chuột (clickstreams) để hiểu hành vi duyệt web của người dùng, từ đó tối ưu hóa giao diện hoặc gợi ý nội dung.

---

## 2. GSP Algorithm (Generalized Sequential Pattern)

*Nguồn tham khảo: Slide 3.9 (cont_)*

### 2.1. Nguyên lý hoạt động

* **Tư duy:** GSP dựa trên phương pháp tiếp cận **Apriori-based**. Nó sử dụng nguyên lý cắt tỉa quen thuộc: *Nếu một chuỗi không phổ biến, thì mọi chuỗi cha chứa nó cũng không thể phổ biến.*
* **Cơ chế:** Quét cơ sở dữ liệu nhiều lần. Bắt đầu từ các chuỗi độ dài 1, sau đó sinh ứng viên (candidate generation) cho các chuỗi độ dài lớn hơn và đếm tần suất.

### 2.2. Các bước thực hiện (Theo chuẩn Apriori)

1. **Bước 1 (Khởi tạo):** Quét CSDL để tìm tất cả các mục đơn lẻ phổ biến (chuỗi có độ dài 1).
2. **Bước 2 (Sinh ứng viên):** Ghép các chuỗi phổ biến ở vòng trước để tạo ra các chuỗi ứng viên mới dài hơn 1 phần tử.
3. **Bước 3 (Cắt tỉa - Pruning):** Dựa vào tính chất Apriori, loại bỏ ngay các chuỗi ứng viên chứa chuỗi con không phổ biến.
4. **Bước 4 (Đếm Support):** Quét lại CSDL một lần nữa để đếm tần suất xuất hiện thực tế của các ứng viên còn lại. Lặp lại từ Bước 2 cho đến khi không tìm thêm được mẫu nào.

### 2.3. Ưu và Nhược điểm của GSP

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **GSP Algorithm** | Dễ hiểu, tận dụng tốt nguyên lý Apriori để cắt tỉa. Cho phép tùy chỉnh ngưỡng `min_sup` linh hoạt. | Chi phí tính toán cực kỳ lớn (Computational Complexity). Phải quét CSDL nhiều lần và sinh ra lượng ứng viên khổng lồ khi dữ liệu lớn. |

---

## 3. Tổng kết & Tra cứu nhanh (Cheatsheet)

### Bảng tóm tắt các thách thức

| Thách thức | Giải pháp / Lưu ý |
| --- | --- |
| **Độ phức tạp tính toán** | Cần áp dụng các kỹ thuật tối ưu hóa như lập chỉ mục (indexing) hoặc các chiến lược cắt tỉa nâng cao. |
| **Chọn tham số (Parameter Tuning)** | Ngưỡng `min_sup` quá cao $\to$ mất mẫu quan trọng. Ngưỡng quá thấp $\to$ bùng nổ dữ liệu rác. Cần thử nghiệm và kiến thức ngành (domain knowledge). |
| **Nhiễu dữ liệu** | Yêu cầu bước Tiền xử lý (Data Preprocessing) kỹ lưỡng để lọc bỏ nhiễu trước khi chạy thuật toán. |

### Từ khóa quan trọng

* **Temporal Order (Thứ tự thời gian):** Yếu tố cốt lõi phân biệt Mining Sequential Patterns với Mining Frequent Itemsets thông thường.
* **Candidate Generation & Pruning:** Hai bước xương sống của thuật toán GSP (kế thừa từ Apriori).

---

*Ghi chú: Nội dung được tổng hợp từ tệp: 3.9 Mining Sequential Patterns( cont_).pptx.*

---
