import speech_recognition as sr
import spacy

nlp = spacy.load('en_core_web_sm')
listener = sr.Recognizer()
recording_duration = 10

def input_audio():
    with sr.Microphone() as source:
        # Adjust the microphone sensitivity to reduce noise
        listener.adjust_for_ambient_noise(source)
        print('listening...')
        audio = listener.listen(source, phrase_time_limit=recording_duration)
        
    try:
        cmd = ""
        cmd = listener.recognize_google(audio, language='en-in', show_all=False)
        print(cmd)
        # print(type(cmd))

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return(cmd)
        
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")
        return(cmd)

    return(cmd)

def keyword_extract():
    input_text = input_audio()

    # apply the spaCy pipeline to the input text
    doc = nlp(input_text)

    # extract noun chunks from the processed document
    noun_chunks = list(doc.noun_chunks)

    # extract phrases from the processed document
    # global phrases
    # phrases = [chunk.text for chunk in doc.noun_chunks if len(chunk) > 1]

    # extract individual keywords from the processed document
    global keywords
    keywords = [token.text for token in doc if not token.is_stop and not token.is_punct and token.pos_ in ['NOUN', 'PROPN']]

    # global no_of_keywords
    # no_of_keywords = len(keywords)
    # print the results
    # print('Noun chunks:', noun_chunks)
    # print('\n')

    # print('Phrases:', phrases)
    # print('\n')

    print('Answer Key Phrases used:', keywords)

def return_keywords():
    return keywords

# keyword_extract()