[<img src="assets/evc_banner_wide.png" alt="Especialização em Visão Computacional | https://sigmoidal.ai)" title="Especialização em Visão Computacional | https://sigmoidal.ai/en)"/>](https://sigmoidal.ai/)

<div align="center">
  
  [![Linkedin Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/carlos-melo-data-science/)](https://www.linkedin.com/in/carlos-melo-data-science/)
  [![YouTube Badge](https://img.shields.io/badge/YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@CarlosMeloSigmoidal)
  [![Instagram Badge](https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/carlos_melo.py)
  [![Twitter Badge](https://img.shields.io/twitter/follow/:carlos_melo_py)](https://twitter.com/carlos_melo_py)

  
</div>

# Especialização em Visão Computacional

Este repositório contém códigos, notebooks e materiais educativos relacionados à Especialização em Visão Computacional, um treinamento criado por Carlos Melo (Sigmoidal). Abrangendo uma variedade de aplicações e técnicas de visão computacional, os notebooks tutoriais oferecem demonstrações práticas e desafiam os usuários a completar certos exercícios. Para garantir a funcionalidade e execução adequada, recomendamos a criação de um ambiente local com as dependências necessárias, conforme instruções fornecidas abaixo.


# Sobre o Instrutor
<p align="left">
Sou um <strong>Engenheiro de Visão Computacional</strong> com formação em Ciências Aeronáuticas pela Academia da Força Aérea e possuo um <strong>Mestrado em Engenharia Aeroespacial</strong> pelo Instituto Tecnológico de Aeronáutica (ITA). Em 2019, fundei a Sigmoidal, uma empresa especializada em consultoria em CV&ML e programas de treinamento imersivos. Até o momento, já eduquei mais de 6.000 alunos em Machine Learning e Visão Computacional.
</p>
<br>

# Configure e Gerencie Seu Ambiente com Poetry

De acordo com a [documentação](https://python-poetry.org/docs/) do Poetry :

> Poetry é uma ferramenta de gerenciamento de pacotes open source para Python que permite declarar as bibliotecas dependentes de um projeto e que gerenciará (instalará/atualizará) essas dependências. Ele funciona no Linux, OS X e Windows.

## Visão Geral
O uso do Poetry consiste nas seguintes etapas:

1. Instale o [Poetry](https://python-poetry.org/docs/#installation) em seu computador.
2. Clone o repositório e instale as dependências.

## 1. Instalação


**Baixe** e instale o Poetry:

| Sistema Operacional | Comando de Instalação |
|---------------------|-----------------------|
| OS X / Linux | `curl -sSL https://install.python-poetry.org \| python -` |
| Windows (PowerShell) | `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content \| python -` |

Mais detalhes sobre a instalação podem ser encontrados [aqui](https://python-poetry.org/docs/#installation).


## 2. Clonando o repositório e instalando as dependências

Primeiro, clone o projeto:

```bash
git clone https://github.com/carlosfab/visao-computacional.git
```

Em seguida, navegue até a pasta do projeto:

```bash
cd visao-computacional
```

E, por fim, instale todas as dependências necessárias usando o Poetry:

```bash
poetry install
```