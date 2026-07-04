# GitHub Copilot Mastery — Reference Guide

Your personal reference for everything learned so far. Updated as we progress through modules. Keep this open alongside your Codespace.

---

## Environment Setup (one-time reference)

**What you're using:**
- **GitHub Codespaces** — a full VS Code environment running in the browser, hosted by GitHub. No local install needed.
- **Repository:** `copilot-practice` on your GitHub account.

**How to get back into your environment next time:**
1. Go to github.com → your `copilot-practice` repo
2. Green **Code** button → **Codespaces** tab → click your existing codespace to resume it (or "Create codespace on main" for a fresh one)

**Key vocabulary:**
- **Repository (repo):** a project folder stored on GitHub with full change history
- **Codespace:** a temporary cloud computer GitHub gives you, with your repo loaded, accessed via browser
- **Terminal:** the black/dark text box at the bottom of VS Code where you type commands directly to the computer
- **Comment:** a line of code starting with `#` in Python — ignored by the computer, read by Copilot and humans

---

## Module 1 — Setup & First Suggestion

**Goal:** See Copilot turn a plain-English comment into working code.

**Key concept:** Copilot predicts code based on: your comment's exact wording, the filename/language, and patterns from its training data. It is NOT reading your mind — always review what it generates.

**Commands/shortcuts:**
| Action | Shortcut |
|---|---|
| Accept a suggestion | `Tab` |
| Reject/dismiss a suggestion | `Esc` |
| Cycle to next alternative | `Alt+]` (Win/Linux) / `Option+]` (Mac) |
| Cycle to previous alternative | `Alt+[` (Win/Linux) / `Option+[` (Mac) |
| Force a suggestion to appear | `Alt+\` (Win/Linux) / `Option+\` (Mac) |
| Run a Python file | `python3 filename.py` (in terminal) |

**Lesson learned:** Copilot sometimes adds extra unrequested code (pattern-matching to common examples it's seen). Always read and clean up what it gives you before trusting it.

---

## Module 2 — Prompting Quality

**Goal:** Understand how comment specificity changes Copilot's output quality.

**Key concept:** The more precisely you define **inputs, outputs, and naming**, the less Copilot has to guess — and the safer/more correct the result.

**Three levels of prompt quality (worst → best):**
1. **Vague comment** (`# sort the list`) → Copilot guesses what "the list" means, often incorrectly, silently.
2. **Specific comment** (`# sort a list of dictionaries by the 'price' key, descending`) → correct logic, generic naming.
3. **Typed function signature** (`def sort_products_by_price(products: list[dict]) -> list[dict]:`) → best result — clear names, correct logic, often auto-generates a docstring too.

**New vocabulary:**
- **Type hint:** annotation telling Python (and readers) what data type a variable/parameter should be, e.g. `products: list[dict]`. Doesn't change how code runs — it's documentation a machine can also check.
- **Lambda:** a small, one-line, unnamed function. `lambda x: x['price']` means "given `x`, return `x['price']`." Used inline, e.g. as a sort key.

**Lesson learned:** Specificity + structure = your biggest lever for good Copilot output. This matters more than any setting or trick.

---

## Module 3 — Copilot Chat

**Goal:** Use conversational AI (not autocomplete) to explain and fix code.

**Key concept:** Chat is a back-and-forth conversation, separate from inline suggestions. You select code, then type a command or question.

**Slash commands:**
| Command | What it does |
|---|---|
| `/explain` | Explains selected code in plain English, including hidden risks/assumptions |
| `/fix` | Diagnoses and proposes a fix for a bug in selected code |
| `/tests` | Generates test cases for a function |
| `@workspace` | Brings in context from your *entire* project, not just the open file |

**How to open Chat:** `Ctrl+Alt+I` (Win/Linux) or `Cmd+Ctrl+I` (Mac)

**New vocabulary:**
- **Traceback:** Python's error report showing the full chain of function calls that led to a crash — read bottom to top: the actual error is at the bottom, the origin of the call is at the top.
- **KeyError:** a crash caused by accessing a dictionary key (`dict['key']`) that doesn't exist.
- **`.get('key', default)`:** the *safe* way to read a dictionary — returns a default value instead of crashing if the key is missing.

