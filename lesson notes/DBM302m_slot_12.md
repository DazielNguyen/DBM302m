

### 1. Xử lý luồng dữ liệu (Stream Data Processing) & Single Scan

* **Bài toán thực tế:** Giảng viên lấy ví dụ về việc cập nhật dữ liệu của các trận đấu thể thao (tỷ số, thẻ đỏ, số đường chuyền...) theo thời gian thực (real-time).
* **Đặc điểm:** Dữ liệu luồng đến liên tục và có khối lượng khổng lồ. Việc lưu trữ toàn bộ dữ liệu này tốn chi phí rất lớn.
* **Giải pháp:** Áp dụng thuật toán **Single Scan** (quét một lần). Hệ thống chỉ nhìn dữ liệu một lần, xử lý, cập nhật thông tin và không cần lưu trữ lại toàn bộ dữ liệu thô để tiết kiệm không gian.

### 2. Ứng dụng AI/IoT và Điện toán biên (Edge Computing)

* **Tối ưu hóa chi phí:** Thay vì chạy các mô hình AI trên các laptop đắt tiền (hàng chục triệu đồng), sinh viên được khuyến khích sử dụng các thiết bị nhúng giá rẻ như Raspberry Pi (khoảng 100 - 150 USD).
* **Triển khai thực tế:** Chuyển đổi các mô hình AI phức tạp sang dạng nhẹ hơn (như TensorFlow Lite) để chạy trực tiếp trên các thiết bị nhúng.
* **Ứng dụng:** Nhận diện khói, lửa, cảnh báo hành vi người dùng (User Behavior) trong các hệ thống nhà thông minh (Smart Home).

### 3. Chiến lược phân tích dữ liệu lớn (Quy tắc 1%)

* **Ví dụ Viettel:** Với một tập khách hàng khổng lồ (ví dụ 100 triệu người dùng), việc phân tích toàn bộ là bất khả thi và lãng phí tài nguyên.
* **Giải pháp:** Thuật toán sẽ tập trung tìm kiếm lỗi hoặc phân tích hành vi của **1% những người dùng năng động nhất** (power users - những người dùng mạng, gọi điện liên tục). Nếu giải quyết được vấn đề cho nhóm này, hệ thống sẽ bao phủ được phần lớn doanh thu và các lỗi phổ biến nhất.

### 4. Thuật toán Lossy Counting (Đếm xấp xỉ)

* **Mục đích:** Tìm ra các phần tử xuất hiện phổ biến (frequent items) trong một luồng dữ liệu khổng lồ mà không tốn nhiều bộ nhớ.
* **Cách hoạt động:** * Chia luồng dữ liệu thành các "bucket" (nhóm). Kích thước của mỗi bucket được tính bằng công thức $1/\epsilon$ (với $\epsilon$ là ngưỡng sai số cho phép). Ví dụ: Nếu sai số cho phép là $0.001$, kích thước bucket sẽ là $1000$ phần tử.
* Thuật toán đếm tần suất xuất hiện của các phần tử. Sau mỗi bucket, hệ thống sẽ **xóa (trừ đi 1)** các phần tử có tần suất xuất hiện quá thấp để giải phóng bộ nhớ, chỉ giữ lại những phần tử thực sự phổ biến.



### 5. Computer Vision (Thị giác máy tính) & Trích xuất đặc trưng

* Để máy tính nhận diện được một hình ảnh (ví dụ: bông hoa), nó không nhìn hình ảnh như con người mà nhìn vào các ma trận điểm ảnh (pixels).
* Hệ thống sẽ tập trung tìm kiếm các **đặc trưng (features)** nổi bật có tính lặp đi lặp lại hoặc có độ tương phản cao (ví dụ: nhụy hoa có màu sắc khác biệt so với cánh hoa và phần viền xung quanh).

### 6. Phân cụm dữ liệu (Cluster Analysis / Clustering)

* **Khái niệm:** Là quá trình gom nhóm các dữ liệu có đặc điểm giống nhau vào cùng một cụm (cluster) và tách biệt các cụm khác nhau.
* **Ứng dụng:** Dùng nhiều trong Marketing (phân loại khách hàng theo độ tuổi, sở thích), hoặc Sinh học (phân nhóm gen).
* **Các kỹ thuật đi kèm:**
* **Giảm chiều dữ liệu (Dimensionality Reduction):** Dùng thuật toán PCA để giảm dữ liệu từ hàng trăm chiều xuống còn 2-3 chiều để con người có thể vẽ biểu đồ và quan sát được.
* **Chuẩn hóa dữ liệu (Normalization):** Bắt buộc phải đưa dữ liệu về cùng một thang đo (ví dụ: từ 0 đến 1) trước khi phân cụm.
* **Phương pháp Elbow:** Dùng để xác định số lượng cụm (K) tối ưu nhất.

### 7. Đi sâu vào thuật toán Lossy Counting (Đếm xấp xỉ trên luồng dữ liệu)

Lossy Counting là một thuật toán cực kỳ thông minh để giải quyết bài toán "tìm kiếm phần tử xuất hiện nhiều nhất (Frequent Items)" trong một luồng dữ liệu (Data Stream) dài vô tận, khi mà bộ nhớ RAM của máy tính là có hạn.

