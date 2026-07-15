import gradio as gr
import requests
FastAPI_URL = "http://localhost:8000/chat"
def chat(user_code):

    try:
        response = requests.post(
            FastAPI_URL,
            json={"debug": user_code},
            timeout=60
        )

        if response.status_code == 200:
            return response.json()["answer"]

        return f"Error: {response.status_code}\n{response.text}"

    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to FastAPI server.\nMake sure the backend is running."

    except Exception as e:
        return f"Unexpected Error:\n{str(e)}"
demo = gr.Interface(fn=chat, inputs="text", outputs="text", title="Code Debugger")
demo.launch()