import re
import unicodedata
from typing import Optional


class TextCleaner:
    def __init__(self,
                 preserve_tokens: bool = True,
                 strip_only_tokens: bool = True,
                 language: str = "multi"):
        self.preserve_tokens = preserve_tokens
        self.strip_only_tokens = strip_only_tokens
        self.language = language.lower()

        # Специальные символы для замены
        self.special_replace = {
            '—': '-', '–': '-', '…': '...',
            '«': '"', '»': '"', '“': '"', '”': '"',
            '‘': "'", '’': "'", 'ㅤ': ' '
        }

        # Распознавание месяцев
        self.months_pattern_ru = (
            r'\b\d{1,2}\s+(января|февраля|марта|апреля|мая|июня|'
            r'июля|августа|сентября|октября|ноября|декабря)\b'
        )
        self.months_pattern_en = (
            r'\b(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|'
            r'jul(?:y)?|aug(?:ust)?|sep(?:t)?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\s+\d{1,2}\b'
        )

    def clean(self, text: str) -> Optional[str]:
        text = str(text)

        # Замена спецсимволов
        for bad, good in self.special_replace.items():
            text = text.replace(bad, good)

        if self.preserve_tokens:
            text = re.sub(r'https?://\S+', ' [LINK] ', text)
            text = re.sub(r'\b[\w.-]+?@\w+?\.\w{2,}\b', ' [EMAIL] ', text)
            text = re.sub(r'\+?\d[\d\s\-\(\)]{6,}\d', ' [PHONE] ', text)
            text = re.sub(r'#\w+', ' [HASHTAG] ', text)
            text = re.sub(r'@\w{3,}', ' [USERNAME] ', text)
            text = re.sub(r'[\u20AC\$\u20BD\u00A5\u00A3]', ' [CURRENCY] ', text)
            text = re.sub(r'\b\d{1,2}[:.\-]\d{2}\b', ' [TIME] ', text)
            text = re.sub(r'\b\d{1,2}[./\-]\d{1,2}[./\-]\d{2,4}\b', ' [DATE] ', text)
            text = re.sub(r'\b\d{4}-\d{2}-\d{2}\b', ' [DATE] ', text)

            if self.language in ('ru', 'multi'):
                text = re.sub(self.months_pattern_ru, ' [DATE] ', text, flags=re.IGNORECASE)

            if self.language in ('en', 'multi'):
                text = re.sub(self.months_pattern_en, ' [DATE] ', text, flags=re.IGNORECASE)

        # Удаление эмодзи и символов из категорий So
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"
            "\U0001F300-\U0001F5FF"
            "\U0001F680-\U0001F6FF"
            "\U0001F1E0-\U0001F1FF"
            "\U00002700-\U000027BF"
            "\U0001F900-\U0001F9FF"
            "\U0001FA00-\U0001FAFF"
            "\U0001FA70-\U0001FAFF"
            "\u200d\uFE0F"]+",
            flags=re.UNICODE
        )
        text = emoji_pattern.sub('', text)

        # Очистка от невидимых и непечатаемых символов
        text = re.sub(r'[\u00A0\u2000-\u200B\u202F\u205F\u3000]', ' ', text)
        text = re.sub(r'[\n\r\t\u2028\u2029\x0b\x0c\x85]+', ' ', text)
        text = ''.join(c for c in text if c.isprintable())

        text = ''.join(
            c for c in text
            if unicodedata.category(c)[0] in ['L', 'N', 'P', 'Z']
            and unicodedata.category(c) != 'So'
        )

        # Финальная нормализация пробелов
        text = re.sub(r'\s+', ' ', text).strip().strip('"').strip("'")

        # Удаление строк, содержащих только токены
        if self.strip_only_tokens and all(re.fullmatch(r'\[[A-Z_]+\]', w) for w in text.split()):
            return None

        return text
