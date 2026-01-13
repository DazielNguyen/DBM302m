# **Slot 2 - Chapter 1 & 2: Warehousing & Visualization**

**Ngày học: 09/01/2026**

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

### 2.1 Định nghĩa về Data Visualization

![07-10-types-of-data-visualization](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/07-10-types-of-data-visualization.jpg)

> Trực quan hóa dữ liệu

- Trực quan hóa dữ liệu là việc **biểu diễn dữ liệu và thông tin** bằng đồ họa sử dụng các yếu tố trực quan như **biểu đồ, đồ thị và bản đồ**.
- Đây là một công cụ mạnh mẽ cho phép khám phá, phân tích và truyền đạt những hiểu biết từ các tập dữ liệu phức tạp một cách **intuitive manger** *trực quan và dễ hiểu*.
- Trong lĩnh vực khai thác dữ liệu, trực quan hóa dữ liệu đóng vai trò quan trọng trong việc phát hiện các mẫu, xu hướng và mối quan hệ mà nếu không sẽ khó xác định được.
- Chiều dữ liệu được ví dụ như 1 cột trong bảng dữ liệu.

### 2.2 Tầm quan trọng của trực quan hóa dữ liệu trong khai thác dữ liệu - Phần 1:

- Trực quan hóa dữ liệu giúp hiểu rõ các **mô hình và cấu trúc tiềm ẩn bên trong dữ liệu**. Nó cho phép xác định các mối tương quan, cụm dữ liệu, các giá trị ngoại lệ và những thông tin chi tiết có giá trị khác, từ đó thúc đẩy việc ra quyết định sáng suốt.

- Nó tạo điều kiện **thuận lợi cho việc truyền đạt hiệu quả** các phát hiện đến nhiều bên liên quan, bao gồm cả đối tượng **kỹ thuật và phi kỹ thuật**. Các hình ảnh trực quan có thể truyền tải thông tin phức tạp dễ dàng hơn so với dữ liệu thô hoặc mô tả bằng văn bản.

### 2.3 Tầm quan trọng của trực quan hóa dữ liệu trong khai thác dữ liệu - Phần 2:

- Bằng cách trực quan hóa dữ liệu, chúng ta có thể **nhanh chóng phát hiện các bất thường**, nhận diện xu hướng và đưa ra dự đoán dựa trên dữ liệu. Điều này cho phép chúng ta thu được những hiểu biết **hữu ích và trích xuất giá trị** từ các tập dữ liệu lớn và phức tạp.

- Trực quan hóa dữ liệu giúp **tăng cường quá trình phân tích dữ liệu khám phá**, cho phép người khai thác dữ liệu tương tác thao tác với các hình ảnh trực quan, lọc dữ liệu và khám phá các mẫu ẩn hoặc các điểm bất thường trong thời gian thực.

![09-Crunching-the-Numbers--Topline-Insights-through-Data-Analytics--The-Importance-of-Data-Visualization](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/09-Crunching-the-Numbers--Topline-Insights-through-Data-Analytics--The-Importance-of-Data-Visualization.webp)

> Tầm quan trọng của Data Visualization

### 2.4 Mục tiêu và lợi ích của trực quan hóa dữ liệu

**Đơn giản hóa sự phức tạp:**

- Các hình ảnh trực quan giúp đơn giản hóa các tập dữ liệu phức tạp bằng cách trình bày thông tin một cách ngắn gọn và có tổ chức. Chúng cô đọng lượng dữ liệu khổng lồ thành các bản tóm tắt trực quan dễ hiểu và dễ diễn giải hơn.

![10](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/10.png)

> Ví dụ đơn giản hóa sự phức tạp trong Visualization

**Xác định các mẫu và xu hướng:**

- Các biểu diễn trực quan giúp chúng ta xác định các mẫu, xu hướng và mối quan hệ giữa các biến số mà có thể không rõ ràng trong dữ liệu thô. Bằng cách phát hiện ra các mẫu này, chúng ta có thể đưa ra dự đoán tốt hơn và rút ra những hiểu biết có thể hành động được.

![11](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/11.webp)

> Ví dụ xác định các mẫu và xu hướng

**Hỗ trợ ra quyết định(Aid Decision- Making):**

- Trực quan hóa dữ liệu cho phép người khai thác dữ liệu đưa ra các quyết định sáng suốt hơn bằng cách cung cấp sự hiểu biết rõ ràng về dữ liệu. Các biểu diễn trực quan hỗ trợ việc xác định các giá trị ngoại lệ, thực hiện so sánh và đánh giá các kịch bản khác nhau.

