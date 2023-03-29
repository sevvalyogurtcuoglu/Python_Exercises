import os
import openai
openai.organization = "org-12hWpUBS4PNGE3MxDw6t9XIW"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()