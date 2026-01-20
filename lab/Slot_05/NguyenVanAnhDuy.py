"""
MINITEST: THUẬT TOÁN APRIORI VÀ FP-GROWTH
Sinh viên: Nguyễn Văn Anh Duy
MSSV: SE181823
CLASS: AI1804
Dataset: Apriori_FPGgrowth.csv
Minimum Support: 2100 giao dịch
"""

import csv
from collections import defaultdict, Counter
from itertools import combinations

# ===========================================================================================
# PHẦN 1: ĐỌC VÀ XỬ LÝ DỮ LIỆU
# ===========================================================================================

def load_transactions(filename):
    """
    Đọc dữ liệu từ file CSV và chuyển thành danh sách các giao dịch
    
    Args:
        filename: Tên file CSV chứa dữ liệu
    
    Returns:
        transactions: List các giao dịch, mỗi giao dịch là một set các sản phẩm
    """
    transactions = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            # Loại bỏ các ô trống và khoảng trắng
            transaction = set([item.strip() for item in row if item.strip()])
            
            if transaction:  # Chỉ thêm giao dịch không rỗng
                transactions.append(transaction)
    
    print(f"Đã tải {len(transactions)} giao dịch từ file {filename}")
    return transactions


# ===========================================================================================
# PHẦN 2: THUẬT TOÁN APRIORI
# ===========================================================================================

