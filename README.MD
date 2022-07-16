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

```
- flask db init : it will create the migrations folder with a version subfolder.
- flask db migrate : it will detect the model changes with an upgrade and downgrade logic set up.
- flask db upgrade : it will apply the model changes you have implemented.
- flask db downgrade : if something goes wrong, you can use this command to unapply changes you have done on your model file.
s```