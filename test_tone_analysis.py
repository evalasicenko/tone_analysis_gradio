import pytest
from tone_analysis import ToneAnalyzer

# Путь к файлу словаря
tone_dict_path = 'tone-dict-uk.tsv'

# Инициализируем объект ToneAnalyzer для использования в тестах
tone_analyzer = ToneAnalyzer(tone_dict_path)

def test_positive_tone():
    text = "Цей текст дуже позитивний."
    result, total_tone = tone_analyzer.analyze_tone(text)
    assert total_tone > 0

def test_negative_tone():
    text = "Цей текст сумний."
    result, total_tone = tone_analyzer.analyze_tone(text)
    assert total_tone < 0

def test_neutral_tone():
    text = "Текст без емоцій."
    result, total_tone = tone_analyzer.analyze_tone(text)
    assert total_tone == 0

def test_empty_input():
    text = ""
    result, total_tone = tone_analyzer.analyze_tone(text)
    assert result == "<div></div>"
    assert total_tone == 0