class Apriori:
    """
    Triển khai thuật toán Apriori để tìm frequent itemsets
    Thuật toán này sử dụng phương pháp bottom-up, bắt đầu từ các itemset đơn
    và dần dần mở rộng lên các itemset lớn hơn
    """
    
    def __init__(self, transactions, min_support):
        """
        Khởi tạo thuật toán Apriori
        
        Args:
            transactions: Danh sách các giao dịch
            min_support: Ngưỡng support tối thiểu (số lượng giao dịch)
        """
        self.transactions = transactions
        self.min_support = min_support
        self.total_transactions = len(transactions)
        
    def get_support(self, itemset):
        """
        Tính support count của một itemset
        Support count = số lượng giao dịch chứa itemset đó
        
        Args:
            itemset: Tập các sản phẩm cần tính support
            
        Returns:
            count: Số lượng giao dịch chứa itemset
        """
        count = 0
        itemset = frozenset(itemset)
        
        for transaction in self.transactions:
            # Kiểm tra xem itemset có là tập con của transaction không
            if itemset.issubset(transaction):
                count += 1
                
        return count
    
    def get_frequent_1_itemsets(self):
        """
        STEP 1: Tìm các frequent itemsets có 1 phần tử (1-itemsets)
        
        Returns:
            frequent_items: Dictionary {itemset: support_count}
        """
        print("\n" + "="*80)
        print("APRIORI - STEP 1: TÌM FREQUENT 1-ITEMSETS")
        print("="*80)
        
        # Đếm tần suất xuất hiện của từng sản phẩm
        item_count = Counter()
        
        for transaction in self.transactions:
            for item in transaction:
                item_count[frozenset([item])] += 1
        
        # Lọc các items có support >= min_support
        frequent_items = {
            itemset: count 
            for itemset, count in item_count.items() 
            if count >= self.min_support
        }
        
        print(f"Tổng số sản phẩm duy nhất: {len(item_count)}")
        print(f"Số lượng frequent 1-itemsets (support >= {self.min_support}): {len(frequent_items)}")
        print("\nTop 10 frequent 1-itemsets:")
        
        # Sắp xếp theo support giảm dần
        sorted_items = sorted(frequent_items.items(), key=lambda x: x[1], reverse=True)
        for i, (itemset, count) in enumerate(sorted_items[:10], 1):
            item_name = list(itemset)[0]
            print(f"  {i}. {{{item_name}}}: {count}")
        
        return frequent_items
    
    def generate_candidates(self, frequent_k_itemsets, k):
        """
        Tạo các candidate (k+1)-itemsets từ frequent k-itemsets
        Sử dụng phương pháp join: nối 2 k-itemsets có (k-1) phần tử chung
        
        Args:
            frequent_k_itemsets: Dictionary các frequent k-itemsets
            k: Kích thước hiện tại của itemsets
            
        Returns:
            candidates: Set các candidate (k+1)-itemsets
        """
        candidates = set()
        itemsets_list = list(frequent_k_itemsets.keys())
        
        # Join step: Nối 2 itemsets có (k-1) phần tử chung
        for i in range(len(itemsets_list)):
            for j in range(i + 1, len(itemsets_list)):
                # Union 2 itemsets
                union = itemsets_list[i] | itemsets_list[j]
                
                # Chỉ thêm nếu union có kích thước k+1
                if len(union) == k + 1:
                    # Prune step: Kiểm tra tất cả k-subsets có trong frequent_k_itemsets không
                    is_valid = True
                    for subset in combinations(union, k):
                        if frozenset(subset) not in frequent_k_itemsets:
                            is_valid = False
                            break
                    
                    if is_valid:
                        candidates.add(union)
        
        return candidates
    
    def get_frequent_k_itemsets(self, frequent_prev, k):
        """
        Tìm frequent k-itemsets từ frequent (k-1)-itemsets
        
        Args:
            frequent_prev: Dictionary các frequent (k-1)-itemsets
            k: Kích thước k cần tìm
            
        Returns:
            frequent_k: Dictionary các frequent k-itemsets
        """
        print(f"\nAPRIORI - STEP {k}: TÌM FREQUENT {k}-ITEMSETS")
        print("-" * 80)
        
        # Tạo candidates
        candidates = self.generate_candidates(frequent_prev, k - 1)
        print(f"Số lượng candidates được tạo: {len(candidates)}")
        
        # Tính support cho từng candidate
        frequent_k = {}
        
        for candidate in candidates:
            support = self.get_support(candidate)
            
            if support >= self.min_support:
                frequent_k[candidate] = support
        
        print(f"Số lượng frequent {k}-itemsets (support >= {self.min_support}): {len(frequent_k)}")
        
        # Hiển thị top 10 itemsets
        if frequent_k:
            print(f"\nTop 10 frequent {k}-itemsets:")
            sorted_items = sorted(frequent_k.items(), key=lambda x: x[1], reverse=True)
            
            for i, (itemset, count) in enumerate(sorted_items[:10], 1):
                items_str = ", ".join(sorted(list(itemset)))
                print(f"  {i}. {{{items_str}}}: {count}")
        
        return frequent_k
    
    def run(self):
        """
        Chạy thuật toán Apriori hoàn chỉnh
        
        Returns:
            all_frequent_itemsets: Dictionary chứa tất cả frequent itemsets
        """
        print("\n" + "#"*80)
        print("BẮT ĐẦU THUẬT TOÁN APRIORI")
        print("#"*80)
        
        all_frequent_itemsets = {}
        
        # Step 1: Tìm frequent 1-itemsets
        frequent_1 = self.get_frequent_1_itemsets()
        all_frequent_itemsets[1] = frequent_1
        
        # Step k: Tìm frequent k-itemsets (k >= 2)
        k = 2
        frequent_prev = frequent_1
        
        while frequent_prev:
            frequent_k = self.get_frequent_k_itemsets(frequent_prev, k)
            
            if not frequent_k:
                print(f"\nKhông tìm thấy thêm frequent {k}-itemsets. Dừng thuật toán.")
                break
            
            all_frequent_itemsets[k] = frequent_k
            frequent_prev = frequent_k
            k += 1
        
        # Tổng kết
        print("\n" + "="*80)
        print("KẾT QUẢ APRIORI")
        print("="*80)
        
        total_itemsets = sum(len(itemsets) for itemsets in all_frequent_itemsets.values())
        print(f"Tổng số frequent itemsets tìm được: {total_itemsets}")
        
        for k, itemsets in all_frequent_itemsets.items():
            print(f"  - Frequent {k}-itemsets: {len(itemsets)}")
        
        return all_frequent_itemsets


# ===========================================================================================
# PHẦN 3: THUẬT TOÁN FP-GROWTH
# ===========================================================================================

class FPNode:
    """
    Node trong FP-Tree
    Mỗi node đại diện cho một sản phẩm trong cây
    """
    
    def __init__(self, item, count=0, parent=None):
        """
        Khởi tạo một node trong FP-Tree
        
        Args:
            item: Tên sản phẩm
            count: Số lần xuất hiện
            parent: Node cha
        """
        self.item = item
        self.count = count
        self.parent = parent
        self.children = {}  # Dictionary {item: FPNode}
        self.next_node = None  # Link đến node cùng item khác trong cây
    
    def increment(self, count):
        """Tăng count của node"""
        self.count += count


