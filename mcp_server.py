from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
import json
import asyncio

app = FastAPI()

@app.post("/mcp")
async def mcp_endpoint(request: Request):
    body = await request.json()
    input_text = body.get("input", "")

    async def gerar_resposta():
        yield {
            "event": "resposta",
            "data": json.dumps({
                "output": f"Você disse: {input_text} — aqui está sua resposta simulada do MCP."
            })
        }
        await asyncio.sleep(0.1)

    return EventSourceResponse(gerar_resposta())
