# Lab 09: Khai phá mẫu tuần tự - Báo cáo

**Sinh viên**: Nguyễn Văn Anh Duy  
**Môn học**: DBM302m  
**Ngày**: 3 tháng 2, 2026  
**Buổi lab**: Slot 09 - Lab In Class

---

## Tóm tắt

Báo cáo này trình bày việc triển khai và phân tích các kỹ thuật khai phá mẫu tuần tự áp dụng cho dữ liệu giao dịch khách hàng. Sử dụng thuật toán PrefixSpan, chúng tôi đã khám phá thành công 11 mẫu tuần tự phổ biến với ngưỡng hỗ trợ tối thiểu là 30%, tiết lộ những hiểu biết quan trọng về hành vi mua hàng của khách hàng.

**Các phát hiện chính:**
- Apple và Donut là những sản phẩm phổ biến nhất (tần suất 70%)
- "Apple → Donut" là chuỗi 2 sản phẩm mạnh nhất (hỗ trợ 50%)
- "Apple → Cereal → Donut" là mẫu tuần tự 3 sản phẩm quan trọng nhất (hỗ trợ 30%)
- Các mẫu tuần tự cung cấp thông tin hữu ích cho việc đề xuất sản phẩm và tối ưu hóa cửa hàng

---

## 1. Giới thiệu

### 1.1 Mục tiêu
Mục tiêu chính của bài lab này là hiểu và triển khai các kỹ thuật khai phá mẫu tuần tự để khám phá các mẫu có ý nghĩa trong dữ liệu giao dịch khách hàng. Khai phá mẫu tuần tự khác với khai phá luật kết hợp truyền thống ở chỗ nó xem xét thứ tự của các sản phẩm trong giao dịch.

### 1.2 Mô tả dữ liệu
- **Tập dữ liệu**: Customer Transactions Dataset (Dữ liệu giao dịch khách hàng)
- **Tổng số giao dịch**: 10
- **Số sản phẩm duy nhất**: 4 (Apple, Banana, Cereal, Donut)
- **Độ dài chuỗi trung bình**: 2.6 sản phẩm mỗi giao dịch
- **Định dạng**: Mỗi giao dịch chứa một chuỗi có thứ tự các sản phẩm đã mua

### 1.3 Phương pháp
Chúng tôi đã triển khai thuật toán **PrefixSpan (Prefix-Projected Sequential Pattern Mining)**, bao gồm:
- Sử dụng phương pháp chia để trị
- Chiếu cơ sở dữ liệu đệ quy để khám phá các mẫu
- Tránh tạo ứng viên (hiệu quả hơn GSP)
- Tìm tất cả các mẫu tuần tự phổ biến trên ngưỡng hỗ trợ tối thiểu

---

## 2. Phân tích dữ liệu

### 2.1 Phân bố tần suất sản phẩm

Phân tích từng sản phẩm cho thấy phân bố tần suất như sau:

| Sản phẩm | Tần suất | Hỗ trợ % |
|----------|----------|----------|
| Apple | 7/10 | 70% |
| Donut | 7/10 | 70% |
| Banana | 6/10 | 60% |
| Cereal | 6/10 | 60% |

**Nhận xét**: Apple và Donut có mức độ phổ biến tương đương, xuất hiện trong 70% tất cả giao dịch, tiếp theo là Banana và Cereal với 60%.

### 2.2 Khám phá mẫu tuần tự

Với ngưỡng hỗ trợ tối thiểu là 3 (30%), chúng tôi đã khám phá **11 mẫu tuần tự phổ biến**:

#### Chuỗi 1 phần tử (4 mẫu):
1. Apple (Support: 7, 70%)
2. Donut (Support: 7, 70%)
3. Banana (Support: 6, 60%)
4. Cereal (Support: 6, 60%)

#### Chuỗi 2 phần tử (6 mẫu):
1. Apple → Donut (Hỗ trợ: 5, 50%)
2. Apple → Cereal (Hỗ trợ: 4, 40%)
3. Apple → Banana (Hỗ trợ: 4, 40%)
4. Cereal → Donut (Hỗ trợ: 4, 40%)
5. Banana → Donut (Hỗ trợ: 3, 30%)
6. Banana → Cereal (Hỗ trợ: 3, 30%)

