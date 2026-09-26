# Git and GitHub - Qin Tian

**Software Development Processes | GitHub: hansu650**

This short walkthrough follows the supplied classroom text-file example. It explains the successful steps recorded in this repository. The repository already exists; clone it to inspect the result.

## 1. Repository and author

For a new, empty practice directory, the lesson starts with:

```bash
git init -b main
git config user.name "Qin Tian"
git config user.email "174235244+hansu650@users.noreply.github.com"
```

`init` starts version control. The name and email identify commits; GitHub authentication is separate. This repository was already initialized before the text-file exercise. Its current remote uses HTTPS with the existing GitHub credentials.

## 2. Stage, inspect and commit

The starter example has `README.md`, `notes.txt`, `.gitignore` and `.env.example`. The first line of `notes.txt` is:

```text
Today I learned Git.
```

The classroom workflow is:

```bash
git status --short
git add README.md notes.txt .gitignore .env.example
git diff --cached
git commit -m "Initial commit"
```

In this existing repository, the equivalent starter commit is named `Adapt classroom Git example for Qin Tian`. It also removes the earlier application's files from the current version. Earlier commits and the release tag remain available.

The second commit adds a line to `notes.txt`:

```bash
printf 'I can track changes.\n' >> notes.txt
git diff
git add notes.txt
git diff --cached
git commit -m "Update learning notes"
```

`diff` shows unstaged changes; `diff --cached` shows the staged changes for the next commit. `commit` records them locally.

## 3. Branch and local merge

```bash
git switch -c feature/intro
printf 'Hello, I am Qin Tian.\nGitHub: hansu650\n' > intro.txt
git add intro.txt
git commit -m "Add introduction"
git switch main
git merge --no-ff feature/intro -m "Merge intro"
```

The introduction is created on the feature branch. It reaches `main` through the merge. `--no-ff` keeps a visible merge commit.

## 4. Push, clone and pull

```bash
git remote -v
git push -u origin main
git clone https://github.com/hansu650/Software-Development-Processes-Demo.git git-class-clone
```

A separate clone demonstrates a second working copy. Both copies are operated by the same account.

The remote update adds `Edited on GitHub.` to `notes.txt`. It is made through GitHub's API, matching the lesson's remote-edit step. Back in the original working copy:

```bash
git switch main
git status
git pull --ff-only
cat notes.txt
```

`pull --ff-only` fetches and fast-forwards when possible. A remote commit does not automatically update local files.

## 5. Feature branch and Pull Request

Completed example: [merged PR #2](https://github.com/hansu650/Software-Development-Processes-Demo/pull/2), adding only the two-line checklist.

```bash
git switch -c feature/checklist
printf 'Check status before commit.\nReview diff before push.\n' > checklist.txt
git add checklist.txt
git diff --cached
git commit -m "Add demo checklist"
git push -u origin feature/checklist
```

Open a Pull Request with **base: main** and **compare: feature/checklist**. Inspect **Files changed**, then merge using **Create a merge commit**. In this single-account exercise, inspecting the changes does not represent an independent peer review.

```bash
git switch main
git pull --ff-only
cat checklist.txt
git --no-pager log --oneline --graph v1.0.0..main
git branch -d feature/checklist
```

Pushing a branch shares it; merging the Pull Request integrates it into `main`. Pull the result into the local copies.

## 6. Check ignored configuration

The example `.env.example` contains only `API_KEY=REPLACE_WITH_YOUR_OWN_VALUE`. A local `.env` with a deliberately invalid demonstration value is ignored.

```bash
git check-ignore -v .env
git ls-files -- .env
git diff --cached
git status --short
```

`git ls-files -- .env` should produce no output. `.gitignore` does not remove an already tracked file or its history.

## Short speaking script

My name is Qin Tian. This repository follows our Git and GitHub classroom example. I started with a README and learning notes, then committed another line to show how Git records changes. I added my introduction on a feature branch and merged it into main. After pushing, I cloned the repository and pulled a change made on GitHub. Finally, I added a checklist on another branch, opened a Pull Request, inspected the changes and merged it. The key steps are add, commit, push, branch, merge and pull. The example configuration contains only a placeholder, and the local configuration file stays outside Git.
