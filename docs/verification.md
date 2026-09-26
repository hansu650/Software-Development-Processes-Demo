# Verification record

Verified on 26 September 2026. This record describes the successful demonstration.

## Development checkpoints

| Checkpoint | Evidence | Result |
|---|---|---|
| Starter application | Commit `32a0d8b` | Seven local tests passed |
| Second working copy | Commit `7881f29` | Cloned the repository, committed the release note and pushed it |
| Task completion | Commit `42931c0` | All 11 unit and command-line tests passed |
| Automated feature checks | [Feature CI run](https://github.com/hansu650/Software-Development-Processes-Demo/actions/runs/36211950888) | Successful |
| English walkthrough | [PR CI run](https://github.com/hansu650/Software-Development-Processes-Demo/actions/runs/36212100302) | Successful |
| Repeatable live demo | `python scripts/demo.py` | Add, list, complete and list succeeded with fresh temporary data |

The test suite covers task creation, completion, persistence and command-line behaviour. GitHub Actions runs the same suite plus a successful add → complete → list smoke test. Later workflow runs are available on the [Actions page](https://github.com/hansu650/Software-Development-Processes-Demo/actions/workflows/ci.yml).

## Integration

[PR #1](https://github.com/hansu650/Software-Development-Processes-Demo/pull/1) contains the feature and presentation guide. Its merge status and checks are visible on GitHub. Both clones are operated by the same person; no independent review is claimed.

After the merge, both working copies are updated using `git pull --ff-only origin main`. The retained feature branch and merge commit make the integration visible in `git log --graph --oneline --all`.

## Release verification

The [v1.0.0 release](https://github.com/hansu650/Software-Development-Processes-Demo/releases/tag/v1.0.0) includes a source ZIP, `SHA256SUMS.txt` and `release-verification.txt`. The verification attachment records the exact tagged commit and the actual local staging output.

The release process archives the tagged source, extracts it into a separate directory, then runs:

```powershell
python -m unittest discover -s tests -v
python scripts/demo.py
```

The staging check uses the task's dedicated Python environment. It verifies the extracted release rather than reinstalling Python on a clean machine. Distribution and local staging are demonstrated; no hosted production deployment is claimed.