#### Chuỗi 3 phần tử (1 mẫu):
1. Apple → Cereal → Donut (Hỗ trợ: 3, 30%)

---

## 3. Phân tích mẫu và các hiểu biết sâu sắc

### 3.1 Các mẫu tuần tự mạnh nhất

**Top 5 mẫu theo hỗ trợ:**
1. **Apple** (70%) - Sản phẩm được mua thường xuyên nhất
2. **Donut** (70%) - Phổ biến ngang với Apple
3. **Banana** (60%) - Phổ biến thứ ba
4. **Cereal** (60%) - Phổ biến thứ tư
5. **Apple → Donut** (50%) - Chuỗi 2 sản phẩm mạnh nhất

### 3.2 Phân tích chuyển đổi sản phẩm

**Các chuyển đổi mua hàng phổ biến:**

1. **Sau khi mua Apple, khách hàng thường mua:**
   - Donut (5 giao dịch)
   - Cereal (4 giao dịch)
   - Banana (4 giao dịch)

2. **Sau khi mua Banana, khách hàng thường mua:**
   - Donut (3 giao dịch)
   - Cereal (3 giao dịch)

3. **Sau khi mua Cereal, khách hàng thường mua:**
   - Donut (4 giao dịch)

**Hiểu biết quan trọng**: Donut thường là sản phẩm cuối cùng trong chuỗi mua hàng, cho thấy nó thường là sản phẩm mua theo cảm tính hoặc bổ sung.

### 3.3 Phân bố độ dài mẫu

- **Mẫu 1 sản phẩm**: 4 (36.4%)
- **Mẫu 2 sản phẩm**: 6 (54.5%)
- **Mẫu 3 sản phẩm**: 1 (9.1%)

Phần lớn các mẫu là chuỗi 2 sản phẩm, cho thấy khách hàng thường tuân theo các mẫu mua hàng đơn giản.

---

## 4. Ảnh hưởng của ngưỡng hỗ trợ

Chúng tôi đã phân tích hành vi của thuật toán với các ngưỡng hỗ trợ tối thiểu khác nhau:

| Min Support | Hỗ trợ % | Tổng số mẫu | Độ dài tối đa |
|-------------|----------|-------------|---------------|
| 2 | 20% | 13 | 3 |
| 3 | 30% | 11 | 3 |
| 4 | 40% | 8 | 2 |
| 5 | 50% | 5 | 2 |

**Nhận xét:**
- Khi hỗ trợ tối thiểu tăng, số lượng mẫu giảm
- Ngưỡng cao hơn loại bỏ các mẫu dài hơn trước
- Ngưỡng hỗ trợ 30-40% cung cấp sự cân bằng tốt giữa số lượng và chất lượng mẫu
- Ngưỡng quá thấp (20%) có thể bao gồm nhiễu; quá cao (50%) có thể bỏ lỡ các mẫu quan trọng

---

## 5. Ứng dụng thực tế

### 5.1 Hệ thống đề xuất sản phẩm

**Chiến lược triển khai:**
- Khi khách hàng mua Apple, đề xuất Donut (khả năng 50%)
- Khi khách hàng mua Apple rồi mua Cereal, đề xuất Donut (khả năng 30%)
- Đề xuất tuần tự tăng tỷ lệ chuyển đổi bằng cách gợi ý các sản phẩm tiếp theo tự nhiên

**Lợi ích mong đợi:**
- Tăng giá trị giao dịch trung bình
- Cải thiện sự hài lòng của khách hàng thông qua đề xuất cá nhân hóa
- Tỷ lệ chuyển đổi cao hơn đối với các sản phẩm được đề xuất

### 5.2 Tối ưu hóa bố trí cửa hàng

**Khuyến nghị:**
1. **Bố trí chiến lược:**
   - Đặt khu Donut gần khu trưng bày Apple (50% đồng xuất hiện theo chuỗi)
   - Đặt Cereal trên đường đi giữa khu Apple và Donut
   - Tạo tầm nhìn trực quan từ khu Apple đến khu Donut

2. **Gói sản phẩm:**
   - Gói kết hợp Apple và Donut dựa trên hỗ trợ tuần tự 50%
   - Gói bữa sáng chứa Apple, Cereal và Donut dựa trên hỗ trợ 30%
   - Kết hợp Banana và Donut dựa trên hỗ trợ tuần tự 30%

