Whip-round

# Pre-commit Hooks Setup

Этот проект использует [`pre-commit`](https://pre-commit.com/) для автоматического запуска линтеров перед коммитом.

## Установка

Установи зависимости для линтинга:

```bash
pip install -r requirements.lint.txt
```

## Настройка pre-commit

Установи хуки:

```bash
pre-commit install
```

Теперь при каждом коммите будут запускаться проверки `flake8` и `isort`.

## Ручной запуск

Проверить все файлы вручную:

```bash
pre-commit run --all-files
```

Проверить конкретные файлы:

```bash
pre-commit run --files path/to/file.py
```

## Конфигурация

Все настройки линтеров находятся в корне проекта в `setup.cfg`.