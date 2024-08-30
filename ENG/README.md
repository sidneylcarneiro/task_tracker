
```markdown
# Task Tracker

A simple task tracker built in Python. This program allows you to create, modify, delete, list, and filter tasks through a command-line interface (CLI). Tasks are saved in a text file for persistence between executions.

## Features

- **Create Task:** Add a new task to the list with an initial status (pending, in progress, or completed).
- **Modify Task:** Change the name and/or status of an existing task.
- **Delete Task:** Remove a task from the list.
- **List Tasks:** Display all tasks or filter by a specific status.
- **Persistence:** Tasks are saved in a text file (`tasks.txt`) so you can access them later.

## How to Use

### Prerequisites

- Python 3.6 or higher.

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/sidneylcarneiro/task_tracker.git
cd task_tracker
```

### Running the Program

To run the program, use the following command:

```bash
python task_tracker.py
```

### Available Commands

- **create**: Add a new task.
- **modify**: Modify an existing task.
- **delete**: Remove a task from the list.
- **list**: List all tasks.
- **filter**: Filter tasks by status (pending, in progress, completed).
- **exit**: Exit the program.

### Usage Examples

#### Create Task

```bash
Enter command> create
Enter task name: Study Python
Enter task status (pending/in progress/completed): pending
```

#### Modify Task

```bash
Enter command> modify
Enter the index of the task to be modified: 0
Enter the new task name (or leave blank to not change): Study Advanced Python
Enter the new task status (or leave blank to not change): in progress
```

#### Delete Task

```bash
Enter command> delete
Enter the index of the task to be deleted: 0
```

#### List Tasks

```bash
Enter command> list
[0] Study Python - in progress
```

#### Filter Tasks

```bash
Enter command> filter
Enter the status to filter (pending/in progress/completed): in progress
[0] Study Advanced Python - in progress
```

## Contributing

If you would like to contribute to this project, feel free to open a [pull request](https://github.com/sidneylcarneiro/task_tracker/pulls) or report issues through the [issues](https://github.com/sidneylcarneiro/task_tracker/issues) page.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

- **Sidney L. Carneiro** - [GitHub](https://github.com/sidneylcarneiro)

```

This English version of the `README.md` covers all the functionalities and usage instructions just like the original Portuguese version.