### 5.3 Quản lý tồn kho

**Quyết định tồn kho dựa trên dữ liệu:**
- Duy trì mức tồn kho cao hơn cho Apple và Donut (tần suất 70%)
- Đảm bảo sẵn có Cereal khi doanh số Apple cao
- Dự đoán nhu cầu Donut dựa trên việc mua Apple trước đó
- Tối ưu hóa điểm đặt hàng lại dựa trên các mẫu tuần tự

### 5.4 Marketing và khuyến mãi

**Chiến lược chiến dịch nhắm mục tiêu:**
1. **Khuyến mãi bán chéo:**
   - Cung cấp giảm giá cho mua Donut sau giao dịch mua Apple
   - Quảng bá Cereal như sản phẩm bổ sung với mua Apple

2. **Chương trình khách hàng thân thiết:**
   - Thưởng cho khách hàng tuân theo chuỗi mua hàng phổ biến
   - Ghi nhận khách hàng hoàn thành các mẫu tuần tự thường xuyên

3. **Marketing cá nhân hóa:**
   - Cung cấp ưu đãi cá nhân hóa dựa trên chuỗi mua hàng trước đó
   - Gợi ý sản phẩm tiếp theo dựa trên các mẫu phổ biến đã xác định

### 5.5 Hiểu hành vi khách hàng

**Hiểu biết về hành vi:**
- Khách hàng thường bắt đầu mua sắm với Apple (70% hiện diện)
- Chuỗi mua hàng trung bình 2.6 sản phẩm
- Donut thường là mua hàng cuối cùng, bổ sung
- Sở thích rõ ràng cho các chuỗi sản phẩm nhất định hơn là kết hợp ngẫu nhiên

---

## 6. Hiệu suất thuật toán

### 6.1 Ưu điểm của PrefixSpan

1. **Không tạo ứng viên**: Không giống GSP, PrefixSpan không tạo chuỗi ứng viên, làm cho nó hiệu quả hơn
2. **Chiếu cơ sở dữ liệu**: Giảm kích thước cơ sở dữ liệu ở mỗi mức đệ quy
3. **Khả năng mở rộng**: Hoạt động tốt trên các tập dữ liệu lớn hơn
4. **Tính đầy đủ**: Tìm tất cả các chuỗi phổ biến đáp ứng ngưỡng hỗ trợ

### 6.2 Độ phức tạp tính toán

- **Độ phức tạp thời gian**: O(n × m × l) trong đó:
  - n = số lượng chuỗi
  - m = độ dài chuỗi trung bình
  - l = số lượng mẫu phổ biến
- **Độ phức tạp không gian**: O(n × m) để lưu trữ chuỗi và mẫu

### 6.3 Hiệu quả thuật toán

Đối với tập dữ liệu của chúng tôi (10 giao dịch):
- Thời gian thực thi: < 10ms (rất hiệu quả)
- Sử dụng bộ nhớ: Tối thiểu
- Khám phá mẫu: Hoàn chỉnh (tất cả các mẫu được tìm thấy)

---

## 7. So sánh: PrefixSpan vs GSP

| Tính năng | PrefixSpan | GSP (Generalized Sequential Pattern) |
|-----------|------------|--------------------------------------|
| **Phương pháp** | Tăng trưởng mẫu, dựa trên chiếu | Dựa trên Apriori, tạo ứng viên |
| **Tạo ứng viên** | Không | Cần thiết cho mỗi cấp |
| **Quét cơ sở dữ liệu** | Nhiều phép chiếu | Nhiều lần quét đầy đủ |
| **Sử dụng bộ nhớ** | Thấp hơn (cơ sở dữ liệu chiếu) | Cao hơn (lưu trữ ứng viên) |
| **Hiệu suất** | Thường nhanh hơn | Chậm hơn với tập dữ liệu lớn |
| **Triển khai** | Phức tạp hơn | Đơn giản hơn về mặt khái niệm |

**Kết luận**: PrefixSpan phù hợp hơn cho trường hợp sử dụng của chúng tôi do tính hiệu quả và khả năng mở rộng.

---

## 8. Thách thức và hạn chế

### 8.1 Thách thức gặp phải

