# YÊU CẦU BÀI LAB: PHÂN CỤM DỮ LIỆU KHÔNG GIAN BẰNG THUẬT TOÁN CHAMELEON

**Mục tiêu:** Sinh viên hiểu và cài đặt được các bước của thuật toán phân cụm đồ thị (Graph-based Clustering) dựa trên nguyên lý của thuật toán CHAMELEON, bao gồm việc xây dựng đồ thị K-NN, phân chia đồ thị và gộp cụm dựa trên các độ đo động (Dynamic Modeling).

**Dữ liệu đầu vào:** File `spatial_dataset.csv` chứa tọa độ 2D (X, Y) của 15 điểm dữ liệu.

---

## CÁC BƯỚC THỰC HIỆN (TASKS)

### Yêu cầu 1: Xây dựng Đồ thị K-NN thưa (Construct K-NN Sparse Graph)
Từ tập dữ liệu tọa độ 2D ban đầu, sinh viên cần viết code để tính toán khoảng cách giữa các điểm và tạo ra một đồ thị K-láng giềng gần nhất (K-Nearest Neighbor Graph).
*   **Định nghĩa cạnh:** Hai điểm $p$ và $q$ sẽ được nối với nhau (có cạnh nối) nếu $q$ nằm trong top $K$ điểm gần nhất của $p$ (hoặc ngược lại).
*   **Trọng số cạnh:** Trọng số của cạnh có thể được tính dựa trên nghịch đảo khoảng cách hoặc mức độ tương đồng giữa 2 điểm.
*   **Output yêu cầu 1:** In ra danh sách các cạnh hoặc ma trận kề, đồng thời **vẽ (plot) đồ thị** này lên mặt phẳng tọa độ (các điểm là node, các đường nối là edge). *Lưu ý: Sinh viên tự chọn tham số K phù hợp (ví dụ: K=3).*

### Yêu cầu 2: Phân chia đồ thị (Partition the Graph)
Từ K-NN Sparse Graph vừa tạo, sử dụng thuật toán phân chia đồ thị (Graph Partitioning - ví dụ: Min-Cut hoặc các thuật toán chia cắt đồ thị cơ bản) để cắt đồ thị lớn thành nhiều đồ thị con (sub-graphs / partitions) nhỏ hơn.
*   **Mục tiêu:** Cắt đứt các cạnh dài/yếu nhất để tạo ra các cụm nhỏ cục bộ (như hình minh họa ở bước 2).
*   **Output yêu cầu 2:** Vẽ lại đồ thị trên mặt phẳng, trong đó **mỗi partition (đồ thị con) được tô một màu khác nhau** để phân biệt.

### Yêu cầu 3: Gộp cụm dựa trên R.I và R.C (Merge Partitions)
Đây là bước cốt lõi của bài. Sinh viên viết hàm để xét các cặp đồ thị con (partition) $C_1$ và $C_2$ có kề nhau hay không. Nếu có, quyết định xem có gộp chúng lại với nhau hay không dựa trên 2 tiêu chí đánh giá động:
1.  **Relative Interconnectivity (RI - Độ liên kết tương đối):**
    *   *Công thức khái quát:* $\text{RI} = \frac{\text{Độ liên kết giữa } C_1 \text{ và } C_2}{\text{Độ liên kết nội bộ của } C_1 \text{ và } C_2}$
    *   *Ý nghĩa:* Đánh giá xem số lượng/trọng số các cạnh nối giữa hai cụm có đủ lớn so với các cạnh nằm bên trong chính mỗi cụm hay không.
2.  **Relative Closeness (RC - Độ gần gũi tương đối):**
    *   *Công thức khái quát:* $\text{RC} = \frac{\text{Độ gần gũi giữa } C_1 \text{ và } C_2}{\text{Độ gần gũi nội bộ của } C_1 \text{ và } C_2}$
    *   *Ý nghĩa:* Đánh giá xem khoảng cách trung bình của các cạnh nối giữa hai cụm có tương đồng với khoảng cách trung bình của các cạnh nội bộ hay không.

*   **Điều kiện gộp (Merge Condition):** Hai cụm $C_1$ và $C_2$ sẽ được gộp lại nếu $RI(C_1, C_2) \geq Threshold_{RI}$ **VÀ** $RC(C_1, C_2) \geq Threshold_{RC}$. *(Sinh viên tự định nghĩa ngưỡng Threshold hoặc thiết lập hàm tối ưu).*
*   **Output yêu cầu 3:** In ra log quá trình gộp (Ví dụ: `Đang gộp cụm 1 và cụm 3 vì RI = ... và RC = ...`).

### Yêu cầu 4: Hiển thị kết quả phân cụm cuối cùng (Final Clusters)
Quá trình gộp cụm ở Yêu cầu 3 sẽ lặp lại cho đến khi không còn cặp cụm nào thỏa mãn điều kiện gộp (RI và RC đều thấp hơn ngưỡng).
*   **Output yêu cầu 4:** 
    *   In ra Console số lượng cụm cuối cùng và danh sách các điểm thuộc từng cụm.
    *   **Vẽ (Plot) biểu đồ Final Clusters:** Tô màu phân biệt cho các cụm hoàn chỉnh cuối cùng (Giống hình minh họa "Final Clusters" góc dưới bên trái của đề bài).

---

**Gợi ý cho sinh viên:** 
*   Ngôn ngữ khuyên dùng: `Python`.
*   Thư viện hỗ trợ: `pandas` (đọc csv), `numpy` (tính toán khoảng cách), `matplotlib` hoặc `networkx` (để xây dựng và vẽ đồ thị K-NN).
*   Với dataset 15 điểm này là một dataset nhỏ (toy dataset), sinh viên có thể code chay (from scratch) các công thức tính toán để nắm vững bản chất thuật toán.