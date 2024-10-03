from flask import Flask, request, send_file
from transformers import pipeline
import PyPDF2
from io import BytesIO

app = Flask(__name__)

# Configurando o pipeline de simplificação de texto
simplify_pipeline = pipeline("text2text-generation", model="t5-small")

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def generate_adapted_text(text):
    # Sugestão de prompt: simplificar o texto para crianças com dificuldades de aprendizagem
    prompt = f"Simplifique o seguinte texto para uma criança com atraso de aprendizagem: {text}"
    result = simplify_pipeline(prompt, max_length=500)
    return result[0]['generated_text']

def create_pdf_from_text(text):
    pdf_buffer = BytesIO()
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_blank_page(width=210, height=297)
    with open("/tmp/adapted_output.pdf", "wb") as f:
        pdf_writer.write(f)
    return "/tmp/adapted_output.pdf"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado", 400

    file = request.files['file']
    original_text = extract_text_from_pdf(file)

    adapted_text = generate_adapted_text(original_text)
    adapted_pdf_path = create_pdf_from_text(adapted_text)

    return send_file(adapted_pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
