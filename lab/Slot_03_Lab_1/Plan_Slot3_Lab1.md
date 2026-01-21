# Plan Lab Slot 3 - Data Visualization & Dashboard

## 📋 Tổng quan
Bài lab gồm 2 phần chính:
- **Phần 2.1**: Data Visualization cơ bản với Pandas & Matplotlib
- **Phần 2.2**: Xây dựng Dashboard tương tác với Dash & Plotly

---

## 🎯 PHẦN 2.1: DATA VISUALIZATION CƠ BẢN

### ✅ Bước 1: Khởi tạo và Nạp dữ liệu
- [ ] **Cell 1: Import thư viện**
  - **Ý tưởng**: Khai báo pandas (as pd) và matplotlib.pyplot (as plt)
  - **Code**: `import pandas as pd` và `import matplotlib.pyplot as plt`
  - **Mục đích**: Chuẩn bị công cụ để xử lý dữ liệu và vẽ biểu đồ

- [ ] **Cell 2: Đọc file CSV**
  - **Ý tưởng**: Nạp file sales_data.csv vào DataFrame
  - **Code**: `df = pd.read_csv('sales_data.csv')`
  - **Kiểm tra**: In ra `type(df)` để xác nhận đã load thành công

---

### ✅ Bước 2: Khám phá dữ liệu (Data Exploration)
- [ ] **Cell 3: Xem dữ liệu mẫu**
  - **Ý tưởng**: Hiển thị 5 dòng đầu để hiểu cấu trúc dữ liệu
  - **Code**: `df.head()`
  - **Quan sát**: Xem các cột: Product, Amount, Date, Region, Quantity

- [ ] **Cell 4: Kiểm tra dữ liệu trống**
  - **Ý tưởng**: Đảm bảo không có giá trị NULL/NaN
  - **Code**: `df.isnull().sum()`
  - **Kỳ vọng**: Tất cả cột đều = 0 (không có dữ liệu trống)

- [ ] **Cell 5: Thống kê tổng quát**
  - **Ý tưởng**: Xem tóm tắt thống kê (mean, max, min, std)
  - **Code**: `df.describe()`
  - **Quan sát**: Amount trung bình, max, min; Quantity trung bình

- [ ] **Cell 6: Lọc dữ liệu theo sản phẩm**
  - **Ý tưởng**: Xem riêng 1 sản phẩm cụ thể (ví dụ: "Laptop")
  - **Code**: `df[df["Product"] == "Laptop"]`
  - **Mục đích**: Thực hành filtering data

---

### ✅ Bước 3: Trực quan hóa dữ liệu

#### 📊 a. Biểu đồ cột (Bar Chart) - So sánh doanh số
- [ ] **Cell 7: Chuẩn bị dữ liệu cho Bar Chart**
  - **Ý tưởng**: Tính tổng doanh số (Amount) theo từng Product
  - **Code**: `product_sales = df.groupby("Product")["Amount"].sum()`
  - **Kiểm tra**: In `product_sales` để xem kết quả

- [ ] **Cell 8: Vẽ Bar Chart**
  - **Ý tưởng**: Tạo biểu đồ cột so sánh doanh số các sản phẩm
  - **Code**:
    ```python
    product_sales.plot(kind="bar", color='skyblue', figsize=(10,6))
    plt.xlabel("Product")
    plt.ylabel("Total Sales (Amount)")
    plt.title("Total Sales by Product")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    ```
  - **Quan sát**: Sản phẩm nào bán chạy nhất?

#### 📈 b. Biểu đồ đường (Line Chart) - Xu hướng thời gian
- [ ] **Cell 9: Chuyển đổi kiểu dữ liệu Date**
  - **Ý tưởng**: Convert cột Date từ string sang datetime
  - **Code**: `df["Date"] = pd.to_datetime(df["Date"])`
  - **Kiểm tra**: In `df["Date"].dtype` để xác nhận đã là datetime64

- [ ] **Cell 10: Chuẩn bị dữ liệu cho Line Chart**
  - **Ý tưởng**: Tính tổng doanh số theo từng ngày
  - **Code**: `daily_sales = df.groupby("Date")["Amount"].sum()`
  - **Sắp xếp**: Đảm bảo dữ liệu theo thứ tự thời gian

