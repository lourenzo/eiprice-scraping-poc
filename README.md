# Eiprice - Teste Scraping - Lourenzo Ferreira

Solução para extrair informações do site Magazine Luiza

## Premissas

* Linguagem [python](https://www.python.org/)
* Utilizar repositório git
* API HTTP utilizando Flask
* Base de dados MongoDB
* Utilizar docker

**Tópicos qualitativos**
* Organização da solução
* Decisões de bibliotecas
* Design do código

(enunciado completo no arquivo `docs/`[email.html](docs/email.html))

## Desenho da solução
* Utilizar [PEP-0008](https://www.python.org/dev/peps/pep-0008/) e [Clean Code para python](https://github.com/zedr/clean-code-python) como guia de estilo para facilitar a manutenção e portabilidade do código, entre outras vantagens.

* Separar camadas: dados (modelos e migrations), services, ferramentas (scripts) e rest api.

* Modelagem de dados:
  * Criar documentação
  * Testar viabilidade de usar o [Ming ODM](https://ming.readthedocs.io/en/latest/index.html) com o flask, fazendo binding com o [Flask-Pymongo](https://flask-pymongo.readthedocs.io/en/latest/).
  * Fallback: [Flask-MongoEngine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)

* Script de varredura do site magazine luiza
    + Momento da execução:
        - Pode ser executado fora do container para gerar um seed antes de gerar / rodar a imagem docker
        - Um script executável dentro do container (utilizar a opção de storage mapeado para uma pasta local na imagem do mongodb)
    + Utilizar [Beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) para realizar a varredura das páginas
    + Informar o status do mapeamento usando status de retorno do script
    + Erros serão mostrados no console, com sugestão de solução, por exemplo o nome das classes mudou, ou até mesmo uma mudança estrutural na página que requer refatoração do parser desta categoria.

* API RESTful feita com [Flask](https://flask.palletsprojects.com/en/1.1.x/), utilizando 
    + Endpoints: 
        - Obtenção de relatório
        - Carga de dados
            - **(opcional)** Um endpoint da API que efetua a varredura e atualiza o banco de dados.
            - **(opcional)** Um enpoint com versão dos dados da api, e status de carregamento caso esteja acontecendo

* Docker:
  + Construir imagem a partir da base [tiangolo/uwsgi-nginx-flask-docker](https://github.com/tiangolo/uwsgi-nginx-flask-docker/blob/master/docker-images/python3.8.dockerfile)
  + Criar cluster Compose:
    - Imagem do mongodb
    - Imagem da aplicação web
    - storage local para dados do mongodb


## Inicializando os containeres

**Dependências**
* Docker 19.03+
* Docker-compose 3+

```sh
docker-compose build
```
