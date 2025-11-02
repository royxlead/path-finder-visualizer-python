def get_neighbors(node, grid):
    """Return orthogonal neighbors for `node` within `grid` bounds.

    node.x is row, node.y is column.
    """
    neighbors = []
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = node.x + dr, node.y + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append(grid[nr][nc])
    return neighbors