class FPTree:
    """
    FP-Tree (Frequent Pattern Tree)
    Cấu trúc dữ liệu nén để lưu trữ thông tin về frequent patterns
    """
    
    def __init__(self, transactions, min_support, is_main_tree=False):
        """
        Khởi tạo và xây dựng FP-Tree
        
        Args:
            transactions: Danh sách các giao dịch
            min_support: Ngưỡng support tối thiểu
            is_main_tree: True nếu là main tree, False nếu là conditional tree
        """
        self.min_support = min_support
        self.header_table = {}  # Header table: {item: (count, first_node)}
        self.root = FPNode('root', 0, None)
        self.is_main_tree = is_main_tree
        
        # Build tree
        self.build_tree(transactions)
    
    def build_tree(self, transactions):
        """
        Xây dựng FP-Tree từ các giao dịch
        
        Args:
            transactions: Danh sách các giao dịch
        """
        # Chỉ in chi tiết khi là main tree
        if self.is_main_tree:
            print("\n" + "="*80)
            print("FP-GROWTH - STEP 1: XÂY DỰNG FP-TREE")
            print("="*80)
            print("\nBước 1.1: Đếm tần suất các sản phẩm...")
        
        # Đếm tần suất xuất hiện của từng item
        item_count = Counter()
        
        for transaction in transactions:
            for item in transaction:
                item_count[item] += 1
        
        # Lọc các items có support >= min_support
        frequent_items = {
            item: count 
            for item, count in item_count.items() 
            if count >= self.min_support
        }
        
        if self.is_main_tree:
            print(f"Số lượng frequent items: {len(frequent_items)}")
            
            # Bước 1.2: Sắp xếp items theo tần suất giảm dần
            print("\nBước 1.2: Sắp xếp items theo tần suất...")
            sorted_items = sorted(frequent_items.items(), key=lambda x: x[1], reverse=True)
            
            print("Top 10 items có tần suất cao nhất:")
            for i, (item, count) in enumerate(sorted_items[:10], 1):
                print(f"  {i}. {item}: {count}")
        else:
            sorted_items = sorted(frequent_items.items(), key=lambda x: x[1], reverse=True)
        
        # Khởi tạo header table
        for item, count in sorted_items:
            self.header_table[item] = [count, None]
        
        if self.is_main_tree:
            # Bước 1.3: Chèn các giao dịch vào FP-Tree
            print("\nBước 1.3: Chèn các giao dịch vào FP-Tree...")
        
        for transaction in transactions:
            # Lọc và sắp xếp items trong transaction theo thứ tự tần suất
            filtered_transaction = [
                item for item in transaction 
                if item in frequent_items
            ]
            
            filtered_transaction.sort(key=lambda x: frequent_items[x], reverse=True)
            
            # Chèn transaction vào tree
            if filtered_transaction:
                self.insert_transaction(filtered_transaction, self.root)
        
        if self.is_main_tree:
            print(f"Đã xây dựng xong FP-Tree với {len(self.header_table)} frequent items")
    
    def insert_transaction(self, transaction, node):
        """
        Chèn một transaction vào FP-Tree
        
        Args:
            transaction: List các items đã được sắp xếp
            node: Node hiện tại trong tree
        """
        if not transaction:
            return
        
        # Lấy item đầu tiên
        first_item = transaction[0]
        
        # Nếu node hiện tại đã có child với item này
        if first_item in node.children:
            node.children[first_item].increment(1)
        else:
            # Tạo child node mới
            new_node = FPNode(first_item, 1, node)
            node.children[first_item] = new_node
            
            # Cập nhật header table
            if self.header_table[first_item][1] is None:
                # Đây là node đầu tiên của item này
                self.header_table[first_item][1] = new_node
            else:
                # Link node này vào chuỗi các nodes cùng item
                current = self.header_table[first_item][1]
                while current.next_node is not None:
                    current = current.next_node
                current.next_node = new_node
        
        # Đệ quy chèn phần còn lại của transaction
        if len(transaction) > 1:
            self.insert_transaction(transaction[1:], node.children[first_item])


