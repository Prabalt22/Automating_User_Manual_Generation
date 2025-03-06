from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

# Sample dictionary
data = {
    1: {'title': 'hello', 'description': 'world', 'screenshot_path': r'C:\Users\Prabal Arvind Tiwari\OneDrive\Desktop\c++\Untitled-24-02-25\screenshot_1.png'},
    2: {'title': 'hello', 'description': 'world', 'screenshot_path': r'C:\Users\Prabal Arvind Tiwari\OneDrive\Desktop\c++\Untitled-24-02-25\screenshot_2.png'},
    3: {'title': 'hello', 'description': 'world', 'screenshot_path': r'C:\Users\Prabal Arvind Tiwari\OneDrive\Desktop\c++\Untitled-24-02-25\screenshot_3.png'},
    4: {'title': 'hello', 'description': 'world', 'screenshot_path': r'C:\Users\Prabal Arvind Tiwari\OneDrive\Desktop\c++\Untitled-24-02-25\screenshot_4.png'},
    5: {'title': 'hello', 'description': 'world', 'screenshot_path': r'C:\Users\Prabal Arvind Tiwari\OneDrive\Desktop\c++\Untitled-24-02-25\screenshot_5.png'}
}

# PDF setup
fileName = 'output.pdf'
pdf = canvas.Canvas(fileName, pagesize=letter)

# page dimension
width, height = letter

y_position = height - 50


for key, value in data.items():
    title = value.get('title','No Title')
    description = value.get('description', 'No Description')
    screenshot_path = value.get('screenshot_path', '')
    
    # Add Title
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y_position, f"Step {key}: {title}")
    y_position -= 20
    
    # Add description
    pdf.setFont("Helvetica", 14)
    pdf.drawString(50, y_position, f"Description: {description}")
    y_position -= 40
    
    # Add Screenshot if available
    try:
        pdf.drawInlineImage(screenshot_path, 50, y_position - 150, width=300, height=150)
        y_position -= 180
    except Exception as e:
        pdf.setFillColor(colors.red)
        pdf.drawString(50, y_position, f"Error loading image: {e}")
        pdf.setFillColor(colors.black)
        y_position -= 40
        
    # add separete file
    pdf.line(30, y_position, width - 30, y_position)
    y_position -= 30
    
    # Start a new page if space is low
    if y_position < 150:
        pdf.showPage()
        y_position = height - 50

pdf.save()
print(f"PDF successfully created: {fileName}")