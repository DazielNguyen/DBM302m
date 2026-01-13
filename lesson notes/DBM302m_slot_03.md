# **Slot 3 - Chapter 2 (Part 2): Non-Numerical Viz & Dashboards**

**Ngày học: 09/01/2026**

**Nội dung chương học:**
- 2.3 Visualization of Non-Numerical Data
- 2.4 Visualization of Dashboards

---

## I. Visualization of Non-Numerical Data (Dữ liệu phi số)

- **Non-Numerical Data** (Dữ liệu phi số), còn được gọi là **Categorical Data** (Dữ liệu phân loại), bao gồm thông tin định tính hoặc mô tả không thể đo lường trên thang đo số. Việc trực quan hóa dữ liệu phi số giúp chúng ta hiểu được **(distribution)** sự phân bố , **(proportions)** tỷ lệ và **(relationships)** mối quan hệ giữa các danh mục hoặc nhóm khác nhau.

### **Pie Charts and Donut Charts**

**Pie Charts** (Biểu đồ hình tròn) thể hiện tỷ lệ của mỗi danh mục dưới dạng các lát cắt của một chiếc bánh tròn. Kích thước của mỗi lát cắt thể hiện **tần suất** tương đối hoặc tỷ lệ của danh mục đó.
- **Chức năng:** Thể hiện tỉ lệ phần trăm (Part-to-whole relationship).
- **Lưu ý quan trọng:** Chỉ nên dùng khi có ít nhóm (dưới 5 nhóm). Nếu quá nhiều lát cắt nhỏ, biểu đồ sẽ rất khó đọc. Không dùng để so sánh chính xác độ lớn.

**Donut Charts** (Biểu đồ hình bánh donut) tương tự như biểu đồ hình tròn nhưng có một lỗ ở giữa, cho phép đặt thêm thông tin hoặc nhãn vào đó.

![01-pie-donut-charts](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_03/01-pie-donut-charts.png)

> Biểu đồ tròn và biểu đồ hình bánh donut

### **Stacked Bar Charts (Biểu đồ cột xếp chồng)**

**Stacked Bar Charts (Biểu đồ cột xếp chồng)** thể hiện thành phần của một danh mục bằng cách xếp chồng các cột hình chữ nhật lên nhau. Mỗi đoạn cột đại diện cho một tiểu danh mục khác nhau, và chiều dài của đoạn cột thể hiện tỷ lệ của tiểu danh mục đó.

![02-stacked-bar-chart](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_03/02-stacked-bar-chart.png)

> Biểu đồ cột xếp chồng

### **Word Clouds and Tag Clouds**

**Word Clouds** (Đám mây từ ngữ) trực quan hóa dữ liệu văn bản, chẳng hạn như từ khóa hoặc tần suất xuất hiện của từ, bằng cách hiển thị các từ với kích thước khác nhau dựa trên tần suất hoặc tầm quan trọng của chúng.

Khi dữ liệu là các đoạn văn, comment, hoặc bài báo, ta không thể dùng biểu đồ cột thông thường.

* **Word Cloud (Đám mây từ):**
* **Nguyên lý:** Kích thước chữ tỷ lệ thuận với tần suất xuất hiện của từ đó trong tập dữ liệu.
* **Chức năng:** Giúp nhìn nhanh các từ khóa nổi bật (Keywords), chủ đề chính được nhắc đến nhiều nhất.
* **Ứng dụng:** Phân tích sentiment khách hàng, tóm tắt nội dung tài liệu.

**Tag Clouds** (Đám mây thẻ) tương tự như đám mây từ ngữ nhưng hiển thị các thẻ hoặc nhãn với kích thước phông chữ khác nhau để thể hiện tần suất hoặc tầm quan trọng của chúng.

![03-word-tag-cloud](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_03/03-word-tag-cloud.png)

> Minh họa Word Clouds và Tag Clouds


### **Chord Diagrams and Network Graphs**

**Chord Diagrams** (Sơ đồ dây cung) thể hiện mối quan hệ và luồng thông tin giữa các thực thể hoặc danh mục khác nhau. Chúng sử dụng các cung hoặc dải để kết nối các thực thể, với độ rộng của các cung thể hiện sức mạnh hoặc tần suất của các kết nối.

**Network Graphs** (Đồ thị mạng (hoặc node-link sơ đồ nút-liên kết)) thể hiện mối quan hệ giữa các thực thể dưới dạng các nút (đỉnh) được kết nối bởi các cạnh (đường thẳng). Chúng rất hiệu quả để trực quan hóa các mạng lưới phức tạp hoặc các mối quan hệ xã hội.

![04-Chord-Diagrams-and-Network-Graphs](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_03/04-Chord-Diagrams-and-Network-Graphs.png)

> Minh họa Chord Diagrams và Network Graphs

### **Tree Diagrams and Sunburst Charts**

