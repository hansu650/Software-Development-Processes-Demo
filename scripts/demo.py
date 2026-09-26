"""Run the successful application workflow using disposable example data."""

from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def main():
    with tempfile.TemporaryDirectory(prefix="git-class-demo-") as directory:
        environment = dict(os.environ, TASKBOARD_FILE=str(Path(directory) / "tasks.json"))
        for arguments in [
            ["add", "Present the Git workflow"],
            ["list"],
            ["done", "1"],
            ["list"],
        ]:
            print("\n$ python taskboard.py " + subprocess.list2cmdline(arguments), flush=True)
            subprocess.run(
                [sys.executable, str(ROOT / "taskboard.py"), *arguments],
                cwd=ROOT, env=environment, check=True,
            )
    if (ROOT / ".git").exists() and shutil.which("git"):
        print("\n$ git log --graph --oneline --decorate --all", flush=True)
        subprocess.run(
            ["git", "--no-pager", "log", "--graph", "--oneline", "--decorate", "--all"],
            cwd=ROOT, check=True,
        )
    print("\nDemo completed successfully. Temporary example data has been removed.")


if __name__ == "__main__":
    main()
