# **Slot 6 - Chapter 3 (Part 3): Mining Closed Patterns & Evaluation**

**Ngày học: 23/01/2026**
**Nội dung chương học:**

* 3.6 Mining Closed Patterns
* 3.7 Pattern Evaluation

---

## I. Mining Closed Patterns - Khai phá mẫu đóng (Slide 3.6)

### 1. Giới thiệu về Close Pattern (Mẫu đóng)

* **Các mẫu đóng** là một dạng biểu diễn cô đọng của các mẫu thường xuyên xuất hiện.
* **Một mẫu đóng** là một **mẫu hoàn chỉnh không thể mở rộng thêm** mà không làm giảm độ hỗ trợ (Support) của nó.
* **Khai thác các mẫu đóng** cung cấp một tập hợp các mẫu ngắn gọn và có ý nghĩa mà không có sự dư thừa.
* **Mục đích của Close Pattern:** Là mẫu gồm đầy đủ và lớn nhất mà vẫn giữ được giá trị Support đó.

![02-Close-Open-Pattern)](/image_lesson_notes/slot_06/02-Close-Open-Pattern%20Large.jpeg)

> **Minh họa thêm về ghi chú của bạn:**
> * **Mẫu mở (Giữ nguyên số):** Giả sử tập `{Bia}` có Support là 10. Nếu bạn thêm vào thành `{Bia, Tã}` mà Support vẫn là 10, thì `{Bia}` là mẫu mở. Nó chưa "đóng" vì có thể mở rộng thêm mà không làm mất đi tần suất xuất hiện.
> * **Mẫu đóng (Thay đổi số):** Nếu bạn thêm bất kỳ món nào khác vào tập `{Bia, Tã}` (ví dụ `{Bia, Tã, Sữa}`) mà Support giảm xuống còn 5, thì tập `{Bia, Tã}` chính là **Mẫu đóng**. 

### 2. Phương pháp chung

* Phương pháp chung để khai thác các mẫu đóng bao gồm các bước sau:
* **Khám phá tất cả các mẫu** thường xuyên bằng cách sử dụng thuật toán thích hợp (ví dụ: Apriori hoặc FPGrowth).
* Xác định các mẫu đóng từ tập hợp các mẫu thường xuyên.
* Loại bỏ các mẫu dư thừa bị bao hàm bởi các mẫu đóng khác.



### 3. Các Thuật Toán về Khai Phá Mẫu Đóng

**Depth-First Search (DFS) Approach:**

* Sử dụng chiến lược tìm kiếm theo **chiều sâu** để duyệt qua lưới mẫu.
* Loại bỏ các tập mục không thường xuyên ngay từ đầu dựa trên các ràng buộc về độ hỗ trợ.
* Tránh việc khám phá dư thừa các mẫu đã đóng để tăng tốc độ.

**PrefixSpan Algorithm:**

* Dựa trên khai thác mẫu tuần tự. Sử dụng chiến lược **chia để trị** đệ quy.
* Sử dụng cơ sở dữ liệu chiếu (Projected databases) để tìm các mẫu khép kín hiệu quả.

**Max-Miner Algorithm:**

* Tập trung vào **Max-itemsets** (Tập mục thường xuyên tối đa).
* Sử dụng phương pháp từ trên xuống (Top-down) để tìm các tập hợp mục lớn nhất không phải là tập con của bất kỳ tập thường xuyên nào khác.

**CLOSET+: Mining Closed Itemsets by Pattern-Growth:**

* Khai thác trực tiếp và hiệu quả các tập mục đóng.
* **Kỹ thuật Item merging:** Nếu Y luôn xuất hiện cùng với X (tần suất bằng nhau), thì Y được gộp vào X ngay lập tức.
* Ví dụ minh họa từ slide:
`d-proj. db: {acef, acf} -> acfd-proj. db: {e}, kết quả nhận được mẫu đóng: acfd:2`

### 4. Ưu điểm của Khai Phá Mẫu Đóng

