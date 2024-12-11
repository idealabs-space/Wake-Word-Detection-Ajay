import pvporcupine
import sounddevice as sd
from dotenv import load_dotenv
import os

load_dotenv()
access_key = os.getenv("PICOVOICE_ACCESS_KEY")

def main():
    try:
        # Path to your custom wake word file
        custom_keyword_path = "D:\\Wake Word Detection\\hey-ajay_en_windows_v3_0_0.ppn"  # Replace with the path to your .ppn file

        # Initialize Porcupine with your custom wake word
        porcupine = pvporcupine.create(
            access_key=os.getenv("PICOVOICE_ACCESS_KEY"),  # Replace with your Picovoice Access Key
            keyword_paths=[custom_keyword_path],  # Use the custom wake word
            sensitivities=[0.8]  # Adjust sensitivity if needed
        )

        print("Listening for custom wake word...")

        # Define the audio callback function
        def audio_callback(indata, frames, time, status):
            if status:
                print(f"Status: {status}")
            pcm = indata[:, 0].astype('int16')  # Convert audio to the required format
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Custom wake word detected!")

        # Start audio stream
        with sd.InputStream(
            channels=1,
            samplerate=porcupine.sample_rate,
            blocksize=porcupine.frame_length,
            dtype="int16",
            callback=audio_callback
        ):
            print("Press Enter to stop...")
            input()  # Keep the script running until user presses Enter

    except pvporcupine.PorcupineInvalidArgumentError as e:
        print(f"PorcupineInvalidArgumentError: {str(e)}")
    except pvporcupine.PorcupineActivationError as e:
        print(f"PorcupineActivationError: {str(e)}")
    except pvporcupine.PorcupineActivationLimitError as e:
        print(f"PorcupineActivationLimitError: {str(e)}")
    except pvporcupine.PorcupineActivationRefusedError as e:
        print(f"PorcupineActivationRefusedError: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        if porcupine:
            porcupine.delete()

if __name__ == "__main__":
    main()
