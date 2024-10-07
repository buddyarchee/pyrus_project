from docx import Document

def get_text_from_docx(path):
    doc = Document(path)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return {
        'statusCode': 200,
        'body': '\n'.join(full_text),
    }
''''''
print(get_text_from_docx(r'C:\folder\esotericism.docx'))
