# Projeto Site Institucional — ONG Gabriel (Back-end)

Descrição técnica e documentação do back-end do site institucional da ONG Gabriel. O código implementa uma API RESTful para gerenciar conteúdo (blog, eventos, depoimentos), autenticação e um pequeno CMS interno para gestão de mídias e conteúdo estático.

**Resumo rápido**

- API REST construída com Django + Django REST Framework.
- Módulos principais: `authentication`, `blog`, `events`, `management` (CMS), `testmonial`.
- Media management com limpeza automática de arquivos e paths únicos para uploads.
- Modelo relacional intermediário (`EventMediaRelation`) para relacionar `Event` ↔ `ManagementMedia` com metadados (ex.: `is_cover`).

**O que há neste repositório**

- Endpoints para CRUD de posts, eventos, depoimentos e recursos de autenticação (JWT).
- Um pequeno CMS (app `management`) para armazenar e reaproveitar mídias (imagens/vídeos) em diferentes entidades.
- Limpeza automática de arquivos de mídia (remoção do arquivo antigo ao atualizar e remoção ao apagar a instância).

Funcionalidades notáveis

- **Management (CMS)**: o app `management` contém o model `ManagementMedia` (em `src/management/models/media.py`) que centraliza arquivos de mídia (imagem e vídeo). Ele gera slugs únicos, armazena metadados (title, caption, alt_text) e expõe um serializer (`management.serializers.ManagementMediaSerializer`) usado por outros apps (`blog`, `testmonial`, `events`).

- **Auto-clean de mídias**: existe lógica para garantir que o arquivo físico seja removido quando uma instância de mídia é atualizada ou deletada:
  - Override de `delete()` em `ManagementMedia` limpa o arquivo do storage.
  - Signals em `src/management/signals/media.py`:
    - `pre_save` apaga o arquivo antigo quando um novo arquivo é enviado para a mesma instância.
    - `post_delete` apaga o arquivo quando a instância é excluída.

- **Modelo relacional intermediário para eventos e suas mídias**: o app `events` usa um `ManyToManyField` com `through='EventMediaRelation'` (`src/events/models.py`). O modelo intermediário `EventMediaRelation` permite:
  - Marcar uma mídia como *cover* (`is_cover`) e garantir apenas uma capa por evento (override de `save()` faz essa normalização).
  - Armazenar metadados de ligação (timestamp, flags) sem poluir `Event` ou `ManagementMedia`.

- **Uploads com caminhos únicos**: funções utilitárias em `src/utils/file_utils.py` geram nomes únicos e subpastas organizadas por tipo (`posts/covers`, `events/covers`, `depoiments/covers`).

Arquitetura e integração entre apps

- `blog` e `testmonial` usam `ManagementMedia` via serializer/PK para criar ou referenciar mídias.
- `events` armazena endereços (`Address`), tipos de evento (`EventType`) e relaciona múltiplas mídias via `EventMediaRelation`.

Stack e dependências (conforme `pyproject.toml`)

- **Python**: >= 3.14
- **Django**: >= 5.2.8
- **Django REST Framework**: >= 3.16.1
- **Simple JWT (djangorestframework-simplejwt)**: >= 5.5.1
- **drf-spectacular** (OpenAPI): >= 0.29.0
- **Banco**: PostgreSQL (recomendado) via `psycopg2-binary` >= 2.9.11
- Outras dependências úteis já declaradas:
  - `django-cors-headers` >= 4.9.0
  - `django-filter` >= 25.2
  - `django-jazzmin` >= 3.0.1 (admin theme)
  - `pillow` >= 12.0.0 (imagem)
  - `whitenoise` >= 6.8.2 (servir estáticos)
  - `dj-database-url` >= 3.0.1
  - `python-decouple` >= 3.8
  - `gunicorn` >= 23.0.0 (prod)

Dev e lint

- Ferramentas de dev estão em `pyproject.toml` (ex.: `ruff` para lint/format).

Estratégia de limpeza de mídias (detalhes técnicos)

- Ao atualizar uma instância de `ManagementMedia` com um novo arquivo, o signal `pre_save` detecta a troca e remove o arquivo antigo do storage.
- Ao deletar uma instância, `post_delete` e o próprio `delete()` do model tentam remover o arquivo do storage (com tratamento de exceções).

Boas práticas seguidas

- Uso de `UUIDField` para PKs em recursos que podem ser expostos publicamente.
- `through` model para M2M quando metadados da relação são necessários (`EventMediaRelation`).
- Paths de upload únicos para evitar colisões e facilitar organização de mídia.

Como rodar (resumo)

1. Crie e ative um virtualenv com Python >= 3.14.
2. Instale dependências:

```bash
uv sync  # ou use `pip install .` se preferir
```

3. Configure `DATABASE_URL` (Postgres) e variáveis de ambiente conforme `src/app/settings.py` usa `python-decouple`.
4. Rode migrações e crie superuser:

```bash
python src/manage.py migrate
python src/manage.py createsuperuser
```

5. Execute em modo de desenvolvimento:

```bash
python src/manage.py runserver
```

Onde olhar no código

- Models de mídia e limpeza: `src/management/models/media.py` e `src/management/signals/media.py`.
- Helpers de upload: `src/utils/file_utils.py`.
- Eventos e relação intermediária: `src/events/models.py`.
- Serializers que integram mídias: `src/blog/serializers.py`, `src/testmonial/serializers.py`.

Contribuições e próximos passos sugeridos

- Validar políticas de armazenamento (S3, backblaze, etc.) e adaptar remoção de arquivos para storage externos.
- Tests automatizados para confirmar comportamento de limpeza de arquivos (mock do storage).
- Painel administrativo (jazzmin) e permissões refinadas para o CMS.

---

## Equipe

Contribuidores e mantenedores listados no repositório GitHub.

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://avatars.githubusercontent.com/u/125938287?v=4&size=64" width="100" ><br>
        <a href="https://github.com/kaironn2" ><b>Jonathas Oliveira</b></a><br>
        <i>BackEnd</i>
      </td>
      <td align="center">
        <img src="https://avatars.githubusercontent.com/u/108550945?v=4" width="100" ><br>
        <a href="https://github.com/thiagoferreirapy" ><b>Thiago Ferreira</b></a><br>
        <i>BackEnd</i>
      </td>
      <td align="center">
        <img src="https://avatars.githubusercontent.com/u/67665085?v=4" width="100" ><br>
        <a href="https://github.com/Sabrinadelpache" ><b>Sabrina Delpache</b></a><br>
        <i>BackEnd</i>
      </td>
      <td align="center">
        <img src="https://avatars.githubusercontent.com/u/109382838?v=4" width="100" ><br>
        <a href="https://github.com/danielerick-dev" ><b>Daniel Erick</b></a><br>
        <i>BackEnd</i>
      </td>
      <td align="center">
        <img src="https://avatars.githubusercontent.com/u/151978350?v=4" width="100" ><br>
        <a href="https://github.com/juhffelix" ><b>Juliana Felix</b></a><br>
        <i>BackEnd</i>
      </td>
    </tr>
  </table>
</div>
