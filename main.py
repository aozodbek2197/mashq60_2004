# 1-mashq
def max_profit_with_cooldown(prices):
    if len(prices) < 2: return 0
    buy, sell, cooldown = float('-inf'), 0, 0
    for price in prices:
        prev_buy = buy
        buy = max(buy, cooldown - price)
        cooldown = sell
        sell = max(sell, prev_buy + price)
    return sell

print(max_profit_with_cooldown([1,2,3,0,2]))
# 2-mashq
def num_islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(num_islands(grid))
# 3-mashq
def merge_k_sorted_lists(lists):
    import heapq
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    return result

lists = [[1,4,5],[1,3,4],[2,6]]
print(merge_k_sorted_lists(lists))