class FPGrowth:
    """
    Triển khai thuật toán FP-Growth để tìm frequent itemsets
    Thuật toán này sử dụng cấu trúc FP-Tree và đệ quy để tìm patterns
    """
    
    def __init__(self, transactions, min_support):
        """
        Khởi tạo thuật toán FP-Growth
        
        Args:
            transactions: Danh sách các giao dịch
            min_support: Ngưỡng support tối thiểu
        """
        self.transactions = transactions
        self.min_support = min_support
        self.frequent_patterns = {}
    
    def get_paths_from_tree(self, node):
        """
        Lấy tất cả các paths từ một node đến root
        
        Args:
            node: Node cần lấy paths
            
        Returns:
            paths: List các paths, mỗi path là (items, count)
        """
        paths = []
        
        while node is not None:
            path = []
            count = node.count
            parent = node.parent
            
            # Đi ngược từ node lên root
            while parent.parent is not None:
                path.append(parent.item)
                parent = parent.parent
            
            if path:
                paths.append((path[::-1], count))  # Đảo ngược path
            
            node = node.next_node
        
        return paths
    
    def mine_tree(self, tree, prefix, step_counter):
        """
        Đào (mine) FP-Tree đệ quy để tìm frequent patterns
        
        Args:
            tree: FP-Tree cần đào
            prefix: Prefix hiện tại (pattern đang xây dựng)
            step_counter: Biến đếm bước để hiển thị
        """
        # Lấy items theo thứ tự tần suất tăng dần (bottom-up)
        items = sorted(
            tree.header_table.items(),
            key=lambda x: x[1][0]
        )
        
        for item, (count, node) in items:
            # Tạo pattern mới bằng cách thêm item vào prefix
            new_pattern = prefix + [item]
            support = count
            
            # Lưu pattern này
            pattern_key = frozenset(new_pattern)
            self.frequent_patterns[pattern_key] = support
            
            # Hiển thị pattern tìm được (chỉ hiển thị một số đầu tiên để không bị spam)
            if len(self.frequent_patterns) <= 20:
                pattern_str = " + ".join(sorted(new_pattern))
                print(f"  ✓ Tìm được pattern: {{{pattern_str}}} với support = {support}")
            
            # Lấy conditional pattern base
            paths = self.get_paths_from_tree(node)
            
            # Nếu có paths, xây dựng conditional FP-Tree và đệ quy
            if paths:
                # Tạo conditional transactions
                conditional_transactions = []
                for path, path_count in paths:
                    for _ in range(path_count):
                        conditional_transactions.append(set(path))
                
                # Xây dựng conditional FP-Tree (không phải main tree nên is_main_tree=False)
                if conditional_transactions:
                    conditional_tree = FPTree(conditional_transactions, self.min_support, is_main_tree=False)
                    
                    # Nếu conditional tree không rỗng, đệ quy
                    if conditional_tree.header_table:
                        step_counter[0] += 1
                        self.mine_tree(conditional_tree, new_pattern, step_counter)
    
    def run(self):
        """
        Chạy thuật toán FP-Growth hoàn chỉnh
        
        Returns:
            frequent_patterns: Dictionary {pattern: support_count}
        """
        print("\n" + "#"*80)
        print("BẮT ĐẦU THUẬT TOÁN FP-GROWTH")
        print("#"*80)
        
        # Step 1: Xây dựng FP-Tree
        fp_tree = FPTree(self.transactions, self.min_support, is_main_tree=True)
        
        # Step 2: Đào FP-Tree để tìm frequent patterns
        print("\n" + "="*80)
        print("FP-GROWTH - STEP 2: ĐÀO FP-TREE ĐỂ TÌM FREQUENT PATTERNS")
        print("="*80)
        print("\nBắt đầu quá trình mining đệ quy...")
        print("(Hiển thị 20 patterns đầu tiên được tìm thấy)\n")
        
        step_counter = [0]  # Dùng list để có thể modify trong hàm đệ quy
        self.mine_tree(fp_tree, [], step_counter)
        
        print(f"\n✓ Đã hoàn thành mining:")
        print(f"  - Tổng số patterns tìm được: {len(self.frequent_patterns)}")
        print(f"  - Số conditional trees được tạo: {step_counter[0]}")
        
        # Phân loại patterns theo kích thước
        patterns_by_size = defaultdict(dict)
        
        for pattern, support in self.frequent_patterns.items():
            size = len(pattern)
            patterns_by_size[size][pattern] = support
        
        # Tổng kết
        print("\n" + "="*80)
        print("KẾT QUẢ FP-GROWTH")
        print("="*80)
        
        total_patterns = len(self.frequent_patterns)
        print(f"Tổng số frequent patterns tìm được: {total_patterns}")
        
        for size in sorted(patterns_by_size.keys()):
            print(f"  - Frequent {size}-itemsets: {len(patterns_by_size[size])}")
        
        # Hiển thị top patterns cho mỗi kích thước
        print("\nTop 5 patterns cho mỗi kích thước:")
        
        for size in sorted(patterns_by_size.keys())[:5]:  # Chỉ hiển thị 5 kích thước đầu
            print(f"\n  Kích thước {size}:")
            sorted_patterns = sorted(
                patterns_by_size[size].items(),
                key=lambda x: x[1],
                reverse=True
            )
            
            for i, (pattern, support) in enumerate(sorted_patterns[:5], 1):
                items_str = ", ".join(sorted(list(pattern)))
                print(f"    {i}. {{{items_str}}}: {support}")
        
        return self.frequent_patterns


