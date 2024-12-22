from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Register Bengali Font
pdfmetrics.registerFont(TTFont('SolaimanLipi', 'SolaimanLipi.ttf'))  # Make sure you have this font

def draw_circle(c, x, y, r):
    c.circle(x, y, r, stroke=1, fill=0)

def generate_omr(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Set font
    c.setFont('SolaimanLipi', 14)

    # Add title
    c.drawString(200, height - 50, "প্রথম আলো পড়াশোনা")

    # Draw Roll Number Section
    c.drawString(50, height - 100, "রোল নাম্বার")
    for i in range(10):
        c.drawString(50 + i * 20, height - 120, str(i))
        for j in range(10):
            draw_circle(c, 55 + i * 20, height - 140 - j * 20, 8)

    # Draw Serial Number Section
    c.drawString(300, height - 100, "সিরিয়াল নাম্বার")
    for i in range(10):
        c.drawString(300 + i * 20, height - 120, str(i))
        for j in range(10):
            draw_circle(c, 305 + i * 20, height - 140 - j * 20, 8)

    # Questions Section
    question_start_y = height - 250
    question_no = 1
    for col in range(4):  # 4 Columns
        x_offset = 50 + col * 130
        y = question_start_y
        for row in range(25):  # 25 Questions per column
            c.drawString(x_offset, y, f"{str(question_no).zfill(2)}")
            for option, text in enumerate("অ আ ই ঈ".split(), start=1):  # Options in Bengali
                draw_circle(c, x_offset + 30 + option * 20, y - 5, 8)
                c.drawString(x_offset + 30 + option * 20 - 5, y - 20, text)
            y -= 30
            question_no += 1

    # Save the file
    c.save()

# Generate the OMR
generate_omr("omr_sheet_bangla.pdf")
