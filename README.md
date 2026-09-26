# Software Development Processes

**W5 · Implementation & Deployment · Git workflow demo**

[![Python checks](https://github.com/hansu650/Software-Development-Processes-Demo/actions/workflows/ci.yml/badge.svg)](https://github.com/hansu650/Software-Development-Processes-Demo/actions/workflows/ci.yml)

[Classroom walkthrough](docs/DEMO.md) · [Pull request](https://github.com/hansu650/Software-Development-Processes-Demo/pull/1) · [Releases](https://github.com/hansu650/Software-Development-Processes-Demo/releases)

A small Python task board demonstrates the successful Git workflow covered in this lecture. You can add a task, mark it complete and list the saved tasks. It uses only the Python standard library.

## What to show

```text
Create repository → add → commit → create feature branch
         → implement + test → push → Pull Request → merge
         → pull the updated main → tag → release
```

| Lecture topic | Demonstration in this repository |
|---|---|
| Version control, p. 4 | Small, named commits and a readable history |
| Git and hosting, pp. 7–9 | Local Git repository and public GitHub remote |
| Basic usage, p. 10 | `init`, `status`, `add`, `diff`, `commit` |
| Remote collaboration, p. 11 | `clone`, `push`, `fetch`, `pull --ff-only` |
| Branches, p. 12 | `feature/complete-task`, PR #1 and its merge |
| Automated checks, pp. 17–19 | 11 passing tests and GitHub Actions |
| Release and deployment, pp. 20–23 | Version tag, downloadable source package and local staging check |

The slide numbers refer to the 25-page W5 lecture. PRs and GitHub Actions are practical extensions. The code and fictional task data were created for this standalone demonstration. Both clones use the same account; they demonstrate separate working copies.

## Run it

Use a dedicated Conda environment with Python 3.12:

```powershell
git clone https://github.com/hansu650/Software-Development-Processes-Demo.git
cd Software-Development-Processes-Demo
conda env create -f environment.yml
conda activate software-development-processes-demo
python scripts/demo.py
```

The demo runs add → list → complete → list with temporary data, then shows the Git history. You can also use the commands individually:

```powershell
python taskboard.py add "Prepare the Git demonstration"
python taskboard.py list
python taskboard.py done 1
python taskboard.py list
python -m unittest discover -s tests -v
git log --graph --oneline --decorate --all
```

`done 1` assumes the task ID is 1 in a fresh data file. Use the ID printed by `add` if a file already contains tasks. The default data file is `.local/tasks.json`; set `TASKBOARD_FILE` to select another file. The app reads the environment, not `.env` files automatically.

## Files to open

| File or page | Purpose |
|---|---|
| `taskboard.py` | Small, readable application |
| `tests/` | Unit, storage and command-line behaviour checks |
| `.github/workflows/ci.yml` | Automatic tests on pushes, PRs and version tags |
| `docs/DEMO.md` | Step-by-step presentation and a short speaking script |
| `docs/verification.md` | Recorded checkpoints and release validation |
| `.gitignore`, `.env.example` | Local data stays outside version control; configuration has a harmless example |

This is a single-user teaching application. The release demonstrates distribution and a local staging run; no hosted production service is operated.

## Git details

Saving a file changes the working tree. `git add` stages a snapshot, `git commit` records it locally, and `git push` shares commits. `git pull` fetches and integrates changes; `--ff-only` requires a fast-forward. See the official [Git basic workflow](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository), [git pull](https://git-scm.com/docs/git-pull) and [branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) documentation.
