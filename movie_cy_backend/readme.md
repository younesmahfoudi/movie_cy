## Installation

Install fastapi with lite server in a docker

```bash
  cd movie_cy_api
  docker build -t moviecyapi .
  docker run -d --name apicontainer -p 81:81 moviecyapi
```

Install in dev

```bash
  cd movie_cy_api
  source .venv/bin/activate
  export PYTHONPATH=$PWD
  pip install -r requirements.txt
  python app/main.py
```
    
## Demo

swagger : http://127.0.0.1:81/docs

## Documentation

[Documentation fastapi docker](https://fastapi.tiangolo.com/deployment/docker/)
