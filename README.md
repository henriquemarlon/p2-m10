# Módulo 10 <> Prova 2

Por trás dos panos está sendo criado um serviço chamado "service" e está sendo utilizado o nginx como proxy reverso e load balancer. Ademais, toda aplicação está virtualizada com Docker e orquestrada por um docker compose. O swagger está disponível na rota: http://localhost/docs. Ademais foi implementada uma estratégia de log que salva todos os deus registros em um arquivo .txt.

## Como rodar o sistema

Para subir a infraestrutura do NGINX junto ao serviço, rode o comando abaixo no seu terminal:

```bash
$ docker compose up
```