![12](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/12.jpg)

> Ví dụ dashboard hỗ trợ ra quyết định

**Nâng cao khả năng khám phá dữ liệu:**

- Các hình ảnh trực quan cho phép khám phá dữ liệu một cách tương tác, giúp người dùng **drill down** *đi sâu* vào các chi tiết cụ thể, lọc dữ liệu và khám phá các góc nhìn khác nhau. Tính tương tác này thúc đẩy sự hiểu biết sâu sắc hơn về dữ liệu cơ bản.

> Trực quan hóa dữ liệu giúp đặt dữ liệu vào đúng ngữ cảnh.

![13](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/13.png)


**Cải thiện giao tiếp:**

- Hình ảnh trực quan là một phương tiện hiệu quả để truyền đạt các phát hiện và hiểu biết cho các bên liên quan. Chúng tạo điều kiện thuận lợi cho việc chia sẻ thông tin một cách trực quan **hấp dẫn và dễ hiểu**, cho phép cộng tác và ra quyết định tốt hơn. Hỗ trợ trong việc communicate tốt hơn. 


### 2.5 Tại sao cần Visualization?

* **Sức mạnh não bộ:** Con người xử lý hình ảnh nhanh hơn văn bản/số liệu gấp nhiều lần.
* **Mục tiêu:**
1. **Exploration (Khám phá):** Tìm ra pattern hoặc outlier (điểm bất thường) mà thống kê thuần túy không thấy.
2. **Communication (Truyền tải):** Kể chuyện với dữ liệu (Data Storytelling) cho stakeholders.

### 2.6 Phân loại dữ liệu để chọn biểu đồ

Việc chọn biểu đồ phụ thuộc vào loại biến (Variable types):

* **Categorical (Định danh):** Nominal (Tên, màu sắc), Ordinal (Xếp hạng).  Thường dùng Bar chart, Pie chart.
* **Numerical (Định lượng):** Discrete (Số nguyên), Continuous (Số thực).  Thường dùng Histogram, Scatter plot, Line chart.

### Tóm tắt

- Data visualization: Graphical data representation.
- Importance in data mining: Clarity, insights, decision support.
- Goals: Simplify, discover, communicate.
- Benefits: Understanding, speed, communication.

