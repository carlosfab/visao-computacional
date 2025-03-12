# API de Processamento de Imagens com AWS API Gateway e Lambda

Este guia fornece instruções passo a passo sobre como criar e configurar uma API de processamento de imagens usando AWS API Gateway e Lambda com Python.

## Configuração Inicial na AWS

Se você ainda não tem uma, crie uma nova conta na AWS. Você precisará ter acesso à AWS a partir do seu ambiente local. Instale a AWS CLI seguindo as instruções disponíveis em [Instalando a AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) e configure-a com seu `aws_access_key_id` e `aws_secret_access_key` conforme descrito em [Configurando os Arquivos da AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

Para obter uma chave de acesso, primeiro você precisa abrir o serviço IAM, encontrar seu usuário, selecionar Credenciais de Segurança, depois atribuir um dispositivo de Autenticação Multifator (MFA) e seguir as instruções. Após configurar e verificar, você pode clicar para criar uma chave de acesso.


### Passo 1: Criar o Repositório ECR

```bash
aws ecr create-repository --repository-name <dê um nome de place holder>  --region us-east-2
```

### Passo 2: Preparar o Dockerfile

```Dockerfile
# Usando a imagem base oficial do Python 3.11 para AWS Lambda
FROM public.ecr.aws/lambda/python:3.11

# Instala as dependências necessárias
RUN pip install numpy requests opencv-python-headless Pillow

# Copia o código da função para o contêiner
COPY app.py ./

# Define o comando para executar a função lambda
CMD ["app.lambda_handler"]

```

### Passo 3: Construir a Imagem Docker

```bash
docker build -t image-deskewer .
```

### Obter Informações da AWS CLI

#### Obter o ID da Conta AWS

```bash
aws sts get-caller-identity --query "Account" --output text
```

#### Obter a Região Padrão Configurada

```bash
aws configure get region
```

### Passo 4: Autenticar no ECR

```bash
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.us-east-2.amazonaws.com
```

### Passo 5: Marcar e Enviar a Imagem para o ECR

```bash
docker tag image-deskewer:latest <your-account-id>.dkr.ecr.us-east-2.amazonaws.com/image-deskewer-repo:latest
docker push <your-account-id>.dkr.ecr.us-east-2.amazonaws.com/image-deskewer-repo:latest
```

### Passo 6: Criar a Função Lambda

```bash
aws lambda create-function --function-name ImageDeskewerFunction --package-type Image --code ImageUri=<your-account-id>.dkr.ecr.us-east-2.amazonaws.com/image-deskewer-repo:latest --role arn:aws:iam::<your-account-id>:role/<your-lambda-execution-role> --region us-east-2
```

E é isso! Você criou uma função Lambda que executa o código no ambiente definido pela imagem Docker que você construiu e enviou para o Amazon ECR.
