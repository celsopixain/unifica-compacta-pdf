# 📄 Unificador e Compressor de PDF

Uma aplicação web local, rápida e privativa construída em Python para manipulação de arquivos PDF. Com este projeto, você pode unir vários documentos ou reduzir o peso de arquivos muito grandes sem precisar enviar seus dados para servidores de terceiros.

---

## 🚀 Funcionalidades

* **Juntar PDFs**: Selecione múltiplos arquivos PDF e una-os em um único documento sequencial.
* **Reduzir Tamanho**: Compacta os fluxos de dados e reduz a qualidade de imagens embutidas para encolher o tamanho (MB) do arquivo.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.13**
* **Streamlit**: Para a criação da interface web interativa.
* **pypdf**: Para a manipulação, união e compressão dos arquivos.
* **Pillow**: Suporte necessário para a extração e compressão de imagens dentro do PDF.

---

## 📥 Instalação

Como o Windows pode apresentar múltiplos caminhos de instalação para o Python, utilize o caminho direto do executável no terminal para garantir que as bibliotecas sejam instaladas no local correto.

Abra o seu terminal (Prompt de Comando ou Git Bash) e execute o comando abaixo:

```bash
C:/Python313/python.exe -m pip install streamlit pypdf pillow