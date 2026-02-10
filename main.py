from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
import math
import requests

load_dotenv()

app = FastAPI()

EMAIL = os.getenv("OFFICIAL_EMAIL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ---------------- HEALTH API ----------------
@app.get("/health")
def health():
    return {
        "is_success": True,
        "official_email": EMAIL
    }

# ---------------- UTILITY FUNCTIONS ----------------
def fibonacci(n):
    if n <= 0:
        raise ValueError("Invalid fibonacci input")
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series[:n]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def lcm_list(arr):
    lcm = arr[0]
    for num in arr[1:]:
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm

def hcf_list(arr):
    hcf = arr[0]
    for num in arr[1:]:
        hcf = math.gcd(hcf, num)
    return hcf

def ask_ai(question):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

    params = {"key": GEMINI_API_KEY}

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Answer in ONE WORD only.\n{question}"
                    }
                ]
            }
        ]
    }

    response = requests.post(url, params=params, json=payload, timeout=15)

    if response.status_code != 200:
        raise Exception(response.text)

    text = response.json()["candidates"][0]["content"]["parts"][0]["text"]

    # Clean punctuation and return one word
    return text.strip().replace(".", "").replace(",", "").split()[0]



# ---------------- BFHL API ----------------
@app.post("/bfhl")
def bfhl(payload: dict):
    try:
        if len(payload.keys()) != 1:
            raise HTTPException(status_code=400, detail="Exactly one key required")

        key, value = list(payload.items())[0]

        if key == "fibonacci":
            if not isinstance(value, int):
                raise HTTPException(status_code=400, detail="Invalid fibonacci input")
            data = fibonacci(value)

        elif key == "prime":
            if not isinstance(value, list):
                raise HTTPException(status_code=400, detail="Invalid prime input")
            data = [x for x in value if isinstance(x, int) and is_prime(x)]

        elif key == "lcm":
            if not isinstance(value, list) or len(value) < 2:
                raise HTTPException(status_code=400, detail="Invalid lcm input")
            data = lcm_list(value)

        elif key == "hcf":
            if not isinstance(value, list) or len(value) < 2:
                raise HTTPException(status_code=400, detail="Invalid hcf input")
            data = hcf_list(value)

        elif key == "AI":
            if not isinstance(value, str):
                raise HTTPException(status_code=400, detail="Invalid AI input")
            data = ask_ai(value)

        else:
            raise HTTPException(status_code=400, detail="Invalid key")

        return {
            "is_success": True,
            "official_email": EMAIL,
            "data": data
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        return {
            "is_success": False,
            "error": str(e)
        }
