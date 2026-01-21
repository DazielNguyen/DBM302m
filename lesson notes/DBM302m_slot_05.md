# **Slot 5 - Chapter 3 (Part 2): Mining Algorithms**
**Ngày học: 20/01/2026**
**Nội dung chương học:**

- 3.2 The Apriori Algorithm
- 3.4 Mining Frequent Patterns by Exploring Vertical Data Format
- 3.5 FPGrowth - A Pattern Growth Approach

**Note:**

$\cap$ $\to$ (Intersection - Giao) là lấy phần chung của 2 Tập

$\cup$ $\to$ (Union - Hợp) là lấy hết của 2 Tập

---
**Tổng quan:**
Sau khi đã hiểu các khái niệm cơ bản (Itemset, Support, Confidence) ở phần trước, vấn đề lớn nhất của Data Mining là hiệu năng. Với hàng triệu giao dịch, việc đếm thủ công là bất khả thi. Phần này giới thiệu 3 chiến lược cốt lõi để giải quyết bài toán tìm **Frequent Itemsets** một cách hiệu quả.

---

## 1. The Apriori Algorithm (Thuật toán Apriori) (Slide 3.2) -> Biểu diễn theo định dạng ngang Horizontal. 

Đây là thuật toán đầu tiên và kinh điển nhất, sử dụng kiến thức trước (prior knowledge) về tính chất của tập phổ biến.

### 1.1. Nguyên lý Apriori (The Apriori Property)

Thuật toán dựa trên nguyên lý **"Đóng giảm" (Downward Closure Property)** để thu hẹp không gian tìm kiếm:

> **Nguyên lý:** Nếu một tập mục (itemset) là phổ biến (frequent), thì **tất cả** các tập con (subsets) của nó cũng phải phổ biến.

* **Ý nghĩa thực tiễn (Cắt tỉa):** Nếu một tập mục con là **không phổ biến** (infrequent), thì tập cha chứa nó chắc chắn không phổ biến. Ta có thể cắt bỏ (prune) nhánh này ngay lập tức mà không cần tính toán thêm.

### 1.2. Quy trình thực hiện (Iterative Approach)

Apriori hoạt động theo cơ chế lặp (Level-wise approach): Tìm tập phổ biến 1-itemset ($L_1$), dùng nó để tìm $L_2$, rồi $L_3$....

Mỗi vòng lặp gồm 2 bước chính:

1. **Join Step (Bước kết nối):** Tạo ra tập ứng viên $C_k$ (độ dài k) bằng cách nối tập phổ biến $L_{k-1}$ với chính nó.
2. **Prune Step (Bước cắt tỉa):**
* Dựa trên nguyên lý Apriori: Loại bỏ bất kỳ ứng viên nào trong $C_k$ nếu nó chứa một tập con kích thước $(k-1)$ không nằm trong $L_{k-1}$
* Đếm tần suất (support) của các ứng viên còn lại trong Database và giữ lại các tập thỏa mãn $min\_sup$.

![01-Apriori-Example](/image_lesson_notes/slot_05/01-Example-Apriori.png)
> Ví dụ về thuật toán Apriori

### 1.3. Nhược điểm (Bottlenecks)

Dù đơn giản, Apriori gặp 2 vấn đề lớn khi dữ liệu lớn:

* **Quét CSDL nhiều lần:** Cần quét toàn bộ Database $k$ lần để tìm mẫu có độ dài $k$.
* **Bùng nổ ứng viên:** Số lượng ứng viên ($C_k$) có thể cực kỳ lớn (hàng triệu), tiêu tốn bộ nhớ và thời gian tính toán.

### 1.4 Điểm mạnh và Yếu của thuật toán Apriori

**Ưu điểm của thuật toán Apriori**

- Tính đơn giản: Thuật toán này đơn giản, dễ hiểu và dễ triển khai.
- Khả năng mở rộng: Nó có thể xử lý hiệu quả các tập dữ liệu lớn bằng cách sử dụng thuộc tính đóng xuống.
- Tính đầy đủ: Thuật toán Apriori đảm bảo tìm thấy tất cả các tập mục thường xuyên.

**Nhược điểm của thuật toán Apriori**

- Chi phí tính toán: Việc tạo ra một số lượng lớn các tập hợp mục ứng cử viên và quét tập dữ liệu nhiều lần có thể tốn kém về mặt tính toán.
- Sử dụng bộ nhớ: Thuật toán yêu cầu một lượng bộ nhớ đáng kể để lưu trữ các tập hợp mục ứng cử viên và số lượng hỗ trợ.
- Không hiệu quả với dữ liệu thưa: Trong các tập dữ liệu có ngưỡng hỗ trợ thấp hoặc các tập hợp mục thưa, thuật toán có thể hoạt động không hiệu quả.

---

## 2. Mining with Vertical Data Format (ECLAT) (Slide 3.4)

Kỹ thuật này (thường gọi là ECLAT) thay đổi **cấu trúc dữ liệu** để tránh việc quét Database lặp lại.

