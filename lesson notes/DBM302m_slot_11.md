# **Slot 11 - Chapter 3 (Part 9): Mining Quality Phrases**

**Ngày học:** 24/02/2026

**Nội dung chương học:**

* Slide 3.11: Mining Quality Phrases

---

## 1. Tổng quan về Mining Quality Phrases (Khai phá cụm từ chất lượng)

*Nguồn tham khảo: Slide 3.11*

### 1.1. Khái niệm cốt lõi

* **Phrase (Cụm từ) vs. Unigram (Từ đơn):** Các từ đơn thường mang ý nghĩa mơ hồ (Ví dụ: "United" có thể là United States, United Airlines) . Cụm từ là một đơn vị ngữ nghĩa tự nhiên, rõ ràng và không mơ hồ (Ví dụ: "United States") .


* **Quality Phrase Mining:** Quá trình chuyển đổi dữ liệu văn bản từ mức độ từ đơn (word granularity) sang mức độ cụm từ (phrase granularity) để tăng hiệu quả xử lý dữ liệu phi cấu trúc .

* **Hạn chế của NLP truyền thống (Chunking/Sequence Labeling):** Các mô hình NLP truyền thống đòi hỏi chi phí gán nhãn rất cao (annotate hundreds of documents), không dễ mở rộng sang các ngôn ngữ hoặc lĩnh vực mới .


### 1.2. Mối quan hệ giữa Phrase Mining và Topic Modeling

Để giảm chi phí gán nhãn, người ta kết hợp Khai phá cụm từ với Mô hình hóa chủ đề (Topic Modeling - như thuật toán LDA) . Có 3 chiến lược chính :

1. **Strategy 1 (Đồng thời):** Suy luận chủ đề và cụm từ cùng lúc. Nhược điểm: Độ phức tạp mô hình cao, dễ bị quá khớp (overfitting) và chạy rất chậm .


2. **Strategy 2 (Topic trước, Phrase sau):** Chạy mô hình chủ đề trước để gán nhãn cho từng từ, sau đó ghép các từ có cùng chủ đề thành cụm (Ví dụ: TurboTopics, KERT) . Nhược điểm: Các từ trong cùng một cụm từ có thể bị gán nhầm vào các chủ đề khác nhau ngay từ đầu .


3. **Strategy 3 (Phrase trước, Topic sau):** Khai phá cụm từ trước để phân đoạn văn bản, sau đó mới chạy mô hình chủ đề (Ví dụ: thuật toán ToPMine) . Đây là chiến lược hiệu quả nhất.

---

## 2. Các thuật toán khai phá cụm từ tiêu biểu

*Nguồn tham khảo: Slide 3.11*

Phần này giới thiệu 2 thuật toán đột phá: ToPMine (Không cần nhãn) và SegPhrase+ (Cần rất ít nhãn).

### 2.1. ToPMine (Không cần dữ liệu huấn luyện - No Training Data)

* **Tư duy:** Thuật toán hoạt động hoàn toàn phi giám sát (unsupervised). Nó tìm các mẫu xuất hiện thường xuyên liền kề nhau và gộp chúng lại dựa trên điểm ý nghĩa thống kê (significance score) .


* **Các bước thực hiện:**
1. **Frequent contiguous pattern mining:** Trích xuất các cụm từ ứng viên dựa trên tần suất.


2. **Agglomerative merging:** Gộp các từ đơn lẻ liền kề thành cụm từ nếu điểm ý nghĩa thống kê của chúng cao (ví dụ kiểm định chi-squared) .


3. **Phrase ranking:** Xếp hạng cụm từ dựa trên 4 tiêu chí của thuật toán KERT: Popularity (Độ phổ biến), Concordance (Độ hòa hợp), Informativeness (Độ thông tin), Completeness (Tính trọn vẹn) .





### 2.2. SegPhrase / SegPhrase+ (Sử dụng tập dữ liệu huấn luyện siêu nhỏ - Tiny Training Sets)

* **Tư duy:** Chỉ cần cung cấp một lượng nhãn cực nhỏ (ví dụ: 300 nhãn cho bộ dữ liệu 1GB) để tăng cường chất lượng cụm từ. Nó huấn luyện một bộ phân loại (Classifier) để tự động phân biệt cụm từ tốt và xấu .


* **Trích xuất đặc trưng (Feature Extraction):**
    * **Concordance:** Kiểm tra xem các phần của cụm từ có xuất hiện cùng nhau nhiều hơn mức ngẫu nhiên không .
    * **Informativeness:** Cụm từ chất lượng thường bắt đầu và kết thúc bằng các từ có nghĩa (non-stopword). Sử dụng chỉ số trung bình IDF và dấu câu (ngoặc kép, gạch nối) để đánh giá .
* **Kiến trúc SegPhrase+ (3 mô-đun chính):**
    1. **ClassPhrase:** Khai phá mẫu thường xuyên, trích xuất đặc trưng và phân loại (bằng Random Forest).
    2. **SegPhrase:** Phân đoạn cụm từ và ước lượng chất lượng cụm từ.
    3. **SegPhrase+:** Lặp lại một vòng nữa để tối ưu hóa chất lượng.

### 2.3. Ưu và Nhược điểm

| Thuật toán | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **ToPMine** | Hoàn toàn không cần gán nhãn thủ công (No training data). Giải quyết được lỗi chia cắt chủ đề của Strategy 2. | Không có sự hướng dẫn của con người nên một số cụm từ có thể đúng ngữ pháp nhưng vô nghĩa trong thực tế. |
| **SegPhrase+** | Tỷ lệ chính xác cực cao. Mở rộng tuyến tính (linearly scalable) tốt với Big Data.| Vẫn cần một lượng nhỏ dữ liệu mồi (tiny training sets hoặc Knowledge Base).|

---

## 3. Tổng kết & Tra cứu nhanh (Cheatsheet)

### Bảng tóm tắt các tiêu chí đánh giá cụm từ (Phrase Ranking Criteria)

| Tiêu chí | Mô tả ngắn gọn | Ví dụ so sánh |
| --- | --- | --- |
| **Popularity** | Tần suất xuất hiện đủ lớn. | <br>*information retrieval* tốt hơn *cross-language information retrieval*.|
| **Concordance** | Các từ kết hợp với nhau một cách tự nhiên. | <br>*strong tea* tự nhiên hơn *powerful tea*.|
| **Informativeness** | Có tính nhận diện chủ đề cao. | Bỏ các cụm vô nghĩa như *this paper*.|
| **Completeness** | Không bị cắt xén khỏi cụm từ dài hơn. | <br>*support vector machine* trọn vẹn hơn *vector machine*.|

### Từ khóa quan trọng

* **Unigram vs N-gram:** Từ đơn (1 từ) so với chuỗi N từ. Khai phá cụm từ bản chất là tìm các N-gram có chất lượng cao.
* **Tiny Training Set:** Đặc trưng đột phá của SegPhrase, phá vỡ định kiến "Máy học cần dữ liệu khổng lồ", chỉ cần 300 nhãn mồi là đủ.
* **Bag-of-words:** Mô hình biểu diễn văn bản cổ điển (xem văn bản như một "túi" chứa các từ lộn xộn, bỏ qua thứ tự), bị thay thế bởi Phrase Mining khi cần giữ nguyên ý nghĩa chuỗi từ.

---

*Ghi chú: Nội dung được tổng hợp từ tệp: 3.11 Mining Quality Phrases.pptx.*