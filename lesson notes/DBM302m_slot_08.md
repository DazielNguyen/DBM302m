# **Slot 08 - Chapter 3 (Part 6): Mining Sequential Patterns**

**Ngày học: 30/01/2026**

**Nội dung chương học:**

* Slide 3.9: Mining Sequential Patterns

---

## 1. Tổng quan về Khai phá mẫu tuần tự (Sequential Patterns)

*Nguồn tham khảo: Slide 3.9*

### 1.1. Khái niệm cốt lõi

* **Sequence Database (Cơ sở dữ liệu tuần tự):** Khác với tập giao dịch thông thường (Transaction DB) chỉ quan tâm đến việc các món hàng xuất hiện cùng nhau, Sequence DB quan tâm đến **thứ tự thời gian** xuất hiện của chúng.
* **Sequential Pattern (Mẫu tuần tự):** Là các chuỗi con (subsequences) xuất hiện thường xuyên trong một tập hợp các chuỗi, thỏa mãn ngưỡng `min_sup`.
* *Ví dụ:* Khách hàng mua Laptop $\to$ 2 tháng sau mua Camera $\to$ 1 tháng sau mua Smartphone.


* **Gapped vs. Non-gapped:** * *Gapped (Có khoảng trống):* Hành vi mua sắm, click web (có thể có các hành động khác xen giữa).
* *Non-gapped (Không khoảng trống):* Chuỗi sinh học (DNA, Protein) bắt buộc phải nối tiếp nhau liên tục.



### 1.2. Quy trình/Kiến trúc

Thuộc tính Apriori (Apriori Property) vẫn đúng trong khai phá mẫu tuần tự:

* **Tính chất:** Nếu một chuỗi $S$ không phổ biến, thì không có bất kỳ chuỗi cha (super-sequence) nào chứa $S$ có thể phổ biến.
* **Quy trình chung:** Thuật toán sẽ tìm các mẫu tuần tự ngắn (độ dài 1), sau đó dùng chúng để sinh ra và kiểm tra các mẫu dài hơn, đồng thời cắt tỉa (prune) các nhánh chứa chuỗi con không phổ biến.

---

## 2. Các thuật toán khai phá mẫu tuần tự

*Nguồn tham khảo: Slide 3.9*

### 2.1. Nguyên lý hoạt động

Slide giới thiệu 4 phương pháp tiếp cận chính để giải quyết bài toán này:

* **GSP (Generalized Sequential Pattern):** Dựa trên nguyên lý Apriori (Sinh ứng viên và Kiểm tra). Quét CSDL nhiều lần để đếm tần suất của các chuỗi.
* **SPADE (Sequential Pattern Discovery using Equivalence classes):** Sử dụng **định dạng dữ liệu dọc (Vertical format)**. Thay vì quét CSDL ngang, nó theo dõi danh sách các ID giao dịch và vị trí thời gian để tính Support bằng phép giao (Intersection).
* **PrefixSpan (Prefix-projected Sequential Pattern mining):** Sử dụng chiến lược **Phát triển mẫu (Pattern-growth)** giống FP-Growth. Nó không sinh ứng viên mà dùng cơ sở dữ liệu chiếu (Projected databases).
* **CloSpan (Closed Sequential Patterns):** Chỉ khai phá các **mẫu tuần tự đóng** (không có chuỗi cha nào có cùng Support) để giảm số lượng mẫu trả về.

### 2.2. Các bước thực hiện (Đại diện: PrefixSpan)

1. **Bước 1 (Tìm mẫu độ dài 1):** Quét CSDL để tìm tất cả các mục phổ biến (Ví dụ: `<a>`, `<b>`, `<c>`).
2. **Bước 2 (Chiếu cơ sở dữ liệu - Projection):** Với mỗi mẫu độ dài 1 (gọi là tiền tố - prefix), tạo ra một CSDL chiếu chỉ chứa các phần hậu tố (hậu tố xuất hiện *sau* tiền tố đó trong các chuỗi gốc).
3. **Bước 3 (Phát triển đệ quy):** Lặp lại quá trình tìm mục phổ biến trên CSDL chiếu để kéo dài chuỗi tiền tố (Ví dụ: từ `<a>` phát triển thành `<ab>`).

### 2.3. Ưu và Nhược điểm

| Thuật toán | Chiến lược cốt lõi | Ưu điểm | Nhược điểm |
| --- | --- | --- | --- |
| **GSP** | Apriori (Ngang) | Dễ hiểu, mở rộng tốt từ bài toán Itemset. | Quét CSDL nhiều lần, sinh lượng ứng viên khổng lồ. |
| **SPADE** | Vertical Format | Nhanh hơn GSP, đếm Support qua phép giao nhanh chóng. | Tốn bộ nhớ để lưu trữ danh sách ID dọc. |
| **PrefixSpan** | Pattern Growth | Không sinh ứng viên, hiệu năng rất cao, thu hẹp CSDL sau mỗi lần chiếu. | Chi phí khởi tạo và duy trì các CSDL chiếu (Projected DBs). |

---

## 3. Tổng kết & Tra cứu nhanh (Cheatsheet)

### Bảng phân biệt Itemset vs. Sequential Pattern

| Đặc điểm | Itemset Mining (Ví dụ: Apriori/FPGrowth) | Sequential Pattern Mining (Ví dụ: PrefixSpan) |
| --- | --- | --- |
| **Yếu tố thời gian** | Không quan tâm. | **Cực kỳ quan trọng** (Thứ tự trước/sau). |
| **Định nghĩa tập hợp** | $\{A, B\}$ giống với $\{B, A\}$. | $\langle A \to B \rangle$ **khác** với $\langle B \to A \rangle$. |
| **Ứng dụng chính** | Phân tích giỏ hàng siêu thị (cùng 1 hóa đơn). | Phân tích hành trình khách hàng (nhiều hóa đơn theo thời gian), phân tích chuỗi DNA. |

### Từ khóa quan trọng

* **Subsequence (Chuỗi con):** Chuỗi được tạo thành bằng cách xóa một hoặc nhiều mục khỏi chuỗi gốc nhưng vẫn giữ nguyên thứ tự tương đối của các mục còn lại.
* **CloSpan:** Thuật toán kết hợp khai phá tuần tự (Sequential) và kỹ thuật nén mẫu đóng (Closed patterns) để giải quyết vấn đề bùng nổ số lượng mẫu.

---

*Ghi chú: Nội dung được tổng hợp từ tệp: 3.9 Mining Sequential Patterns.pptx.*

---

