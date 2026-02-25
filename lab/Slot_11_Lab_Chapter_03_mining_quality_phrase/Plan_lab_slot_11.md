# Plan Lab Slot 11 - Mining Quality Phrases from Sentiment140

## 📋 Tổng quan
Bài lab gồm 3 phần dựa trên tutorial:
- **Phần 1**: Giới thiệu khái niệm Quality Phrase Mining & ứng dụng trong NLP
- **Phần 2**: Phân loại và trích xuất các loại Quality Phrases (Noun, Verb, Adj-Noun)
- **Phần 3**: Hands-on Mining bằng PMI và Log-Likelihood Ratio trên dataset Sentiment140

**Dataset**: [Sentiment140 - Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140)  
**Kỹ thuật chính**: Pointwise Mutual Information (PMI), Log-Likelihood Ratio (LLR)

---

## 🎯 PHẦN 1: GIỚI THIỆU & SETUP

### ✅ Bước 1: Cài đặt thư viện & Import
- [ ] **Cell 1 (Markdown)**: Tiêu đề bài lab + mô tả mục tiêu
  - **Nội dung**: Giải thích Quality Phrase Mining là gì, tại sao quan trọng trong NLP & Sentiment Analysis
  - **Ghi chú**: Nêu rõ 2 kỹ thuật sẽ dùng: PMI và LLR

- [ ] **Cell 2: Cài đặt thư viện**
  - **Ý tưởng**: Cài các thư viện cần thiết nếu chưa có
  - **Code**: `!pip install nltk pandas numpy matplotlib wordcloud`
  - **Mục đích**: Đảm bảo môi trường đầy đủ

- [ ] **Cell 3: Import thư viện**
  - **Ý tưởng**: Khai báo toàn bộ thư viện cần dùng
  - **Code**: Import `pandas`, `numpy`, `re`, `math`, `collections.Counter`, `nltk` (tokenize, pos_tag, stopwords), `matplotlib.pyplot`, `wordcloud.WordCloud`
  - **Mục đích**: Chuẩn bị công cụ xử lý văn bản và trực quan hóa

- [ ] **Cell 4: Download NLTK data**
  - **Ý tưởng**: Tải resource cần thiết của NLTK
  - **Code**: `nltk.download('punkt')`, `nltk.download('averaged_perceptron_tagger')`, `nltk.download('stopwords')`
  - **Kiểm tra**: Xác nhận download thành công

---

## 📄 PHẦN 2: NẠP DỮ LIỆU & TIỀN XỬ LÝ

### ✅ Bước 2: Load và khám phá dữ liệu Sentiment140

- [ ] **Cell 5: Đọc dataset**
  - **Ý tưởng**: Nạp file CSV Sentiment140 (6 cột: target, id, date, flag, user, text)
  - **Code**: `df = pd.read_csv('sentiment140.csv', encoding='latin-1', names=['target','id','date','flag','user','text'])`
  - **Kiểm tra**: In `df.shape` → kỳ vọng 1,600,000 dòng

- [ ] **Cell 6: Khám phá dữ liệu**
  - **Ý tưởng**: Hiểu cấu trúc và nội dung dataset
  - **Code**: `df.head()`, `df['target'].value_counts()`, `df.info()`
  - **Quan sát**: Cột `target` có 2 giá trị: 0 (negative), 4 (positive)

- [ ] **Cell 7: Lấy mẫu nhỏ để xử lý nhanh**
  - **Ý tưởng**: Giới hạn dataset để thực hành nhanh hơn (5,000–10,000 dòng)
  - **Code**: `df_sample = df.sample(n=10000, random_state=42).reset_index(drop=True)`
  - **Lý do**: Dataset gốc 1.6M dòng sẽ rất chậm khi tính PMI/LLR

### ✅ Bước 3: Làm sạch văn bản (Text Preprocessing)

- [ ] **Cell 8: Định nghĩa hàm làm sạch văn bản**
  - **Ý tưởng**: Loại bỏ URLs, mentions (@user), hashtags, ký tự đặc biệt, chuyển chữ thường
  - **Code**: Hàm `clean_text(text)` dùng `re.sub()` để xóa URL (`http\S+`), mentions (`@\w+`), hashtags (`#\w+`), ký tự không phải chữ cái
  - **Kiểm tra**: Test trên 1 câu mẫu có URL và @mention

- [ ] **Cell 9: Áp dụng làm sạch**
  - **Ý tưởng**: Áp dụng hàm clean_text cho toàn bộ cột text
  - **Code**: `df_sample['clean_text'] = df_sample['text'].apply(clean_text)`
  - **So sánh**: In 5 dòng `text` gốc vs `clean_text` để xác nhận

