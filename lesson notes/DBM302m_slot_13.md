# **Slot 13 - Chapter 4 Introduction to Cluster Analysis & Similarity Measures for Cluster Analysis**

**Ngày học: 03/03/2026**

**Nội dung chương học:**

- 4.1 Introduction to Cluster Analysis( cont_).pptx 
- 4.2 Similarity Measures for Cluster Analysis.pptx (50% - 3 objective đầu tiên)

---

## 1. Tổng quan về Clustering (Gom cụm dữ liệu)

Giảng viên mở đầu bằng việc nhắc lại bản chất của Clustering. Khác với Classification (Phân loại) cần có nhãn (label) cho trước, **Clustering là bài toán Unsupervised Learning (Học không giám sát)**. Thuật toán sẽ tự động nhận diện các điểm dữ liệu có đặc điểm giống nhau và gom chúng lại thành từng cụm mà không cần biết trước mỗi cụm đại diện cho cái gì.

## 2. Các phương pháp Gom cụm chính (Clustering Methods)

Giảng viên phân chia Clustering thành các nhóm phương pháp tiếp cận cơ bản sau:

* **Hierarchical Clustering (Phân cụm phân cấp):** Tổ chức dữ liệu theo cấu trúc hình cây (Tree-based). Dữ liệu được gom thành các cụm lồng vào nhau (Nested clusters). Có hai hướng tiếp cận:
* **Agglomerative (Bottom-up):** Đi từ dưới lên. Bắt đầu với mỗi điểm dữ liệu là một cụm riêng lẻ, sau đó gộp dần các cụm gần nhau lại cho đến khi tạo thành một cụm lớn duy nhất.
* **Divisive (Top-down):** Đi từ trên xuống. Bắt đầu với tất cả dữ liệu nằm chung một cụm khổng lồ, sau đó chẻ nhỏ dần ra.


* **Partitioning Clustering (Phân cụm phân hoạch):** Chia dữ liệu thành các cụm tách biệt hoàn toàn, không lồng ghép vào nhau. Thuật toán tiêu biểu nhất là **K-Means**. Người dùng cần xác định trước số lượng cụm (K) muốn chia.
* **Density-based Clustering (Dựa trên mật độ):** Thuật toán tìm kiếm các khu vực có mật độ điểm dữ liệu tập trung dày đặc để tạo thành cụm. Phương pháp này rất hiệu quả trong việc loại bỏ nhiễu (outliers). Thuật toán tiêu biểu là DBSCAN.
* **Grid-based Clustering (Dựa trên lưới):** Không gian dữ liệu được chia thành các ô vuông (grid) để xử lý tính toán.
* **Model-based Clustering (Dựa trên mô hình):** Sử dụng các mô hình thống kê, xác suất để gom cụm.

## 3. Các thuộc tính của Cụm (Cluster Types)

* **Exclusive (Độc quyền):** Một điểm dữ liệu chỉ thuộc về duy nhất một cụm (Ví dụ: K-Means).
* **Non-exclusive / Overlapping (Chồng chéo):** Một điểm dữ liệu có thể thuộc về nhiều cụm khác nhau.
* **Fuzzy Clustering (Cụm mờ):** Mỗi điểm dữ liệu sẽ có một "trọng số" hoặc "xác suất" (từ 0 đến 1) thể hiện mức độ thuộc về từng cụm.

## 4. Vai trò của con người trong phân tích cụm

Giảng viên nhấn mạnh một điểm cốt lõi: Thuật toán chỉ làm nhiệm vụ tính toán và gom nhóm (ví dụ: tạo ra 5 cụm khách hàng). **Thuật toán không biết các cụm đó có ý nghĩa gì**.
Nhiệm vụ của con người (Data Analyst/Business Analyst) là nhìn vào đặc điểm của từng cụm, giải thích ý nghĩa, đặt tên cho chúng (ví dụ: Cụm khách hàng VIP, Cụm khách hàng vãng lai) và từ đó đưa ra các chiến lược kinh doanh phù hợp.

## 5. Đo lường sự tương đồng và khoảng cách (Similarity & Distance Measures)

Để thuật toán biết điểm dữ liệu nào giống nhau để gom lại, nó phải dựa vào việc đo khoảng cách. Khoảng cách càng ngắn, dữ liệu càng giống nhau. Các công thức đo lường chính bao gồm:

* **Euclidean Distance:** Khoảng cách đường thẳng trực tiếp giữa hai điểm (đường chim bay).
* **Manhattan Distance:** Khoảng cách di chuyển theo hình zíc-zắc, vuông góc (giống như đi trên các khối nhà ở thành phố Manhattan).
* **Minkowski Distance:** Là một công thức tổng quát, bao trùm cả Euclidean và Manhattan tùy thuộc vào tham số được thiết lập.

