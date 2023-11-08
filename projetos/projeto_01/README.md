# Projeto 01 - Substituição de Fundo Verde em Vídeos (Chroma Key)

Este script substitui o fundo verde em um vídeo (chroma key) por um vídeo ou imagem de fundo selecionada.

## Instalação

```bash
git clone https://github.com/carlosfab/visao-computacional.git
cd visao-computacional/projetos/projeto_01/
pip install -r requirements.txt
```

## Como Usar

Para usar o script, execute o seguinte comando no terminal, substituindo `<video_entrada>` pelo caminho do vídeo com o fundo verde e `<video_fundo>` pelo caminho do vídeo ou imagem que será usado como novo fundo.

```bash
python projeto_01.py -i <video_entrada> -b <video_fundo>
```

### Argumentos

* `-i`, `--input`: Caminho para o vídeo de entrada com fundo verde.
* `-b`, `--background`: Caminho para o vídeo ou imagem de fundo que substituirá o fundo verde.

## Contato

Este repositório faz parte do programa de [Especialização em Visão Computacional](https://escola.sigmoidal.ai/especializacao-em-visao-computacional). Para dúvidas, sugestões ou feedbacks:

> **Carlos Melo** - [Contato](https://sigmoidal.ai/contato/)