- [ ] **Cell 10: Tokenize văn bản**
  - **Ý tưởng**: Tách từng câu thành danh sách các token (từ)
  - **Code**: `df_sample['tokens'] = df_sample['clean_text'].apply(nltk.word_tokenize)`
  - **Kiểm tra**: Xem mảng tokens của 3 câu đầu

- [ ] **Cell 11: Loại bỏ Stopwords**
  - **Ý tưởng**: Xóa các từ phổ biến không mang ý nghĩa (the, is, at, …)
  - **Code**: Load `stopwords.words('english')`, lọc tokens không nằm trong stopword list
  - **Lưu vào**: `df_sample['filtered_tokens']`

---

## 🔍 PHẦN 3: PHÂN LOẠI QUALITY PHRASES (Activity 2)

### ✅ Bước 4: POS Tagging & Trích xuất Phrase theo loại

- [ ] **Cell 12 (Markdown)**: Giải thích 3 loại Quality Phrases
  - **Nội dung**: Noun Phrases (NN, NNP, NNS), Verb Phrases (VB, VBD, VBG), Adjective-Noun Phrases (JJ + NN)
  - **Ví dụ minh họa**: Mỗi loại 2-3 ví dụ

- [ ] **Cell 13: POS Tagging**
  - **Ý tưởng**: Gán nhãn từ loại cho từng token
  - **Code**: `df_sample['pos_tags'] = df_sample['filtered_tokens'].apply(nltk.pos_tag)`
  - **Kiểm tra**: Xem POS tags của 3 câu đầu

- [ ] **Cell 14: Trích xuất Noun Phrases**
  - **Ý tưởng**: Tìm chuỗi Noun liên tiếp (NN*, NNP*)
  - **Code**: Hàm `extract_noun_phrases(pos_tags)` — lấy bigrams/trigrams toàn là danh từ
  - **Kết quả**: List tất cả noun phrases, đếm tần suất bằng `Counter`

- [ ] **Cell 15: Trích xuất Adjective-Noun Phrases**
  - **Ý tưởng**: Tìm cặp (JJ + NN) — rất quan trọng trong Sentiment Analysis
  - **Code**: Hàm `extract_adj_noun_phrases(pos_tags)` — duyệt cặp bigram liên tiếp
  - **Kết quả**: Top 20 Adj-Noun phrases phổ biến nhất

- [ ] **Cell 16: Trích xuất Verb Phrases**
  - **Ý tưởng**: Tìm bigrams có tag VB*, VBG, VBD
  - **Code**: Hàm `extract_verb_phrases(pos_tags)`
  - **Kết quả**: Top 20 Verb phrases

- [ ] **Cell 17: Tổng hợp và hiển thị**
  - **Ý tưởng**: In bảng so sánh 3 loại phrases với tần suất
  - **Code**: Dùng `pd.DataFrame` để tạo bảng Noun / Adj-Noun / Verb phrases top 10

---

## 📊 PHẦN 4: HANDS-ON MINING — PMI & LLR (Activity 3)

### ✅ Bước 5: Pointwise Mutual Information (PMI)

- [ ] **Cell 18 (Markdown)**: Giải thích PMI
  - **Công thức**: `PMI(w1, w2) = log2( P(w1,w2) / (P(w1) × P(w2)) )`
  - **Ý nghĩa**: PMI cao → w1 và w2 hay xuất hiện cùng nhau hơn ngẫu nhiên → quality phrase

- [ ] **Cell 19: Đếm Unigram và Bigram**
  - **Ý tưởng**: Xây dựng frequency tables cho từng từ và từng cặp từ
  - **Code**:
    - Flatten tất cả `filtered_tokens` thành 1 list lớn → đếm bằng `Counter` → `unigram_counts`
    - Tạo bigrams từ mỗi câu → flatten → đếm bằng `Counter` → `bigram_counts`
  - **Kiểm tra**: In top 10 unigram và bigram

- [ ] **Cell 20: Tính PMI cho tất cả bigrams**
  - **Ý tưởng**: Áp dụng công thức PMI, lọc bigrams có tần số tối thiểu (≥ 5)
  - **Code**: Hàm `compute_pmi(bigram_counts, unigram_counts, total_words)` trả về dict `{bigram: pmi_score}`
  - **Lọc**: Chỉ giữ bigrams với `bigram_count >= 5` để tránh nhiễu

- [ ] **Cell 21: Hiển thị Top 30 Quality Phrases theo PMI**
  - **Ý tưởng**: Sắp xếp theo PMI giảm dần, in bảng phrase + PMI score
  - **Code**: Tạo DataFrame `pmi_df`, sort_values theo PMI, hiển thị top 30
  - **Quan sát**: Nhận xét về các cụm từ có PMI cao nhất

### ✅ Bước 6: Log-Likelihood Ratio (LLR)

