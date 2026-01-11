# **Slot 2 - Chapter 1 & 2: Warehousing & Visualization**

**Nội dung chương học:**
- Data Warehouse - **1.4**
- Visualization - **2.1 & 2.2**

---

## 1. Introduction to Data Warehousing (Kho dữ liệu)

### 1.1. Khái niệm Data Warehouse là gì?

- Data Warehouse là nơi lưu trữ tập trung cho khối lượng dữ liệu khổng lồ.
- Chúng cung cấp dữ liệu lịch sử để hỗ trợ ra quyết định và phân tích.
- Data Warehouse đóng vai trò quan trọng trong việc tạo điều kiện thuận lợi cho việc ra quyết định dựa trên dữ liệu.

**Đặc điểm chính:** 

### 1.2. Các thành phần của Data Warehousing

- Các thành phần của Data Warehouse bao gồm nguồn dữ liệu, quy trình ETL, đặc điểm chính Data Warehouse (Hướng chủ đề **(Subject-oriented)**, Tích hợp **(Integrated)**, Có yếu tố thời gian **(Time-variant)**, và Ổn định **(Non-volatile)**.) và các **khối OLAP**
- Mỗi thành phần đều có một vai trò cụ thể trong hệ sinh thái Data Warehouse
- Cùng nhau, các thành phần này cho phép lưu trữ, chuyển đổi và phân tích dữ liệu một cách hiệu quả. 

### 1.3. OLAP (Online Analytical Processing)

![02-OLAP](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/02-Online-Analytical-Processing.png)

> Hình ảnh minh họa kiến trúc của OLAP

- **OLAP** là viết tắt của **Xử lý Phân tích Trực tuyến (Online Analytical Processing)**.
- Hệ thống OLAP cho phép phân tích dữ liệu **đa chiều**.
- Các loại OLAP bao gồm **MOLAP, ROLAP và HOLAP.**
- OLAP đóng vai trò quan trọng trong việc hỗ trợ các nhiệm vụ phân tích dữ liệu phức tạp.

### 1.4. Kiến trúc Data Warehouse

![01-DataWareHouseArchitect](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/01-data-warehouse-layout.png)

> Hình ảnh minh họa kiến trúc của Data Warehouse

- Kiến trúc Data Warehouse bao gồm ba lớp chính: **data sources**, **the data warehouse itself**, and **the front-end reporting and analysis tools**
- Mỗi lớp phục vụ một mục đích riêng biệt trong quy trình Data Warehouse.
- Kiến trúc này tạo điều kiện thuận lợi cho việc trích xuất, chuyển đổi, tải và truy cập dữ liệu của người dùng.

### 1.5. Data Source (Nguồn dữ liệu)

![04-Data-sources](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/04-Main_Sources_of_Big_Data_visual_selectionR36L0A.webp)

> Dữ liệu có thể đến từ nhiều nguồn khác nhau, bao quát tất cả các khía cạnh trong cuộc sống hàng ngày của chúng ta. 

- Nguồn dữ liệu đề cập đến **nguồn gốc của dữ liệu** cho kho dữ liệu.
- Ví dụ bao gồm **cơ sở dữ liệu, tập tin, nguồn bên ngoài**, v.v.
- Trích xuất dữ liệu (Data Extraction) là quá trình thu thập và chuyển dữ liệu từ các nguồn này vào kho dữ liệu.

### 1.6. ETL Process

![03-ETL](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/03-etl-process.webp)

> Quy trình xử lý ETL

- ETL là viết tắt của Extract (Trích xuất), Transform (Chuyển đổi), Load (Tải).
- Các quy trình ETL rất quan trọng đối với kho dữ liệu, bao gồm việc trích xuất dữ liệu, chuyển đổi và tải dữ liệu vào kho dữ liệu.
- Đảm bảo chất lượng dữ liệu là một khía cạnh quan trọng của quy trình ETL.

### 1.7 Data Warehouse Design (Thiết kế kho dữ liệu)

![05-Star-Vs-Snowflake](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/05-Star-Vs-Snowflake.webp)

> Lược đồ Star vs Snowflake Schemas

