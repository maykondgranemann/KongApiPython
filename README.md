# KongApiPython

1- Gerar imagem do docker, no terminal:
cd api-python
docker build -f Dockerfile -t [image-name] .
ex: docker build -f Dockerfile -t api-python .

2 - Criar os conteiners do docker atraves da imagem gerada no passo 1
ex0: docker run --name "servico0" -p 5000:5000 -e "SERVICE_NAME=Servico0" -d  maykon/api-python
ex1: docker run --name "servico1" -p 5001:5000 -e "SERVICE_NAME=Servico1" -d  maykon/api-python
ex2: docker run --name "servico2" -p 5002:5000 -e "SERVICE_NAME=Servico2" -d  maykon/api-python
ex2: docker run --name "servico3" -p 5003:5000 -e "SERVICE_NAME=Servico3" -d  maykon/api-python
obs alterar o nome a porta e o valor da variavel SERVICE_NAME para cada novo container gerado

3 - Testar no navegador atraves:
http://localhost:<porta_container> 
deve aparecer o valor da variavel SERVICE_NAME
