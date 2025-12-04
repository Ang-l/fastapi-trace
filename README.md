# fastapi-trace



## run
```
1. docker-compose up -d
2. pip install -r requirements.txt
3. uvicorn app:app --reload
```

## test
```
1. curl http://127.0.0.1:8000/hello     # {"msg": "Hello from FastAPI!, "traceId": "76432d780f617cd5a0993c63726802bc"}
2. show page http://localhost:16686/trace/76432d780f617cd5a0993c63726802bc
```