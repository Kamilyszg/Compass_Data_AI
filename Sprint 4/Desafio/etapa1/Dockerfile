# versao da imagem-base, será utilizada para dar origem a minha imagem
FROM python:3.9.21-slim 

# definindo diretório da imagem: subdiretório app
WORKDIR /app

# copia o arquivo da aplicação para minha imagem/ diretório de trabalho
COPY carguru.py .

# comandos que serão realizados na iniciação do container
CMD ["python", "carguru.py"]