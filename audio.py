import speech_recognition as so


def analyzeaudio(path):

    recognizer = so.Recognizer()
    with so.AudioFile(path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)

        analysis_result: str = analyser(text)
        return analysis_result
    except so.UnknownValueError:
        return {"error": "Could not understand audio"}
    except so.RequestError as e:
        return {"error": f"Could not request results; {e}"}


def analyser(text):

    if "emergency" in text:
        return "emergency"
    elif "important" in text:
        return "important"
    else:
        return "not important"


if __name__ == "__main__":

    path = "C:/Users/user/Desktop/gomugie/input3.wav"
    result = analyzeaudio(path)
    print("Analysis Result:", result)
