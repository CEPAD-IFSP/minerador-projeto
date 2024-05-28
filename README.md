# minerador-projeto

Scripts para puxar automaticamente as issues e dados do andamento do projeto via repositório

## Funcionamento

Utiliza python e a api do github para coletar as informações e salvar em um arquivo. 

## Para executar

* Python >= 3.10
* Bibliotecas do requirements.txt
* arquivo .env com informações sobre o repositório (sensíveis e não versionadas).
Exemplo de .env
```shell
GITHUB_TOKEN=your_github_token_here
REPO_OWNER=repo_owner
REPOS=REPO_NAME_1, REPO_NAME_2, REPO_NAME_3
```

Com estes requisitos, execute o arquivo principal:

```shell
python main.py
```

## TODO

* Salvar arquivo em bucket do GCS para automações.
* Github actions para rotar automaticamente o script diariamente.
* Ler diretamenteo o projects e não o repositório (estudar possibilidade). 