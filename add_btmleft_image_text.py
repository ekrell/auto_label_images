#!/usr/bin/python3

# Evan Krell
# Script adds a textbox to the bottom left corner of an image

import matplotlib.pyplot as plt
from PIL import Image, ImageFont, ImageDraw 
import numpy as np
from optparse import OptionParser

# Options
parser = OptionParser()
parser.add_option("-i", "--image",
        help = "Image to add text to")
parser.add_option("-w", "--write",
        help = "Path to save new image to")
parser.add_option("-t", "--text", 
        help = "Text to write on image (Use '@@' to separate lines)")
parser.add_option("-f", "--font",
        help = "Path to truetype font")
parser.add_option("-s", "--size_font_min",
        help = "Minimum font size",
        default = 20)
parser.add_option("-r", "--resize_width",
        help = "New image width",
        default = 1000)
parser.add_option("-o", "--offset",
        help = "Distance away from edges for box",
        default = 10)
parser.add_option("-c", "--color",
        help = "Color of textboxt (R,G,B,A), where all values in [0, 255]",
        default = "34,34,34,170")
(options, args) = parser.parse_args()

file_img = options.image
file_out = options.write
text = options.text
file_font = options.font
base_font_size = options.size_font_min
offset_base = options.offset
new_width = options.resize_width
textbox_color = tuple(np.array(options.color.split(",")).astype("int"))

# Sanity check options
if file_img is None:
    print("Must supply image path!\nExiting...")
    exit(0)
if text is None:
    print("Must supply text for image!\nExiting...")
    exit(0)
if file_font is None:
    print("Must supply truetype font path!\nExiting...")
    exit(0)

# Convert text to list of lines
text_lines = text.split("@@")

# Init font
font = ImageFont.truetype(file_font, base_font_size)

# Plot image
img = Image.open(file_img)
width, height = img.size

# Resize image
wpercent = (new_width / float(width))
new_height = int((float(height) * float(wpercent)))
img = img.resize((new_width, new_height), Image.BICUBIC)
width, height = img.size

# Init drawing on image
draw = ImageDraw.Draw(img, "RGBA")

# Determine text line sizes
n_lines = len(text_lines)
text_line_widths = np.zeros(n_lines)
for i in range(n_lines):
    text_line_widths[i] = font.getsize(text_lines[i])[0]
max_text_width = np.max(text_line_widths)
longest_line_idx = np.argmax(text_line_widths)

# Update font sizes per line based on longest
font_line_sizes = np.zeros(n_lines)
for i in range(n_lines):
    font_size_ = base_font_size
    while ImageFont.truetype(file_font, font_size_).getsize(text_lines[i])[0] < max_text_width: 
        font_size_ += 1
    font_line_sizes[i] = font_size_
line_fonts = [ImageFont.truetype(file_font, int(font_line_sizes[i])) for i in range(n_lines)]


text_line_widths = np.zeros(n_lines)
for i in range(n_lines):
    text_line_widths[i] = line_fonts[i].getsize(text_lines[i])[0]
max_text_width = np.max(text_line_widths)
longest_line_idx = np.argmax(text_line_widths)

# Determine height of text box (draw each line, but don't draw it)
offset_accum = height - offset_base
for i in range(n_lines - 1, -1, -1):
    text_width, text_height = line_fonts[i].getsize(text_lines[i])
    # Subtract text line's height to update offset
    offset_accum -= text_height
      
# Draw text background box
shape = [(offset_base - 2, offset_accum - 2), (offset_base + max_text_width + 2, height - offset_base + 2)]
draw.rounded_rectangle(shape, fill = textbox_color, radius = 10)

# Type text
offset_accum = height - offset_base
for i in range(n_lines - 1, -1, -1):
    # Draw line
    text_width, text_height = line_fonts[i].getsize(text_lines[i])
    draw.text((offset_base, offset_accum - text_height), text_lines[i], font = line_fonts[i], align ="left")
    # Subtract text line's height to update offset
    offset_accum -= text_height

# Write or show image
if file_out:
    img.save(file_out)
else:
    img.show()