1. **Tiền xử lý dữ liệu**: Phải phân tích file CSV thủ công do chuỗi phân cách bằng dấu phẩy
2. **Lựa chọn ngưỡng hỗ trợ**: Cần thử nghiệm để tìm ngưỡng tối ưu
3. **Diễn giải mẫu**: Một số mẫu có thể là ngẫu nhiên hơn là nhân quả

### 8.2 Hạn chế của tập dữ liệu

1. **Kích thước mẫu nhỏ**: Chỉ 10 giao dịch hạn chế ý nghĩa thống kê
2. **Số sản phẩm hạn chế**: Chỉ 4 sản phẩm duy nhất làm giảm độ phức tạp của mẫu
3. **Không có thông tin thời gian**: Thiếu timestamp ngăn phân tích dựa trên thời gian
4. **Không có ID khách hàng**: Không thể phân tích hành vi khách hàng cá nhân theo thời gian

### 8.3 Hạn chế của thuật toán

1. **Độ nhạy ngưỡng hỗ trợ**: Khám phá mẫu phụ thuộc nhiều vào ngưỡng
2. **Không có thước đo độ tin cậy**: Không giống luật kết hợp, không cung cấp điểm tin cậy
3. **Nghiêm ngặt về thứ tự**: Yêu cầu thứ tự chuỗi chính xác (không cho phép khoảng trống)

---

## 9. Cải tiến tương lai

### 9.1 Cải tiến thuật toán

1. **Triển khai GSP**: So sánh hiệu suất với PrefixSpan
2. **Thêm điểm tin cậy**: Tính xác suất có điều kiện của các mẫu
3. **Hỗ trợ ràng buộc khoảng trống**: Cho phép các sản phẩm không liên tiếp trong chuỗi
4. **Ràng buộc thời gian**: Xem xét các mẫu trong khung thời gian cụ thể

### 9.2 Cải tiến tập dữ liệu

1. **Tập dữ liệu lớn hơn**: Phân tích hàng nghìn giao dịch để có tính hợp lệ thống kê tốt hơn
2. **Dữ liệu thời gian**: Bao gồm timestamp để phân tích mẫu dựa trên thời gian
3. **Phân khúc khách hàng**: Phân tích mẫu theo nhân khẩu học khách hàng
4. **Thuộc tính bổ sung**: Bao gồm danh mục sản phẩm, giá cả, số lượng

### 9.3 Kỹ thuật nâng cao

1. **Mẫu tuần tự đóng**: Giảm sự dư thừa của mẫu
2. **Mẫu tuần tự cực đại**: Biểu diễn gọn nhất
3. **Mẫu tuần tự âm**: Khám phá những sản phẩm KHÔNG được mua cùng nhau
4. **Khai phá mẫu tương phản**: So sánh các mẫu giữa các phân khúc khách hàng

---

## 10. Kết luận

### 10.1 Tóm tắt thành tựu

Bài lab này đã thành công trong việc trình diễn việc triển khai và ứng dụng khai phá mẫu tuần tự sử dụng thuật toán PrefixSpan. Các thành tựu chính bao gồm:

1. Triển khai thành công thuật toán PrefixSpan từ đầu
2. Khám phá 11 mẫu tuần tự phổ biến trong dữ liệu giao dịch khách hàng
3. Xác định mối quan hệ tuần tự mạnh nhất (Apple → Donut: hỗ trợ 50%)
4. Phân tích tác động của ngưỡng hỗ trợ đến khám phá mẫu
5. Tạo trực quan hóa toàn diện để phân tích mẫu
6. Phát triển ứng dụng kinh doanh thực tế cho các mẫu đã khám phá

### 10.2 Bài học chính

1. **Mẫu tuần tự tiết lộ thứ tự**: Không giống luật kết hợp, mẫu tuần tự nắm bắt thứ tự thời gian của các sự kiện
2. **Ngưỡng hỗ trợ rất quan trọng**: Chọn ngưỡng phù hợp cân bằng số lượng và chất lượng mẫu
3. **Giá trị kinh doanh thực tế**: Mẫu tuần tự dịch trực tiếp sang các chiến lược kinh doanh khả thi
4. **Hiệu quả thuật toán quan trọng**: Phương pháp dựa trên chiếu của PrefixSpan hiệu quả hơn các phương pháp tạo ứng viên

### 10.3 Tác động kinh doanh

Các mẫu đã khám phá cung cấp giá trị kinh doanh thực tế trong nhiều lĩnh vực:

