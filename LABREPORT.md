# Lab Assignment 4 — Lab Report

- **Student:** Muhammad Muneeb Azhar (SP23-BSE-125)
- **Course:** CSC418 DevOps for Cloud Computing — Dr. M. Hasanain Chaudary
- **Assignment:** Student Task Manager Development and Version Control Using Git and GitHub
- **Date:** 18 November 2026
- **Repository:** https://github.com/monebzz/studenttaskmanager
- **Release:** v1.0.0 — https://github.com/monebzz/studenttaskmanager/releases/tag/v1.0.0

## What was built

A Python console app (`main.py` + `task_manager.py`) that adds,
displays, completes, and deletes student tasks, saving them to
`tasks.json`. It was developed on feature branches, reviewed in
pull requests linked to GitHub Issues, tested with `unittest`,
checked by a GitHub Actions workflow, and released as v1.0.0.
Screenshots of the key steps are in `labevidence/`.

| Requirement (Part H) | Delivered |
|---|---|
| At least 12 meaningful commits | 20+ commits on `main` (see `git log --graph`) |
| 3 feature branches | `feature/addtask`, `feature/completetask`, `feature/deletetask` (2 commits each) |
| 4 Issues | #1 Add task validation, #2 Complete task, #3 Delete task, #4 Documentation |
| 5 merged Pull Requests | 7 merged (PR #5–#11: three features, two conflict branches, tests/Actions, docs) |
| 1 resolved conflict | README “Project status” line — PR #9 first refused to merge (merge conflict), resolved on `main`, then merged |
| 3 automated tests | 8 tests in `tests/` (add, complete, delete, display) |
| 1 workflow | `.github/workflows/tests.yml` — runs on push and PRs to `main` |
| 1 release | v1.0.0 |

## 1. Git vs GitHub; add, commit, and push

Git is the version-control tool that runs on my own computer. It
tracks changes in files, keeps the history of commits and branches,
and lets me work offline. GitHub is a website that hosts Git
repositories online, so the same history can be shared, reviewed
in pull requests, and built by Actions.

- `git add` stages changes — it marks which files go into the
  next commit. Nothing is saved in history yet.
- `git commit` saves a snapshot of the staged changes in the
  local repository, with a message saying what changed and why.
- `git push` uploads local commits to GitHub, so the remote
  repository (and anyone else looking at it) sees them.

In short: add prepares, commit records locally, push publishes.

## 2. Why branches and Pull Requests are used; what causes merge conflicts

Branches let different pieces of work grow separately from `main`
without breaking it. I built validation on `feature/addtask`,
completing on `feature/completetask`, and deleting on
`feature/deletetask`, two commits on each, and only merged each
one into `main` after it worked. If a branch goes wrong, `main`
is untouched, and two people (or two features) can progress at
the same time.

A Pull Request is how a branch is proposed, reviewed, and merged.
It shows exactly which files changed, links the related Issue,
and lets someone leave a review comment before merging. That is
the quality check before new code reaches `main`.

A merge conflict happens when two branches change the same lines
of the same file in different ways and Git cannot decide which
version is right. In this assignment I did it on purpose: both
conflict branches changed the same “Project status: Planning”
line in `README.md` — one to “In Progress”, the other to
“Completed”. Git stopped the second merge and left conflict
markers (`<<<<<<<`, `=======`, `>>>>>>>`) in the file for me
to resolve by hand.

## 3. fetch vs pull; merge vs rebase

`git fetch` only downloads the new commits and branches from
GitHub; it does not change my working files. `git pull` does a
fetch and then merges the new commits into my current branch,
so my files are updated. I used fetch when I wanted to look
first, and pull when I wanted to bring `main` up to date.

`git merge` joins two branches and keeps both histories, adding
a merge commit where they join — the graph shows where a feature
branch started and where it came back in. `git rebase` instead
moves my commits on top of the other branch, one by one, so the
history looks like a straight line. Merge keeps the true history
(including the conflict resolution commit); rebase makes a
cleaner-looking history but rewrites commit hashes, so it should
not be used on commits other people already have.

## 4. How GitHub Issues and Actions help a development team

Issues turn work into a list everyone can see. Each one has a
title, a description, and a label (for example `enhancement`
or `documentation`), so the team knows what is planned, what
is a bug, and what is still open. My four Issues matched the
features and the documentation, and each pull request linked
its Issue, so the work and the discussion stay connected.

Actions runs checks automatically. My workflow runs
`python -m unittest discover -s tests -v` on every push to
`main` and on every pull request to `main`. If a test fails,
the run goes red before the code is merged, so a broken change
cannot slip into `main` unnoticed. The team gets the same
check on every change, without anyone having to remember to
run the tests by hand.

## 5. One difficulty I faced and how I solved it

The display test failed on its first run. I had written the
test to expect the marker `[done]` for a completed task, but
the app actually prints `[x]` — `1. [x] CSC418 Assignment 4`.
The test run showed `FAILED (failures=1)` with the exact
line: `'[done]' not found in '1. [x] CSC418 Assignment 4'`.

Instead of changing the app to match a wrong guess, I read
the failure message, checked `display_tasks()` in
`task_manager.py`, and saw the real marker is `[x]`. I fixed
the test to expect `[x]`, re-ran the suite, and all 8 tests
passed. The same failure then showed up as a red GitHub
Actions run and the fix as a green one, which is exactly what
the workflow is for: the test caught my mistake before the
code was merged.

## How to verify (viva)

```bash
git clone https://github.com/monebzz/studenttaskmanager.git
cd studenttaskmanager
python3 main.py
python3 -m unittest discover -s tests -v
git log --oneline --graph
git branch -a
```

On GitHub: Commits and the commit graph, the three feature
branches, Issues #1–#4, merged Pull Requests #5–#11, the
Actions tab (one failed run, then a successful run), and
Release v1.0.0.
