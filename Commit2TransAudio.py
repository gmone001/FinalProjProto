
# set the REQUESTS_CA_BUNDLE environment variable to the path of the certificate file
os.environ["REQUESTS_CA_BUNDLE"] = "cacert.pem"

#disable SSL certificate verification (not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context

def perform_translation(text, target_language):
    translation = translate(text, target_language)
    return translation

def get_user_input():
    #ask the user if they want to type or speak
    choice = input("Do you want to type or speak? (type/speak): ").lower()

    if choice == 'type':
        #get our user input for the text to be translated
        return input("Enter the text in English to translate to Spanish: ")
    elif choice == 'speak':
        #speech recognition to get input from the user's microphone
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Speak into the microphone...")
            audio_data = recognizer.listen(source, timeout=5)

        try:
            print("Processing audio...")
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    print("Invalid choice. Exiting.")
    return None

def main():
    text_to_translate = get_user_input()

    if text_to_translate is None:
        return

    #check the input is not empty
    if not text_to_translate:
        print("Input text cannot be empty. Exiting.")
        return

    target_language = 'es'  # Target language is Spanish

    translation = perform_translation(text_to_translate, target_language)
    print(f"Translation: {translation}")

if __name__ == "__main__":
    main()

