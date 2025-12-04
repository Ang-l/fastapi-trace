from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor


def init_tracer(app, service_name="fastapi-demo-service", endpoint="http://localhost:4317"):
    """
        Initialize OpenTelemetry Tracer and automatically inject link tracing into FastAPI and Requests
        Args:
        App: FastAPI instance
        Service_name: Service Name
        Endpoint: OTLP receiver
    """

    resource = Resource(attributes={"service.name": service_name})

    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    otlp_exporter = OTLPSpanExporter(endpoint=endpoint)
    provider.add_span_processor(BatchSpanProcessor(otlp_exporter))

    # Automatic injection of link tracking
    FastAPIInstrumentor().instrument_app(app)
    RequestsInstrumentor().instrument()

    print(f"[OTEL] tracing initialized → {service_name}, exporter={endpoint}")


def get_trace_id():
    """get traceId"""
    span = trace.get_current_span()
    ctx = span.get_span_context()
    return format(ctx.trace_id, '032x')
















