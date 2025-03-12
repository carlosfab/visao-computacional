# Usando a imagem base oficial do Python 3.11 para AWS Lambda
FROM public.ecr.aws/lambda/python:3.11

# Instala as dependências necessárias
RUN pip install numpy requests opencv-python-headless Pillow

# Copia o código da função para o contêiner
COPY app.py ./

# Define o comando para executar a função lambda
CMD ["app.lambda_handler"]
