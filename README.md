
# Animal image detection


## Install requirements
```shell
pip install -r requirements.txt
```

## Get model and training data
```shell
dvc pull
```

## Start flask app
```shell
flask --app main run
```

## Start flask app (docker option)
```shell
docker compose up
```

## Training and creating a model

- Run the training file
```shell
python training.py
```
