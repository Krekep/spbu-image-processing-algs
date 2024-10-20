[![Check code style](https://github.com/JetBrains-Research/formal-lang-course/actions/workflows/code_style.yml/badge.svg)](https://github.com/JetBrains-Research/formal-lang-course/actions/workflows/code_style.yml)
[![Code style](https://img.shields.io/badge/Code%20style-black-000000.svg)](https://github.com/psf/black)
---
# Алгоритмы обработки изображений

Данный репозиторий содержит домашние работы по курсу "Алгоритмы обработки изображений".

Технологии:
- Python 3.8+
- Pytest для unit тестирования
- GitHub Actions для CI
- Сторонние пакеты из `requirements.txt` файла

## Инструкция по запуску

### Тесты

- Тесты домашних заданий размещены в папке `tests`.
- Для работы с тестами рекомендуется использовать [`pytest`](https://docs.pytest.org/en/stable/).
- Для запуска тестов необходимо из корня проекта выполнить следующую команду:
  ```shell
  python ./scripts/run_tests.py
  ```

## Структура репозитория

```text
.
├── .github - файлы для настройки CI и проверок
├── examples - примеры использования алгоритмов обработки изображений
├── project - исходный код домашних работ
├── scripts - вспомогательные скрипты для автоматизации разработки
├── tests - директория для unit-тестов домашних работ
├── README.md - основная информация о проекте
└── requirements.txt - зависимости для настройки репозитория
```

## Контакты

- Павел Алимов [@Krekep](https://github.com/Krekep)
