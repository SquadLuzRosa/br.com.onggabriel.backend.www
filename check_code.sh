#!/bin/bash

# Para executar este arquivo é necessário que você dê permissão, execute: chmod +x check_code.sh
# E para iniciar, execute: ./check_code.sh

while true; do
    echo ""
    echo "🔧 Escolha uma opção:"
    echo "1) Rodar Flake8"
    echo "2) Rodar Testes"
    echo "3) Rodar Ambos (Flake8 + Testes)"
    echo "4) Sair"
    read -p "Digite o número da opção: " opcao

    case $opcao in
        1)
            echo "🔍 Rodando Flake8..."
            flake8 . > flake8_output.txt

            if [ $? -ne 0 ]; then
                echo "❌ Flake8 encontrou problemas:"
                cat flake8_output.txt
            else
                echo "✅ Flake8 passou!"
            fi
            ;;
        2)
            echo "🧪 Rodando testes Django..."
            python manage.py test > test_output.txt

            if [ $? -ne 0 ]; then
                echo "❌ Testes falharam!"
                cat test_output.txt
            else
                echo "✅ Todos os testes passaram!"
            fi
            ;;
        3)
            echo "🔍 Rodando Flake8..."
            flake8 . > flake8_output.txt

            if [ $? -ne 0 ]; then
                echo "❌ Flake8 encontrou problemas:"
                cat flake8_output.txt
            else
                echo "✅ Flake8 passou!"
            fi

            echo "🧪 Rodando testes Django..."
            python manage.py test > test_output.txt

            if [ $? -ne 0 ]; then
                echo "❌ Testes falharam!"
                cat test_output.txt
            else
                echo "✅ Todos os testes passaram!"
            fi
            ;;
        4)
            echo "👋 Saindo..."
            break
            ;;
        *)
            echo "❗ Opção inválida. Tente novamente."
            ;;
    esac
done
