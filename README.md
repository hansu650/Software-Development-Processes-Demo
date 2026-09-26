# Software Development Processes

**Git and GitHub classroom demonstration by Qin Tian (@hansu650)**

A small text-file project following the Git and GitHub example supplied in class. The example structure and successful workflow are retained, with my name and GitHub account filled in.

[Classroom walkthrough](docs/DEMO.md) | [Commit history](https://github.com/hansu650/Software-Development-Processes-Demo/commits/main/) | [Merged classroom PR #2](https://github.com/hansu650/Software-Development-Processes-Demo/pull/2)

## Example files

| File | Purpose |
|---|---|
| `README.md` | Project description |
| `notes.txt` | Learning notes changed across several commits |
| `intro.txt` | My introduction, added on `feature/intro` |
| `checklist.txt` | A short checklist, added through a pull request |
| `.gitignore` | Rules that keep local files out of commits |
| `.env.example` | A harmless configuration placeholder |

## Git workflow

```text
edit -> status / diff -> add -> diff --cached -> commit -> push
branch -> commit -> merge
remote update -> pull --ff-only
feature branch -> push -> Pull Request -> merge -> pull
```

Git records local versions. GitHub hosts the remote repository and provides the Pull Request interface. A commit records a local version; a push shares commits; a pull retrieves and integrates remote changes.

## Open the example

Use Git Bash, starting in a directory without an existing `Software-Development-Processes-Demo` folder:

```bash
git clone https://github.com/hansu650/Software-Development-Processes-Demo.git
cd Software-Development-Processes-Demo
cat notes.txt
cat intro.txt
cat checklist.txt
git --no-pager log --oneline --graph v1.0.0..main
```

This example needs only Git and a text editor. `.env.example` contains an invalid placeholder; a local `.env` is ignored.

The supplied lesson is the basis for this exercise. The earlier Python demonstration remains in the repository history and the `v1.0.0` tag.