- **Tăng cường doanh thu**: Đề xuất sản phẩm dựa trên mẫu tuần tự có thể tăng giá trị giao dịch trung bình
- **Trải nghiệm khách hàng**: Gợi ý cá nhân hóa cải thiện trải nghiệm mua sắm tổng thể
- **Hiệu quả vận hành**: Bố trí cửa hàng dựa trên dữ liệu có thể giảm thời gian tìm kiếm của khách hàng
- **Quản lý tồn kho**: Dự trữ dự đoán dựa trên mẫu giảm lãng phí và tình trạng hết hàng
- **Hiệu quả marketing**: Chiến dịch nhắm mục tiêu dựa trên mẫu tuần tự cho thấy tỷ lệ chuyển đổi được cải thiện

### 10.4 Nhận xét kết luận

Khai phá mẫu tuần tự cung cấp những hiểu biết có giá trị để hiểu hành vi khách hàng và tối ưu hóa hoạt động kinh doanh. Thuật toán PrefixSpan khám phá hiệu quả các mẫu hỗ trợ ra quyết định chiến lược trong nhiều lĩnh vực:
- Hệ thống đề xuất sản phẩm thương mại điện tử
- Tối ưu hóa bố trí cửa hàng bán lẻ
- Quản lý và dự báo tồn kho
- Phát triển chiến dịch marketing
- Phân tích hành trình khách hàng

Hiểu cả các sản phẩm được mua và thứ tự tuần tự của chúng cho phép các tổ chức phát triển các chiến lược hiệu quả hơn để cải thiện trải nghiệm khách hàng và hiệu quả vận hành. Nghiên cứu này chứng minh khả năng ứng dụng thực tế của khai phá mẫu tuần tự trong phân tích bán lẻ và phân tích hành vi khách hàng.

---

## Phụ lục

### A. Chi tiết triển khai kỹ thuật

**Ngôn ngữ lập trình**: Python 3.10  
**Thư viện sử dụng**:
- pandas: Thao tác dữ liệu
- numpy: Tính toán số học
- matplotlib: Trực quan hóa
- seaborn: Trực quan hóa nâng cao
- collections.Counter: Đếm tần suất sản phẩm

**Triển khai thuật toán**: Class PrefixSpan tùy chỉnh với các phương thức cho:
- Kiểm tra chuỗi con
- Tính toán hỗ trợ
- Khám phá sản phẩm phổ biến
- Chiếu cơ sở dữ liệu
- Khai phá mẫu đệ quy

### B. Khả dụng code

Triển khai đầy đủ có sẵn trong Jupyter notebook:
`LAB_09.ipynb`

Notebook bao gồm:
- Triển khai đầy đủ PrefixSpan
- Code tiền xử lý dữ liệu
- Hàm trực quan hóa
- Script phân tích mẫu
- Phân tích so sánh trên các ngưỡng hỗ trợ

### C. Thống kê tập dữ liệu

```
Tập dữ liệu: customer_transactions_dataset.csv
Tổng số giao dịch: 10
Số sản phẩm duy nhất: 4 (Apple, Banana, Cereal, Donut)
Độ dài chuỗi trung bình: 2.6 sản phẩm
Độ dài chuỗi tối thiểu: 2 sản phẩm
Độ dài chuỗi tối đa: 4 sản phẩm
Tổng số lần xuất hiện sản phẩm: 26
```

### D. Tài liệu tham khảo

1. Pei, J., Han, J., Mortazavi-Asl, B., Wang, J., Pinto, H., Chen, Q., ... & Hsu, M. C. (2004). Mining sequential patterns by pattern-growth: The prefixspan approach. *IEEE Transactions on knowledge and data engineering*, 16(11), 1424-1440.

2. Agrawal, R., & Srikant, R. (1995). Mining sequential patterns. *Proceedings of the eleventh international conference on data engineering* (pp. 3-14). IEEE.

3. Han, J., Pei, J., & Kamber, M. (2011). *Data mining: concepts and techniques* (3rd ed.). Elsevier.

4. Zaki, M. J. (2001). SPADE: An efficient algorithm for mining frequent sequences. *Machine learning*, 42(1), 31-60.

---

**Kết thúc báo cáo**

*Báo cáo này được chuẩn bị như một phần của Lab 09: Khai phá mẫu tuần tự cho môn học DBM302m.*