- Thiết kế kho dữ liệu hiệu quả là yếu tố thiết yếu để đạt hiệu suất tối ưu.
- Những yếu tố cần xem xét chính bao gồm việc lựa chọn giữa **lược đồ hình sao và hình bông tuyết**, cũng như định nghĩa các bảng chiều và bảng sự kiện.
- Một kho dữ liệu được thiết kế tốt sẽ nâng cao khả năng truy xuất và phân tích dữ liệu. 

### 1.8 Data Warehouse Loading

- Tải dữ liệu là quá trình chèn dữ liệu vào kho dữ liệu.
- Nó bao gồm việc lập lịch, tự động hóa và giám sát để giữ cho dữ liệu luôn được cập nhật.
- Tải dữ liệu tăng dần (kích hoạt bằng cách ghi đè) là một phương pháp phổ biến để cập nhật hiệu quả chỉ những dữ liệu mới hoặc đã thay đổi.

### 1.9 Data Warehouse Querying

- Truy vấn kho dữ liệu là một bước quan trọng để trích xuất thông tin chi tiết.
- Các truy vấn SQL và OLAP thường được sử dụng để truy xuất thông tin cụ thể.
- **Tốc độ và hiệu quả** trong truy vấn rất quan trọng để đưa ra quyết định kịp thời.


### 1.11 Data Warehouse Security

- Bảo mật dữ liệu là yếu tố tối quan trọng trong môi trường kho dữ liệu.
- Kiểm soát truy cập dựa trên vai trò (RBAC) thường được sử dụng để quản lý quyền của người dùng.
- Mã hóa và các biện pháp tuân thủ là cần thiết để bảo vệ dữ liệu nhạy cảm.

### 1.11 Data Warehouse Maintenance

- Việc bảo trì định kỳ là cần thiết để duy trì hoạt động trơn tru của kho dữ liệu.
- Các công việc này bao gồm các quy trình sao lưu và phục hồi.
- Tối ưu hóa hiệu năng là điều cần thiết để tối ưu hóa các quy trình truy xuất và phân tích dữ liệu.

### 1.12 OLAP Cubes

- Khối OLAP là cấu trúc dữ liệu đa chiều.
- Chúng cho phép tổng hợp và phân tích dữ liệu hiệu quả.
- Khối OLAP là một thành phần cơ bản của hệ thống OLAP để khám phá và báo cáo dữ liệu phức tạp.

### 1.13 Phân biệt OLTP và OLAP (Rất quan trọng)

Đây là kiến thức nền tảng để hiểu tại sao cần Data Warehouse.

| Đặc điểm | OLTP (Online Transaction Processing) | OLAP (Online Analytical Processing) |
| --- | --- | --- |
| **Mục đích** | Vận hành hàng ngày (Day-to-day operations). | Phân tích, ra quyết định (Decision making). |
| **Dữ liệu** | Chi tiết, cập nhật liên tục (Real-time). | Tóm tắt, lịch sử (Historical), dữ liệu lớn. |
| **User** | Nhân viên, hệ thống bán hàng (Clerks, DBAs). | Quản lý, Data Analyst, AI Engineer. |
| **Ví dụ** | Mua hàng Shopee, rút tiền ATM. | Báo cáo doanh thu quý, dự báo xu hướng. |


### 1.14 Mô hình dữ liệu (Data Modeling)

Trong DW, ta không dùng 3NF (chuẩn hóa cao) mà dùng **Dimensional Modeling** để truy vấn nhanh hơn:

* **Fact Table:** Chứa dữ liệu định lượng (số liệu, metrics). *Ví dụ: Doanh thu, Số lượng bán.*
* **Dimension Table:** Chứa dữ liệu ngữ cảnh (mô tả). *Ví dụ: Thời gian, Khách hàng, Sản phẩm.*
* **Schema:**
* *Star Schema:* Đơn giản, 1 bảng Fact ở giữa, các bảng Dim xung quanh.
* *Snowflake Schema:* Phức tạp hơn, các bảng Dim được chuẩn hóa phân cấp.

### Lợi ích của Data Warehouse: 

![06-Benefits_of_Data_Warehouses](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/06-Benefits_of_Data_Warehouses.webp)

> Benefits of DataWarehouse 

Data Warehouse mang lại nhiều lợi ích, bao gồm:
- Cải thiện khả năng ra quyết định
- Lưu trữ dữ liệu tập trung
- Phân tích dữ liệu lịch sử
- Tăng cường báo cáo và phân tích
Những lợi ích này khiến kho dữ liệu trở nên thiết yếu đối với các chiến lược dựa trên dữ liệu của các tổ chức.


