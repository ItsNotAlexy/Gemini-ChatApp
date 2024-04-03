import requests, json, os
import google.generativeai as genai


def get_gemini_response(text):
    genai.configure(api_key=os.environ['gemini'])

    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]

    model = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config=generation_config,
        safety_settings=safety_settings,
    )

    convo = model.start_chat(
        history=[
            {"role": "user", "parts": ["Hello, How are you?"]},
            {"role": "model", "parts": ["I'm good, how are you?"]},
        ]
    )
    try:
        convo.send_message(text)
        return convo.last.text
    except genai.types.BlockedPromptException:
        return "Sorry, For safety reasons I can't respond to that."
