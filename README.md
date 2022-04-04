# CRUD users


## Requisites

- python >= 3.9
- pip >= 22.0.3


## Installation

```sh
git clone https://github.com/stalinscj/crud-users-cli.git
```

```sh
cd crud-users-cli
```

```sh
pip install -r requirements.txt
```

```sh
python -m pip install pytest
```


## Running tests

```sh
pytest
```


## Running script

```sh
python main.py ACTION [create_user, read_user, update_user, delete_user] PARAMS
```

```sh
python main.py [ACTION] --help
```

## Examples

```sh
python main.py create_user --first_name Luis --last_name Cova --age 32 --email luis@email.com
```

```sh
python main.py read_user
```

```sh
python main.py read_user --id 1
```

```sh
python main.py update_user --id 1 --first_name Juan --last_name Mora --age 16 --email juan@email.com
```

```sh
python main.py delete_user --id 1
```
