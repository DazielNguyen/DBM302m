## Lab 4.3 Density and Grid-based clustering methods

**Mục tiêu chung của Lab 4.3:** Làm quen và thực hành trực tiếp với các kỹ thuật gom cụm dựa trên mật độ (Density-based) và dựa trên lưới (Grid-based) trên các tập dữ liệu. Thời lượng dự kiến để hoàn thành là 1 slot (khoảng 2 tiếng 15 phút)

Dưới đây là chi tiết từng hoạt động bạn cần làm:

### Hoạt động 1: Giới thiệu về Gom cụm (Introduction to Clustering) 

[x] Thảo luận về tầm quan trọng cũng như các ứng dụng thực tế của gom cụm (clustering) trong phân tích dữ liệu
[x] Nêu rõ các mục tiêu chính của gom cụm, cụ thể là việc nhóm các điểm dữ liệu có tính chất tương đồng lại với nhau.
[x] Giải thích sự khác biệt giữa hai phương pháp gom cụm (dựa trên mật độ và dựa trên lưới) so với các phương pháp truyền thống như phân vùng (partitioning) và phân cấp (hierarchical).

### Hoạt động 2: Gom cụm dựa trên mật độ (Density-Based Clustering) 

[x] Trình bày về các phương pháp gom cụm dựa trên mật độ, lấy thuật toán DBSCAN làm trọng tâm.
[x] Giải thích cơ chế hoạt động của DBSCAN và phân tích các ưu điểm của nó, đặc biệt nhấn mạnh vào khả năng xử lý nhiễu (noise) và nhận diện các cụm có hình dạng bất quy tắc (irregularly shaped clusters).
[x] **Phần thực hành mã nguồn:** Truy cập link Kaggle được cung cấp ([https://www.kaggle.com/datasets/ankit8467/dataset-for-dbscan](https://www.kaggle.com/datasets/ankit8467/dataset-for-dbscan)) để lấy tập dữ liệu không gian. Sau đó, tiến hành lập trình áp dụng thuật toán DBSCAN lên tập dữ liệu này.
[x] **Phần tinh chỉnh mô hình:** Thực hiện thay đổi các tham số đầu vào như `epsilon` và số điểm tối thiểu (`minimum points`), sau đó quan sát và đánh giá sự thay đổi của kết quả gom cụm.

### Hoạt động 3: Gom cụm dựa trên lưới (Grid-Based Clustering) 
[x] Trình bày về các phương pháp gom cụm dựa trên không gian lưới, tiêu biểu là thuật toán CLIQUE.
[x] Giải thích cách thuật toán CLIQUE chia không gian dữ liệu thành các ô lưới (grids) và cách nó xác định những vùng có mật độ dữ liệu cao.
[x] **Phần thực hành mã nguồn:** Sử dụng một tập dữ liệu được giao để lập trình áp dụng thuật toán CLIQUE.
[x] **Phần tinh chỉnh mô hình:** Thử nghiệm thay đổi kích thước lưới (grid sizes) và ngưỡng mật độ tối thiểu (minimum density thresholds) để quan sát mức độ ảnh hưởng của chúng đến kết quả phân cụm.

### Hoạt động 4: So sánh và Thảo luận (Comparison and Discussion) 
[x] Tiến hành so sánh chi tiết giữa hai phương pháp: gom cụm dựa trên mật độ và gom cụm dựa trên lưới.
[x] Đưa ra các ưu điểm và nhược điểm của từng phương pháp.
[x] Dựa trên các ưu/nhược điểm đó, thảo luận xem mỗi phương pháp sẽ phù hợp để áp dụng cho những loại tập dữ liệu nào trong thực tế.

## Hoạt động 4: So sánh và Thảo luận (Comparison and Discussion)

- Câu hỏi: Tiến hành so sánh chi tiết giữa hai phương pháp: gom cụm dựa trên mật độ và gom cụm dựa trên lưới.
-> Câu trả lời: DBSCAN làm việc trực tiếp trên từng điểm và quan hệ lân cận giữa các điểm. CLIQUE làm việc qua lớp trung gian là lưới (ô), rồi gom cụm bằng các ô dày đặc liên thông. Vì vậy DBSCAN thường bám hình dạng cụm mượt hơn, còn CLIQUE đổi lại tốc độ và khả năng mở rộng tốt hơn.
Ví dụ cụ thể: trên dữ liệu Weight-Height, DBSCAN nhận diện cụm dựa trên vùng điểm dày; còn mô hình CLIQUE trong notebook nhận diện cụm theo vùng ô lưới có mật độ cao.

- Câu hỏi: Đưa ra các ưu điểm và nhược điểm của từng phương pháp.
-> Câu trả lời: DBSCAN: ưu điểm là phát hiện cụm bất quy tắc và lọc nhiễu tốt; nhược điểm là nhạy với `eps`, `min_samples` và khó ổn định khi mật độ các cụm chênh lệch lớn. CLIQUE: ưu điểm là nhanh, dễ mở rộng cho dữ liệu lớn/nhiều chiều; nhược điểm là kết quả phụ thuộc mạnh vào `grid_size` và `min_points`, có thể làm biên cụm bị thô do chia ô.
Ví dụ cụ thể: với cấu hình CLIQUE chặt hơn như `grid=24, min_pts=8`, tỷ lệ noise tăng rõ rệt; trong khi cấu hình thưa hơn như `grid=12, min_pts=4` cho ít noise hơn nhưng cụm có thể bị gộp nhiều hơn.

- Câu hỏi: Dựa trên các ưu/nhược điểm đó, thảo luận xem mỗi phương pháp sẽ phù hợp để áp dụng cho những loại tập dữ liệu nào trong thực tế.
-> Câu trả lời: Nên chọn DBSCAN khi dữ liệu có nhiễu, cụm hình dạng phức tạp và chưa biết trước số cụm. Nên chọn CLIQUE khi dữ liệu rất lớn hoặc nhiều chiều, cần xử lý nhanh và chấp nhận mức xấp xỉ theo lưới.
Ví dụ cụ thể: phát hiện cụm điểm bất thường trong dữ liệu vị trí GPS phù hợp với DBSCAN; phân tích tập dữ liệu lớn nhiều thuộc tính để tìm vùng dày đặc sơ bộ phù hợp với CLIQUE.