- [ ] **Cell 11: Vẽ Line Chart**
  - **Ý tưởng**: Xem xu hướng doanh số theo thời gian
  - **Code**:
    ```python
    daily_sales.plot(kind="line", color='green', marker='o', figsize=(12,6))
    plt.xlabel("Date")
    plt.ylabel("Total Sales (Amount)")
    plt.title("Sales Trend Over Time")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    ```
  - **Quan sát**: Doanh số có tăng/giảm theo thời gian?

#### 🔵 c. Biểu đồ phân tán (Scatter Plot) - Phân bổ điểm bán
- [ ] **Cell 12: Vẽ Scatter Plot**
  - **Ý tưởng**: Xem phân bổ từng giao dịch theo ngày
  - **Code**:
    ```python
    plt.figure(figsize=(12,6))
    plt.scatter(df["Date"], df["Amount"], alpha=0.6, c='coral', edgecolors='black')
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Sales Distribution by Date")
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    ```
  - **Quan sát**: Có outlier (điểm bất thường) nào không?

---

## 🚀 PHẦN 2.2: XÂY DỰNG DASHBOARD TƯƠNG TÁC

> **Lưu ý**: Phần này nên làm trong file Python riêng (`.py`) thay vì Notebook vì Dash cần chạy server.

### ✅ Bước 1: Cài đặt thư viện Dash
- [ ] **Terminal: Cài đặt Dash**
  - **Lệnh**: `pip install dash plotly`
  - **Kiểm tra**: `pip list | grep dash`

---

### ✅ Bước 2: Tạo file Python cho Dashboard
- [ ] **Tạo file: `dashboard_app.py`**
  - **Vị trí**: Trong cùng folder với notebook
  - **Mục đích**: Tách code Dashboard ra khỏi notebook để dễ quản lý

---

### ✅ Bước 3: Xây dựng code Dashboard

#### 📦 Cell/Phần 1: Import và Load Data
- [ ] **Import thư viện Dashboard**
  - **Ý tưởng**: Khai báo Dash, dcc, html, Input, Output
  - **Code**:
    ```python
    import dash
    from dash import dcc, html, Input, Output
    import plotly.express as px
    import plotly.graph_objects as go
    import pandas as pd
    ```

- [ ] **Load dữ liệu với xử lý ngoại lệ**
  - **Ý tưởng**: Dùng try-except để xử lý trường hợp thiếu file
  - **Code**:
    ```python
    try:
        df = pd.read_csv('sales_data.csv')
        df['Date'] = pd.to_datetime(df['Date'])
    except FileNotFoundError:
        # Tạo dữ liệu giả lập (Mock Data)
        df = pd.DataFrame({
            'Product': ['Laptop', 'Phone', 'Tablet'] * 10,
            'Amount': [1000, 500, 300] * 10,
            'Date': pd.date_range('2024-01-01', periods=30, freq='D')
        })
    ```

#### 🎨 Cell/Phần 2: Khởi tạo Dash App
- [ ] **Tạo instance Dash**
  - **Ý tưởng**: Khởi tạo ứng dụng Dash
  - **Code**: `app = dash.Dash(__name__)`

#### 🏗️ Cell/Phần 3: Thiết kế Layout
- [ ] **Xây dựng giao diện HTML**
  - **Ý tưởng**: Tạo cấu trúc với tiêu đề và 2 biểu đồ song song
  - **Code**:
    ```python
    app.layout = html.Div([
        html.H1("📊 Sales Dashboard", 
                style={'textAlign': 'center', 'color': '#2c3e50'}),
        
        html.Div([
            # Biểu đồ Bar Chart
            html.Div([
                dcc.Graph(id='bar-chart')
            ], style={'width': '48%', 'display': 'inline-block'}),
            
            # Biểu đồ Line Chart
            html.Div([
                dcc.Graph(id='line-chart')
            ], style={'width': '48%', 'display': 'inline-block'})
        ], style={'display': 'flex', 'justifyContent': 'space-around'})
    ])
    ```

