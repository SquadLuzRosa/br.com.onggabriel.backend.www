---
name: ISSUE TEMPLATE FOR BUG
about: "Use this template to report issues or unexpected behaviors in the system. "
title: PROTOCOLO | SOLICITANTE | TITULO DA DEMANDA | BUG
labels: bug
assignees: ""
---

# Descrição do Bug

Descreva claramente o comportamento inesperado ou o erro que está ocorrendo. Explique **o que** aconteceu, **quando** ocorreu e **como** foi percebido. Tente ser o mais específico possível para facilitar a investigação.

Exemplo: Ao tentar acessar a rota `/api/v1/login/`, o servidor retorna um erro 500, sem mensagem de erro específica.

# Como Reproduzir

Descreva os passos detalhados para reproduzir o erro. Se possível, forneça as etapas exatas para que outros possam testar o bug.

Exemplo:

1.  Acesse o endpoint `/api/v1/login/` com as credenciais do usuário.
2.  Clique em "Login".
3.  Observe que o servidor retorna um erro 500.

# Comportamento Esperado

Descreva o que deveria ocorrer em vez do erro.

Exemplo: O login deveria ser bem-sucedido e o usuário ser redirecionado para a página principal.

# Captura de Tela ou Logs

Se possível, forneça capturas de tela, logs ou qualquer outro tipo de evidência que ajude a entender o problema.

- **Logs do servidor**: Se o erro gerar um log no servidor, inclua o trecho relevante.
- **Captura de Tela**: Se houver uma interface gráfica envolvida, inclua uma captura de tela do erro.

Exemplo:  
![Erro de login](https://link-para-captura-de-tela.com)

# Ambiente

Inclua informações sobre o ambiente onde o bug foi encontrado:
Exemplo:

- **Sistema Operacional**: Ubuntu 20.04
- **Versão do Django**: 3.2.5
- **Versão do Python**: 3.8.5

# Impacto

Informe o impacto do bug no uso da aplicação. Ele está impedindo a execução de uma funcionalidade crítica ou é apenas um erro cosmético?

Exemplo: Esse bug impede os usuários de fazerem login, o que afeta todos os usuários que tentam acessar a aplicação.