**Tree Diagrams** (Sơ đồ cây) biểu diễn cấu trúc hoặc mối quan hệ phân cấp bằng cách sử dụng cấu trúc phân nhánh với các nút. Mỗi cấp độ đại diện cho một danh mục khác nhau, và kích thước hoặc màu sắc của các nút có thể biểu thị thông tin bổ sung.

**Sunburst Charts** (Biểu đồ hình tia nắng) là một phần mở rộng của sơ đồ cây, trong đó hệ thống phân cấp được hiển thị dưới dạng các vòng tròn đồng tâm. Kích thước hoặc góc của mỗi phần biểu thị tỷ lệ hoặc giá trị liên quan đến danh mục đó.


![05-Tree-Diagrams-and-Sunburst-Charts](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_03/05-Tree-Diagrams-and-Sunburst-Charts.png)

> Tree Diagrams and Sunburst Charts

### **Các phương pháp trực quan hóa dữ liệu đa chiều: PCA**

**Kỹ thuật giảm chiều** được sử dụng để chuyển đổi dữ liệu đa chiều thành không gian ít chiều hơn trong khi vẫn giữ lại hầu hết sự biến thiên của dữ liệu gốc.

**Các bước của PCA:**

- Chuẩn hóa dữ liệu
- Tính ma trận hiệp phương sai
- Tính toán các vectơ riêng và giá trị riêng
- Chọn các thành phần chính
- Chiếu dữ liệu

![06-calculate-PCA](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_03/06-calculate-PCA.png)

> Các bước tính PCA


### **Các phương pháp trực quan hóa dữ liệu đa chiều: Phân tích đa chiều (Multidimensional Scaling) - MDS**

**Kỹ thuật được** sử dụng để trực quan hóa sự tương đồng và khác biệt giữa các điểm dữ liệu trong không gian có chiều thấp hơn.

**Các bước của MDS:**

- Xác định ma trận khoảng cách: Tính toán khoảng cách hoặc sự khác biệt giữa các cặp điểm dữ liệu.
- Áp dụng giảm chiều: Tìm một biểu diễn có chiều thấp hơn giúp bảo toàn khoảng cách giữa các cặp điểm càng sát càng tốt.
- MDS dựa trên hệ mét so với MDS không dựa trên hệ mét: MDS dựa trên hệ mét bảo toàn khoảng cách thực tế, trong khi MDS không dựa trên hệ mét bảo toàn thứ tự xếp hạng của khoảng cách.


![07-guide-to-multidimensional-scaling-in-python-with-scikit-learn](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_03/07-guide-to-multidimensional-scaling-in-python-with-scikit-learn.webp)

> Cách tính Multidimensional Scaling

![08-multi-scaling](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_03/08-multi-scaling.png)

> Minh hóa trực quan hóa Multidimensional Scaling

### **Parallel Coordinates Plot for High-Dimensional Data (Biểu đồ tọa độ song song cho dữ liệu đa chiều)**

**Kỹ thuật trực quan hóa** hiển thị dữ liệu đa biến trên các trục song song, trong đó mỗi trục đại diện cho một biến khác nhau.

**Cấu trúc đồ thị:**

- Mỗi điểm dữ liệu được biểu diễn bằng một đường thẳng nối các điểm trên mỗi trục song song tương ứng với giá trị biến của nó.

- Các điểm dữ liệu có mẫu tương tự sẽ có các đường thẳng gần nhau hơn, và các điểm ngoại lệ sẽ nổi bật.

![09-Parallel-Coordinates](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_03/09-Parallel-Coordinates.png)

> Minh hóa trực quan hóa Multidimensional Scaling

### **So sánh các phương pháp**

**PCA vs. MDS**

- PCA tập trung vào việc nắm bắt sự biến thiên và bảo toàn mẫu, trong khi MDS nhấn mạnh vào việc bảo toàn khoảng cách.
- PCA lý tưởng cho việc nén dữ liệu và lựa chọn đặc trưng, ​​trong khi MDS phù hợp để trực quan hóa cấu trúc tương đồng và khác biệt.

**PCA vs. Parallel Coordinates Plot**

- PCA chiếu các điểm dữ liệu lên các chiều mới, làm cho nó phù hợp với việc giảm chiều và trực quan hóa.
- Biểu đồ tọa độ song song hiển thị các điểm dữ liệu trực tiếp trên các biến gốc, cho phép xem chi tiết từng bản ghi dữ liệu riêng lẻ.

**MDS vs. Parallel Coordinates Plot**

- MDS nhằm mục đích trực quan hóa khoảng cách giữa các cặp dữ liệu, điều này rất hữu ích để hiểu cấu trúc khác biệt trong dữ liệu.

- Biểu đồ tọa độ song song tập trung hơn vào việc khám phá mối quan hệ giữa các biến, làm nổi bật các mẫu và xu hướng.

**Lựa chọn Phương pháp Phù hợp:**

- Tiêu chí lựa chọn:
    + Đặc điểm dữ liệu
    + Mục tiêu phân tích
    + Khám phá dữ liệu
