def draw_grid(grid, canvas):
    
    canvas.delete("all")  
    
    cell_size = canvas.winfo_width() // len(grid)
    
    for row in grid:
        for node in row:
            x0 = node.x * cell_size
            y0 = node.y * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            
            if getattr(node, "is_start", False):
                fill_color = "#0000FF"  
            elif getattr(node, "is_end", False): 
                fill_color = "#FFA500"  
            else:  
                fill_color = rgb_to_hex(node.color)
            
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill_color, outline="black")

def rgb_to_hex(rgb):
    return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
