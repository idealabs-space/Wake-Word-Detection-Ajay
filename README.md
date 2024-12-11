****# Wake Word Detection with Porcupine****
---
## Overview
This repository provides a Python-based implementation for wake word detection using **Porcupine** from Picovoice. The script listens for a custom wake word using a `.ppn` file and triggers a response upon detection. It leverages **SoundDevice** for real-time audio input and **dotenv** for securely managing environment variables.

---

## Features
- Detects custom wake words defined in `.ppn` files.
- Utilizes Porcupine's on-device speech recognition.
- Adjustable sensitivity for fine-tuned detection.
- Comprehensive error handling for robust operation.

---

## Prerequisites

### Dependencies
Ensure you have the following installed:
1. **Python 3.7+**
2. Required Python libraries:
    ```bash
    pip install pvporcupine sounddevice python-dotenv
    ```

### Picovoice Access Key
1. Sign up at [Picovoice Console](https://console.picovoice.ai/).
2. Create a new project to obtain your Access Key.

### Custom Wake Word File
1. Use Picovoice Console to generate a `.ppn` file for your custom wake word.
2. Save the file locally and note its path.

---

## Setup

### Environment Variables
1. Create a `.env` file in the project directory:
    ```bash
    touch .env
    ```
2. Add your Picovoice Access Key to the `.env` file:
    ```
    PICOVOICE_ACCESS_KEY=<your_access_key>
    ```

### File Structure
Ensure the following structure:
```
project_directory/
|— main.py
|— .env
|— custom_keyword.ppn
```

---

## Usage

### Running the Script
1. Update the `custom_keyword_path` in the script to point to your `.ppn` file:
    ```python
    custom_keyword_path = "Enter you’re custom keyword path here "
    ```
2. Execute the script:
    ```bash
    python main.py
    ```
3. Speak the custom wake word to test detection.

### Stopping the Script
Press **Enter** in the terminal to gracefully stop the application.

---

## Configuration

### Sensitivity
Adjust the sensitivity parameter in the `porcupine.create` function to control detection behavior:
```python
sensitivities=[0.8]  # Values range from 0.0 to 1.0
```
- Higher values increase detection sensitivity.
- Lower values reduce false positives.

---

## Error Handling
The script includes error handling for common issues:
- **`PorcupineInvalidArgumentError`**: Invalid arguments such as an incorrect `.ppn` path or access key.
- **`PorcupineActivationError`**: Issues activating the Picovoice engine.
- **`PorcupineActivationLimitError`**: Exceeded the limit of allowed activations.
- **`PorcupineActivationRefusedError`**: Access key refused.

Ensure:
- The `.ppn` file matches your platform.
- Your Access Key is valid and active.

---

## Example Interaction
1. User sets up the script with a custom wake word `hey-ajay`.
2. When the wake word is detected, the terminal outputs:
    ```
    Custom wake word detected!
    ```

---

## Future Enhancements
- Implement audio feedback upon detection.
- Add support for multiple wake words.
- Integrate with other voice-enabled services.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Acknowledgements
- [Picovoice Documentation](https://picovoice.ai/docs/)
- [SoundDevice Documentation](https://python-sounddevice.readthedocs.io/)
- [dotenv Documentation](https://pypi.org/project/python-dotenv/)

---

