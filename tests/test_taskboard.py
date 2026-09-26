import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from taskboard import Task, TaskBoard, load_board, save_board


class TaskBoardTests(unittest.TestCase):
    def test_new_board_is_empty(self):
        self.assertEqual(TaskBoard().tasks, [])

    def test_add_trims_title_and_uses_next_available_id(self):
        board = TaskBoard([Task(7, "Existing example")])
        task = board.add("  Prepare demo  ")
        self.assertEqual((task.id, task.title, task.done), (8, "Prepare demo", False))

    def test_blank_title_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "must not be empty"):
            TaskBoard().add("   ")

    def test_missing_file_creates_empty_board(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(load_board(Path(directory) / "missing.json").tasks, [])

    def test_storage_preserves_text_and_completion_state(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nested" / "tasks.json"
            board = TaskBoard([Task(3, "Prepare \u2605 demo", True)])
            save_board(board, path)
            self.assertEqual(load_board(path).tasks, board.tasks)

    def test_invalid_storage_is_rejected(self):
        invalid_values = [
            {"id": 1},
            [{"id": 0, "title": "Bad", "done": False}],
            [{"id": True, "title": "Bad", "done": False}],
            [{"id": 1, "title": " ", "done": False}],
            [{"id": 1, "title": "Bad", "done": "false"}],
            [{"id": 1, "title": "Bad", "done": False}] * 2,
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tasks.json"
            for value in invalid_values:
                with self.subTest(value=value):
                    path.write_text(json.dumps(value), encoding="utf-8")
                    with self.assertRaises(ValueError):
                        load_board(path)
            path.write_text("not json", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_board(path)

    def test_cli_add_and_list_use_selected_data_file(self):
        with tempfile.TemporaryDirectory() as directory:
            environment = dict(os.environ, TASKBOARD_FILE=str(Path(directory) / "demo.json"))
            script = Path(__file__).resolve().parents[1] / "taskboard.py"
            result = subprocess.run(
                [sys.executable, str(script), "add", "Read Git history"],
                env=environment, text=True, capture_output=True, check=True,
            )
            self.assertIn("Added #1", result.stdout)
            result = subprocess.run(
                [sys.executable, str(script), "list"],
                env=environment, text=True, capture_output=True, check=True,
            )
            self.assertIn("[ ] #1 Read Git history", result.stdout)


if __name__ == "__main__":
    unittest.main()
