### Requirements

```bash
$ pip install -r requirements.txt
```
### Enable debugger

```bash
export FLASK_ENV=development
```

```bash
cd ./src && flask run
```

### Extra Info

```bash
flask db init: ele criará a pasta de migrações com uma subpasta de versão.
flask db migrate: ele detectará as alterações desse modelo com uma configuração de lógica de upgrade e downgrade.
flask db upgrade: ele aplicará as mudanças de modelo que você implementou.
flask db downgrade: se algo der errado, você pode usar este comando para não aplicar as alterações feitas no arquivo de modelo.
```