## 6. Các loại dữ liệu đầu vào (Data Types)

Thuật toán gom cụm xử lý nhiều loại dữ liệu khác nhau:

* **Numeric (Dữ liệu số):** Các giá trị định lượng có thể tính toán toán học (chiều cao, cân nặng, thu nhập).
* **Categorical / Nominal (Dữ liệu phân loại/định danh):** Các giá trị dạng nhãn, danh mục không có tính thứ tự (màu sắc áo: đỏ, xanh, vàng).
* **Binary (Dữ liệu nhị phân):** Chỉ có 2 giá trị (0 hoặc 1, True hoặc False).


## 7. Chi tiết Thuật toán K-Means (K-Means Clustering)

Giảng viên đã trình bày cụ thể từng bước hoạt động của thuật toán gom cụm K-Means, một thuật toán thuộc nhóm Partitioning (Phân hoạch):

* **Bước 1 (Khởi tạo):** Người dùng phải xác định trước số lượng cụm $K$ mong muốn. Thuật toán sẽ chọn ngẫu nhiên $K$ điểm trong không gian dữ liệu để làm tâm cụm ban đầu (gọi là Centroids).
* **Bước 2 (Gán cụm - Assignment):** Thuật toán tính toán khoảng cách từ mỗi điểm dữ liệu đến $K$ tâm cụm. Điểm dữ liệu nào gần tâm nào nhất sẽ được gán vào cụm của tâm đó.
* **Bước 3 (Cập nhật tâm - Update):** Sau khi các cụm được hình thành, thuật toán sẽ tính toán lại vị trí của các tâm cụm. Tâm mới sẽ là điểm trung bình (mean) của tất cả các điểm dữ liệu đang nằm trong cụm đó.
* **Bước 4 (Lặp lại):** Lặp lại Bước 2 và Bước 3 cho đến khi vị trí của các tâm cụm không còn thay đổi nữa (đạt trạng thái hội tụ).

**Nhược điểm của K-Means:** Thuật toán này rất nhạy cảm với các điểm dữ liệu nhiễu (outliers). Vì tâm cụm được tính bằng giá trị trung bình, một điểm nhiễu có giá trị quá lớn hoặc quá nhỏ sẽ kéo lệch vị trí của tâm cụm một cách sai lệch.

## 8. Thuật toán K-Medoids (Biến thể của K-Means)

Để khắc phục điểm yếu nhạy cảm với nhiễu của K-Means, giảng viên giới thiệu thuật toán **K-Medoids**.

* Thay vì lấy giá trị trung bình toán học (mean) làm tâm cụm ảo, K-Medoids sẽ chọn một **điểm dữ liệu thực tế** nằm ở vị trí trung tâm nhất của cụm để làm tâm (gọi là Medoid).
* Cách tiếp cận này giúp thuật toán ổn định hơn và ít bị ảnh hưởng bởi các giá trị ngoại lai (outliers).

## 9. Chi tiết Hierarchical Clustering (Gom cụm phân cấp)

Giảng viên đi sâu vào cách tiếp cận **Agglomerative (Bottom-up - Đi từ dưới lên)** trong gom cụm phân cấp:

* **Cơ chế:** Ban đầu, hệ thống coi mỗi điểm dữ liệu là một cụm độc lập (nếu có $N$ điểm thì có $N$ cụm). Ở mỗi bước tiếp theo, thuật toán sẽ tìm ra hai cụm có khoảng cách gần nhau nhất và gộp chúng lại thành một cụm lớn hơn. Quá trình này lặp lại cho đến khi tất cả các điểm được gộp chung thành một cụm duy nhất.
* **Cách tính khoảng cách giữa hai cụm (Inter-cluster similarity):** Khi các điểm đã tạo thành cụm, việc đo khoảng cách giữa cụm A và cụm B được thực hiện qua các phương pháp (Linkage methods) sau:
* **MIN (Single Linkage):** Lấy khoảng cách ngắn nhất giữa hai điểm bất kỳ thuộc hai cụm khác nhau.
* **MAX (Complete Linkage):** Lấy khoảng cách xa nhất giữa hai điểm bất kỳ thuộc hai cụm khác nhau.
* **Group Average:** Tính trung bình cộng khoảng cách của tất cả các cặp điểm giữa cụm A và cụm B.
* **Distance between centroids:** Tính khoảng cách trực tiếp giữa hai tâm (centroid) của hai cụm.

## 10. Biểu diễn bằng Dendrogram

