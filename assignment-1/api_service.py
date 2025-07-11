from fastapi import FastAPI
from pydantic import BaseModel
import cohere
import uvicorn

# Replace with your actual key
COHERE_API_KEY = "wAxVCab3xnABNI8EkReLEtEa7tnPUAiF7srUPoFC"
co = cohere.Client(COHERE_API_KEY)

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/extract")
def extract_metadata(req: TextRequest):
    prompt = f"""
You are an intelligent assistant trained to extract metadata from legal agreement documents.
Extract the following fields:
- agreement_value
- start_date
- end_date
- renewal_notice_days
- party_one
- party_two

Input:
{req.text}

Output as JSON:
"""

    try:
        response = co.generate(
            model="command-r-plus",
            prompt=prompt,
            max_tokens=300,
            temperature=0.2
        )
        return {"metadata": response.generations[0].text.strip()}
    except Exception as e:
        return {"error": str(e)}
