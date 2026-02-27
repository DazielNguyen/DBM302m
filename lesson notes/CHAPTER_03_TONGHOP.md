# MASTER STUDY GUIDE - CHAPTER 3: PATTERN DISCOVERY

**Môn học:** Data Mining | **Hệ thống hóa toàn bộ Chương 3**

**Bức tranh toàn cảnh (The Big Picture):**
Khai phá mẫu (Pattern Discovery) là quá trình tìm kiếm các quy luật (regularities), tập mục (itemsets) hoặc cấu trúc xuất hiện thường xuyên trong dữ liệu. Nó là cốt lõi của bài toán hệ thống gợi ý (Recommender Systems), phân tích giỏ hàng (Market Basket Analysis) và phát hiện bất thường (Anomaly Detection).

---

## PHẦN I: NỀN TẢNG VÀ THUẬT TOÁN CƠ BẢN (Basic & Algorithms)

*Nguồn: Slide 3.1, 3.2, 3.4, 3.5*

### 1. Khái niệm cốt lõi

* **Frequent Itemset (Tập mục phổ biến):** Các món hàng thường được mua cùng nhau (Ví dụ: Bia và Tã lót).
* **Support ($s$):** Tần suất xuất hiện của một tập mục trên tổng số giao dịch. (Ví dụ: 5% số hóa đơn có mua Bia và Tã).
* **Confidence ($c$):** Độ tin cậy của luật $A \to B$. Biết khách đã mua A, xác suất mua B là bao nhiêu? ($c = Support(A \cup B) / Support(A)$).

### 2. Ba chiến lược khai phá mẫu (The 3 Mining Algorithms)

| Thuật toán | Chiến lược cốt lõi | Cấu trúc dữ liệu | Ưu / Nhược điểm chính |
| --- | --- | --- | --- |
| **1. Apriori** | Sinh ứng viên & Kiểm tra (Generate & Test) | Ngang (Horizontal) | **Ưu:** Dễ hiểu, tận dụng tính chất cắt tỉa (Downward Closure).<br><br>**Nhược:** Quét CSDL nhiều lần, sinh hàng triệu ứng viên rác. |
| **2. ECLAT** | Giao tập hợp (Intersection) | Dọc (Vertical - TID set) | **Ưu:** Đếm Support cực nhanh bằng phép giao (AND bitwise).<br><br>**Nhược:** Tốn bộ nhớ lưu danh sách ID giao dịch. |
| **3. FP-Growth** | Phát triển mẫu (Pattern Growth) | Cây nén (FP-Tree) | **Ưu:** **Không sinh ứng viên**, chỉ quét CSDL 2 lần, cực nhanh.<br><br>**Nhược:** Thuật toán đệ quy phức tạp, cây có thể phình to nếu dữ liệu nhiễu. |

---

## PHẦN II: TỐI ƯU HÓA - NÉN & ĐÁNH GIÁ MẪU (Optimization)

*Nguồn: Slide 3.6, 3.7*

Khi dữ liệu khổng lồ, thuật toán trả về hàng triệu luật. Chúng ta cần nén chúng lại (giảm số lượng) và đánh giá chúng (lọc ra luật chất lượng).

### 1. Nén mẫu (Pattern Compression)

* **Frequent Pattern:** Tất cả các mẫu vượt ngưỡng $min\_sup$. (Quá nhiều, dư thừa).
* **Closed Pattern (Mẫu đóng):** Là mẫu lớn nhất mà không bị giảm số lượng (Support).
> *Note (Ghi nhớ nhanh): Mẫu mở là thay đổi Items nhưng giữ nguyên số Support. Mẫu đóng là thay đổi Items thì buộc phải thay đổi Support. Kỹ thuật này nén không mất tin (Lossless).*


* **Max Pattern (Mẫu cực đại):** Mẫu lớn nhất không bị chứa trong bất kỳ mẫu phổ biến nào khác. Nén mất tin (Lossy) nhưng cực kỳ gọn nhẹ.

### 2. Đánh giá mẫu (Pattern Evaluation)

Support và Confidence dễ gây hiểu lầm nếu món hàng đó vốn dĩ đã bán rất chạy (Ví dụ: Sữa). Ta cần các độ đo sắc bén hơn:

* **Lift:** Đo lường sự tương quan (Correlation). Lift > 1 là tương quan dương (hỗ trợ nhau mua); Lift < 1 là tương quan âm.
* **Độ đo bất biến Null (Null-invariant):** Trong Big Data, số lượng giao dịch "không mua cả A và B" là khổng lồ (Null transactions). Cần dùng các độ đo không bị ảnh hưởng bởi Null như **Kulczynski (Kulc)** kết hợp với **Imbalance Ratio (IR)** để đánh giá độ gắn kết.

---

## PHẦN III: CÁC DẠNG MẪU PHỨC TẠP (Advanced Patterns)

