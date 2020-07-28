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
* Modelagem de dados: utilizar o [Ming ODM](https://ming.readthedocs.io/en/latest/index.html) (veja [este artigo](https://www.mongodb.com/blog/post/using-the-python-toolkit-ming-to-accelerate-your) em inglês para maiores explicações), para obter uma forma de `ODM` (Object-Document Mapping) leve e baseada na estrutura do `SQLAlchemy` para mapear `collections` para `Models`, validar estruturas de documentos e um conceito de transações em memória chamado `Unit of Work`.
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