### Tóm tắt Chapter 1: 
- Kho dữ liệu tập trung hóa dữ liệu để phân tích.
- Các thành phần bao gồm ETL, nguồn dữ liệu, khối dữ liệu và kiến ​​trúc.
- OLAP cho phép phân tích đa chiều.
- Kho dữ liệu nâng cao khả năng ra quyết định và báo cáo.
- Bảo mật, bảo trì và chất lượng dữ liệu là rất quan trọng.
- Nó đóng vai trò then chốt trong các chiến lược dựa trên dữ liệu.
















---

## 2. Introduction to Data Visualization (Tổng quan trực quan hóa)

*Nguồn tham khảo: Slide 2.1*

### 2.1. Tại sao cần Visualization?

* **Sức mạnh não bộ:** Con người xử lý hình ảnh nhanh hơn văn bản/số liệu gấp nhiều lần.
* **Mục tiêu:**
1. **Exploration (Khám phá):** Tìm ra pattern hoặc outlier (điểm bất thường) mà thống kê thuần túy không thấy.
2. **Communication (Truyền tải):** Kể chuyện với dữ liệu (Data Storytelling) cho stakeholders.



### 2.2. Phân loại dữ liệu để chọn biểu đồ

Việc chọn biểu đồ phụ thuộc vào loại biến (Variable types):

* **Categorical (Định danh):** Nominal (Tên, màu sắc), Ordinal (Xếp hạng).  Thường dùng Bar chart, Pie chart.
* **Numerical (Định lượng):** Discrete (Số nguyên), Continuous (Số thực).  Thường dùng Histogram, Scatter plot, Line chart.

---

## 3. Visualization of Numerical Data (Hiển thị dữ liệu số)

*Nguồn tham khảo: Slide 2.2*

Phần này tập trung vào các kỹ thuật cho dữ liệu **Numerical** (quan trọng nhất cho AI/ML).

### 3.1. Univariate Analysis (Phân tích 1 biến)

Dùng để xem phân phối của *một* thuộc tính (ví dụ: Phân phối tuổi của khách hàng).

* **Histogram:**
* Chia dữ liệu thành các khoảng (bins).
* Giúp nhìn thấy: Độ lệch (Skewness), Đỉnh (Modality), và Phân phối chuẩn (Normal distribution).


* **Box Plot (Biểu đồ hộp):** *Cực kỳ quan trọng để xử lý Outlier.*
* Hiển thị 5 thông số: Min, Q1 (25%), Median (50%), Q3 (75%), Max.
* Các điểm nằm ngoài "râu" (whiskers) là **Outliers**.



### 3.2. Bivariate Analysis (Phân tích 2 biến)

Dùng để tìm mối quan hệ giữa *hai* thuộc tính (ví dụ: Giá nhà vs. Diện tích).

* **Scatter Plot (Biểu đồ phân tán):**
* Mỗi điểm là một quan sát (x, y).
* Giúp nhìn thấy: Tương quan (Correlation) - Tuyến tính hay phi tuyến tính, Tích cực hay tiêu cực.



### 3.3. Tra cứu nhanh: Khi nào dùng biểu đồ nào?

| Loại biểu đồ | Mục đích sử dụng (Use Case) | Code Library (Python) |
| --- | --- | --- |
| **Histogram** | Xem phân phối (Distribution), kiểm tra độ lệch. | `plt.hist()`, `sns.histplot()` |
| **Box Plot** | Tìm Outliers, so sánh phân phối giữa các nhóm. | `plt.boxplot()`, `sns.boxplot()` |
| **Scatter Plot** | Tìm mối quan hệ (Correlation) giữa 2 biến số. | `plt.scatter()`, `sns.scatterplot()` |
| **Line Chart** | Xem xu hướng theo thời gian (Time-series). | `plt.plot()`, `sns.lineplot()` |
| **Heatmap** | Xem ma trận tương quan (Correlation Matrix). | `sns.heatmap()` |

---

*Lưu ý: File này tổng hợp kiến thức nền tảng về hạ tầng dữ liệu và kỹ năng trực quan hóa số liệu, phục vụ trực tiếp cho bước EDA (Exploratory Data Analysis) trong Python.*
