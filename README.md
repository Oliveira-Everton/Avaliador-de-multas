# Avaliador-de-multas
  - Criando um avaliador de multas

https://hackmd.io/ce0sYTdATrGaeGGm8iWDFA?edit

## Requisitos
- [Python 3.11.0](https://www.python.org/downloads/release/python-3110/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

## Para contribuir

Todos os comandos devem ser rodados dentro do `Pipenv`

### Configurando o projeto para desenvolvimento
Para começar instale as dependências do projeto rodando
```
pipenv install --dev
```
Verifique se consegue rodar os testes
```
pipenv run python -m unittest
```

### Rodando o Lint
```
pylama
```

### Rodando os testes
```
python -m unittest
```

### Cobertura dos testes
Rode os testes
```
coverage run -m unittest
```
Para Mostrar o resultado rode
```
coverage report
```
