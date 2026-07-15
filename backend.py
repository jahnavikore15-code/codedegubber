from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
app = FastAPI()
client = genai.Client(api_key="AQ.Ab8RN6JMuX74cpJ2YcfL5Kg0ZU89_J73bRTgifiQM9RUbkU7Ng")
class ChatRequest(BaseModel):
    debug: str
@app.post("/chat")
def chat(request: ChatRequest):

    prompt = f"""
You are an Expert AI Code Debugger.

Analyze the given code carefully.

Follow EXACTLY this format:

Syntax Errors:
- Mention all syntax errors.
- If none, write "No syntax errors found."

Runtime Errors:
- Mention all runtime errors.
- If none, write "No runtime errors found."

Logical Errors:
- Mention all logical errors.
- If none, write "No logical errors found."

Explanation:
- Explain every error in simple language.

Corrected Code:
- Provide the corrected code.

Final Answer:
- Summarize the debugging result.

Code:
{request.debug}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "answer": response.text
    }