* **Vấn đề cốt lõi:** Nếu luồng dữ liệu liên tục đổ về (như log web, luồng tweet, dữ liệu cảm biến IoT), bạn không thể lưu một bảng băm (Hash Table) chứa mọi phần tử và số lần xuất hiện của chúng vì bộ nhớ sẽ nhanh chóng bị đầy.
* **Cơ chế hoạt động chi tiết:**
1. **Chia luồng thành các "Bucket" (Nhóm/Cửa sổ):** Luồng dữ liệu được chia thành các đoạn nhỏ bằng nhau. Độ dài của mỗi đoạn (ký hiệu là $w$) được tính bằng công thức $w = 1/\epsilon$, với $\epsilon$ là sai số cho phép. Ví dụ, nếu bạn chấp nhận sai số $1\% (\epsilon = 0.01)$, mỗi bucket sẽ chứa $100$ phần tử.
2. **Đếm và Cập nhật:** Máy tính duy trì một danh sách (từ điển) các phần tử đang được theo dõi và số lần xuất hiện (tần suất) của chúng. Khi một phần tử mới đi vào:
* Nếu nó đã có trong danh sách, tăng tần suất lên 1.
* Nếu chưa có, thêm nó vào danh sách với tần suất là 1.


3. **Xóa rác (Cắt tỉa) tại ranh giới Bucket:** Đây là bước quan trọng nhất. Mỗi khi kết thúc một bucket (nhận đủ $w$ phần tử), hệ thống sẽ quét qua danh sách và **trừ đi 1** ở tất cả các tần suất. Bất kỳ phần tử nào có tần suất tụt xuống 0 sẽ bị **xóa khỏi bộ nhớ**.


* **Tại sao nó hiệu quả?** Những phần tử hiếm khi xuất hiện (như rác, nhiễu) sẽ chỉ đạt tần suất thấp và nhanh chóng bị "trừ mòn" đến 0 tại các ranh giới bucket rồi bị xóa đi, giải phóng bộ nhớ. Ngược lại, những phần tử thực sự phổ biến sẽ liên tục được cộng dồn, tốc độ cộng nhanh hơn tốc độ bị trừ, nên chúng sẽ luôn tồn tại trong danh sách.
* **Đánh đổi (Lossy):** Thuật toán này gọi là "Lossy" (có mất mát) vì nó không đếm chính xác tuyệt đối 100%. Tuy nhiên, nó đảm bảo tìm ra được tất cả các phần tử phổ biến vượt qua một ngưỡng cho trước với một mức sai số $\epsilon$ đã biết trước, đồng thời tiết kiệm dung lượng RAM một cách tối đa.

### 8. Đi sâu vào Phân cụm dữ liệu (Cluster Analysis / Clustering)

Phân cụm là một kỹ thuật **Học máy không giám sát (Unsupervised Learning)**. Nghĩa là bạn đưa cho máy tính một tập dữ liệu thô, không hề có nhãn (không nói cho máy biết ai là khách VIP, ai là khách vãng lai), và máy tính phải tự tìm ra các khuôn mẫu ẩn để gom nhóm chúng lại.

Nguyên tắc tối thượng của phân cụm là: **Các điểm trong cùng một cụm phải càng giống nhau càng tốt, và các cụm phải càng khác biệt nhau càng tốt.**

Để thực hiện phân cụm thành công, đặc biệt với các thuật toán phổ biến như K-Means, quá trình này đòi hỏi các bước và kỹ thuật đi kèm rất khắt khe:

* **Chuẩn hóa dữ liệu (Normalization/Standardization):**
* *Lý do:* Phân cụm hoạt động dựa trên việc tính **khoảng cách** (thường là khoảng cách Euclidean) giữa các điểm dữ liệu. Nếu bạn có 2 đặc trưng: "Tuổi" (từ 18 đến 80) và "Thu nhập" (từ 5,000,000 VND đến 100,000,000 VND), thì đặc trưng "Thu nhập" sẽ hoàn toàn lấn át "Tuổi" trong công thức tính khoảng cách vì con số của nó quá lớn.
* *Cách làm:* Bắt buộc phải ép các thang đo này về cùng một dải, ví dụ như từ 0 đến 1 (Min-Max Scaling) hoặc theo phân phối chuẩn (Z-score).


* **Thuật toán K-Means (Thuật toán phổ biến nhất):**
1. Chọn ngẫu nhiên $K$ điểm làm trung tâm cụm (Centroid) ban đầu.
2. Tính khoảng cách từ mọi điểm dữ liệu đến $K$ trung tâm này. Điểm nào gần trung tâm nào nhất thì gán vào cụm đó.
3. Cập nhật lại vị trí của $K$ trung tâm bằng cách lấy điểm chính giữa (trung bình cộng) của tất cả các điểm vừa được gán vào cụm.
4. Lặp lại bước 2 và 3 cho đến khi các trung tâm không thay đổi vị trí nữa (thuật toán hội tụ).


* **Phương pháp Elbow (Xác định số cụm K tối ưu):**
* *Vấn đề:* Máy tính không tự biết nên chia dữ liệu thành 2, 3, hay 10 cụm. Bạn phải cung cấp tham số $K$ cho nó.
* *Cách làm:* Bạn chạy thuật toán K-Means nhiều lần với $K = 1, 2, 3, 4, 5...$ Ở mỗi lần, bạn tính tổng bình phương khoảng cách từ các điểm đến trung tâm cụm của nó (gọi là WCSS - Within-Cluster Sum of Square). $K$ càng tăng thì WCSS càng giảm.
* *Dấu hiệu nhận biết:* Vẽ đồ thị WCSS theo $K$, đồ thị sẽ dốc xuống. Điểm mà tại đó độ dốc của đồ thị gãy gập lại (trông như một cái "cùi chỏ" - Elbow), thì đó chính là số lượng cụm tối ưu. Qua điểm đó, việc tăng thêm cụm không mang lại nhiều giá trị phân loại nữa.