- Quá trình lặp lại và Thử nghiệm

### **Những yếu tố cần cân nhắc khi trực quan hóa dữ liệu phi số một cách hiệu quả**

- Chọn kỹ thuật trực quan hóa phù hợp dựa trên **bản chất của dữ liệu phi số** và những thông tin bạn muốn truyền tải.
- Sử dụng **nhãn** rõ ràng và ngắn gọn cho từng danh mục hoặc thực thể để đảm bảo sự hiểu biết và diễn giải.
- Áp dụng **màu sắc và tín hiệu** trực quan phù hợp để phân biệt các danh mục hoặc nhóm khác nhau.
- Đảm bảo hình ảnh trực quan thể hiện **chính xác tỷ lệ hoặc mối quan hệ** giữa các dữ liệu phi số.
- Sử dụng **tính tương tác**, chẳng hạn như **chú thích hoặc bộ lọc**, để cung cấp thêm thông tin hoặc cho phép người dùng khám phá dữ liệu chi tiết hơn.


---

## 2. Visualization of Dashboards (Bảng điều khiển)

Sau khi đã tạo ra các biểu đồ riêng lẻ (Charts), ta cần tập hợp chúng lại để kể một câu chuyện dữ liệu hoàn chỉnh.

### 2.1. Dashboard là gì?

Dashboard là một giao diện trực quan hiển thị thông tin quan trọng nhất cần thiết để đạt được một hoặc nhiều mục tiêu.

* **Đặc điểm:** Thông tin được gom gọn trên một màn hình (consolidated on a single screen) để người xem có thể giám sát trong nháy mắt.
* **Mục tiêu:** Hỗ trợ ra quyết định (Decision Making) và giám sát hiệu suất (Monitoring).

### 2.2. Các thành phần chính của Dashboard

Một Dashboard chuẩn thường bao gồm các "mảnh ghép" sau:

1. **KPIs (Key Performance Indicators):** Các chỉ số đo lường hiệu suất quan trọng nhất (thường là các con số lớn, nằm trên cùng). Ví dụ: *Tổng doanh thu, Lợi nhuận ròng.*
2. **Charts & Graphs:** Các biểu đồ (Bar, Line, Pie...) để diễn giải chi tiết cho KPI.
3. **Tables (Bảng dữ liệu):** Hiển thị chi tiết dòng dữ liệu khi cần tra cứu cụ thể.
4. **Filters/Interactivity (Bộ lọc):** Cho phép người dùng tương tác (chọn ngày tháng, chọn khu vực) để dữ liệu tự động cập nhật theo.

### 2.3. Nguyên tắc thiết kế Dashboard (Design Principles)

Thiết kế Dashboard không chỉ là "vẽ cho đẹp", mà là "thiết kế để dùng".

* **Clarity (Sự rõ ràng):** Tránh lộn xộn (Clutter). Chỉ hiển thị những gì thực sự cần thiết.
* **Relevance (Sự liên quan):** Dữ liệu phải phục vụ đúng mục tiêu của người xem (Ví dụ: Dashboard cho CEO khác với Dashboard cho Kỹ thuật viên).
* **Simplicity (Sự đơn giản):** Sử dụng màu sắc hợp lý (không quá lòe loẹt), font chữ dễ đọc.
* **Consistency (Sự nhất quán):** Giữ nguyên quy ước màu sắc và bố cục xuyên suốt các trang.

---

## 3. Tổng kết & Từ khóa (Cheatsheet)

### So sánh nhanh: Khi nào dùng biểu đồ nào?

| Loại dữ liệu | Biểu đồ đề xuất | Mục đích chính |
| --- | --- | --- |
| **So sánh các nhóm** (Categorical) | **Bar Chart** | So sánh độ lớn, số lượng. |
| **Xem tỉ lệ phần trăm** (Categorical) | **Pie Chart** | Xem cơ cấu (Part-to-whole). |
| **Xem xu hướng** (Time-series) | **Line Chart** | Xem sự thay đổi theo thời gian. |
| **Phân tích văn bản** (Text) | **Word Cloud** | Tìm từ khóa phổ biến. |

### Thuật ngữ Dashboard

* **Interactive Dashboard:** Bảng điều khiển cho phép người dùng click, lọc, zoom dữ liệu (khác với Static Report - báo cáo tĩnh dạng PDF/Giấy).
* **Real-time Monitoring:** Khả năng cập nhật dữ liệu ngay lập tức khi có sự thay đổi thực tế.
* **Data Aggregation:** Quá trình tổng hợp dữ liệu chi tiết thành các chỉ số tổng quan (Sum, Average) để hiển thị lên Dashboard.

---

*Lưu ý: Phần này hoàn thiện kỹ năng Trực quan hóa dữ liệu (Visualization) trong quy trình Data Mining. Từ việc vẽ biểu đồ đơn lẻ đến việc xây dựng hệ thống báo cáo quản trị.*