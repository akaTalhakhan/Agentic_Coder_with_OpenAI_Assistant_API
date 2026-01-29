from openai import OpenAI
import google.generativeai as genai
from typing import List, Dict, Any


def get_ai_response(prompt: str, api_key: str, model: str) -> str:
    """Get response from AI model"""
    try:
        if "ChatGPT" in model or "GPT" in model:
            return get_openai_response(prompt, api_key, model)
        elif "Gemini" in model:
            return get_gemini_response(prompt, api_key)
        else:
            return "Model not supported yet. Please select ChatGPT or Gemini."
    except Exception as e:
        return f"Error: {str(e)}"


def get_openai_response(prompt: str, api_key: str, model: str) -> str:
    """Get response from OpenAI models using the new v1.0+ API"""
    try:
        client = OpenAI(api_key=api_key)

        model_map = {
            "ChatGPT-4o": "gpt-4o",
            "ChatGPT-4": "gpt-4",
            "GPT-3.5-Turbo": "gpt-3.5-turbo",
            "ChatGPT": "gpt-3.5-turbo",
        }

        response = client.chat.completions.create(
            model=model_map.get(model, "gpt-3.5-turbo"),
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert programming assistant. Provide detailed, accurate, and well-formatted responses using markdown. Focus on code quality, best practices, and comprehensive analysis.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
            max_tokens=4000,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"OpenAI API Error: {str(e)}"


def get_gemini_response(prompt: str, api_key: str) -> str:
    """Get response from Google Gemini"""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")

        response = model.generate_content(
            f"You are an expert programming assistant. Provide detailed, accurate, and well-formatted responses using markdown. Focus on code quality, best practices, and comprehensive analysis.\n\nPrompt: {prompt}"
        )
        return response.text
    except Exception as e:
        return f"Gemini API Error: {str(e)}"
