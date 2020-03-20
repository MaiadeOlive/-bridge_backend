# bridge_test_back

## Iniciando o projeto 

Na raiz do projeto instale o virtualenv

```
$ virtualenv -p python3 venv

```
Ative o ambiente virtual

```
$ source venv/bin/activate

```
Em caso de Windows 
(https://virtualenv.pypa.io/en/stable/userguide/)

```
> \venv\Scripts\activate

```
### Dentro do ambiente virtual

```
(venv) $ pip install flask flask-restful 

```

### Subir a aplicação

```
(venv) $ FLASK_APP=run.py FLASK_DEBUG=1 flask run

``` 

## Calculador

Projeto teste de calculo de divisores e números primos.

A aplicação recebe um numero por input no frontend e envia para o backend para os cálculos, retornando o response com os possíveis divisores e se o número é ou não primo.

### Usando Endpoint

* endpoint: /calculate/<int:num>
    
    * GET = recebe o numero como parâmetro e retorna a response

### Usando Web

* Adicione o numero ao input e clique em calcular o número, o resultado será exibido no card ao lado.

### Tecnologias

Para esta aplicação utilizei a linguagem Python com o framework Flask e importei as bibliotecas request, para as requisições, reqparse para o envio de parametros, Resource para separação das rotas para o comprimento das requisições http (recebimento dos dados e envio do resultado ao frontend)

Decidi por esta linguagem por ter sido minha primeira linguagem de programação e o Flask por ser um framework muito leve e prático.