- [ ] **Cell 22 (Markdown)**: Giải thích LLR
  - **Công thức**: LLR dựa trên bảng contingency 2x2, tính `G² = 2 × Σ(O × log(O/E))`
  - **Ưu điểm so với PMI**: LLR ổn định hơn với bigrams tần suất thấp, phù hợp corpus lớn

- [ ] **Cell 23: Tính LLR cho tất cả bigrams**
  - **Ý tưởng**: Xây dựng contingency table cho từng bigram, tính G²
  - **Code**: Hàm `compute_llr(w1, w2, bigram_counts, unigram_counts, total_words)`
    - Tính: k11 (cả 2 cùng xuất hiện), k12, k21, k22
    - Trả về LLR score
  - **Lọc**: Áp dụng cùng threshold `bigram_count >= 5`

- [ ] **Cell 24: Hiển thị Top 30 Quality Phrases theo LLR**
  - **Ý tưởng**: Sắp xếp theo LLR giảm dần, in bảng phrase + LLR score
  - **Code**: Tạo DataFrame `llr_df`, sort_values theo LLR, hiển thị top 30
  - **Quan sát**: So sánh danh sách với PMI

### ✅ Bước 7: So sánh PMI vs LLR

- [ ] **Cell 25: Bảng so sánh kết quả**
  - **Ý tưởng**: Đặt top 20 PMI và top 20 LLR cạnh nhau trong 1 DataFrame
  - **Code**: `comparison_df = pd.concat([pmi_top20, llr_top20], axis=1)`
  - **Quan sát**: Nhận xét sự khác biệt giữa 2 phương pháp

---

## 📈 PHẦN 5: TRỰC QUAN HÓA KẾT QUẢ

### ✅ Bước 8: Visualize Quality Phrases

- [ ] **Cell 26: Word Cloud từ Top PMI Phrases**
  - **Ý tưởng**: Tạo Word Cloud với trọng số là PMI score
  - **Code**: Tạo dict `{phrase_string: pmi_score}`, dùng `WordCloud(width=800, height=400).generate_from_frequencies()`
  - **Hiển thị**: Dùng `plt.imshow()` + `plt.axis('off')`, tiêu đề "Top Quality Phrases by PMI"

- [ ] **Cell 27: Bar Chart Top 20 PMI Phrases**
  - **Ý tưởng**: Biểu đồ cột ngang (horizontal bar) so sánh PMI score
  - **Code**: `pmi_top20.plot(kind='barh', figsize=(10,8), color='steelblue')`
  - **Nhận xét**: Cụm từ nào có PMI cao nhất?

- [ ] **Cell 28: Bar Chart Top 20 LLR Phrases**
  - **Ý tưởng**: Biểu đồ cột ngang so sánh LLR score
  - **Code**: `llr_top20.plot(kind='barh', figsize=(10,8), color='coral')`
  - **Nhận xét**: Cụm từ nào có LLR cao nhất?

- [ ] **Cell 29: Phân tích Phrases theo Sentiment (Positive vs Negative)**
  - **Ý tưởng**: Tách dataset thành 2 nhóm (positive: target=4, negative: target=0), tính PMI riêng cho từng nhóm
  - **Code**: `df_pos = df_sample[df_sample['target']==4]`, `df_neg = df_sample[df_sample['target']==0]`
  - **Vẽ**: 2 bar chart song song top 10 positive phrases vs top 10 negative phrases
  - **Quan sát**: Phrases đặc trưng của mỗi nhóm sentiment là gì?

---

## 🏁 PHẦN 6: KẾT LUẬN

- [ ] **Cell 30 (Markdown)**: Kết luận bài lab
  - **Nội dung bao gồm**:
    - Tóm tắt kết quả PMI và LLR tìm được
    - So sánh ưu/nhược của PMI vs LLR
    - Ý nghĩa của Quality Phrase Mining trong Sentiment Analysis
    - Đề xuất cải tiến (trigrams, phương pháp nâng cao hơn như AutoPhrase)

---

## 🔧 Công cụ & Thư viện
| Thư viện | Mục đích |
|---|---|
| `pandas` | Load và xử lý dữ liệu |
| `nltk` | Tokenize, POS tagging, Stopwords |
| `re` | Regex để làm sạch văn bản |
| `math`, `collections` | Tính toán PMI, LLR; đếm tần suất |
| `matplotlib` | Vẽ biểu đồ Bar Chart |
| `wordcloud` | Tạo Word Cloud |

## 📌 Lưu ý quan trọng
- Dataset Sentiment140 cần download từ Kaggle và đặt cùng thư mục với notebook
- Dùng `df.sample(n=10000)` để chạy nhanh, có thể tăng lên 50,000+ sau khi code ổn định
- PMI threshold tần suất: bigram ≥ 5 lần để tránh overfitting với từ hiếm
