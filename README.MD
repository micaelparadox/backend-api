### Requirements

```bash
$ pip install -r requirements.txt
```
### Extra Infos

```bash
export FLASK_ENV=development
```

```bash
cd ./src && flask run
```
### Generate an specific Migration

```bash
$ flask db init
$ flask db migrate
```
### Db reversion to a previous version

```bash
$ flask db downgrade
```
```bash
$ flask db revision --rev-id ('someID of reversion') 
```