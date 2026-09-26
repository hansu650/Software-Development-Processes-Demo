# Software Development Processes

**W5 · Implementation & Deployment · Git workflow demonstration**

一个独立的 Python 任务清单小程序，用实际提交记录演示这节课的 Git 工作流程。

The example uses only the Python standard library. It is a teaching demo with fictional tasks.

## Run

Use Python 3.12 or later in a dedicated environment:

```powershell
python taskboard.py add "Prepare Git demonstration"
python taskboard.py list
python -m unittest discover -s tests -v
```

Data is stored in `.local/tasks.json`, which Git ignores. Set the `TASKBOARD_FILE` environment variable to choose a different local data file.

## Learning goals

- Save changes with `git add` and `git commit`.
- Share history with `git push`, `git clone`, and `git pull`.
- Develop a feature on a branch, review the diff, and merge it.
- Resolve a real merge conflict and undo a deliberate change using `git revert`.
- See a test fail before implementing the next feature, then pass after implementation.
- Run automated checks and identify a release with a version tag.
