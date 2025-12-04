from fastapi import FastAPI
import time, requests
from opentelemetry import trace
from otel_setup import init_tracer

from middlewares.trace_middleware import trace_id_middleware

app = FastAPI()

init_tracer(app, service_name="fastapi-demo-service")
app.middleware("http")(trace_id_middleware)


@app.get("/hello")
def hello():
    time.sleep(0.3)
    return {"msg": "Hello from FastAPI!"}


@app.get("/call-httpbin")
def call_external():
    r = requests.get("https://httpbin.org/delay/1")
    return {"status": r.status_code, "origin": "httpbin"}


@app.get("/nested")
def nested():
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span("step1"):
        time.sleep(0.2)
    with tracer.start_as_current_span("step2"):
        time.sleep(0.1)
    with tracer.start_as_current_span("step3"):
        time.sleep(0.3)
    with tracer.start_as_current_span("step4"):
        time.sleep(0.2)

    return {"msg": "Nested spans done"}