* **Concise Pattern Representation:** Cung cấp biểu diễn không dư thừa, giảm số lượng mẫu cần phân tích.
* **Enhanced Efficiency:** Xử lý nhanh hơn do tránh tạo ra các mẫu dư thừa.
* **Reduced Pattern Analysis:** Nắm bắt những mẫu quan trọng và giàu thông tin nhất, đơn giản hóa việc giải thích dữ liệu.

### 5. Ứng dụng của Closed Pattern Mining

* **Association Rule Mining:** Tạo ra các luật liên kết không trùng lặp và có ý nghĩa hơn.
* **Anomaly Detection:** Hỗ trợ xác định các hành vi hiếm gặp hoặc bất thường.
* **Recommender Systems:** Cung cấp đề xuất cá nhân hóa dựa trên các tập mục có tiện ích cao.

### 6. Tóm tắt & Tra cứu nhanh (Cheatsheet)

| Tiêu chí | Frequent Itemset | Closed Itemset | Max-Itemset |
| --- | --- | --- | --- |
| **Định nghĩa** | Support≥min_sup | Không có tập cha nào có cùng Support | Không có tập cha nào là Frequent |
| **Tính bảo toàn** | Đầy đủ thông tin | **Lossless** (Không mất tin) | **Lossy** (Mất tin support con) |
| **Kích thước** | Lớn nhất | Trung bình | Nhỏ nhất (Gọn nhất) |

**Từ khóa quan trọng:**

* **Lossless Compression:** Nén không mất thông tin (Closed Pattern).
* **Item Merging:** Kỹ thuật gộp các mục luôn đi cùng nhau để giảm không gian tìm kiếm.
* **Sub-itemset Pruning:** Cắt tỉa các tập con để tránh tính toán dư thừa.

---

## II. Pattern Evaluation (Đánh giá Mẫu). 

### 1. Sự cần thiết của đánh giá mẫu

### 1.1. Khái niệm cốt lõi

* **Interestingness Measures (Độ đo sự thú vị):** Một quy trình khai phá có thể tạo ra hàng nghìn luật, nhưng không phải luật nào cũng hữu ích. Độ đo này giúp lọc ra các luật thực sự có giá trị.
* **Objective Measures (Độ đo khách quan):** Dựa trên thống kê và cấu trúc dữ liệu (Support, Confidence, Lift).
* **Subjective Measures (Độ đo chủ quan):** Dựa trên cái nhìn của người dùng. Một mẫu là thú vị nếu nó:
* Phù hợp với truy vấn người dùng (Query-based).
* Gây bất ngờ, đi ngược lại hiểu biết thông thường (Unexpectedness).
* Có tính mới hoặc tính thời điểm (Actionable).



### 1.2. Hạn chế của Support và Confidence

Support và Confidence đôi khi có thể gây hiểu lầm. Một luật có Confidence cao chưa chắc đã phản ánh một mối quan hệ thực sự nếu các món hàng đó vốn dĩ đã rất phổ biến.

* **Ví dụ:** Nếu 90% khách hàng mua Sữa, và 80% khách hàng mua Bánh mì. Luật $\{Sữa\} \to \{Bánh mì\}$ có thể có Confidence cao đơn giản vì cả hai đều bán chạy, chứ không phải vì khách mua cái này thì sẽ mua cái kia.


### 2. Các độ đo tương quan (Correlation Measures)
### 2.1. Lift (Độ nâng)

* **Tư duy:** Kiểm tra xem sự xuất hiện của A và B có độc lập với nhau hay không.
* **Công thức:**

$$Lift(A, B) = \frac{P(A \cup B)}{P(A)P(B)} = \frac{Confidence(A \to B)}{Support(B)}$$

* **Ý nghĩa:**
* **Lift > 1:** A và B có tương quan dương (Mua A thúc đẩy mua B).
* **Lift = 1:** A và B độc lập.
* **Lift < 1:** A và B tương quan âm (Mua A làm giảm khả năng mua B).



### 2.2. Chi-square ($\chi^2$) Analysis