#### ⚙️ Cell/Phần 4: Callback Logic - Tương tác
- [ ] **Xây dựng callback cho tương tác**
  - **Ý tưởng**: Khi chọn vùng trên Bar Chart → Line Chart cập nhật
  - **Code**:
    ```python
    @app.callback(
        [Output('bar-chart', 'figure'),
         Output('line-chart', 'figure')],
        [Input('bar-chart', 'selectedData')]
    )
    def update_charts(selectedData):
        # Xử lý dữ liệu lọc
        if selectedData is None or not selectedData.get('points'):
            filtered_df = df
        else:
            # Lấy danh sách Product được chọn
            selected_products = [point['x'] for point in selectedData['points']]
            filtered_df = df[df['Product'].isin(selected_products)]
        
        # Tạo Bar Chart
        product_sales = filtered_df.groupby('Product')['Amount'].sum().reset_index()
        bar_fig = px.bar(product_sales, x='Product', y='Amount',
                         title='Total Sales by Product',
                         color='Amount',
                         color_continuous_scale='Blues')
        
        # Tạo Line Chart
        daily_sales = filtered_df.groupby('Date')['Amount'].sum().reset_index()
        line_fig = px.line(daily_sales, x='Date', y='Amount',
                           title='Sales Trend Over Time',
                           markers=True)
        
        return bar_fig, line_fig
    ```

#### ▶️ Cell/Phần 5: Chạy Server
- [ ] **Khởi động ứng dụng**
  - **Ý tưởng**: Bật server với debug mode
  - **Code**:
    ```python
    if __name__ == '__main__':
        app.run(debug=True, port=8050)
    ```

---

### ✅ Bước 4: Chạy và Kiểm thử Dashboard
- [ ] **Chạy file Python từ Terminal**
  - **Lệnh**: `python dashboard_app.py`
  - **Kết quả**: Server chạy tại `http://127.0.0.1:8050`

- [ ] **Kiểm tra chức năng tương tác**
  - Mở trình duyệt → `http://127.0.0.1:8050`
  - Thử chọn vùng trên Bar Chart (drag/lasso tool)
  - Xem Line Chart tự động cập nhật theo sản phẩm được chọn

- [ ] **Test các tính năng**
  - Zoom in/out trên biểu đồ
  - Hover để xem giá trị chi tiết
  - Reset selection để xem toàn bộ dữ liệu

---

## 📝 GHI CHÚ QUAN TRỌNG

### Cấu trúc Cell trong Notebook (Phần 2.1)
```
Cell 1:  Import libraries
Cell 2:  Load data
Cell 3:  Explore - head()
Cell 4:  Explore - isnull()
Cell 5:  Explore - describe()
Cell 6:  Explore - filter
Cell 7:  Process - groupby for bar
Cell 8:  Visualize - Bar Chart
Cell 9:  Process - convert date
Cell 10: Process - groupby for line
Cell 11: Visualize - Line Chart
Cell 12: Visualize - Scatter Plot
```

### Tách file cho Phần 2.2
Vì Dashboard cần chạy server liên tục, nên:
- **Notebook**: Giữ phần 2.1 (khám phá + visualization cơ bản)
- **File .py riêng**: Phần 2.2 (Dashboard app)

---

## ✨ LƯU Ý TRƯỚC KHI CHẠY

1. **Đường dẫn file**: Đảm bảo `sales_data.csv` cùng folder với notebook/script
2. **Thư viện**: Cài đủ pandas, matplotlib, dash, plotly
3. **Dash không chạy trong Jupyter**: Phải tạo file `.py` riêng cho phần 2.2
4. **Debug mode**: Giúp tự động reload khi sửa code

---

## 🎯 MỤC TIÊU ĐẠT ĐƯỢC

- [x] Hiểu cách load và explore dữ liệu với Pandas
- [x] Vẽ được 3 loại biểu đồ cơ bản (Bar, Line, Scatter)
- [x] Xây dựng được Dashboard tương tác
- [x] Hiểu callback mechanism trong Dash
- [x] Biết cách xử lý lỗi (try-except) và tạo mock data

---

**🚀 Sẵn sàng bắt đầu? Hãy làm từng bước và check ✅ khi hoàn thành!**
