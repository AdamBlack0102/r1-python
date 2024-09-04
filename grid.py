def dfs(i, j):
    # 检查当前格子是否越界或者包含磁铁，或者已经被访问过
    if i < 0 or i >= H or j < 0 or j >= W or grid[i][j] == '#' or visited[i][j]:
        return 0

    visited[i][j] = True
    count = 1

    # 在每次移动之前检查周围是否存在磁铁
    if grid[i + 1][j] != '#' and not visited[i + 1][j]:
        count += dfs(i + 1, j)  # 向下移动
    if grid[i - 1][j] != '#' and not visited[i - 1][j]:
        count += dfs(i - 1, j)  # 向上移动
    if grid[i][j + 1] != '#' and not visited[i][j + 1]:
        count += dfs(i, j + 1)  # 向右移动
    if grid[i][j - 1] != '#' and not visited[i][j - 1]:
        count += dfs(i, j - 1)  # 向左移动

    return count
