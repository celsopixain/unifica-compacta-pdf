import io
from pypdf import PdfWriter
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Unificador e Compressor de PDF",
    page_icon="📄",
    layout="centered",
)

st.title("📄 Unificador e Compressor de PDF")
st.write("Suba seus arquivos e processe-os localmente com total privacidade.")
st.write("Desenvolvido por Celso Ricardo de Albuquerque - [LinkedIn](https://www.linkedin.com/in/celso-albuquerque/)")


# Criação das abas para separar as funções
aba1, aba2 = st.tabs(["Juntar PDFs", "Reduzir Tamanho"])

# --- ABA 1: JUNTAR PDFS ---
with aba1:
    st.header("Juntar PDFs")
    arquivos_juntar = st.file_uploader(
        "Selecione os PDFs que deseja unir",
        type=["pdf"],
        accept_multiple_files=True,
        key="uploader_juntar",
    )

    if arquivos_juntar:
        st.write(f"📎 **{len(arquivos_juntar)} arquivo(s) selecionado(s):**")

        # Exibe a ordem e permite que o usuário veja como vai ficar
        for i, arquivo in enumerate(arquivos_juntar):
            st.text(f"{i+1}. {arquivo.name}")

        nome_final = st.text_input(
            "Nome do arquivo final", value="PDF_Unificado.pdf"
        )

        if st.button("Unificar Arquivos", type="primary"):
            try:
                # Usando o PdfMerger que você já tem (ou o fallback para PdfWriter se der erro)
                try:
                    merger = PdfMerger()
                except Exception:
                    merger = PdfWriter()

                for arquivo in arquivos_juntar:
                    merger.append(arquivo)

                # Salva em memória para o usuário baixar
                output = io.BytesIO()
                merger.write(output)
                merger.close()

                st.success("🎉 PDFs unidos com sucesso!")

                # Botão de download nativo do Streamlit
                st.download_button(
                    label="📥 Baixar PDF Unificado",
                    data=output.getvalue(),
                    file_name=nome_final,
                    mime="application/pdf",
                )
            except Exception as e:
                st.error(f"Ocorreu um erro ao juntar os arquivos: {e}")

# --- ABA 2: REDUZIR TAMANHO ---
with aba2:
    st.header("Reduzir Tamanho")
    arquivo_reduzir = st.file_uploader(
        "Selecione o PDF para comprimir", type=["pdf"], key="uploader_reduzir"
    )

    if arquivo_reduzir:
        st.write(f"📄 Arquivo: **{arquivo_reduzir.name}**")

        # Slider para escolher a qualidade
        qualidade = st.slider(
            "Qualidade das imagens (menor = arquivo mais leve)",
            min_value=10,
            max_value=100,
            value=50,
            step=5,
        )

        if st.button("Reduzir Tamanho", type="primary"):
            try:
                with st.spinner("Comprimindo arquivo..."):
                    # Lê o arquivo enviado
                    writer = PdfWriter(clone_from=arquivo_reduzir)

                    # Comprime conteúdos e imagens (como fizemos antes)
                    for page in writer.pages:
                        page.compress_content_streams()
                        for img in page.images:
                            try:
                                img.replace(img.image, quality=qualidade)
                            except Exception:
                                pass

                    output_red = io.BytesIO()
                    writer.write(output_red)

                    st.success("🎉 Arquivo comprimido com sucesso!")

                    st.download_button(
                        label="📥 Baixar PDF Reduzido",
                        data=output_red.getvalue(),
                        file_name=f"reduzido_{arquivo_reduzir.name}",
                        mime="application/pdf",
                    )
            except Exception as e:
                st.error(f"Ocorreu um erro ao reduzir o arquivo: {e}")