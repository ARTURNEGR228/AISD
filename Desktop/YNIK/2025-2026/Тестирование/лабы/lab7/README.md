## Лабораторная работа 6 — Автоматизация тестирования поиска Яндекс

Автоматизированные UI‑тесты для проверки поиска на `ya.ru` с использованием Selenium WebDriver, паттерна Page Object Model, pytest и Allure.

### Структура проекта
- `pages/` — Page Object классы (`YandexFormPage`)
- `tests/` — тестовые сценарии
- `conftest.py` — фикстуры pytest (браузер, base_url)
- `pytest.ini` — базовая конфигурация pytest
- `requirements.txt` — зависимости

### Установка
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

### Запуск тестов
- Обычный запуск: `pytest tests/test_yandex_form.py -v`
- Параллельно (2 потока): `pytest tests/test_yandex_form.py -n 2 -v`
- С генерацией Allure: `pytest tests/test_yandex_form.py --alluredir=allure-results -v`

### Allure отчеты
- Просмотр отчета: `allure serve allure-results`
- Генерация статического отчета: `allure generate allure-results -o allure-report --clean`

### Примечания
- Для безголового запуска установите переменную `HEADLESS=true`.
- Скриншоты при падении можно добавлять через Allure (опционально).

