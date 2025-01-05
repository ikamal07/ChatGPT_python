from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_daily_planner(pdf_file):
    # Page setup
    width, height = letter
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.setFont("Helvetica", 10)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Daily Planner")

    # Date and Focus
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, "Date:")
    c.drawString(50, height - 110, "Focus:")
    c.drawString(50, height - 140, "Goal:")

    # Schedule
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 180, "Schedule:")
    c.setFont("Helvetica", 10)
    for i, time in enumerate(range(7, 22)):  # 7 AM to 9 PM
        c.drawString(50, height - 200 - (i * 20), f"{time}:00")

    # How do I want to feel & Grateful For
    c.setFont("Helvetica", 12)
    c.drawString(300, height - 80, "How do I want to feel?")
    c.line(300, height - 85, 550, height - 85)
    c.drawString(300, height - 110, "Grateful for:")
    for i in range(4):
        c.line(300, height - 120 - (i * 20), 550, height - 120 - (i * 20))

    # Key Tasks
    c.setFont("Helvetica-Bold", 12)
    c.drawString(300, height - 180, "Key Tasks:")
    c.setFont("Helvetica", 10)
    for i in range(10):
        c.drawString(300, height - 200 - (i * 20), f"{i + 1}.")
        c.circle(550, height - 195 - (i * 20), 5)

    # Notes
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 500, "Notes:")
    c.line(50, height - 510, 550, height - 510)
    for i in range(8):
        c.line(50, height - 520 - (i * 20), 550, height - 520 - (i * 20))

    # Habits
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 700, "Habits:")
    c.setFont("Helvetica", 10)
    for i in range(5):
        c.drawString(50, height - 720 - (i * 20), f"{i + 1}.")
        c.circle(150, height - 715 - (i * 20), 5)

    # Save the PDF
    c.save()
    print(f"Daily planner saved to {pdf_file}")

# Generate the planner
create_daily_planner("daily_planner.pdf")
