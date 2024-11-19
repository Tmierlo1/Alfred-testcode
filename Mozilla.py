import os
import time
from TTS.api import TTS

def generate_audio_files_with_timing():
    # Tekst die je wilt omzetten naar spraak
    text_list = [
        "Hallo! Hoe was je dag vandaag? Wat kan ik voor je doen?",
        "Het snelst groeiende gras ter wereld is bamboe, dat wel één meter per dag kan groeien.",
        "De trein vertrekt over 5 minuten. Zorg dat je op tijd bent.",
        "De regenboog heeft zeven kleuren: rood, oranje, geel, groen, blauw, indigo en violet.",
        "Kun jij de röntgenfoto’s van meneer De Jong analyseren?",
    ]

    # Gebruik een pretrained Mozilla TTS-model
    model_name = "tts_models/nl/css10/vits"  # Vervang met een geschikt Nederlands model als beschikbaar
    tts = TTS(model_name)

    # Bestanden opslaan in dezelfde map als het script
    script_folder = os.path.dirname(os.path.abspath(__file__))

    # Tijdmetingen opslaan
    generation_times = []

    # Door de tekst itereren en audiobestanden genereren
    for i, sentence in enumerate(text_list):
        output_path = os.path.join(script_folder, f"output_{i + 1}.wav")
        print(f"Genereren van audio voor zin {i + 1}: {sentence}")

        # Start timer
        start_time = time.time()

        # Audio genereren
        tts.tts_to_file(text=sentence, file_path=output_path)

        # Stop timer
        end_time = time.time()
        generation_time = end_time - start_time
        generation_times.append(generation_time)

        print(f"Bestand opgeslagen: {output_path}")
        print(f"Tijd voor generatie van zin {i + 1}: {generation_time:.2f} seconden")

    # Gemiddelde berekenen
    average_time = sum(generation_times) / len(generation_times)
    print(f"\nGemiddelde tijd voor alle generaties: {average_time:.2f} seconden")

if __name__ == "__main__":
    generate_audio_files_with_timing()
