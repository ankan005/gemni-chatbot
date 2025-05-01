# search.py

from vertexai.preview import generative_models
import vertexai

import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="xenon-notch-457918-a7", location="us-central1")  # <-- Must set location!

def search_gemini(prompt):
    model = GenerativeModel("gemini-1.5-pro")
    responses = model.generate_content(
        prompt,
    )
    return responses.text
