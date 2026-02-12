Team Forking & Upstream Sync Guide
🎯 Goal

This guide explains how our team should:

Fork the main repository properly

Keep their fork updated automatically or easily

Avoid constantly running git pull

Work safely without pushing directly to the main repository

This ensures:

The main repository stays clean

Everyone stays updated

Collaboration is organized and professional

📌 Project Structure Overview

We follow this model:

Main Repository (Upstream)
        ↓
   Team Member Fork
        ↓
 Local Clone (Your Machine)


Upstream → The official project repository

Fork → Your personal copy on GitHub

Local Clone → The version on your computer

🛠 Step 1 — Fork the Repository

Go to the main repository page.

Click Fork (top-right corner).

Select your GitHub account.

Now you have:

github.com/your-username/project-name


This is your personal copy.

🖥 Step 2 — Clone Your Fork (NOT the main repo)

Clone your fork to your local machine:

git clone https://github.com/your-username/project-name.git
cd project-name

🔗 Step 3 — Connect to the Upstream Repository (IMPORTANT)

You must connect your fork to the original repository.

Add the upstream remote:

git remote add upstream https://github.com/original-owner/project-name.git


Verify:

git remote -v


You should see:

origin    https://github.com/your-username/project-name.git
upstream  https://github.com/original-owner/project-name.git


Now your fork knows where the main project lives.

🔄 How to Update Your Fork (Manual Method)

Whenever the main repository updates:

git fetch upstream
git checkout main
git merge upstream/main
git push origin main


This:

Gets new changes from main repo

Merges them into your fork

Pushes updated version to your GitHub fork

🚀 Easy Update Method (GitHub UI)

Instead of terminal:

Go to your fork on GitHub

Click "Sync fork"

Click "Update branch"

This pulls changes from upstream into your fork automatically.

No git pull needed locally unless you're updating your machine.

🤖 Automatic Sync (Recommended for Team)

We can automate syncing using GitHub Actions.

Create this file in your fork:

.github/workflows/sync.yml


Paste:

name: Sync Fork

on:
  schedule:
    - cron: "0 */6 * * *"   # every 6 hours
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Sync with upstream
        run: |
          git remote add upstream https://github.com/original-owner/project-name.git
          git fetch upstream
          git checkout main
          git merge upstream/main
          git push origin main


Then:

Go to Actions tab

Enable workflows

Now your fork will auto-update every 6 hours.

🧠 Important Rules for Team
❌ DO NOT:

Push directly to upstream repository

Work directly on main

Merge without syncing first

✅ ALWAYS:

Before starting work:

git fetch upstream
git merge upstream/main


Or use Sync Fork button.

🌿 Proper Development Workflow
1️⃣ Sync First
git fetch upstream
git merge upstream/main

2️⃣ Create a Feature Branch
git checkout -b feature/my-feature

3️⃣ Work Normally
git add .
git commit -m "Added new feature"
git push origin feature/my-feature

4️⃣ Open Pull Request

From:

your fork → upstream main


The team lead reviews and merges.

🔐 Why This Workflow Is Important
Benefit	Why It Matters
No accidental overwrites	Main repo stays stable
Everyone stays updated	No outdated code
Clean PR system	Easier review
Professional workflow	Industry standard
❓ Can We Force Forks to Stay Updated?

No.

GitHub forks are independent repositories.

We cannot:

Force updates

Push to someone else's fork

Control their copy

We can only:

Provide workflow instructions

Provide sync automation

Require updated branch before PR

🏷 Best Practice for Team Projects

To minimize conflicts:

Protect main branch in upstream

Require pull request before merging

Require branch to be up to date before merge

Use version tags (v1.0.0, v1.1.0)

Maintain a CHANGELOG.md

🧩 Alternative Strategy (If You Want Zero Forking)

If the goal is simply "everyone stays updated":

Instead of forking, use:

A single repository

Add members as collaborators

Use feature branches

Protect main

This is better for small teams.

Forking is better for:

Open-source

External contributors

Large distributed teams

📌 Recommended Setup For Our Team

If this is a closed team project:

👉 Do NOT fork
👉 Use branches inside one shared repository

If this is semi-open or distributed:

👉 Fork + upstream sync + PR workflow

🎯 Final Summary
Action	Required?
Fork main repo	✅ Yes
Add upstream remote	✅ Yes
Sync before work	✅ Always
Create feature branches	✅ Yes
Use PR to merge	✅ Yes
Direct push to main	❌ Never
🏁 End Result

With this system:

The main project remains stable

Everyone can work independently

Forks stay updated

No unnecessary git pull chaos

Workflow is industry-level professional

If you'd like, I can also create:

A simplified version for beginners

A diagram version

A version specific to your FastAPI + React structure

Or a team policy document with rules and enforcement steps
