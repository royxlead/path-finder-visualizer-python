def draw_grid(grid, canvas):
    
    canvas.delete("all")  
    # grid is a list of rows: grid[row][col]
    if not grid:
        return

    rows = len(grid)
    cols = len(grid[0])

    # use separate width/height to avoid distortion
    cell_width = max(1, canvas.winfo_width() // cols)
    cell_height = max(1, canvas.winfo_height() // rows)

    for row in grid:
        for node in row:
            # node.x == row index, node.y == column index
            x0 = node.y * cell_width
            y0 = node.x * cell_height
            x1 = x0 + cell_width
            y1 = y0 + cell_height

            if getattr(node, "is_start", False):
                fill_color = "#0000FF"
            elif getattr(node, "is_end", False):
                fill_color = "#FFA500"
            else:
                fill_color = rgb_to_hex(node.color)

            canvas.create_rectangle(x0, y0, x1, y1, fill=fill_color, outline="black")

def rgb_to_hex(rgb):
    return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
