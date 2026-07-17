import os
from dotenv import load_dotenv

# Путь к файлу .env
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")

print(f"[DEBUG] Проверяю путь: {file_path}")
print(f"[DEBUG] Файл существует: {os.path.exists(file_path)}")

# Пытаемся загрузить
result = load_dotenv(dotenv_path=file_path, override=True)
print(f"[DEBUG] Результат load_dotenv: {result}")

# Проверяем переменную
val = os.getenv("GITHUB_TOKEN")
print(f"[DEBUG] Значение GITHUB_TOKEN: '{val}'")