### 2.1. Chuyển đổi định dạng (Vertical Format)

Thay vì lưu trữ theo chiều ngang (Giao dịch chứa những món nào?), ta lưu theo chiều dọc (Món hàng xuất hiện trong những giao dịch nào?).

* **Horizontal:** $Tid \to \{item_1, item_2, ...\}$.
* **Vertical:**  $Item \to \{Tid_1, Tid_2, ...\}$ (Tập hợp các ID giao dịch - gọi là Tid-set).

![02-ECLAT](/image_lesson_notes/slot_05/02-ECLAT.png)
> Biểu đồ thể hiện 2 cách lưu trữ khác nhau

### 2.2. Cơ chế tính toán (Intersection)

Để tìm Support của tập $\{A, B\}$, ta không cần đếm.  Ta chỉ cần lấy **giao của hai tập Tid**:

$$Tidset(A) \cap Tidset(B) = Tidset(AB)$$

* Độ dài của tập giao chính là Support.
* **Ưu điểm:** Biến bài toán đếm thành bài toán cắt/giao tập hợp, không cần quét lại Database gốc.

### 2.3 Ưu điểm của Vertical Data Format (Định dạng dọc)

**Compact Data Representation: Biểu diễn dữ liệu gọn nhẹ**

- Định dạng dọc giảm thiểu sự trùng lặp bằng cách lưu trữ mỗi mục một lần, cùng với các giao dịch tương ứng.
- Yêu cầu **ít bộ nhớ hơn so với định dạng ngang.**

**Efficient Support Counting: Đếm hỗ trợ hiệu quả**

- Định dạng dọc cho phép đếm hỗ trợ tập hợp mục một cách hiệu quả.
- Giảm số lần duyệt qua tập dữ liệu, dẫn đến hiệu suất được cải thiện.

**Items Table: Bảng Mặt hàng**
- Chứa danh sách các mặt hàng duy nhất có trong tập dữ liệu.
- Mỗi mặt hàng được liên kết với một tập hợp các mã định danh giao dịch (TID) nơi nó xuất hiện.

**Transaction Table: Bảng Giao dịch**
- Lưu trữ các mã định danh giao dịch và các mặt hàng liên kết với mỗi giao dịch.
- Cho phép truy cập nhanh chóng

### 2.4 Các thuật toán khai thác các Pattern thường xuyên trong định dạng dọc Vertical Format

**Thuật toán Bitmap dọc (Vertical Bitmap - VB):**

- Sử dụng biểu diễn bitmap để đếm số lần xuất hiện của các tập mục một cách hiệu quả.
- Thực hiện các phép toán bitwise để thực hiện giao và hợp của các bitmap.

> Giải thích đơn giản: Bitmap ở đây là dùng AND, OR, XOR,.. 

> [A______B______C______D]

> [0______1______0______1]

> [0______0______1______0]

> Biểu diễn dưới dạng 0, 1. Như 0 là hết hàng, 1 là còn hàng. 

**Thuật toán Hỗ trợ tối thiểu dọc (Vertical Minimum Support - VMS):**

- Áp dụng thuộc tính đóng xuống để loại bỏ các tập mục ít xuất hiện.
- Quét bảng giao dịch và duy trì số lần xuất hiện cho mỗi mục.

> Áp dụng tính chất DownWard -> Tập cha muốn phổ biến thì tất cả nhánh con phải phổ biến

**Thuật toán Mẫu tối đa dọc (Vertical Maximal Patterns - VMP):**

- Tập trung vào việc tìm kiếm các tập mục xuất hiện nhiều nhất (các tập mục không bị bao hàm bởi bất kỳ tập mục xuất hiện nhiều nào khác).
- Sử dụng định dạng dữ liệu dọc và áp dụng chiến lược tìm kiếm theo chiều rộng.

> Hiểu nôm na là mẫu cực đại. 

> Ví dụ: Tập A[1, 2, 3]  ;  B[1, 2, 3, 4] Tìm [1, 2, 3]

> Nó sẽ lấy tập B. Những tập nào không nằm trong tập họp khác thì sẽ là mẫu cực đại

### 2.5 Lợi ích của việc khai thác các Frequent Patterns

**Improved Performance - Cải thiện hiệu suất:**

- Vertical data format (Định dạng dữ liệu dọc) giảm số lần duyệt qua tập dữ liệu, dẫn đến khai thác nhanh hơn.
- Cho phép đếm hỗ trợ và các kỹ thuật cắt tỉa hiệu quả.

**Scalability - Khả năng mở rộng:**

- Vertical format đặc biệt hữu ích cho các tập dữ liệu quy mô lớn với nhiều giao dịch và mặt hàng.
- Xử lý hiệu quả các tập mặt hàng đa chiều.

### 2.6 Application - Ứng dụng hiện nay.

- Phân tích giỏ hàng để hiểu hành vi khách hàng.
- Tin sinh học để khám phá mối liên hệ giữa các gen. Phân tích những bộ Gen lỗi,....
- Khai thác dữ liệu web để xác định các mẫu hành vi người dùng.