*Nguồn: Slide 3.8, 3.9, 3.10, 3.11*

Không chỉ dừng lại ở "Giỏ hàng siêu thị", Pattern Discovery được mở rộng ra nhiều chiều không gian và thời gian.

### 1. Khai phá đa chiều & Đa cấp (Multi-dimensional & Multi-level)

* **Multi-level:** Tìm luật ở nhiều mức độ chi tiết (Sữa $\to$ Sữa bò $\to$ Sữa Dairyland). *Lưu ý: Ngưỡng Support phải giảm dần (Level-reduced) khi đi xuống các cấp chi tiết hơn.*
* **Quantitative:** Khai phá trên dữ liệu số (Tuổi, Thu nhập). Cần thực hiện bước **Rời rạc hóa (Discretization)** biến số thành các khoảng trước khi chạy thuật toán.

### 2. Mẫu tuần tự (Sequential Patterns)

Yếu tố **Thứ tự thời gian** được đưa vào. Khách hàng mua A $\to$ sau đó mua B.

* Thuật toán **GSP**: Dựa trên Apriori (Sinh ứng viên).
* Thuật toán **PrefixSpan**: Dựa trên FP-Growth (Phát triển đệ quy, không sinh ứng viên).
* *Ứng dụng:* Phân tích Clickstream web, phân tích chuỗi gen sinh học.

### 3. Mẫu Không gian - Thời gian & Quỹ đạo (Spatiotemporal & Trajectory)

* Tìm kiếm các mối quan hệ Topo (cắt nhau, gần nhau). Dựa trên nguyên lý **Tự tương quan không gian (Spatial Autocorrelation)**: Những thứ gần nhau thì giống nhau.
* *Khai phá chu kỳ (Periodicity):* Dùng biến đổi Fourier (Fourier Transform) để tìm quy luật lặp lại trong các điểm dữ liệu rời rạc (Ví dụ: Quỹ đạo chim di cư).

### 4. Khai phá cụm từ chất lượng (Quality Phrases)

Biến chuỗi từ đơn (Unigrams) thành các cụm từ có ý nghĩa (Phrases).

* **ToPMine:** Thuật toán không cần gán nhãn (Unsupervised).
* **SegPhrase+:** Thuật toán dùng lượng nhãn siêu nhỏ (Tiny training set - 300 nhãn) kết hợp Random Forest để phân loại cụm từ tốt/xấu cực kỳ chính xác.

---

## PHẦN IV: THÁCH THỨC VÀ XU HƯỚNG TƯƠNG LAI (Frontiers)

*Nguồn: Slide 3.12*

### 1. Dữ liệu luồng (Data Streams)

* **Đặc điểm:** Chảy liên tục, vô hạn, tốc độ cao.
* **Giải pháp:** Chỉ được phép quét dữ liệu 1 lần (Single-scan). Sử dụng thuật toán đếm xấp xỉ **Lossy Counting** (chia nhỏ thành các bucket, bỏ qua các item quá hiếm, đảm bảo sai số nằm trong ngưỡng $\epsilon$).

### 2. Ứng dụng đột phá & Vấn đề Bảo mật

* **Software Debugging:** Tìm mẫu thực thi code phổ biến $\to$ Các đoạn code vi phạm mẫu chính là Lỗi (Bugs).
* **Privacy (Bảo mật):** Khai phá dữ liệu đe dọa quyền riêng tư. Cần cân bằng giữa độ chính xác của mô hình và các rào cản bảo mật (Input privacy - ẩn dữ liệu gốc, Output privacy - giấu tri thức nhạy cảm).

---

## CHEATSHEET TỔNG HỢP KỲ THI (Quick Review)

| Khái niệm / Thuật toán | "Keyword" khóa để nhớ nhanh |
| --- | --- |
| **Apriori Property** | Tính chất "Đóng giảm". Tập con của tập phổ biến cũng phải phổ biến. Dùng để cắt tỉa. |
| **FP-Tree** | Cấu trúc cây nén. Header Table + Conditional Pattern Base. Không sinh ứng viên. |
| **Lossless Compression** | Nén không mất tin = **Closed Pattern**. (Tìm ra mẫu dài nhất mà Support không đổi). |
| **Lift / Kulc** | Độ đo dùng để loại bỏ các luật Confidence cao giả tạo. Kulc là Null-invariant. |
| **PrefixSpan** | Thuật toán tìm mẫu **Tuần tự** (Sequential) theo hướng chia để trị (Projected Database). |
| **SegPhrase+** | NLP. Tìm cụm từ chất lượng cao bằng **Tiny Training Set** (Dữ liệu huấn luyện nhỏ). |
| **Lossy Counting** | Thuật toán cho **Data Streams**. Quét 1 lần, đếm xấp xỉ, có bảo đảm sai số. |

---
