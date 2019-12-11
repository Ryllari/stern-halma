# Stern Halma / Chinese Checkers / Damas Chinesas
Jogo desenvolvido em Python utilizando Pygame para GUI e Pyro4 para comunicação para a disciplinade Programação Paralela e Distribuída


## Como executar:
Obs: Todos os comandos abaixo devem ser executados na pasta principal do projeto
### Configurando o ambiente
Em uma máquina com Python 3.6 ou superior, execute:
```
pip install -r requirements.txt
```
Isso irá instalar os pacotes necessários.

### Definindo o namingserver
#### Localmente:
```
python -m Pyro4.naming
```

#### Em rede:
```
pyro4-ns -n your_hostname # (192.168.0.1)
```

Caso tenha interesse em listar os registros do namingserver, execute:
```
python -m Pyro4.nsc list
```


### Executando o jogo
#### Iniciando o servidor de comunicação
Para iniciar o servidor do jogo, execute em um novo terminal:
```
python server.py
```

#### Ininciando o jogo
O jogo permite apenas dois usuários por vez. Para cada usuário, execute em um terminal diferente o seguinte comando:
```
python start.py
```

Now, enjoy it! <3

## Observacoes
Requisitos do projeto: https://github.com/Ryllari/stern-halma/blob/master/ProjetoRMI.pdf

Autor: Ryllari R. M. Santana
