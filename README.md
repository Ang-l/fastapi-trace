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
<img width="3408" height="962" alt="image" src="https://github.com/user-attachments/assets/cfeafdff-b63b-416a-ae9f-892eb682f4ca" />