---

## 3. FP-Growth (Frequent Pattern Growth) - (Slide 3.5)

Đây là thuật toán hiện đại, giải quyết triệt để nhược điểm "sinh ứng viên" của Apriori.

### 3.1. Ý tưởng cốt lõi: Chia để trị (Divide-and-Conquer)

FPGrowth là một thuật toán phổ biến để khai thác các mẫu thường xuyên xuất hiện trong các tập dữ liệu giao dịch.

FP-Growth **không sinh ứng viên (No candidate generation)**. Nó nén dữ liệu vào một cấu trúc cây gọi là **FP-Tree**, sau đó chia nhỏ cây này để khai phá.

### 3.2. Cấu trúc FP-Tree

FP-Tree là cấu trúc nén cao độ nhưng giữ nguyên thông tin liên kết của các tập mục.

* **Quy trình xây dựng (Chỉ 2 lần quét DB):**
1. **Scan 1:** Đếm tần suất các item, loại bỏ các item không phổ biến, và sắp xếp item theo tần suất giảm dần (Frequency descending).
2. **Scan 2:** Đọc từng giao dịch và chèn vào cây. Các giao dịch có chung phần đầu (prefix) sẽ dùng chung nhánh cây, giúp nén dữ liệu.



### 3.3. Quy trình khai phá (Pattern Growth)

**Recursive Mining (Khai thác đệ quy):**

- Thực hiện duyệt theo chiều sâu của cây FP để khai thác các mẫu thường xuyên.
- Mỗi đường dẫn trong cây FP đại diện cho một mẫu thường xuyên.

**Conditional Pattern Base and Conditional FP-Tree (Cơ sở mẫu có điều kiện và cây FP có điều kiện):**

- Trích xuất cơ sở mẫu có điều kiện cho mỗi mục thường xuyên trong cây FP.
- Xây dựng cây FP có điều kiện cho mỗi mục thường xuyên bằng cách sử dụng cơ sở mẫu có điều kiện tương ứng của nó.

**Recursive Tree Growth (Phát triển cây đệ quy):**

- Áp dụng thuật toán FPGrowth một cách đệ quy cho mỗi cây FP có điều kiện.

- Tạo ra các mẫu thường xuyên bằng cách thêm mục thường xuyên vào mỗi đường dẫn trong cây FP có điều kiện.

Thay vì kiểm tra toàn bộ, thuật toán phát triển mẫu (Pattern Growth) từ các mẫu ngắn:

1. Bắt đầu từ item có tần suất thấp nhất trong cây (dưới đáy Header Table).
2. Tìm **Conditional Pattern Base**: Tất cả các đường dẫn từ gốc đến item đó.
3. Xây dựng **Conditional FP-Tree**: Cây con chỉ chứa các đường dẫn liên quan.
4. Đệ quy khai phá trên cây con này.

![03-FP](/image_lesson_notes/slot_05/03-FP_Growth.png)

> Ví dụ: Xây dựng cây FP từ cơ sở dữ liệu dịch thuật

### 3.4. Ưu điểm vượt trội

* **Hiệu quả:** Không cần sinh tập ứng viên giả (candidate generation) và giảm chi phí tính toán.
* **Tốc độ:** Nhanh hơn Apriori ít nhất một bậc độ lớn, đặc biệt khi dữ liệu dày đặc. Nó tận dụng cấu trúc cây FP để tăng tốc độ khám phá các mẫu thường xuyên.
* **Tiết kiệm I/O:** Chỉ cần quét Database đúng 2 lần, bất kể mẫu dài bao nhiêu. FPGrowth xử lý hiệu quả các tập dữ liệu có số lượng lớn các mục và tập hợp mục đa chiều. Nó đặc biệt hiệu quả trong việc khai thác các mẫu phức tạp trong các tập dữ liệu như vậy.

### 3.5 Application and Use Cases

**FPGrowth có nhiều ứng dụng khác nhau, bao gồm:**

- Phân tích giỏ hàng để xác định các mặt hàng thường xuyên xuất hiện cùng nhau.
- Phân tích trình tự DNA trong tin sinh học.
- Phát hiện xâm nhập trong an ninh mạng.
- Hệ thống đề xuất cho các đề xuất cá nhân hóa.

---

## 4. Bảng so sánh tổng kết

| Đặc điểm | Apriori (Cổ điển) | FP-Growth (Hiện đại) |
| --- | --- | --- |
| **Chiến lược** | Generate & Test (Sinh & Kiểm tra) | Divide & Conquer (Chia để trị) |
| **Sinh ứng viên** | **Có** (Rất tốn kém) | **Không** (Lợi thế lớn) |
| **Số lần quét DB** | Quét $k$ lần | Quét **2** lần duy nhất |
| **Cấu trúc dữ liệu** | Danh sách ngang (Horizontal) | Cây nén (FP-Tree) |
| **Hiệu năng** | Chậm khi $min\_sup$ thấp | Rất nhanh và hiệu quả |

