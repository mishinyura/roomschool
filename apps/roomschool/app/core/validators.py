import re

import bleach


def sanitize_text(value: str) -> str:
    """Очистка от HTML/JS"""
    return bleach.clean(value, tags=[], attributes={}, strip=True)


def validate_phone(phone: str) -> bool:
    """Простая проверка телефона"""
    return bool(re.fullmatch(r"\+?\d{10,15}", phone))