**Terminal trick learned (for fixing corrupted files cleanly):**
```bash
cat > filename.py << 'EOF'
[paste your full clean code here]
EOF
```
This completely overwrites a file's content in one shot — useful when the editor gets messy from Copilot auto-suggestions interfering.

**Lesson learned:** "The code runs without crashing" ≠ "the code is correct for your use case." Always ask whether Copilot's fix reflects the *right* business behavior, not just the simplest technical patch.

---

## Module 4 — Custom Instructions

**Goal:** Set project-wide rules Copilot follows automatically, without repeating yourself.

**Key concept:** A file at `.github/copilot-instructions.md` is read automatically by Copilot before it generates anything — like a permanent style/rules brief for your whole project.

**How to create it:**
```bash
mkdir -p .github
cat > .github/copilot-instructions.md << 'EOF'
- All Python functions must have type hints and docstrings
- When accessing dictionary keys that might be missing, always use .get() with a sensible default instead of square-bracket access
- Prefer list comprehensions over explicit for-loops where it keeps the code readable
EOF
```

**How to verify it's working:** Ask Copilot for a new function with **zero style guidance** in your prompt — if it still follows your rules automatically, it's working.

**New vocabulary:**
- **Type hint** vs **Docstring**: type hints declare *what data types* go in/out (machine-checkable, terse); docstrings explain *what the function does* in human sentences (for people, more detail).

**Lesson learned:** Custom instructions are a strong nudge, not a guarantee — they reduce how often you need to correct Copilot, but you still review output every time.

---

## Module 5 — Agent Mode

**Goal:** Delegate multi-step, multi-file tasks and review autonomous AI work.

**Key concept:** Agent Mode = delegation, not assistance. You describe a *goal*; it plans, creates/edits multiple files, and may propose terminal commands — pausing for your approval at each significant step (depending on your approval settings).

**How to use it:**
1. Open Chat panel → click "+" for a new session
2. Set mode to **Agent** (dropdown near the input box)
3. Describe the full task, including any constraints (e.g., "follow the custom instructions in `.github/copilot-instructions.md`")

**What can go wrong (watch for this):**
- It may add behavior/logic you didn't explicitly ask for (e.g., input validation) — not wrong, but a decision it made unilaterally. Always identify what it added beyond your literal request.
- It may auto-apply changes rather than pause for approval, depending on your settings — review AFTER the fact if this happens, don't skip the review step.

### Testing — full concept explanation

**What a test is:** code that automatically checks whether other code behaves correctly, using `assert` statements — replacing manual "run it and eyeball the output" checking.

**Anatomy of a test:**
```python
def test_add_item_to_empty_inventory():   # name describes the scenario
    inventory = []                         # set up starting condition
    updated = add_item(inventory, "Widget", 9.99, 5)  # call the real function
    assert len(updated) == 1               # the actual claim being checked
```
`assert X` means "I claim X is true — if not, stop and report a failure."

**Running tests:**
```bash
pytest
```

**Reading pytest output:**
```
collected 5 items                                    ← how many test_ functions it found
test_inventory.py .....                    [100%]    ← one dot per PASSED test; F = failed test
5 passed in 0.02s                                     ← final summary line (always check this)
```
If a file has a mix, it might show `..F..` — the `F`'s position tells you which test failed. Multiple test files each get their own line, and the "collected" count is a total across all files.

