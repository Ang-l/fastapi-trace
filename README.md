# fastapi-trace

使用 FastAPI 与 OpenTelemetry (OTEL) 构建一个具备完善可观测性的 Web 服务。
项目实现了端到端的分布式链路追踪功能，包括对 API 请求、内部业务逻辑、多级嵌套流程、以及外部 HTTP 调用的自动与手动埋点。同时，通过 OTLP 协议将 trace 数据上报至 Jaeger 或任意支持 OTLP 的可观测性平台。


## run  python>=3.9
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

```
1. curl http://127.0.0.1:8000/nested
# {
#  "msg": "Nested spans done",
#  "traceId": "16420495e3f29a3e5170f3f778b7652c"
#  }

2. show page http://localhost:16686/trace/16420495e3f29a3e5170f3f778b7652c
```
<img width="3416" height="1764" alt="image" src="https://github.com/user-attachments/assets/7cdabacc-c625-4f0f-b232-b6c4562b3e0f" />
