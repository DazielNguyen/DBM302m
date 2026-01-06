
# **Slot 1 - Cshapter 1: Introduction & Fundamentals**

**Tổng quan chương:**
Chương này thiết lập nền tảng tư duy cho toàn bộ môn học. Chúng ta đi từ **Định nghĩa (1.1)** (Data Mining là gì, tại sao cần?)  **Hiểu dữ liệu (1.2)** (Dữ liệu thô trông như thế nào, đo lường ra sao?)  **Tiền xử lý (1.3)** (Làm sạch và biến đổi dữ liệu để sẵn sàng cho mô hình).

---

## 1. Introduction to Data Mining (Tổng quan)

*Nguồn tham khảo: Slide 1.1*

### 1.1. Tại sao cần Data Mining?

Trong kỷ nguyên số, chúng ta đang "chết chìm trong dữ liệu nhưng đói khát tri thức" (Drowning in data & starving for knowledge).

* **Mục tiêu:** Tự động hóa việc phân tích dữ liệu lớn để tìm ra các mẫu (patterns) có giá trị.
* **Định nghĩa:** Là quá trình khám phá tri thức, trích xuất các mẫu thú vị (hợp lệ, mới lạ, hữu ích, dễ hiểu) từ lượng dữ liệu khổng lồ.

### 1.2. The Data Mining Pipeline (Quy trình chuẩn)

Đây là "xương sống" của môn học. Mọi bài toán Data Mining đều đi qua các bước này:

1. **Data Collection:** Thu thập dữ liệu từ nhiều nguồn.
2. **Data Preprocessing:** Làm sạch, tích hợp, chuyển đổi và thu giảm dữ liệu (Chi tiết tại mục 3).
3. **Data Mining:** Áp dụng thuật toán để tìm mẫu.
4. **Pattern Evaluation:** Đánh giá độ chính xác và ý nghĩa của mẫu tìm được.
5. **Knowledge Presentation:** Trực quan hóa và báo cáo kết quả.



### 1.3. Bốn góc nhìn chính (The 4 Views)

Hệ thống Data Mining được xây dựng dựa trên sự tương tác của 4 yếu tố :

* **Data View:** Hiểu thuộc tính và cấu trúc dữ liệu.
* **Technique View:** Các kỹ thuật khai phá (Classification, Clustering, v.v.).
* **Knowledge View:** Cách giải thích và đánh giá tri thức tìm được.
* **Application View:** Ứng dụng vào thực tế (Kinh doanh, Y tế, v.v.).

---

## 2. Data Understanding (Hiểu dữ liệu)

*Nguồn tham khảo: Slide 1.2*

Trước khi xử lý, ta cần hiểu "nguyên liệu" đầu vào.

### 2.1. Cấu trúc dữ liệu

* **Data Objects (Đối tượng):** Là các phần tử trong tập dữ liệu (ví dụ: một dòng trong bảng, một hồ sơ khách hàng).
* **Attributes (Thuộc tính):** Là các đặc điểm của đối tượng (ví dụ: tuổi, thu nhập). Có các loại: Nominal, Ordinal, Numeric.

### 2.2. Công cụ phân tích cơ bản

Để hiểu sơ bộ về dữ liệu, ta dùng:

* **Descriptive Statistics (Thống kê mô tả):** Mean, Median, Mode, Variance, Standard Deviation. Giúp hiểu xu hướng tập trung và độ phân tán.
* **Data Visualization:** Biểu đồ, đồ thị để nhìn nhanh pattern.

### 2.3. Data Similarity Measures (Các độ đo tương đồng)

Đây là kiến thức **quan trọng** để chạy các thuật toán như Clustering hay Recommendation sau này.

| Độ đo (Measure) | Đặc điểm & Ứng dụng |
| --- | --- |
| **Euclidean Distance** | Đo khoảng cách đường thẳng giữa 2 điểm. Dùng cho dữ liệu số (Numeric data) .|
| **Cosine Similarity** | Đo góc giữa 2 vector, không quan tâm độ lớn. Dùng phổ biến trong Text Mining.|
| **Jaccard Similarity** | Đo độ giao nhau giữa các tập hợp (). Dùng cho dữ liệu phân loại (Categorical/Binary) .|
| **Pearson Correlation** | Đo mối quan hệ tuyến tính giữa 2 biến số (từ -1 đến +1). Dùng trong thống kê.|

---

## 3. Data Preprocessing (Tiền xử lý dữ liệu)

*Nguồn tham khảo: Slide 1.3*

**Mục tiêu:** Cải thiện chất lượng dữ liệu để tăng độ chính xác của mô hình ("Garbage in, garbage out").

### 3.1. Quy trình Tiền xử lý (Full Flow)

Dữ liệu thô thường bị lỗi, thiếu hoặc không nhất quán. Ta xử lý theo 4 bước lớn:

#### B1: Data Cleaning (Làm sạch)

* **Nhiệm vụ:** Xử lý giá trị thiếu (Missing values), nhiễu (Noisy data), và dữ liệu rác.


**Kỹ thuật:**
* *Missing Data:* Điền bằng Mean/Median, hoặc dùng KNN (Imputation).* 
- *Duplicate:* Loại bỏ các bản ghi trùng lặp.

#### B2: Data Integration (Tích hợp)

* **Nhiệm vụ:** Gom dữ liệu từ nhiều nguồn (Database, Files) thành một kho chung.
* **Thách thức:** Xử lý xung đột định dạng (Schema matching), dư thừa dữ liệu (Redundancy) .

#### B3: Data Transformation (Biến đổi)

* **Nhiệm vụ:** Đưa dữ liệu về dạng phù hợp cho thuật toán.


* **Kỹ thuật Key:**
* **Normalization (Chuẩn hóa):** Đưa dữ liệu về khoảng [0, 1] (Min-Max Scaling) hoặc chuẩn hóa Z-score.


* **Encoding:** Chuyển dữ liệu phân loại (Categorical) sang số (One-hot encoding, Label encoding).

#### B4: Data Reduction (Thu giảm)

* **Nhiệm vụ:** Giảm kích thước dữ liệu nhưng giữ lại thông tin quan trọng.


* **Kỹ thuật:**
* *Dimensionality Reduction:* Giảm số lượng thuộc tính (PCA, Feature Selection).
* *Numerosity Reduction:* Giảm số lượng dòng dữ liệu.
---

## 4. Tổng kết & Từ khóa (Cheatsheet)

* **3Vs/5Vs:** Đặc điểm của Big Data (Volume, Variety, Velocity,...) .
* **Feature Engineering:** Tạo ra các thuộc tính mới từ thuộc tính cũ để tăng sức mạnh dự báo.
* **Outlier/Anomaly:** Các điểm dữ liệu bất thường, lệch xa so với chuẩn.

---

*Lưu ý: File này tổng hợp nội dung từ các slide 1.1, 1.2, và 1.3 môn Data Mining.*