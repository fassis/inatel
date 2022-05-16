# inatel

## Inatel Teste Técnico
## Gestão de Unidades Básicas de Saúde e Dados diários de Covid 19 no Brasil

## Requisitos
1. Django >= 3.2
2. Python >= 3.8
3. PostgresSQL >= 9.4

## Deploy com Docker
0. Tenha o Docker plenamente instalado e configurado

1. Clone o repositório.
```console
git clone https://github.com/fassis/inatel.git inatel
cd inatel
```

2. Rode o comando do docker-composer
```console
docker-compose up -d
```

3. Acesse a aplicação na porta 8000. 
A aplicação já terá criado um superusuário com as credenciais:
login: admin
senha: admin
```console
http://localhost:8000
```

As informações e conteúdos desta aplicação são apenas para fins de demonstrações técnicas
Portanto não dispõe de dados sensíveis de terceiros.