[Kiến thức ôn lại một số thuật toán trong Machine Learning](https://www.youtube.com/watch?v=59XV4o8hOBk&t=613s)

---
## 3. Visualization of Numerical Data (Hiển thị dữ liệu số)

Phần này tập trung vào các kỹ thuật cho dữ liệu **Numerical** (quan trọng nhất cho AI/ML).

### 3.1 Numerical Data (Dữ liệu số)

- Dữ liệu số bao gồm các **giá trị định lượng có thể đo lường** và **biểu diễn bằng thang đo số**. Việc trực quan hóa dữ liệu số giúp chúng ta hiểu được sự phân bố, **xu hướng và mối quan hệ giữa các biến số số**.

### 3.2 Numerical Data Visualization (Trực quan hóa dữ liệu số)

- Trực quan hóa dữ liệu số đề cập đến việc **biểu diễn dữ liệu định lượng bằng đồ thị, biểu đồ và đồ thị** để **truyền đạt thông tin** một cách hiệu quả.

- **Não bộ con người** xử lý thông tin **trực quan hiệu quả hơn** dữ liệu thô.

- Việc trực quan hóa giúp xác định các mẫu, xu hướng và các điểm bất thường trong dữ liệu số, dẫn đến việc ra **quyết định tốt hơn**.

### 3.3 Các loại hình trực quan hóa khác nhau và ứng dụng của chúng 


**Line Graphs (Biểu đồ đường): Mô tả xu hướng theo thời gian hoặc dữ liệu có thứ tự**
- Biểu đồ đường nối các điểm dữ liệu bằng các đường thẳng để thể hiện xu hướng theo thời gian hoặc một biến số có thứ tự.
- Thể hiện xu hướng thị trường chứng khoán, theo dõi sự thay đổi nhiệt độ, thể hiện sự tăng trưởng dân số.

**Bar Charts (Biểu đồ cột): Hiển thị dữ liệu phân loại bằng hình chữ nhật**

- Biểu đồ cột sử dụng các cột hình chữ nhật để so sánh dữ liệu phân loại.
- Trực quan hóa kết quả khảo sát, so sánh doanh số bán hàng của các sản phẩm khác nhau, hiển thị phân bố tần suất.

**Scatter Plot (Biểu đồ phân tán): Trực quan hóa mối quan hệ giữa hai biến số**

- Biểu đồ phân tán sử dụng các điểm dữ liệu để hiển thị mối quan hệ giữa hai biến số dạng số. Giả sử biến số a thay đổi thì biến số b sẽ bị ảnh hưởng như thế nào?
- Đánh giá mối tương quan giữa các biến số, xác định các cụm hoặc xu hướng, phát hiện các giá trị ngoại lệ.

**Line Charts and Area Charts**

- **Biểu đồ đường** hiển thị các điểm dữ liệu được nối bằng các đường thẳng, thể hiện xu hướng hoặc sự thay đổi của một biến số theo thời gian hoặc một chiều liên tục khác.

- **Biểu đồ vùng** tương tự như biểu đồ đường nhưng được tô màu hoặc vẽ hoa văn bên dưới đường thẳng, thể hiện giá trị tích lũy của biến số.

![14](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/14.png)

**Bar Charts and Histograms**

- **Biểu đồ cột** sử dụng các thanh hình chữ nhật có chiều dài hoặc chiều cao khác nhau để biểu thị giá trị của các danh mục hoặc nhóm khác nhau. Chúng hữu ích để so sánh dữ liệu rời rạc hoặc dữ liệu phân loại.

- **Biểu đồ tần số** hiển thị sự phân bố của dữ liệu liên tục bằng cách chia dữ liệu thành các khoảng hoặc khoảng thời gian và biểu thị tần suất hoặc số lượng điểm dữ liệu trong mỗi khoảng dưới dạng các thanh dọc.

![15](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/15.png)

**Scatter Plots and Bubble Charts**

- **Biểu đồ phân tán** thể hiện mối quan hệ giữa hai biến số dạng số. Mỗi điểm dữ liệu được biểu diễn dưới dạng một điểm trên đồ thị, với một biến số trên trục x và biến số còn lại trên trục y.

- **Biểu đồ bong bóng** là một phần mở rộng của biểu đồ phân tán, trong đó một biến số dạng số bổ sung được biểu thị bằng kích thước hoặc màu sắc của các điểm dữ liệu, tạo thêm chiều sâu cho hình ảnh trực quan.

![16](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/16.png)

**Box Plots and Violin Plots**

- **Biểu đồ hộp** (còn được gọi là biểu đồ hộp và râu) hiển thị các số liệu thống kê tóm tắt của một biến số dạng số, bao gồm giá trị nhỏ nhất, lớn nhất, trung vị, tứ phân vị và các giá trị ngoại lệ. Chúng cung cấp cái nhìn sâu sắc về phân bố và độ lệch của dữ liệu.
- **Biểu đồ violin** kết hợp biểu đồ hộp với biểu đồ mật độ hạt nhân, cung cấp cái nhìn chi tiết hơn về phân bố và mật độ của dữ liệu.

![17](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/17.png)

**Heatmaps and Treemaps**

- **Biểu đồ nhiệt (Heatmap)** sử dụng các ô được mã hóa màu trong một lưới để biểu diễn giá trị của một biến số dạng số trên hai chiều. Chúng hiệu quả trong việc trực quan hóa các tập dữ liệu lớn và xác định các mẫu hoặc mối tương quan.

- **Biểu đồ cây (Treemap)** biểu diễn dữ liệu phân cấp dưới dạng các hình chữ nhật lồng nhau, với kích thước của mỗi hình chữ nhật tỷ lệ thuận với một giá trị số. Chúng hữu ích để hiển thị các mối quan hệ phân cấp và so sánh tỷ lệ.

![18](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/18.png)

### 3.4 Choosing the Right Visualization for Your Data

**Các yếu tố ảnh hưởng đến việc lựa chọn hình thức trực quan hóa:**

- Bản chất của dữ liệu (phân loại, thứ tự, số): Các loại dữ liệu khác nhau yêu cầu các hình thức trực quan hóa cụ thể.
- Phân bố và độ chi tiết của dữ liệu: Phân bố dữ liệu ảnh hưởng đến việc lựa chọn hình thức trực quan hóa.

**Hướng dẫn về việc kết hợp các loại dữ liệu với các hình thức trực quan hóa:**

- Sơ đồ cây quyết định để lựa chọn hình thức trực quan hóa phù hợp: Hướng dẫn từng bước để chọn đúng loại biểu đồ.
- Ví dụ về các lựa chọn trực quan hóa đúng và sai: Hình minh họa để củng cố khái niệm.

### 3.5 Các yếu tố thiết kế và cách sử dụng màu sắc (Elements of Design and Colour Usage)

**Tầm quan trọng của các nguyên tắc thiết kế trong trực quan hóa dữ liệu:**

- Nhấn mạnh sự rõ ràng, đơn giản và nhất quán: Đề cập đến tầm quan trọng của thiết kế trong trực quan hóa dữ liệu.
- Trực quan hóa được thiết kế tốt so với trực quan hóa được thiết kế kém.

![19](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/19.png)

**Lựa chọn bảng màu phù hợp cho dữ liệu số:**

- Giải quyết các vấn đề tiềm ẩn về chứng mù màu: Đảm bảo tính khả dụng và toàn diện.
- Ví dụ về các bảng màu phù hợp cho dữ liệu số

![20](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/20.png)

**Những lưu ý về chứng mù màu và khả năng tiếp cận:**

- Thiết kế hình ảnh trực quan dễ tiếp cận cho người dùng mù màu: Áp dụng các phương pháp tốt nhất cho thiết kế toàn diện.
- Ví dụ trực quan về hình ảnh trực quan có và không có lưu ý đến chứng mù màu.

![21](https://github.com/DazielNguyen/DBM302m/blob/main/image_lesson_notes/slot_02/21.png)

### 3.6 Các phương pháp tốt nhất để trực quan hóa dữ liệu số

- Chọn kỹ thuật trực quan hóa phù hợp dựa trên bản chất của dữ liệu và những thông tin bạn muốn truyền tải.
- Đảm bảo việc ghi nhãn rõ ràng cho các trục, tiêu đề và chú thích để cung cấp ngữ cảnh và hỗ trợ việc diễn giải.
- Sử dụng thang đo và phạm vi trục phù hợp để tránh làm sai lệch dữ liệu hoặc gây hiểu lầm cho người xem.
- Áp dụng màu sắc và các tín hiệu trực quan một cách cẩn trọng để làm nổi bật các mẫu, xu hướng hoặc các điểm dữ liệu cụ thể.
- Cân nhắc thêm các tính năng tương tác, chẳng hạn như phóng to hoặc lọc, để cho phép người dùng khám phá dữ liệu chi tiết hơn.

### Univariate Analysis (Phân tích 1 biến)

Dùng để xem phân phối của *một* thuộc tính (ví dụ: Phân phối tuổi của khách hàng).

* **Histogram:**
* Chia dữ liệu thành các khoảng (bins).
* Giúp nhìn thấy: Độ lệch (Skewness), Đỉnh (Modality), và Phân phối chuẩn (Normal distribution).


* **Box Plot (Biểu đồ hộp):** *Cực kỳ quan trọng để xử lý Outlier.*
* Hiển thị 5 thông số: Min, Q1 (25%), Median (50%), Q3 (75%), Max.
* Các điểm nằm ngoài "râu" (whiskers) là **Outliers**.



### Bivariate Analysis (Phân tích 2 biến)

Dùng để tìm mối quan hệ giữa *hai* thuộc tính (ví dụ: Giá nhà vs. Diện tích).

* **Scatter Plot (Biểu đồ phân tán):**
* Mỗi điểm là một quan sát (x, y).
* Giúp nhìn thấy: Tương quan (Correlation) - Tuyến tính hay phi tuyến tính, Tích cực hay tiêu cực.

### Tra cứu nhanh: Khi nào dùng biểu đồ nào?

| Loại biểu đồ | Mục đích sử dụng (Use Case) | Code Library (Python) |
| --- | --- | --- |
| **Histogram** | Xem phân phối (Distribution), kiểm tra độ lệch. | `plt.hist()`, `sns.histplot()` |
| **Box Plot** | Tìm Outliers, so sánh phân phối giữa các nhóm. | `plt.boxplot()`, `sns.boxplot()` |
| **Scatter Plot** | Tìm mối quan hệ (Correlation) giữa 2 biến số. | `plt.scatter()`, `sns.scatterplot()` |
| **Line Chart** | Xem xu hướng theo thời gian (Time-series). | `plt.plot()`, `sns.lineplot()` |
| **Heatmap** | Xem ma trận tương quan (Correlation Matrix). | `sns.heatmap()` |
