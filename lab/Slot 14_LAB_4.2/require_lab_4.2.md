# Lab 4.2: Partitioning-based and Hierarchical clustering methods

## Objective
- Khóa học nhằm giúp học viên làm quen với cả phương pháp phân cụm dựa trên phân vùng và phân cụm theo thứ bậc, cũng như có kinh nghiệm thực hành áp dụng các kỹ thuật này vào các tập dữ liệu.

## Hoạt động 1: Giới thiệu về Phân cụm
- Thảo luận về tầm quan trọng và ứng dụng của phân cụm trong phân tích dữ liệu.
- Thảo luận về các mục tiêu chính của phân cụm, bao gồm việc nhóm các điểm dữ liệu tương tự nhau.
- Giải thích cách phân cụm có thể tiết lộ những hiểu biết và mô hình ẩn trong dữ liệu.

## Hoạt động 2: Các loại phương pháp phân cụm
- Thảo luận về các phương pháp phân cụm dựa trên phân vùng, chẳng hạn như K-Means và K-Medoids.
- Giải thích khái niệm về các phương pháp phân cụm phân cấp, bao gồm các phương pháp kết tụ và phân chia.
- Thảo luận về thời điểm sử dụng từng loại phương pháp dựa trên đặc điểm của dữ liệu.

## Hoạt động 3: Thực hành phân cụm K-Means
- Làm việc với một tập dữ liệu cho trước (ví dụ: một tập hợp các điểm dữ liệu số).
- Áp dụng thuật toán phân cụm K-Means cho tập dữ liệu.
- Thử nghiệm với các giá trị K khác nhau (số lượng cụm) và giải thích kết quả.

## Hoạt động 4: Thực hành phân cụm phân cấp
- Thực hiện phân cụm phân cấp bằng phương pháp gom nhóm hoặc phân chia.
- Trực quan hóa và giải thích biểu đồ cây phân cụm phân cấp.

## Hoạt động 5: So sánh và Thảo luận
- Thảo luận về kinh nghiệm sử dụng cả hai phương pháp phân cụm.
- Thảo luận về ưu điểm và nhược điểm của phân cụm dựa trên phân vùng và phân cụm phân cấp.

---

#### 💬 Thảo luận 2 – Tóm tắt Kết quả trên Dữ liệu Khách hàng Trung tâm Thương mại

1. **Cả hai phương pháp đều hội tụ về 5 cụm**, xác nhận tính vững chắc của phân khúc này.
2. 5 phân khúc rõ ràng và có thể hành động:
   - 🔴 **Thu nhập cao × Chi tiêu cao** → Khách hàng VIP mục tiêu cao cấp
   - 🟠 **Thu nhập cao × Chi tiêu thấp** → Cần thu hút / bán thêm
   - 🟡 **Thu nhập trung bình × Chi tiêu trung bình** → Khách hàng trung thành cốt lõi
   - 🟢 **Thu nhập thấp × Chi tiêu cao** → Cơ hội trả góp / tín dụng
   - 🔵 **Thu nhập thấp × Chi tiêu thấp** → Nhạy cảm về giá; hướng đến giảm giá
3. **Điểm Silhouette (~0.55)** cho thấy các cụm tách biệt tốt và gắn kết — các đặc trưng được chọn (thu nhập và điểm chi tiêu) có tính phân biệt cao.
4. Với hệ thống đề xuất sản xuất xử lý hàng triệu khách hàng, **K-Means** được ưa chuộng vì tốc độ.  
   Để khám phá phân khúc ban đầu hoặc khi K chưa biết, **Phân cụm Kết tụ** với dendrogram là công cụ khám phá tốt hơn.