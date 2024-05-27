## This example with Quickstream python library
## How to Run
### Run local Kafka
```cmd
docker-compose up -d
```

### install quickstream requirements
```cmd
pip install -r requirements.txt
```

### Produce messages
```cmd
python producer.py
```

### Consume messages
```cmd
python consumer.py
```