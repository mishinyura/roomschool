from fastapi import FastAPI, Request
import httpx
import os
# from yandex_cloud_ml_sdk import YCloudML

app = FastAPI()

IAM_TOKEN = 'Api-Key AQVNxRZNcABvEo2OBTSVlIRTuUP8tmLdoiULlUme' #os.getenv("YANDEX_IAM_TOKEN", "твой_IAM_токен")
FOLDER_ID = 'b1gb1uv7of5ra6hgeqgq' #os.getenv("YANDEX_FOLDER_ID", "твой_folder_id")

YANDEXGPT_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

SYSTEM_PROMPT = "Ты учитель, помогаешь ученикам решать задачи, но не решаешь за них."

PROMPT = """
Ты помощник по обучению. Твоя задача — не давать прямых ответов на задачи, а помогать ученику разобраться самому. Если ученик задает вопрос по решению, подскажи ему логику, задай наводящий вопрос или объясни общий подход, но не выдавай финальный ответ.
"""


@app.post("/ask")
async def ask_yandexgpt(request: Request):
    data = await request.json()
    user_message = data.get("question")

    payload = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.7,
            "maxTokens": 200
        },
        "messages": [
            {"role": "system", "text": SYSTEM_PROMPT},
            {"role": "user", "text": user_message}
        ]
    }

    headers = {
        "Authorization": f"{IAM_TOKEN}",
        "Content-Type": "application/json",
        "x-folder-id": FOLDER_ID
    }

    print(headers, payload)

    async with httpx.AsyncClient() as client:
        response = await client.post(YANDEXGPT_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        print(result)

    # Ответ модели находится по адресу result['result']['alternatives'][0]['message']['text']
    answer = (
        result.get('result', {})
        .get('alternatives', [{}])[0]
        .get('message', {})
        .get('text', "Извините, не удалось получить ответ.")
    )

    return {"answer": answer}