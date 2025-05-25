#!/bin/bash

# Rodando Flake8
echo "🔍 Rodando Flake8..."
flake8 . > flake8_output.txt

if [ $? -ne 0 ]; then
    echo "❌ Flake8 encontrou problemas:"
    cat flake8_output.txt
else
    echo "✅ Flake8 passou!"
fi

# Rodando os testes Django
echo "🧪 Rodando testes Django..."
python manage.py test > test_output.txt

if [ $? -ne 0 ]; then
    echo "❌ Testes falharam!"
    cat test_output.txt
else
    echo "✅ Todos os testes passaram!"
fi
