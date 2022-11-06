# Trabalho 2 - SmartOffice

## Requisitos
- Docker
- Python 3

## Preparando ambiente
1. Rode o RabbitMQ via Docker:
``` 
docker-compose up -d
```

2. Instale as dependências:
```
pip install -r requirements.txt
```

3. Rode os arquivos correspondentes aos devices, isto é:
- _AirConditioner.py_
- _Humidifier.py_
- _Lamp.py_

4. Execute o _HomeAssistant.py_
5. Finalmente execute a aplicação cliente _client.py_