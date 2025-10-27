from google import genai
from google.genai import types
from google.genai.errors import APIError
from django.conf import settings
from django.core.cache import cache
import json
import re

client = genai.Client(api_key=settings.GEMINI_API_KEY)


# TODO fix cache not saving betwen project restarts

def geminiCronicIssues(car_model: str):

    # cache
    car_safe = re.sub(r'[^a-zA-Z0-9]', '_', car_model)
    cache_key = f"car_issues_{car_safe}"
    cached = cache.get(cache_key)
    if cached:
        print(f"{cache_key} cached")
        return cached

    prompt = (
        f"Lista JSON dos problemas crónicos mais comuns do {car_model}, "
        f"com nome do problema, descrição curta e quilometragem média. "
        f"Responde em português de Portugal."
    )

    schema = types.Schema(
        type=types.Type.ARRAY,
        items=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "problema": types.Schema(type=types.Type.STRING),
                "descricao": types.Schema(type=types.Type.STRING),
                "media_km": types.Schema(type=types.Type.INTEGER)
            },
            required=["problema", "descricao", "media_km"]
        )
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.3,
                response_mime_type="application/json",
                response_schema=schema
            )
        )

        if response.text is None:
            return None

        data = json.loads(response.text)

        # data = {"message": "Hello", "status": "success"}

        cache.set(cache_key, data, timeout=87000)  # cache 1 dia?
        return data

    except (APIError, json.JSONDecodeError) as e:
        print(f"Gemini error: {e}")
        return None
