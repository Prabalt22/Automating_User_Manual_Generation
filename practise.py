from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

data = {
    1: {'title': 'Click "document"', 'description': 'Perform the action to proceed.', 'screenshot_path': r'C:\Path\to\screenshot_1.png'},
    2: {'title': 'Open Menu', 'description': 'Access additional options.', 'screenshot_path': r'C:\Path\to\screenshot_2.png'},
}

file_name = 'styled_output.pdf'
pdf = canvas.Canvas(file_name, pagesize=letter)

page_width, page_height = letter
y_position = page_height - 80  # Start a bit lower

for step, value in data.items():
    title = value.get('title', 'No Title')
    description = value.get('description', 'No Description')
    screenshot_path = value.get('screenshot_path', '')

    container_width = page_width - 100  
    container_height = 50  
    pdf.setFillColorRGB(0.094, 1, 0)  
    pdf.roundRect(50, y_position - container_height, container_width, container_height, 10, fill=1, stroke=0)

    circle_x = 80
    circle_y = y_position - (container_height/2)
    circle_radius = 15
    pdf.setFillColor(colors.white)  
    pdf.circle(circle_x, circle_y, circle_radius, fill=1, stroke=0)
    
    pdf.setFillColor(colors.black)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(circle_x, circle_y - 5, str(step))

    pdf.setFillColor(colors.black)
    pdf.setFont("Helvetica-Bold", 14)
    title_x = circle_x + circle_radius + 15  
    title_y = circle_y - 5  
    pdf.drawString(title_x, title_y, title)

    # Move down after the container
    y_position -= container_height + 20

    # Description
    pdf.setFont("Helvetica", 12)
    pdf.drawString(80, y_position, description)
    y_position -= 30

    # Add Screenshot (with Error Handling)
    try:
        pdf.drawInlineImage(screenshot_path, 80, y_position - 180, width=400, height=180)
        y_position -= 200
    except Exception as e:
        pdf.setFillColor(colors.red)
        pdf.drawString(80, y_position, f"Error loading image: {e}")
        pdf.setFillColor(colors.black)
        y_position -= 40

    # Divider Line
    pdf.line(50, y_position, page_width - 50, y_position)
    y_position -= 40

    # Page Break if Space is Low
    if y_position < 150:
        pdf.showPage()
        y_position = page_height - 80

pdf.save()
print(f"PDF successfully created: {file_name}")