# term-agenda

Agenda pessoal interativa via terminal, feita em Python.

O **term-agenda** é um projeto simples e intencionalmente minimalista para organizar compromissos pessoais diretamente pelo terminal, sem dependência de interfaces gráficas ou serviços externos.

Ele foi pensado para evoluir aos poucos:

* **V0**: interação por menu no terminal (input/output)
* **V1**: Integração com banco de dados usando `PostgreSQL`
* **V2**: TUI completa usando `Textual`

---

## ✨ Funcionalidades (V0)

* Menu interativo no terminal
* Listar compromissos
* Adicionar novos compromissos
* Marcar compromissos como concluídos
* Persistência local em arquivo JSON

---

## 🧠 Filosofia do projeto

* Uso pessoal
* Foco em simplicidade e clareza
* Código fácil de evoluir
* Arquitetura preparada para TUI no futuro

---

## 📦 Estrutura do projeto

```text
term-agenda/
├── pyproject.toml
├── src/
│   └── term_agenda/
│       ├── __main__.py
│       ├── main.py
│       ├── commands.py
│       ├── storage.py
│       └── models.py
└── data/
    └── agenda.json
```

---

## 🚀 Instalação

Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale o projeto em modo editável:

```bash
pip install -e .
```

---

## ▶️ Como usar

Execute o app pelo terminal:

```bash
term-agenda
```

Ou, alternativamente:

```bash
python -m term_agenda
```

---

## 🧭 Exemplo de uso

```text
=== TERM AGENDA ===

1) Listar compromissos
2) Adicionar compromisso
3) Marcar como concluído
4) Sair

Selecione uma opção:
```

---

## 🗺️ Roadmap

* [x] Menu interativo no terminal
* [x] Persistência local
* [ ] Validação de datas e horários
* [ ] Edição de compromissos
* [ ] Filtros (hoje / semana)
* [ ] Migração para TUI com Textual

---

## 🛠️ Requisitos

* Python 3.10+

---

## 📄 Licença

Projeto pessoal para estudo e uso próprio.
