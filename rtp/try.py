import google.generativeai as genai

genai.configure(api_key="AIzaSyB3j6x74WE1pqjOVR2zLtn6Od30_MRmxp0")  # Use your API key

models = genai.list_models()
for model in models:
    print(f"Name: {model.name}")
    print(f"Description: {model.description}")
    print(f"Supported Generation Methods: {model.supported_generation_methods}")
    print("-" * 20)
