import json
from fastapi import Request
from starlette.responses import Response, StreamingResponse

from otel_setup import get_trace_id


async def trace_id_middleware(request: Request, call_next):
    response = await call_next(request)

    if isinstance(response, StreamingResponse) and not (
            response.media_type and response.media_type.startswith("application/json")
    ):
        return response

    body = b""
    async for chunk in response.body_iterator:
        body += chunk

    media_type = response.media_type or response.headers.get("content-type", "")
    if not media_type.startswith("application/json"):
        headers = dict(response.headers)
        headers.pop("content-length", None)
        return Response(
            content=body,
            status_code=response.status_code,
            headers=headers,
            media_type=response.media_type,
            background=getattr(response, "background", None),
        )

    try:
        data = json.loads(body.decode("utf-8"))
    except Exception as e:
        print('json load body decode error:', str(e))

        headers = dict(response.headers)
        headers.pop("content-length", None)
        return Response(
            content=body,
            status_code=response.status_code,
            headers=headers,
            media_type=response.media_type,
            background=getattr(response, "background", None),
        )

    if isinstance(data, dict):
        data["traceId"] = get_trace_id()
        new_body = json.dumps(data, ensure_ascii=False).encode("utf-8")
    else:
        new_body = body

    headers = dict(response.headers)
    headers.pop("content-length", None)

    return Response(
        content=new_body,
        status_code=response.status_code,
        headers=headers,
        media_type="application/json",
        background=getattr(response, "background", None),
    )