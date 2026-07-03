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

*(This module is still in progress — more commands will be added here as we continue: `git add`, `git commit`, `git push`, and opening the PR itself on GitHub.)*

---

## Still to come (will be added to this guide as we go)
- **Module 7 — CI/CD with GitHub Actions:** writing a `.yml` workflow file that auto-runs tests on every push/PR
- **Module 8 — Code Review & Merge:** Copilot-generated PR descriptions, automated code review, resolving comments
- **Module 9 — Cloud Agent:** assigning a GitHub Issue and letting Copilot build + PR it autonomously

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
