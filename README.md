
```markdown
# Task Tracker

Um simples rastreador de tarefas criado em Python. Este programa permite que você crie, altere, delete, liste e filtre tarefas através de uma interface de linha de comando (CLI). As tarefas são salvas em um arquivo de texto para persistência entre execuções.

## Funcionalidades

- **Criar Tarefa:** Adicione uma nova tarefa à lista com um status inicial (pendente, em andamento, ou concluída).
- **Alterar Tarefa:** Modifique o nome e/ou status de uma tarefa existente.
- **Deletar Tarefa:** Remova uma tarefa da lista.
- **Listar Tarefas:** Exiba todas as tarefas ou filtre por status específico.
- **Persistência:** As tarefas são salvas em um arquivo de texto (`tarefas.txt`) para que você possa acessá-las posteriormente.

## Como Usar

### Pré-requisitos

- Python 3.6 ou superior.

### Instalação

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/sidneylcarneiro/task_tracker.git
cd task_tracker
```

### Executando o Programa

Para executar o programa, use o seguinte comando:

```bash
python task_tracker.py
```

### Comandos Disponíveis

- **criar**: Adicione uma nova tarefa.
- **alterar**: Altere uma tarefa existente.
- **deletar**: Exclua uma tarefa da lista.
- **listar**: Liste todas as tarefas.
- **filtrar**: Filtre as tarefas por status (pendente, em andamento, concluída).
- **sair**: Saia do programa.

### Exemplos de Uso

#### Criar Tarefa

```bash
Digite o comando> criar
Digite o nome da tarefa: Estudar Python
Digite o status da tarefa (pendente/em andamento/concluída): pendente
```

#### Alterar Tarefa

```bash
Digite o comando> alterar
Digite o índice da tarefa a ser alterada: 0
Digite o novo nome da tarefa (ou deixe em branco para não alterar): Estudar Python Avançado
Digite o novo status da tarefa (ou deixe em branco para não alterar): em andamento
```

#### Deletar Tarefa

```bash
Digite o comando> deletar
Digite o índice da tarefa a ser deletada: 0
```

#### Listar Tarefas

```bash
Digite o comando> listar
[0] Estudar Python - em andamento
```

#### Filtrar Tarefas

```bash
Digite o comando> filtrar
Digite o status para filtrar (pendente/em andamento/concluída): em andamento
[0] Estudar Python Avançado - em andamento
```

## Contribuindo

Se você quiser contribuir com este projeto, sinta-se à vontade para abrir um [pull request](https://github.com/sidneylcarneiro/task_tracker/pulls) ou reportar problemas através das [issues](https://github.com/sidneylcarneiro/task_tracker/issues).

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

## Autor

- **Sidney L. Carneiro** - [GitHub](https://github.com/sidneylcarneiro)

```