* Toàn bộ quá trình gộp cụm (Agglomerative) được trực quan hóa bằng một biểu đồ hình cây gọi là **Dendrogram**.
* Trục tung của Dendrogram thể hiện khoảng cách (hoặc độ tương đồng) tại thời điểm hai cụm được gộp lại với nhau.
* Người phân tích có thể dựa vào Dendrogram để quyết định cắt cây ở một mức độ cao (khoảng cách) nhất định, từ đó thu được số lượng cụm (K) phù hợp nhất với bài toán mà không cần phải đoán trước số $K$ như thuật toán K-Means.
---

### CHÚ THÍCH CÁC THUẬT NGỮ QUAN TRỌNG

| Thuật ngữ | Tiếng Việt | Giải thích chuyên sâu |
| --- | --- | --- |
| **Unsupervised Learning** | Học không giám sát | Kỹ thuật học máy nơi dữ liệu đầu vào không được dán nhãn sẵn. Hệ thống tự tìm ra cấu trúc, quy luật và mối liên hệ ẩn bên trong dữ liệu. |
| **Clustering** | Gom cụm | Một kỹ thuật của Unsupervised Learning, nhằm nhóm các đối tượng dữ liệu sao cho các đối tượng trong cùng một nhóm (cụm) có tính tương đồng cao, và khác biệt với các cụm khác. |
| **Hierarchical Clustering** | Gom cụm phân cấp | Xây dựng hệ thống các cụm theo cấu trúc hình cây (Dendrogram). Nó giúp người dùng thấy được thứ bậc và cách dữ liệu được gộp/tách qua từng giai đoạn. |
| **K-Means** | Thuật toán K-Means | Một thuật toán Gom cụm phân hoạch phổ biến. Nó chia tập dữ liệu thành *K* cụm (K do người dùng định nghĩa trước) dựa trên việc tìm ra điểm trung tâm (centroid) tối ưu cho mỗi cụm. |
| **Density-based** | Dựa trên mật độ | Phương pháp tìm các khu vực có mật độ dữ liệu cao và phân tách chúng khỏi các khu vực có mật độ thấp. Ưu điểm lớn nhất là có thể nhận diện các cụm có hình dạng bất kỳ và xử lý tốt dữ liệu nhiễu (noise). |
| **Euclidean Distance** | Khoảng cách Euclidean | Cách đo khoảng cách đường thẳng ngắn nhất giữa hai điểm trong không gian. Nó được tính bằng định lý Pythagoras. |
| **Manhattan Distance** | Khoảng cách Manhattan | Đo khoảng cách giữa hai điểm dựa trên tổng chênh lệch tuyệt đối dọc theo các trục tọa độ. (Giống như việc bạn không thể đi xuyên qua các tòa nhà mà phải đi dọc theo các con đường vuông góc). |
| **Fuzzy Clustering** | Gom cụm mờ | Thay vì chỉ định cứng nhắc "một điểm chỉ thuộc một cụm", gom cụm mờ gán cho mỗi điểm một giá trị xác suất để nó có thể thuộc về nhiều cụm cùng một lúc. |


| Thuật ngữ | Tiếng Việt | Giải thích chuyên sâu |
| --- | --- | --- |
| **Centroid** | Tâm cụm | Một điểm trung tâm đại diện cho toàn bộ một cụm trong không gian dữ liệu. Trong K-Means, điểm này thường là trung bình cộng (mean) tọa độ của tất cả các điểm trong cụm đó và có thể không phải là một điểm dữ liệu có thật. |
| **Convergence** | Trạng thái hội tụ | Trạng thái mà thuật toán dừng lại vì không tìm thấy sự cải thiện nào nữa. Trong K-Means, hội tụ xảy ra khi việc tính lại trung bình không làm các centroid di chuyển nữa, và không có điểm dữ liệu nào bị đổi sang cụm khác. |
| **Outlier** | Điểm nhiễu / Giá trị ngoại lai | Các điểm dữ liệu nằm cách xa bất thường so với phần lớn các điểm dữ liệu còn lại. Chúng thường gây sai số lớn cho các mô hình tính toán dựa trên trung bình (như K-Means). |
| **Medoid** | Tâm cụm thực tế | Tương tự như Centroid, nhưng Medoid bắt buộc phải là một điểm dữ liệu thực tế đang tồn tại trong tập dữ liệu (không phải là một điểm tọa độ ảo được tính ra). |
| **Linkage** | Phương pháp liên kết | Tiêu chí để đo lường khoảng cách giữa hai nhóm điểm (hai cụm) với nhau, thay vì chỉ đo giữa hai điểm đơn lẻ. |
| **Dendrogram** | Biểu đồ hệ thống phân cấp | Một sơ đồ dạng cây hiển thị trình tự các cụm được kết hợp (hoặc chia tách) ở mỗi bước. Nó cung cấp cái nhìn toàn cảnh về cấu trúc phân tầng của dữ liệu. |

