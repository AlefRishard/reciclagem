# Projeto Mapa de Reciclagem - Manaus

![Capa do Projeto](URL_DA_SUA_IMAGEM_DE_CAPA_AQUI)
*Uma breve legenda para a imagem, por exemplo: "Visualização do mapa de calor dos pontos de coleta em Manaus."*

---

### Badges

![Status do Projeto](https://img.shields.io/badge/status-em%20andamento-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![Django Version](https://img.shields.io/badge/django-5.2%2B-green)

---

### Índice

* [Descrição do Projeto](#descrição-do-projeto)
* [Status do Projeto](#status-do-projeto)
* [Funcionalidades e Demonstração](#funcionalidades-e-demonstração-da-aplicação)
* [Acesso ao Projeto](#acesso-ao-projeto)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Pessoas Contribuidoras](#pessoas-contribuidoras)
* [Pessoas Desenvolvedoras](#pessoas-desenvolvedoras-do-projeto)
* [Licença](#licença)

---

## Descrição do Projeto

Este projeto é uma aplicação web geoespacial desenvolvida para mapear e visualizar pontos de coleta de reciclagem e informações relevantes sobre bairros na cidade de Manaus. O objetivo é fornecer uma ferramenta interativa para que os cidadãos possam localizar facilmente onde descartar diferentes tipos de materiais recicláveis, incentivando a prática da reciclagem na região.

---

## Status do Projeto

⌛ Em andamento

---

## Funcionalidades e Demonstração da Aplicação

#### Funcionalidades

* 🗺️ **Mapa Interativo:** Visualização de dados geográficos sobre uma base de mapa (OpenStreetMap).
* 📊 **API GeoJSON:** Endpoints para servir os dados de pontos e bairros no formato GeoJSON, permitindo a integração com outras ferramentas.
* 🖥️ **Painel Administrativo:** Interface de administração para gerenciar os dados geográficos (adicionar, editar, remover pontos).

#### Demonstração

![Demonstração da Camada de Bairros](URL_PARA_SEU_GIF_OU_SCREENSHOT_AQUI)
*Visualização da camada de bairros sobre o mapa.*

---

## Acesso ao Projeto

Siga os passos abaixo para executar o projeto localmente.

**Pré-requisitos:**
* Python 3.11+
* PostgreSQL com a extensão PostGIS ativada
* Um gerenciador de pacotes Python (como `venv`)

**Instalação:**

1.  Crie e ative o ambiente virtual:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3.  Configure as variáveis de ambiente. Crie um arquivo `.env` na raiz do projeto e adicione as credenciais do seu banco de dados:
    ```env
    SECRET_KEY=sua_chave_secreta_aqui
    DEBUG=True
    DATABASE_URL=postgis://SEU_USUARIO:SUA_SENHA@localhost:5432/SEU_BANCO
    ```

4.  Aplique as migrações para criar as tabelas no banco de dados:
    ```bash
    python manage.py migrate
    ```

5.  (Opcional) Carregue os dados iniciais (se você tiver scripts de carga):
    ```bash
    python manage.py shell
    >>> from ponto.load import run_pontos
    >>> run_pontos()
    ```

6.  Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
A aplicação estará disponível em `http://127.0.0.1:8000/`.

---

## Tecnologias Utilizadas

* **Backend:** Python, Django, GeoDjango, Django REST Framework
* **Frontend:** HTML, CSS, JavaScript, Leaflet.js, jQuery, Leaflet.heat
* **Banco de Dados:** PostgreSQL com a extensão PostGIS
* **Bibliotecas Python Adicionais:** `psycopg2-binary`, `django-leaflet`, `django-geojson`, `python-decouple`

---

## Pessoas Desenvolvedoras do Projeto

| [<img src="https://avatars.githubusercontent.com/u/44144161?s=400&v=4" width=115><br><sub>Gab</sub>](https://github.com/oliv-gabriel) |
| :---: |

---
