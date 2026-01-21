## Hướng dẫn 2.1: 

### Bước 1: Khởi tạo và Nạp dữ liệu

Trước tiên, bạn cần chuẩn bị môi trường làm việc bằng cách khai báo các công cụ cần thiết:
-	Khai báo thư viện: Sử dụng từ khóa import để nạp thư viện pandas (thường đặt tên rút gọn là pd) và thư viện matplotlib.pyplot (thường đặt là plt).
-	Nạp file CSV: Sử dụng hàm read_csv() của Pandas để đọc file sales_data.csv. Bạn cần gán kết quả này vào một biến (ví dụ: df) để thực hiện các thao tác tiếp theo.
### Bước 2: Khám phá dữ liệu (Data Exploration)
Trước khi phân tích, bạn cần hiểu dữ liệu của mình trông như thế nào.
-	Xem dữ liệu mẫu: Sử dụng phương thức .head() trên biến df để hiển thị 5 dòng đầu tiên.
-	Kiểm tra dữ liệu trống: Để đảm bảo dữ liệu "sạch", hãy kết hợp phương thức .isnull() và .sum() để đếm số lượng ô trống trong từng cột.
-	Thống kê tổng quát: Sử dụng hàm .describe() để máy tính tự động tính toán các thông số như trung bình (mean), giá trị lớn nhất (max), nhỏ nhất (min) của các cột chứa số.
-	Lọc dữ liệu: Để xem riêng một mặt hàng, bạn sử dụng cú pháp lọc theo điều kiện: df[df["Tên_Cột"] == "Giá_Trị_Cần_Lọc"].
### Bước 3: Trực quan hóa dữ liệu (Data Visualization)
Đây là bước biến các con số khô khan thành hình ảnh dễ hiểu.

a. Biểu đồ cột (Bar Chart) - So sánh doanh số

-	Xử lý dữ liệu: Bạn cần nhóm dữ liệu theo cột "Product" bằng hàm .groupby(), sau đó chọn cột "Amount" và dùng hàm .sum() để tính tổng.
-	Vẽ biểu đồ: Sử dụng phương thức .plot() với tham số kind="bar".
-	Trang trí: Sử dụng plt.xlabel(), plt.ylabel() và plt.title() để thêm nhãn cho các trục và tiêu đề. Cuối cùng dùng plt.show() để hiển thị.

b. Biểu đồ đường (Line Chart) - Xu hướng thời gian

-	Chuyển đổi kiểu dữ liệu: Cột ngày tháng thường bị hiểu nhầm là văn bản. Bạn phải dùng hàm pd.to_datetime() để chuyển đổi cột "Date" về đúng định dạng thời gian.
-	Gom nhóm theo ngày: Tương tự biểu đồ cột, hãy nhóm theo "Date" và tính tổng "Amount".
-	Vẽ biểu đồ: Sử dụng .plot() với kind="line" để quan sát sự tăng trưởng.

c. Biểu đồ phân tán (Scatter Plot) - Phân bổ điểm bán

-	Vẽ điểm dữ liệu: Thay vì tính tổng, bạn dùng trực tiếp hàm plt.scatter() và truyền vào hai trục tương ứng là cột ngày tháng và cột số tiền.
-	Tối ưu hiển thị: Nếu các nhãn ngày tháng bị dính vào nhau, hãy dùng lệnh plt.xticks() với tham số rotation=45 để xoay chữ giúp dễ đọc hơn.

## Hướng dẫn 2.2: 

### 1. Tư duy Thiết kế Hệ thống (Workflow)

Một ứng dụng Dashboard chuyên nghiệp thường được xây dựng dựa trên 3 lớp nền tảng:

1.	Lớp Dữ liệu (Data): Đọc, xử lý và chuẩn bị dữ liệu sẵn sàng để hiển thị.
2.	Lớp Giao diện (Layout): Định nghĩa cấu trúc hình ảnh của Dashboard (vị trí tiêu đề, biểu đồ).
3.	Lớp Tương tác (Interactivity/Callback): Định nghĩa cách các thành phần phản hồi khi người dùng thao tác.

--- 

### 2. Các bước Thực hiện Chi tiết

#### Bước 1: Quản lý Dữ liệu

Trong môi trường web, ứng dụng có thể bị sập hoàn toàn nếu không tìm thấy file dữ liệu. Bạn cần xây dựng một cơ chế dự phòng:
-	Xử lý ngoại lệ: Sử dụng cấu trúc try...except trong Python để kiểm tra việc nạp file sales_data.csv.
-	Dữ liệu giả lập (Mock Data): Trong phần except FileNotFoundError, hãy sử dụng Pandas để tạo một DataFrame tạm thời với các cột "Product", "Amount", và "Date". Điều này đảm bảo ứng dụng vẫn có dữ liệu để demo ngay cả khi file CSV bị thiếu.

#### Bước 2: Thiết lập Giao diện (Layout)

Dash sử dụng các thành phần HTML để xây dựng giao diện. Bạn cần sắp xếp các khối sau:
-	Thành phần tĩnh: Sử dụng html.H1 cho tiêu đề chính và html.Div để bao bọc các phần của Dashboard.
-	Thành phần biểu đồ: Sử dụng dcc.Graph (Dash Core Components) để tạo không gian chứa cho các biểu đồ Plotly. Đừng quên đặt id cho từng biểu đồ để gọi lại sau này.
-	Tối ưu bố cục: Để hiển thị hai biểu đồ nằm ngang hàng thay vì xếp chồng, hãy sử dụng thuộc tính CSS style={'display': 'flex'} trong html.Div bao quanh chúng.



#### Bước 3: Xây dựng Cơ chế Tương tác (Callback Logic)

Đây là "trái tim" của Dashboard, giúp cập nhật biểu đồ dựa trên hành động của người dùng.
-	Xác định Đầu vào (Input): Bạn cần lấy thông tin từ thuộc tính selectedData của biểu đồ Bar Chart khi người dùng quét chọn vùng.
-	Xử lý logic trong hàm:
	+ Kiểm tra lựa chọn: Nếu selectedData là None hoặc trống, hãy trả về toàn bộ dữ liệu gốc.
	+ Trích xuất dữ liệu: Khi có vùng chọn, bạn cần truy cập vào Dictionary/JSON để lấy danh sách tên các "Product" từ key 'x' trong danh sách các điểm (points).
	+ Lọc dữ liệu: Sử dụng phương thức .isin() của Pandas để lọc DataFrame gốc dựa trên danh sách sản phẩm vừa trích xuất.
-	Xác định Đầu ra (Output): Hàm phải trả về các đối tượng biểu đồ mới (đã cập nhật dữ liệu sau khi lọc) để Dash tự động cập nhật vào các dcc.Graph tương ứng trên giao diện.

#### Bước 4: Vận hành và Kiểm thử

Để quá trình lập trình diễn ra nhanh chóng, hãy kích hoạt chế độ Debug:
-	Sử dụng lệnh app.run(debug=True) để ứng dụng tự động tải lại (hot reload) mỗi khi bạn thay đổi code mà không cần khởi động lại thủ công.

