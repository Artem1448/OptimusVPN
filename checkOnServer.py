from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def auth():
    return HTMLResponse(content="Всё гуд!")

@app.post("/yoomoney")
async def receive_payment(
    request: Request,
    notification_type: str = Form(...),
    operation_id: str = Form(...),
    amount: str = Form(...),
    currency: str = Form(...),
    datetime: str = Form(...),
    sender: str = Form(...),
    codepro: str = Form(...),
    label: str = Form(...),
    sha1_hash: str = Form(...),
):
    with open("payments.txt", "a", encoding="UTF-8") as file:
        file.write(f"{amount} - {label} - {datetime}\n")

    return 0
