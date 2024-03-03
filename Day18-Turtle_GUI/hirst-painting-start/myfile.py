import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 12)
for color in colors:
    first_color = color
    rgb = color.rgb
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    sequence = (r, g, b)
    rgb_colors.append(sequence)
print(rgb_colors)
