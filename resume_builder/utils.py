from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import weasyprint
from django.template.loader import render_to_string

def generate_pdf_reportlab(resume):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=12,
        alignment=1,  # Center alignment
        textColor=colors.darkblue
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=6,
        textColor=colors.darkblue,
        borderWidth=1,
        borderColor=colors.darkblue,
        borderPadding=5
    )
    
    story = []
    
    # Title
    story.append(Paragraph(resume.full_name, title_style))
    story.append(Spacer(1, 12))
    
    # Contact Info
    contact_info = f"{resume.email} | {resume.phone}"
    story.append(Paragraph(contact_info, styles['Normal']))
    story.append(Paragraph(resume.address, styles['Normal']))
    story.append(Spacer(1, 12))
    
    # Summary
    if resume.summary:
        story.append(Paragraph("SUMMARY", heading_style))
        story.append(Paragraph(resume.summary, styles['Normal']))
        story.append(Spacer(1, 12))
    
    # Experience
    if resume.experiences.exists():
        story.append(Paragraph("EXPERIENCE", heading_style))
        for exp in resume.experiences.all():
            end_date = "Present" if exp.is_current else exp.end_date.strftime("%Y-%m-%d")
            exp_header = f"<b>{exp.job_title}</b> at {exp.company} ({exp.start_date.strftime('%Y-%m-%d')} - {end_date})"
            story.append(Paragraph(exp_header, styles['Normal']))
            story.append(Paragraph(exp.description, styles['Normal']))
            story.append(Spacer(1, 6))
    
    # Education
    if resume.education.exists():
        story.append(Paragraph("EDUCATION", heading_style))
        for edu in resume.education.all():
            end_date = "Present" if edu.is_current else edu.end_date.strftime("%Y-%m-%d")
            edu_header = f"<b>{edu.degree}</b> from {edu.institution} ({edu.start_date.strftime('%Y-%m-%d')} - {end_date})"
            story.append(Paragraph(edu_header, styles['Normal']))
            if edu.grade:
                story.append(Paragraph(f"Grade: {edu.grade}", styles['Normal']))
            story.append(Spacer(1, 6))
    
    # Skills
    if resume.skills.exists():
        story.append(Paragraph("SKILLS", heading_style))
        skills_data = []
        for skill in resume.skills.all():
            skills_data.append([skill.name, skill.proficiency.title()])
        
        skills_table = Table(skills_data, colWidths=[3*inch, 2*inch])
        skills_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(skills_table)
    
    doc.build(story)
    buffer.seek(0)
    return buffer

def generate_pdf_weasyprint(resume):
    html_string = render_to_string('resume_builder/resume_pdf_template.html', {'resume': resume})
    
    html = weasyprint.HTML(string=html_string)
    pdf_buffer = BytesIO()
    html.write_pdf(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer