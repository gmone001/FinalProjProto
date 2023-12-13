import os
import ssl
from mtranslate import translate
# using mstranslate library since it is free and does not require an API key
import speech_recognition as sr
from transformers import pipeline

# Set the REQUESTS_CA_BUNDLE environment variable to the path of the certificate file
os.environ["REQUESTS_CA_BUNDLE"] = "cacert.pem"

# Disable SSL certificate verification (not recommended for production) - this is not needed if you are using the mtranslate library
ssl._create_default_https_context = ssl._create_unverified_context

def perform_translation(text, target_language):
    translation = translate(text, target_language)
    return translation

def main():
    # Get user input for the text to be translated
    text_to_translate = input("Enter the text in English to translate to Spanish: ")

    # Ensure the input is not empty
    if not text_to_translate:
        print("Input text cannot be empty. Exiting.")
        return

    target_language = 'es'  # Target language is Spanish for testing and project purposes

    translation = perform_translation(text_to_translate, target_language)
    print(f"Translation: {translation}")

if __name__ == "__main__":
    main()