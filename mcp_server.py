from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
import asyncio
import json

app = FastAPI()

# Permitir chamadas de qualquer origem (ideal para desenvolvimento e testes com n8n)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/mcp")
async def mcp_endpoint(request: Request):
    body = await request.json()
    input_text = body.get("input", "")

    # Função geradora de resposta SSE
    async def gerar_resposta():
        await asyncio.sleep(0.1)  # Evita envio imediato antes da conexão estabilizar
        yield {
            "event": "resposta",
            "data": json.dumps({
                "output": f"✅ Você disse: '{input_text}' — resposta simulada do MCP."
            })
        }

    return EventSourceResponse(gerar_resposta())
