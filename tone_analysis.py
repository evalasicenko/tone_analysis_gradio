import csv
import re

class ToneAnalyzer:
    def __init__(self, dictionary_path):
        self.tone_dict = self.load_dictionary(dictionary_path)

    def load_dictionary(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as tsv_file:
                reader = csv.reader(tsv_file, delimiter='\t')
                next(reader)  # Пропускаємо заголовок
                tone_dict = {row[0].lower(): int(row[1]) for row in reader}
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file_path} не знайдено!")
        except Exception as e:
            raise Exception(f"Помилка при завантаженні словника: {str(e)}")
        return tone_dict

    def analyze_tone(self, text):
        words = re.findall(r'\w+|\s+|[^\w\s]', text)
        highlighted_text = []
        total_tone = 0

        for word in words:
            tone = self.tone_dict.get(word.lower(), 0)
            color = 'green' if tone > 0 else 'red' if tone < 0 else None
            if color:
                highlighted_text.append(f"<span style='color:{color};'>{word}</span>")
            else:
                highlighted_text.append(word)
            total_tone += tone

        tone_label = self.get_tone_label(total_tone)

        return f"<div>{''.join(highlighted_text)}</div>", total_tone, tone_label

    def get_tone_label(self, total_tone):
        if total_tone > 0:
            return "Позитивний"
        elif total_tone < 0:
            return "Негативний"
        else:
            return "Нейтральний"
