# Guia de Implantação

Este diretório contém os pacotes prontos para implantação de cada um dos 4 sites. Cada pasta deve ser copiada para o seu respectivo repositório no GitHub.

## Sites Preparados:

1.  **site-data-savings**: A versão completa do "The Data Savings Act".
2.  **site-dsa**: A versão "Treaty of Detroit" do DSA.
3.  **site-dw-ai**: Landing page do DrumWave AI.
4.  **site-idr**: Site do International Data Reserve.

## Como implantar:

1.  Crie um novo repositório no GitHub para o site.
2.  Copie todo o **conteúdo** da pasta correspondente (ex: `site-idr/*`) para a raiz do seu novo repositório.
3.  O deploy será automático se você tiver o Coolify ou GitHub Pages configurado para monitorar esse repositório.
4.  Cada pasta já inclui:
    *   `index.html`: O arquivo principal na raiz.
    *   `assets/` ou `Imagens/`: Apenas os arquivos necessários para aquele site específico.
    *   `Dockerfile`: Configurado para rodar um servidor Nginx leve.
    *   `.gitignore`: Para evitar arquivos temporários.

## Limpeza realizada:
Todos os arquivos desnecessários, scripts de automação antigos e backups foram removidos para garantir que você tenha apenas o código de produção limpo.
