# InclusiveEdu

InclusiveEdu é um projeto que transforma PDFs de material didático em uma versão adaptada para crianças com atraso de aprendizagem. O projeto utiliza uma interface web em Angular e um serviço back-end em Python, que faz uso de modelos de IA do Hugging Face para simplificar o conteúdo.

## Estrutura do Projeto

- **frontend/**: Aplicação Angular responsável pelo upload do PDF e exibição do PDF processado.
- **backend/**: Serviço REST em Python que recebe o PDF, processa o conteúdo com um modelo de IA, e retorna o PDF adaptado.

## Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/edu-adapt.git
   ```

2. Siga as instruções nas pastas `frontend/` e `backend/` para rodar o projeto.

## Tecnologias Utilizadas

- **Angular** (Frontend)
- **Python** (Backend)
- **Hugging Face Transformers** para IA
- **PyPDF2** para manipulação de PDFs

## Contribuição

Contribuições são bem-vindas! Por favor, crie um _pull request_ ou abra uma _issue_ para discutir mudanças.
