Here's a description for the GitHub repository:

---

# Tone Analysis Application

This application performs sentiment analysis on Ukrainian text, categorizing its tone as positive, negative, or neutral. It highlights words in the text based on their tone (green for positive, red for negative) and provides an overall tone score.

## Features
- **Text Tone Analysis**: Analyzes input text and determines its overall tone based on a custom dictionary.
- **Word Highlighting**: Positive words are highlighted in green, while negative words are highlighted in red.
- **Tone Categorization**: Classifies the tone of the text as "Positive", "Negative", or "Neutral" based on the overall tone score.
- **Gradio Interface**: User-friendly interface built with Gradio, allowing users to input text and see the results in real-time.

## How It Works
1. **Text Analysis**: The program uses a dictionary of words with assigned tone values (positive, negative, or neutral) to analyze the input text.
2. **Tone Calculation**: It calculates the total tone by summing the individual word tones.
3. **Categorization**: The overall tone is classified:
   - Positive: If the total tone score is greater than 0.
   - Negative: If the total tone score is less than 0.
   - Neutral: If the total tone score is exactly 0.
4. **Output**: The text is returned with highlighted words (green for positive, red for negative), and the overall tone score and tone classification are displayed.

## Requirements
- Python 3.x
- `gradio` library for the user interface.
- A custom tone dictionary (`tone-dict-uk.tsv`) containing words and their associated tone values.
- (you can use https://github.com/lang-uk/tone-dict-uk)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/evalasicenko/tone_analysis_gradio.git
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Make sure the tone dictionary (`tone-dict-uk.tsv`) is in the same directory as the script or provide its path.

## Usage
To run the application, simply execute the following command:
```bash
python app.py
```
The Gradio interface will launch in your browser, where you can input text to analyze its tone.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--- 

You can customize the GitHub repository description and adjust the instructions to your specific project setup.
