# Classroom demonstration

**Software Development Processes · W5 Implementation & Deployment**

This walkthrough takes about five minutes. Share the repository home page when only a project link is requested. The commands below explain the completed workflow; the existing repository and feature branch are already set up.

## 1. Show the repository and application

Open the repository home page. Explain that Git records local history while GitHub hosts the remote repository. The example task board supports `add`, `list` and `done`.

```powershell
python scripts/demo.py
```

The script creates a task with temporary data, displays `[ ]`, marks the task complete, then displays `[x]`. It finishes by showing the Git history. Each run uses fresh temporary data.

## 2. Explain the first commit

Open the first commit, `32a0d8b`, to show the starter application and seven tests. The initial workflow was:

```powershell
git init -b main
git status
git add .
git diff --cached
git commit -m "chore: initialize task board with add, list and seven tests"
```

Saving changes the working tree. `git add` stages a snapshot; `git commit` records it locally. A local commit is not automatically uploaded.

## 3. Show the remote and the second clone

```powershell
git remote -v
git push -u origin main
git clone https://github.com/hansu650/Software-Development-Processes-Demo.git
git fetch origin
git pull --ff-only origin main
```

Push shares commits with GitHub. Clone creates another working copy with the code and history. Two clones were used for this demonstration; the second updated the release note. Both use the same account.

Fetch updates remote-tracking information. Pull also integrates changes into the current branch. This example explicitly requests a fast-forward with `--ff-only`.

## 4. Show the feature branch

The starter program could add and list tasks. The `feature/complete-task` branch adds task completion and tests.

```powershell
git branch feature/complete-task
git checkout feature/complete-task
# Edit the application and tests.
python -m unittest discover -s tests -v
git add taskboard.py tests/test_complete.py
git diff --cached
git commit -m "feat: add task completion with eleven passing tests"
git push -u origin feature/complete-task
```

Open the feature commit and show the small change to the application alongside its tests. All 11 tests pass. Branching lets the feature develop separately from main until it is ready to integrate.

## 5. Show the pull request and automated checks

Open [PR #1](https://github.com/hansu650/Software-Development-Processes-Demo/pull/1). Show its description, **Files changed**, **Checks** and merge status. Open a passing [GitHub Actions run](https://github.com/hansu650/Software-Development-Processes-Demo/actions/workflows/ci.yml) to see the unit tests and the add → complete → list smoke test.

A PR organizes changes for inspection on GitHub. This demonstration uses one account and has no independent reviewer. The PR is merged after its automated checks pass.

The lecture's local merge command is `git checkout main` followed by `git merge feature/complete-task`. This repository uses the GitHub PR merge, preserving a merge commit. Afterwards, update the local copies:

```powershell
git checkout main
git pull --ff-only origin main
git log --graph --oneline --decorate --all
```

The graph distinguishes feature development from integration into main.

## 6. Show the release

Open [release v1.0.0](https://github.com/hansu650/Software-Development-Processes-Demo/releases/tag/v1.0.0). The tag identifies a specific commit; the downloadable source package represents that version. Show the release notes and checksum, then the recorded local staging validation.

```powershell
git tag -a v1.0.0 -m "First classroom demonstration release"
git push origin v1.0.0
```

Commit, push, merge and release are separate steps. This example distributes source and verifies it in a separate local directory. GitHub Actions automates testing; it does not deploy an online production service.

## Short speaking script

> This repository demonstrates the Git workflow from our Software Development Processes lecture. The example is a small Python task board. I first created a repository and committed the basic add and list features. Then I used a separate branch to add task completion and its tests. I pushed the branch and opened a pull request, where the changes and automated checks are visible. After the checks passed, I merged the branch into main and pulled the updated version into the local copies. Finally, I tagged version 1.0.0 and prepared a downloadable release. The key distinction is that committing records a local version, pushing shares it, merging integrates changes, and releasing identifies a version for users.

## Useful distinctions

| Term | Meaning in this demonstration |
|---|---|
| Working tree | Files being edited |
| Staging area | Selected content for the next commit |
| Local repository | Saved commits on one computer |
| Remote repository | Shared commits hosted on GitHub |
| Feature branch | Work on task completion before integration |
| Pull request | GitHub page for inspecting proposed changes |
| Merge | Integration of the feature into main |
| Continuous integration | Automatic checks on pushes and PRs |
| Tag | A name identifying a particular version |
| Release | Version notes and a downloadable package |

Official references: [recording changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository), [git pull](https://git-scm.com/docs/git-pull), [branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).
