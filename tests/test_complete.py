import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from taskboard import TaskBoard


class CompleteTaskTests(unittest.TestCase):
    def test_complete_changes_only_the_selected_task(self):
        board = TaskBoard()
        first = board.add("Write tests")
        second = board.add("Implement feature")
        completed = board.complete(first.id)
        self.assertTrue(completed.done)
        self.assertFalse(second.done)

    def test_completing_twice_is_idempotent(self):
        board = TaskBoard()
        task = board.add("Demonstrate Git")
        board.complete(task.id)
        board.complete(task.id)
        self.assertTrue(task.done)
        self.assertEqual(len(board.tasks), 1)

    def test_unknown_id_is_rejected_without_modifying_tasks(self):
        board = TaskBoard()
        task = board.add("Keep this task")
        with self.assertRaisesRegex(ValueError, "Task #99 does not exist"):
            board.complete(99)
        self.assertFalse(task.done)

    def test_cli_done_persists_and_missing_id_returns_error(self):
        with tempfile.TemporaryDirectory() as directory:
            environment = dict(os.environ, TASKBOARD_FILE=str(Path(directory) / "demo.json"))
            script = Path(__file__).resolve().parents[1] / "taskboard.py"

            def run(*arguments, check=True):
                return subprocess.run(
                    [sys.executable, str(script), *arguments], env=environment,
                    text=True, capture_output=True, check=check,
                )

            run("add", "Present the project")
            self.assertIn("Completed #1", run("done", "1").stdout)
            self.assertIn("[x] #1 Present the project", run("list").stdout)
            failure = run("done", "99", check=False)
            self.assertEqual(failure.returncode, 2)
            self.assertIn("Task #99 does not exist", failure.stderr)


if __name__ == "__main__":
    unittest.main()
