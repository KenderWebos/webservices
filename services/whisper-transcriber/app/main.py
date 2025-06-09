from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import whisper
import tempfile

app = FastAPI()
model = whisper.load_model("small")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def form():
    return """
    <html>
        <head>
            <title>Transcriptor de Audio</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }
                h2 {
                    color: #333;
                }
                form {
                    margin: 20px 0;
                    padding: 20px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                }
                input[type="submit"] {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #45a049;
                }
                pre {
                    background-color: #f5f5f5;
                    padding: 15px;
                    border-radius: 5px;
                    white-space: pre-wrap;
                }
                a {
                    color: #4CAF50;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <h2>Transcriptor de Audio</h2>
            <form action="/transcribe" enctype="multipart/form-data" method="post">
                <input type="file" name="file" accept="audio/*">
                <input type="submit" value="Transcribir">
            </form>
        </body>
    </html>
    """

@app.post("/transcribe", response_class=HTMLResponse)
async def transcribe(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        result = model.transcribe(tmp.name, language="Spanish")
    return f"""
    <html>
        <head>
            <title>Resultado de la Transcripción</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                h3 {{
                    color: #333;
                }}
                pre {{
                    background-color: #f5f5f5;
                    padding: 15px;
                    border-radius: 5px;
                    white-space: pre-wrap;
                }}
                a {{
                    color: #4CAF50;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            <h3>Texto transcrito:</h3>
            <pre>{result['text']}</pre>
            <br>
            <a href='/'>Volver</a>
        </body>
    </html>
    """ 