**Proving a test is real (do this on any new test suite you don't trust yet):**
1. Deliberately introduce a small, wrong change to your code (a "fake bug")
2. Run `pytest` again
3. Confirm it correctly shows `F` and a failure — this proves the test isn't just always saying "pass" regardless of correctness
4. Undo the fake bug, confirm `pytest` returns to all passing

**Reading a pytest failure:**
```
E       AssertionError: assert 1 == 0
E        +  where 1 = ... {'name': 'FreeSample', 'price': 0.0, 'quantity': 1}.get
```
Pytest shows you the actual data at the moment of failure — no need to add your own debug prints.

**Key safe-overwrite trick used to intentionally break code for testing:**
```bash
sed -i 's/OLD_TEXT/NEW_TEXT/' filename.py
```
And to undo it, swap old/new back.

**Lesson learned:** A passing test only proves the code satisfies *that specific check* — not that it does everything you intended. Tests only catch what they're specifically written to catch.

---

## Module 6 — Copilot CLI

**Goal:** Use Copilot directly from the terminal, outside any editor UI.

**Key concept:** Same underlying reasoning as Agent Mode, delivered as a terminal command instead of a chat panel.

**Command format:**
```bash
copilot -p "your plain-English task description"
```
`-p` = "prompt mode" — runs once, non-interactively, and exits (no back-and-forth session).

**When to actually use CLI vs. the editor:**
- No graphical editor available (e.g., SSH'd into a server)
- Quick one-off tasks while already working in a terminal
- Scripting/automating repetitive tasks
- Managing multiple projects without opening each in a full editor

**Important safety behavior:** In `-p` (non-interactive) mode, CLI **cannot** ask for your permission mid-task (no one is present to respond) — so it refuses to run commands entirely rather than assume "yes." This is intentional: the more autonomous/unattended a mode is, the *more* cautious it should be, not less. If it needs to verify something (like running tests) and can't get permission, it tells you plainly instead of guessing or pretending it verified something it didn't.

**Lesson learned:** Trust CLI's code-reading and suggestions, but independently verify any claim it couldn't actually execute-check itself (e.g., run `pytest` yourself if it says "tests should pass" but couldn't run them).

---

## Module 6.5 — Git & PR Workflow *(in progress)*

**Goal:** Move from working directly on `main` to a safe branch → commit → push → Pull Request flow.

**Key vocabulary:**
| Term | Meaning |
|---|---|
| **Branch** | An isolated parallel copy of your code — experiment safely without touching `main` |
| **Commit** | A saved snapshot of changes, with a short descriptive message |
| **Push** | Sending your local commits up to GitHub so they exist online |
| **Pull Request (PR)** | A formal request to merge your branch into `main`, with space for review/comments and (later) automated tests |
| **Merge** | Actually combining your branch's changes into `main` |

**Commands so far:**
```bash
git checkout -b branch-name     # create + switch to a new branch
git status                      # see current branch and pending changes
```

### The core save cycle: add → commit → push

**`git add .`** — stages your changes (marks them "ready to be committed"). The `.` means "everything in this folder and subfolders." Must have a space between `add` and `.` (`git add.` is an error — that's not a real command).

**`git commit -m "description"`** — saves a **checkpoint snapshot** of your staged files, locally only, with a required description of what changed. Nothing has left your Codespace yet. You can commit many times before ever pushing.

**`git push`** — sends all your saved local commits up to GitHub.com, making them visible online. Until you push, your work only exists in your Codespace — if the Codespace were lost, uncommitted-and-unpushed work would be too.

**Analogy:**
| Step | Like... |
|---|---|
| Edit files | Writing in a document |
| `git add` | Putting pages into an envelope, ready to mail |
| `git commit -m "..."` | Sealing the envelope, writing a label describing the contents |
| `git push` | Actually mailing the envelope — now it exists elsewhere too |

**`.gitignore`** — a file listing things Git should never track (e.g., auto-generated folders like Python's `__pycache__/`). Create with:
```bash
echo "__pycache__/" > .gitignore
```

**Full real example used:**
```bash
git add .
git commit -m "Add inventory tracker, tests, custom instructions, and tutorial guide"
git push
```

**Reading `git status` output:**
- `Untracked files` = Git sees them but isn't saving their history yet
- `Changes to be committed` = staged, ready for `git commit`
- `Your branch is ahead of 'origin/main' by N commits` = you have local commits GitHub doesn't have yet — need to `git push`
- `nothing to commit, working tree clean` = everything is saved and in sync

*(This module continues with: creating a real feature branch, opening a Pull Request on GitHub.)*

---

## Module 7 — CI/CD with GitHub Actions

**Goal:** Make tests run automatically on every Pull Request, so no one has to remember to type `pytest` by hand.

**Key concept:** CI = Continuous Integration — automatically verifying every proposed change (every PR) the moment it's opened, on a brand-new, disposable cloud machine (not your Codespace, not your laptop). This proves the code works in a clean environment, not just "worked on my machine."

**Important nuance:** creating the workflow makes tests **run and show a ✅/❌ status** — it does NOT by itself block the merge button. Actually preventing merge-when-failing requires a separate "branch protection rule" (not set up in this project, but good to know exists).

**Where the workflow file lives:**
```
.github/workflows/ci.yml
```

**The complete working file:**
```yaml
name: Run Tests

on: [pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install pytest
        run: pip install pytest

      - name: Run tests
        run: pytest
```

**Line-by-line meaning:**
| Line | Meaning |
|---|---|
| `name: Run Tests` | Label shown in GitHub's Checks tab / Actions dashboard |
| `on: [pull_request]` | Trigger — run whenever a PR is opened or updated |
| `runs-on: ubuntu-latest` | Use a fresh, disposable Ubuntu Linux machine |
| `uses: actions/checkout@v4` | Official pre-built action: download the repo's code onto that machine |
| `uses: actions/setup-python@v5` | Official pre-built action: install Python (version specified via `with:`) |
| `run: pip install pytest` | A direct terminal command (`run:` vs. `uses:` — running your own command vs. using someone else's pre-built action) |
| `run: pytest` | The actual test run — same command you've been typing manually |

**YAML indentation rule:** works like Python's indentation — consistent nesting defines structure. A step (`- name: ...`) must be indented under `steps:`, which must be indented under the job (`test:`), which is indented under `jobs:`. Get it wrong and the whole file fails to parse.

**Safe way to write/fix a YAML file (same trick as fixing corrupted Python files):**
```bash
cat > .github/workflows/ci.yml << 'EOF'
[paste the full correct YAML here]
EOF
```

**Committing and pushing it (the exact cycle, no shortcuts):**
```bash
git add .
git commit -m "Add CI workflow to run pytest automatically on pull requests"
git push
```
Remember: `git add` (stage) → `git commit -m "..."` (seal with a label) → `git push` (mail it). Skipping the commit step means push has nothing new to send, even if the file is staged.

**Where to see it working:**
- PR page → **Checks** tab → shows the workflow name and a green ✅ or red ❌
- Click into it to see the full step-by-step log (checkout → Python setup → pytest install → pytest run), matching your YAML exactly

**Lesson learned:** you watched real, automated tests run on a machine you never touched, triggered purely by `git push` — this is the actual "workflow to PR to CI/CD" pipeline you set out to learn.

---

## Module 8 — Code Review & Merge

**Goal:** Get an automated review on your PR, then merge it properly into `main`.

**How to request Copilot as a reviewer:** on the PR page, right sidebar → "Reviewers" → click "Request" next to Copilot.

**What Copilot's review does:** reads your actual diff/files (not just the summary) and leaves comments — inline on specific lines, and/or a general PR overview describing what changed across every file.

**Real issue it caught in this project:** scope creep — a PR titled "Improved error message" had grown to include a CI workflow and two documentation files. Copilot flagged this as a genuine concern:
> "This scope mismatch makes it harder to review and to track the intent of the change; consider either updating the PR title/description to reflect the broader changes or splitting the docs/CI work into separate PR(s)."

**Fix chosen:** honestly updated the PR title and description to reflect everything actually included, rather than splitting into multiple PRs (acceptable for a learning project; splitting is the stricter real-world practice).

**Merged vs. Closed — an important distinction:**
| Status | Meaning |
|---|---|
| Open | Still active, not yet resolved either way |
| Closed (no merge icon) | Withdrawn — none of the changes went into `main` |
| **Merged** (purple badge) | Changes were successfully combined into `main` — this is what you want |

**Always verify a merge actually happened** — don't just trust the label:
```bash
git checkout main
git pull
cat filename.py   # confirm your change is really there
```

---

## Module 9 — Cloud Agent

**Goal:** Assign a GitHub Issue and have Copilot independently create a branch, write code + tests, and open a PR — with zero manual Agent Mode steps.

**How it differs from Agent Mode:**
| | Agent Mode (Module 5) | Cloud Agent (Module 9) |
|---|---|---|
| Branch creation | You, manually | Copilot, automatically |
| Code writing | Copilot, with your live approval per step | Copilot, working independently |
| PR opening | You, manually | Copilot, automatically |

**How to trigger it:**
1. Create a clear, complete GitHub Issue (title + detailed description of exactly what's needed, including function signature, edge cases, and a reminder to follow `.github/copilot-instructions.md`)
2. In the Issue's right sidebar, under "Assignees," assign it to **Copilot**
3. Copilot automatically creates a branch, writes the code, and opens a linked PR — often starting as "[WIP]" or "Draft" while it works

**Two safety gates you may hit before merging an agent-created PR:**
1. **"1 workflow awaiting approval"** — GitHub requires a human with write access to explicitly approve running CI on PRs from automated agents (a safeguard against a compromised/malicious automated PR silently executing arbitrary code). Click "Approve workflows to run."
2. **"Draft pull requests cannot be merged"** — click "Ready for review" first.

**Review discipline — same as always, even though it's more autonomous:**
- Read the actual code diff, not just Copilot's own summary of it
- Check it against your original issue requirements, item by item
- Check it against your custom instructions (type hints, docstrings, `.get()` usage)
- **Check out the branch locally and run the tests yourself** — don't just trust that "Checks" shows green or that Copilot's description claims success

```bash
git fetch origin
git checkout name-of-agents-branch
pytest
```

**Lesson learned:** more autonomy on the AI's side means review discipline matters *more*, not less — the entire course's central theme, applied at its most hands-off point.

---

## Course Complete — Full Pipeline Achieved

You now have real, hands-on experience with the entire pipeline originally asked for: **describe a task → Copilot writes code (via inline suggestions, Chat, Agent Mode, CLI, or a fully autonomous Cloud Agent) → branch → PR → automated CI/CD tests → automated code review → merge into main.**

Just as importantly, you practiced the discipline that makes this safe in real teams: reading diffs before merging, proving tests are real by breaking code on purpose, catching AI-added behavior you didn't ask for, and verifying claims yourself rather than trusting labels or summaries at face value.

---

## Complete Git Command Reference

Everything from branches to checkout to the save cycle, in one place — including a few you haven't used yet but will need.

### Checking where you are
```bash
git status                  # current branch, staged/unstaged/untracked files
git branch                  # list all local branches (★ marks current one)
git branch -a               # list local AND remote branches
git log                     # full commit history (press 'q' to exit)
git log --oneline           # compact one-line-per-commit history
```

### Creating and switching branches
```bash
git checkout -b new-branch-name     # create a NEW branch and switch to it
git checkout existing-branch-name   # switch to an EXISTING branch (no -b)
git switch new-branch-name          # newer alternative to checkout for switching
git switch -c new-branch-name       # newer alternative to checkout -b (creates + switches)
```
**Key distinction:** `-b` = "build/create new." Leaving it off = "just switch to something that already exists." Using `-b` on a branch that already exists gives: `fatal: a branch named 'X' already exists`.

### The core save cycle (do this constantly)
```bash
git add .                        # stage everything changed
git add filename.py              # stage just one specific file
git commit -m "clear description of what changed"
git push                         # send commits to GitHub (existing branch)
git push --set-upstream origin branch-name   # first push of a BRAND NEW branch only
```

### Getting the latest changes from GitHub
```bash
git fetch origin        # download info about new branches/commits, WITHOUT merging them in
git pull                # download AND merge the latest changes into your current branch
```
**Difference:** `fetch` just looks and reports what's new remotely (safe, non-destructive, doesn't touch your files). `pull` = `fetch` + automatically merges those changes into what you're currently on. Use `pull` when you want to update your current branch (e.g., updating your local `main` after merging a PR on GitHub).

### Checking out someone else's branch (e.g., reviewing a Cloud Agent's PR)
```bash
git fetch origin
git checkout branch-name-from-github
```
Fetch first so Git knows the branch exists, then checkout to actually switch to it locally.

### Undoing / cleaning up (good to know, use carefully)
```bash
git restore --staged filename.py    # un-stage a file (after git add, before commit)
git restore filename.py             # discard uncommitted changes to a file (careful — permanent)
git branch -d branch-name           # delete a local branch (only if already merged)
git branch -D branch-name           # force-delete a local branch (even if not merged — careful)
```

### Comparing changes
```bash
git diff                    # see unstaged changes (what you've edited, not yet added)
git diff --staged           # see staged changes (what's about to be committed)
```

### Ignoring files permanently
```bash
echo "__pycache__/" > .gitignore     # create/overwrite with one ignored pattern
echo "*.log" >> .gitignore           # APPEND another pattern (note: >> not >, or you'll erase the file)
```

### Common typo traps (all seen firsthand this session)
| Typo | Problem |
|---|---|
| `git add.` | Missing space — not a real command |
| `git commit "message"` | Missing `-m` flag — Git thinks "message" is a filename |
| `git push --set-upstream orgin branch` | Misspelled `origin` |
| `git checkout -b existing-branch` | `-b` fails if the branch already exists — drop `-b` to just switch |

### Full real-world sequence, start to finish (what you actually did across Modules 6.5–9)
```bash
git checkout -b my-feature-branch          # 1. create a branch for new work
# ... make your code changes ...
git add .                                  # 2. stage everything
git commit -m "describe the change"        # 3. commit locally
git push --set-upstream origin my-feature-branch   # 4. push + link to GitHub (first time only)
# ... open a PR on GitHub, get it reviewed/merged ...
git checkout main                          # 5. switch back to main
git pull                                   # 6. pull down the now-merged changes
```

---

## How to talk about this on your resume / in interviews

**Don't claim you're a software engineer from this alone** — be precise about what this training gives you, since overclaiming is easy to catch out in an interview. Here's how to frame it honestly and strongly.

### Resume bullet point options (pick based on your actual role/target)

**If applying for a role that touches development workflows (PM, QA, DevOps-adjacent, technical support, etc.):**
> Hands-on experience using GitHub Copilot (Chat, Agent Mode, CLI) to accelerate development workflows, including automated testing (pytest) and Git/PR-based collaboration in a GitHub Codespaces environment.

**If applying for a more technical/engineering-adjacent role:**
> Practical experience with AI-assisted development using GitHub Copilot — writing and reviewing Copilot-generated Python code, building automated test suites with pytest, and managing feature branches through pull requests. Configured project-level Copilot custom instructions to enforce team coding standards.

**Skills section additions (only list what you've actually done):**
- GitHub Copilot (Chat, Agent Mode, CLI)
- Python (basic — function writing, type hints, reading/debugging tracebacks)
- pytest (writing and running automated tests)
- Git & GitHub (branches, commits, pull requests)
- *(add once completed)* GitHub Actions / CI-CD pipelines

### What NOT to claim
- Don't say "proficient in Python" if this is your only exposure — say "AI-assisted Python development" or "foundational Python."
- Don't claim "CI/CD engineering experience" until you've actually built and run a working GitHub Actions workflow (Module 7) — right now you understand the concept, not the practice.
- Don't overstate Agent Mode/CLI as if you built something from scratch — be honest it was AI-assisted, and instead emphasize your **review and verification discipline** (catching unrequested logic, proving tests work by breaking code) — that's a genuinely valuable, differentiated skill to highlight, since many people just accept AI output blindly.

### The strongest thing to say in an interview
If asked about this experience, the strongest answer isn't "I used Copilot to write code" — it's:

> "I learned to treat AI-generated code the way you'd treat a junior developer's pull request — I reviewed every suggestion, verified claims by actually running tests, and proved test coverage was real by intentionally introducing bugs and confirming they were caught. I also learned where AI tools set safety boundaries, like Copilot CLI refusing to run commands without explicit permission in non-interactive mode."

This signals judgment and rigor, not just tool familiarity — which is what actually differentiates candidates in AI-assisted-development hiring right now.

### A tip for later
Once you finish through Module 9, your actual portfolio piece is the **`copilot-practice` repo itself** — a real GitHub repo showing branches, PRs, passing CI checks, and commit history. Link it directly on your resume/LinkedIn once it's in good shape; a real, browsable repo is far more convincing than any bullet point.

---

*This guide will be updated as we complete each remaining module — just ask and I'll add the next section.*
