# **Slot 4 - Chapter 3: Pattern Discovery (Khai phá mẫu)**

**Ngày học: 16/01/2026**

**Nội dung chương học:**
- 3.1 Introduction to Pattern Discovery in Data Mining

---

## 1. Tổng quan về Pattern Discovery

### 1.1. Pattern Discovery là gì?

Là quá trình tìm kiếm các quy luật (regularities) hoặc các mẫu (patterns) xuất hiện thường xuyên trong tập dữ liệu lớn.

* **Frequent Patterns (Mẫu phổ biến):** Là các mẫu (tập mục, chuỗi con, hoặc cấu trúc con) xuất hiện trong dữ liệu với tần suất không nhỏ hơn một ngưỡng do người dùng quy định.

* **Các loại mẫu chính:**
    * **Itemsets:** Tập hợp các mục (Ví dụ: {Sữa, Bánh mì}).
    * **Subsequences:** Chuỗi tuần tự (Ví dụ: Mua PC $\to$ Mua màn hình $\to$ Mua chuột).
    * **Substructures:** Cấu trúc con (Dùng trong đồ thị hoặc mạng lưới).

![02](/image_lesson_notes/slot_04/01-Mining-Frequent-Patterns-And-Association-Rules-3-2048.webp)

### 1.2. Tại sao cần Pattern Discovery?

Nó là nền tảng cho nhiều nhiệm vụ khai phá dữ liệu khác:

* Tìm ra các đặc tính nội tại của dữ liệu.
* Là cơ sở cho: Phân tích kết hợp (Association), Phân loại (Classification), và Phân cụm (Clustering) .

---

## 2. Market Basket Analysis (Phân tích giỏ hàng)

*Ví dụ kinh điển nhất của Pattern Discovery.*

* **Bối cảnh:** Tại quầy thu ngân siêu thị, dữ liệu mua sắm của khách hàng được ghi lại.
* **Mục tiêu:** Tìm ra thói quen mua sắm. *Ví dụ: Khách mua Bia thường sẽ mua thêm Tã lót (Beer & Diapers)*.
* **Ứng dụng:** Giúp bố trí kệ hàng, cross-sell (bán chéo), và up-sell (bán gia tăng).

Khái niệm này mô phỏng hành vi tại quầy thu ngân. Hình ảnh phổ biến nhất là ví dụ về "Bia và Tã lót" (Beer and Diapers).

**Giải thích đơn giản:**

* **Input:** Dữ liệu hóa đơn bán lẻ.
* **Goal:** Tìm mối quan hệ "Nếu mua A thì sẽ mua B".

* **Ví dụ:** Nếu một khách hàng mua *Bánh mì* và *Sữa*, xác suất họ mua thêm *Trứng* là bao nhiêu?

![02](/image_lesson_notes/slot_04/02-market-basket-analysis-example.webp)

---

## 3. Các khái niệm cốt lõi (Basic Concepts)

*Phần này chứa các định nghĩa toán học quan trọng để giải bài tập.*

### 3.1. Itemset (Tập mục)

* **Itemset($X$):** Một tập hợp chứa một hoặc nhiều mục (items).
* **k-itemset:** Một itemset chứa đúng $k$ mục.

### 3.2. Support (Độ hỗ trợ)

Đo lường độ phổ biến của một itemset.

* **Absolute Support (Tần suất tuyệt đối):** Số lần itemset $X$ xuất hiện trong cơ sở dữ liệu.
* **Relative Support (Tần suất tương đối - $s$):** Tỷ lệ phần trăm các giao dịch chứa $X$.

$$Support(X) = \frac{\text{Số giao dịch chứa } X}{\text{Tổng số giao dịch}}$$

### 3.3. Frequent Itemset (Tập phổ biến)

Một itemset $X$ được gọi là **Frequent** nếu độ hỗ trợ ($s$) của nó lớn hơn hoặc bằng ngưỡng tối thiểu (**min_sup**).

![03](/image_lesson_notes/slot_04/03-frequent-patterns-l.jpg)

---

## 4. Association Rules (Luật kết hợp)

### 4.1. Định nghĩa

Luật kết hợp là một quy tắc có dạng: **$X \to Y$**.

* Nghĩa là: Nếu có $X$, khả năng cao sẽ có $Y$.
* Điều kiện: $X, Y$ là các itemset và $X \cap Y = \emptyset$ (không trùng nhau).

### 4.2. Độ đo đánh giá luật (Rule Evaluation Metrics)

Để biết một luật có "mạnh" hay không, ta dùng 2 chỉ số:

1. **Support (s):** Xác suất cả $X$ và $Y$ cùng xuất hiện trong toàn bộ dữ liệu.

$$Support(X \to Y) = P(X \cup Y)$$

2. **Confidence (c):** Xác suất có $Y$ khi biết đã có $X$ (Độ tin cậy)

$$Confidence(X \to Y) = P(Y|X) = \frac{Support(X \cup Y)}{Support(X)}$$

> Rất nhiều bạn bị nhầm lẫn giữa hai khái niệm này. Hãy nhìn vào công thức và biểu đồ dưới đây:

**Cách nhớ nhanh:**

* **Support (Độ phổ biến):** Trả lời câu hỏi *"Cặp đôi này có hay xuất hiện không?"*.
* Nếu bạn bán được 100 đơn, mà có 5 đơn chứa cả (Bia, Tã)  Support = 5/100 = 5%.
* Nếu Support quá thấp (ví dụ 0.001%), có thể đó chỉ là sự ngẫu nhiên, không đáng quan tâm.

