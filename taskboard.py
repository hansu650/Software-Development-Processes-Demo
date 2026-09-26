"""A small, single-user task board for a Git workflow demonstration."""

import argparse
from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TaskBoard:
    def __init__(self, tasks=None):
        self.tasks = list(tasks or [])

    def add(self, title):
        title = title.strip()
        if not title:
            raise ValueError("Task title must not be empty.")
        next_id = max((task.id for task in self.tasks), default=0) + 1
        task = Task(next_id, title)
        self.tasks.append(task)
        return task

    def complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                return task
        raise ValueError(f"Task #{task_id} does not exist.")


def load_board(path):
    path = Path(path)
    if not path.exists():
        return TaskBoard()
    rows = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(rows, list):
        raise ValueError("Task data must be a JSON list.")
    tasks = []
    seen = set()
    for row in rows:
        if (
            not isinstance(row, dict)
            or set(row) != {"id", "title", "done"}
            or type(row["id"]) is not int
            or row["id"] < 1
            or row["id"] in seen
            or not isinstance(row["title"], str)
            or not row["title"].strip()
            or type(row["done"]) is not bool
        ):
            raise ValueError("Task data contains an invalid or duplicate task.")
        seen.add(row["id"])
        tasks.append(Task(**row))
    return TaskBoard(tasks)


def save_board(board, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps([asdict(task) for task in board.tasks], ensure_ascii=False, indent=2)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload + "\n", encoding="utf-8")
    temporary.replace(path)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    add_command = commands.add_parser("add", help="Add a task")
    add_command.add_argument("title")
    done_command = commands.add_parser("done", help="Complete a task")
    done_command.add_argument("task_id", type=int)
    commands.add_parser("list", help="List tasks")
    args = parser.parse_args(argv)
    path = Path(os.environ.get("TASKBOARD_FILE", ".local/tasks.json"))
    try:
        board = load_board(path)
        if args.command == "add":
            task = board.add(args.title)
            save_board(board, path)
            print(f"Added #{task.id}: {task.title}")
        elif args.command == "done":
            task = board.complete(args.task_id)
            save_board(board, path)
            print(f"Completed #{task.id}: {task.title}")
        else:
            for task in board.tasks:
                marker = "x" if task.done else " "
                print(f"[{marker}] #{task.id} {task.title}")
            if not board.tasks:
                print("No tasks yet.")
    except (OSError, ValueError) as error:
        parser.exit(2, f"Error: {error}\n")


if __name__ == "__main__":
    main()
