from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def export_pdf(filename, content):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []

    paragraphs = content.split("\n")

    for para in paragraphs:
        elements.append(Paragraph(para, styles['BodyText']))
        elements.append(Spacer(1, 10))

    doc.build(elements)