* **Confidence (Độ tin cậy):** Trả lời câu hỏi *"Nếu đã lấy món A rồi, thì chắc bao nhiêu % sẽ lấy món B?"*.
* Trong 10 người mua Bia, có 7 người mua thêm Tã  Confidence (Bia  Tã) = 70%.
* Đây là chỉ số quan trọng để quyết định độ mạnh của luật.



### 4.3. Quy trình khai phá (Mining Roadmap)

Để tìm ra luật kết hợp, ta làm 2 bước:

1. **Find Frequent Itemsets:** Tìm tất cả các itemset có $support \ge min\_sup$. *(Bước này tốn nhiều tài nguyên máy tính nhất)*.


2. **Generate Strong Rules:** Từ các frequent itemsets, tạo ra các luật có $confidence \ge min\_conf$.

---

## 5. Nén mẫu (Compressed Patterns)

Khi dữ liệu lớn, số lượng *Frequent Patterns* tìm được có thể cực kỳ nhiều, gây khó khăn cho việc lưu trữ và phân tích. Ta cần các dạng nén:

### 5.1. Closed Pattern (Mẫu đóng) - Nén không mất tin (Lossless)

Một itemset $X$ là **Closed** nếu:

1. $X$ là frequent (phổ biến).
2. Không có "mẫu cha" (super-pattern) nào của $X$ có cùng giá trị Support với $X$.

* *Ý nghĩa:* Lưu trữ Closed patterns giúp giữ lại thông tin đầy đủ về Support nhưng loại bỏ các mẫu dư thừa.

![04](/image_lesson_notes/slot_04/04-chpt2interSec4Fig2.jpg)

### 5.2. Max Pattern (Mẫu cực đại) - Nén có mất tin (Lossy)

Một itemset $X$ là **Max** nếu:

1. $X$ là frequent.
2. Không có "mẫu cha" nào của $X$ là frequent.

* *Ý nghĩa:* Chỉ quan tâm xem mẫu dài nhất là gì, không quan tâm tần suất của các mẫu con. Giúp giảm số lượng mẫu đáng kể.

![05](/image_lesson_notes/slot_04/05-maximalfrequent.jpg)

---

## 6. Tổng kết & Tra cứu nhanh (Cheatsheet)

### Bảng công thức quan trọng

| Chỉ số | Công thức | Ý nghĩa |
| --- | --- | --- |
| **Support** | $P(A \cup B)$ | Tần suất A và B cùng xuất hiện trên tổng số. |
| **Confidence** | $\frac{Support(A \cup B)}{Support(A)}$ | Nếu mua A thì bao nhiêu % sẽ mua B? |
| **Strong Rule** | $\ge min\_sup$ VÀ $\ge min\_conf$ | Luật đủ mạnh để xem xét. |

### So sánh Closed vs Max Pattern

| Loại mẫu | Định nghĩa ngắn gọn | Đặc điểm nén |
| --- | --- | --- |
| **Frequent** | $Sup \ge min\_sup$ | Dạng cơ bản, số lượng rất lớn. |
| **Closed** | Không có cha nào cùng Support | **Lossless** (Không mất thông tin). |
| **Max** | Không có cha nào là Frequent | **Lossy** (Mất thông tin support con), gọn nhất. |




### Frequent, Closed, và Max Patterns (Các dạng mẫu)

Đây là phần khó hiểu nhất về mặt lý thuyết tập hợp. Để dễ hình dung, người ta thường dùng biểu đồ dạng lưới (Lattice) để minh họa mối quan hệ cha-con.

**Giải thích bằng ví dụ:**
Giả sử bạn có dữ liệu xuất hiện như sau trong cơ sở dữ liệu:

* Mẫu `{A, B}` xuất hiện 100 lần.
* Mẫu con `{A}` xuất hiện 100 lần.
* Mẫu con `{B}` xuất hiện 100 lần.

**Phân biệt:**

1. **Frequent Itemset:** Cả `{A}`, `{B}`, `{A, B}` đều là Frequent (nếu ngưỡng min_sup < 100).
* *Vấn đề:* Lưu hết cả 3 cái thì tốn chỗ quá, vì thông tin bị lặp lại.


2. **Closed Pattern (Nén không mất tin):**
* Ta thấy `{A, B}` xuất hiện 100 lần. `{A}` cũng 100 lần.
* Tức là: Cứ hễ thấy A là thấy B đi cùng. `{A}` không cung cấp thêm thông tin gì mới về tần suất so với `{A, B}`.
*  Ta chỉ cần lưu `{A, B}` là đủ. `{A, B}` là Closed Pattern.
* 
*Định nghĩa:* Một mẫu là Closed nếu không có mẫu cha nào có **cùng tần suất** với nó.


3. **Max Pattern (Nén tối đa - chấp nhận mất chi tiết):**
* Giả sử `{A, B, C}` là mẫu dài nhất thỏa mãn ngưỡng (Frequent).
* Ta chỉ lưu `{A, B, C}` và bỏ qua tất cả các con của nó (`{A,B}`, `{A}`, `{B,C}`...).
* 
*Định nghĩa:* Một mẫu là Max nếu không có mẫu cha nào là Frequent.


* *Nhược điểm:* Bạn biết `{A, B}` là phổ biến, nhưng bạn không biết chính xác tần suất của `{A, B}` là bao nhiêu, chỉ biết nó  min_sup.

### Tóm tắt trực quan:

* **Frequent Patterns:** Tất cả các mẫu thỏa mãn (Rất nhiều, Rất nặng).
* **Closed Patterns:** Tập con thu gọn, giữ nguyên thông tin về tần suất (Gọn hơn, Đủ tin).
* **Max Patterns:** Tập con gọn nhất, chỉ giữ lại "biên giới" của các mẫu phổ biến (Gọn nhất, Mất tin tần suất).