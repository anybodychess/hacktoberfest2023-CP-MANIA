class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return

        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        self.build(left_node, start, mid)
        self.build(right_node, mid + 1, end)

        self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def update(self, node, start, end, index, value):
        if start == end == index:
            self.tree[node] = value
            return

        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        if index <= mid:
            self.update(left_node, start, mid, index, value)
        else:
            self.update(right_node, mid + 1, end, index, value)

        self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 0

        if left <= start and right >= end:
            return self.tree[node]

        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2

        left_sum = self.query(left_node, start, mid, left, right)
        right_sum = self.query(right_node, mid + 1, end, left, right)

        return left_sum + right_sum

# Example Usage
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

print(seg_tree.query(0, 0, len(arr) - 1, 1, 3))  # Output: 15

seg_tree.update(0, 0, len(arr) - 1, 2, 10)
print(seg_tree.query(0, 0, len(arr) - 1, 1, 3))  # Output: 20
