#!/usr/bin/env bash
set -e

echo 'Деплой скрипта Анализ Рейтинга Брендов'

if ! command -v python3 &> /dev/null; then
  echo 'python3 не найден, пожалуйста установите python'
  exit 1
fi

if ! command -v pip &> /dev/null; then
  echo 'pip не найден, пожалуйста установите pip'
  exit 1
fi

if [ ! -d 'venv' ]; then
  echo 'Создается виртуальное окружение...'
  python3 -m venv venv
fi

source venv/bin/activate

echo 'Установка зависимостей'
pip install -U pip
pip install -r requirements.txt

echo 'Запуск тестов...'
PYTHONPATH=. pytest --cov=reports --disable-warnings -q

echo 'Деплой завершен успешно, для помощи используйте -h'