* **Tư duy:** Kiểm tra xem sự khác biệt giữa tần suất quan sát được và tần suất mong đợi (nếu độc lập) có ý nghĩa thống kê hay không.

### **Công thức Chi-bình phương ($\chi^2$)**

$$\chi^2 = \frac{N \times (ad - bc)^2}{(a + c)(b + d)(a + b)(c + d)}$$


**Trong đó:**

- $a$: Độ hỗ trợ (Support) của cả $A$ và $B$.
- $b$: Độ hỗ trợ của $B$ mà không có $A$.
- $c$: Độ hỗ trợ của $A$ mà không có $B$.
- $d$: Các giao dịch còn lại (không chứa cả $A$ và $B$).
- $N$: Tổng số lượng giao dịch ($N = a + b + c + d$).

**Giải thích ý nghĩa**

* **Giá trị  càng cao:** Cho thấy sự phụ thuộc lẫn nhau giữa các mục ( và ) càng mạnh.
* **Giá trị  càng thấp:** Gợi ý rằng các mục có mối quan hệ yếu hoặc độc lập với nhau.

* **Ý nghĩa:** Nếu giá trị $\chi^2$ vượt quá một ngưỡng nhất định, ta bác bỏ giả thuyết độc lập $\to$ A và B có tương quan.

## 3. Null-Invariant Measures (Độ đo bất biến với giá trị Null)

Trong dữ liệu lớn, số lượng giao dịch không chứa cả A và B (Null transactions) là rất lớn. Các độ đo như Lift hay $\chi^2$ bị ảnh hưởng nặng nề bởi số lượng Null này, dẫn đến kết quả sai lệch. Ta cần các độ đo  **Null-invariant**.

### 3.1. Các chỉ số quan trọng

- **Jaccard Index:** Tỷ lệ giao nhau trên tập hợp.
- **Cosine Similarity:** Đo góc giữa hai vector tần suất.
- **Kulczynski (Kulc) Measure:** Trung bình cộng của Confidence hai chiều:
$$Kulc(A, B) = \frac{1}{2} (P(A|B) + P(B|A))$$
- **Imbalance Ratio (IR):** Đo sự mất cân bằng về tần suất giữa A và B:
$$IR(A, B) = \frac{|Support(A) - Support(B)|}{Support(A) + Support(B) - Support(A \cup B)}$$


* **Imbalance Ratio (IR):** Đo sự mất cân bằng về tần suất giữa A và B:



### 3.2. Tư duy kết hợp (Kulc + IR)

Để đánh giá một luật một cách toàn diện nhất trên tập dữ liệu lớn:

1. Sử dụng **Kulc** để xem độ gắn kết mạnh hay yếu (Gần 1 là mạnh).
2. Sử dụng **IR** để xem sự gắn kết đó có cân bằng không. Nếu IR cao, nghĩa là một món rất phổ biến còn món kia thì rất hiếm.

---

## 4. Tổng kết & Tra cứu nhanh (Cheatsheet)

### Bảng so sánh các độ đo sự thú vị

| Độ đo | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Confidence** | Dễ hiểu, phổ biến. | Dễ gây hiểu lầm nếu items quá phổ biến. |
| **Lift** | Đo được tương quan âm/dương. | Bị ảnh hưởng bởi số lượng giao dịch trống (Null). |
| **Kulc** | **Null-invariant**, hiệu quả với Big Data. | Cần kết hợp với IR để thấy bức tranh toàn cảnh. |
| **Cosine** | Tốt cho dữ liệu dạng văn bản/vector. | Không phản ánh rõ tính imbalance như Kulc + IR. |

### Từ khóa quan trọng

* **Null-invariant:** Đặc tính không thay đổi kết quả khi thêm vào hàng triệu giao dịch không liên quan.
* **Correlation vs Association:** Khai phá mẫu không chỉ tìm sự kết hợp (Association) mà còn phải tìm sự tương quan (Correlation).
* **Strong Rule:** Luật thỏa mãn cả `min_sup`, `min_conf` và có độ đo tương quan (như Lift hoặc Kulc) tốt.