# ===========================================================================================
# PHẦN 4: CHƯƠNG TRÌNH CHÍNH
# ===========================================================================================

def main():
    """
    Hàm chính để chạy cả 2 thuật toán Apriori và FP-Growth
    """
    print("\n" + "="*80)
    print("MINITEST: THUẬT TOÁN APRIORI VÀ FP-GROWTH")
    print("Sinh viên: Nguyễn Văn Anh Duy")
    print("MSSV: SE181823")
    print("CLASS: AI1804")
    print("="*80)
 
    # Cấu hình
    filename = 'Apriori_FPGgrowth.csv'
    min_support = 2100  # Thay đổi giá trị này để tìm combo có nhiều sản phẩm hơn
                        # 2100: Tìm combo 2 sản phẩm (yêu cầu đề bài)
                        # 1200: Tìm được 55 combo 3 sản phẩm
                        # 1000: Tìm được 220 combo 3 sản phẩm
                        # 600: Tìm được 18 combo 4 sản phẩm + 220 combo 3 sản phẩm
    
    print(f"\nCấu hình:")
    print(f"  - Dataset: {filename}")
    print(f"  - Minimum Support: {min_support} giao dịch")
    
    # Đọc dữ liệu
    print("\n" + "="*80)
    print("ĐỌC DỮ LIỆU")
    print("="*80)
    
    transactions = load_transactions(filename)
    
    print(f"\nThông tin dữ liệu:")
    print(f"  - Tổng số giao dịch: {len(transactions)}")
    print(f"  - Kích thước giao dịch trung bình: {sum(len(t) for t in transactions) / len(transactions):.2f} sản phẩm")
    
    # Chạy Apriori
    print("\n\n")
    apriori = Apriori(transactions, min_support)
    apriori_results = apriori.run()
    
    # Chạy FP-Growth
    print("\n\n")
    fpgrowth = FPGrowth(transactions, min_support)
    fpgrowth_results = fpgrowth.run()
    
    # So sánh kết quả
    print("\n\n" + "="*80)
    print("SO SÁNH KẾT QUẢ 2 THUẬT TOÁN")
    print("="*80)
    
    apriori_total = sum(len(itemsets) for itemsets in apriori_results.values())
    fpgrowth_total = len(fpgrowth_results)
    
    print(f"\n{'Thuật toán':<20} {'Số frequent itemsets':<25} {'Ghi chú':<30}")
    print("-" * 80)
    print(f"{'Apriori':<20} {apriori_total:<25} {'Phương pháp generate-and-test':<30}")
    print(f"{'FP-Growth':<20} {fpgrowth_total:<25} {'Phương pháp pattern growth':<30}")
    
    print("\n" + "="*80)
    print("COMBO SẢN PHẨM NÊN ĐI CÙNG NHAU")
    print("="*80)
    
    # Lấy tất cả patterns có nhiều items và support cao
    all_patterns = []
    patterns_dict = {}  # Để loại bỏ duplicate giữa 2 thuật toán
    
    # Từ Apriori
    for size, itemsets in apriori_results.items():
        if size >= 2:  # Chỉ lấy combo từ 2 sản phẩm trở lên
            for itemset, support in itemsets.items():
                key = frozenset(itemset)
                if key not in patterns_dict:
                    patterns_dict[key] = (itemset, support, size, 'Apriori')
    
    # Từ FP-Growth
    for pattern, support in fpgrowth_results.items():
        size = len(pattern)
        if size >= 2:  # Chỉ lấy combo từ 2 sản phẩm trở lên
            key = frozenset(pattern)
            if key not in patterns_dict:
                patterns_dict[key] = (pattern, support, size, 'FP-Growth')
            # Nếu đã có từ Apriori, đánh dấu là cả 2
            elif patterns_dict[key][3] == 'Apriori':
                patterns_dict[key] = (pattern, support, size, 'Cả 2')
    
    all_patterns = list(patterns_dict.values())
    
    # Sắp xếp theo: kích thước giảm dần, sau đó support giảm dần
    all_patterns.sort(key=lambda x: (x[2], x[1]), reverse=True)
    
    # Phân tích số lượng combo theo kích thước
    size_distribution = defaultdict(int)
    for _, _, size, _ in all_patterns:
        size_distribution[size] += 1
    
    print("\nPhân bố combo theo số lượng sản phẩm:")
    for size in sorted(size_distribution.keys(), reverse=True):
        print(f"  - Combo {size} sản phẩm: {size_distribution[size]} patterns")
    
    # Hiển thị top combo
    print("\n" + "-"*84)
    print("TOP 30 COMBO SẢN PHẨM CÓ SUPPORT CAO NHẤT")
    print("-"*84)
    print(f"\n{'#':<4} {'Combo sản phẩm':<55} {'Support':<10} {'Kích thước':<12} {'Nguồn':<10}")
    print("-" * 95)
    
    for i, (itemset, support, size, source) in enumerate(all_patterns[:30], 1):
        items_str = " + ".join(sorted(list(itemset)))
        if len(items_str) > 54:
            items_str = items_str[:51] + "..."
        print(f"{i:<4} {items_str:<55} {support:<10} {size} sản phẩm{'':<4} {source:<10}")
    
    # Đề xuất về combo lớn hơn
    if max(size_distribution.keys()) == 2:
        print("\n" + "="*80)
        print("LƯU Ý")
        print("="*80)
        print(f"Với min_support = {min_support}, chỉ tìm thấy combo tối đa 2 sản phẩm.")
        print("Để tìm combo có 3+ sản phẩm, cần giảm min_support xuống.")
        print("\nGợi ý dựa trên thử nghiệm thực tế:")
        print("  - min_support = 1200: Tìm được 55 combo 3 sản phẩm")
        print("  - min_support = 1000: Tìm được 220 combo 3 sản phẩm")
        print("  - min_support = 600:  Tìm được 18 combo 4 sản phẩm")
        print("\nVí dụ combo 4 sản phẩm (support=624):")
        print("  → Lassi + Panner + Sweet + Tea Powder")
    elif max(size_distribution.keys()) == 3:
        print("\n" + "="*80)
        print("LƯU Ý")
        print("="*80)
        print(f"Với min_support = {min_support}, tìm thấy combo tối đa 3 sản phẩm.")
        print("Để tìm combo 4+ sản phẩm, cần giảm min_support xuống còn 600.")
        print("\nVí dụ combo 4 sản phẩm tốt nhất (support=624):")
        print("  → Lassi + Panner + Sweet + Tea Powder")
    elif max(size_distribution.keys()) >= 4:
        print("\n" + "="*80)
        print("KẾT QUẢ TỐT!")
        print("="*80)
        print(f"Với min_support = {min_support}, đã tìm được combo {max(size_distribution.keys())} sản phẩm!")
        print(f"Đây là những insight có giá trị cao về hành vi mua hàng của khách.")
    
    # Hiển thị một số insights thú vị
    print("\n" + "="*80)
    print("INSIGHTS VÀ KHUYẾN NGHỊ")
    print("="*80)
    
    # Sản phẩm xuất hiện nhiều nhất trong các combo
    product_frequency = Counter()
    for itemset, support, size, source in all_patterns[:30]:
        for item in itemset:
            product_frequency[item] += 1
    
    print("\nTop 10 sản phẩm xuất hiện nhiều nhất trong các combo:")
    for i, (product, freq) in enumerate(product_frequency.most_common(10), 1):
        print(f"  {i}. {product}: xuất hiện trong {freq} combo")
    
    print("\nKhuyến nghị:")
    print("  ✓ Đặt các combo có support cao gần nhau trong cửa hàng")
    print("  ✓ Tạo gói khuyến mãi cho các combo phổ biến")
    print("  ✓ Tối ưu kho hàng dựa trên mối quan hệ giữa các sản phẩm")


if __name__ == "__main__":
    main()
