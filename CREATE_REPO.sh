# Initialize git repo locally
git init

# Add source code
git add .

# Commit source code
git commit -m "Initial commit"

# Create repo on GitHub
gh repo create dashboard --public --source=. --remote=origin

# Push source to GitHub
git push -u origin main

# Create develop branch
git checkout -b develop
git push -u origin develop

# On GitHub, go to Settings > Branches and add a branch protection rule for main:
# - Require pull request reviews before merging
# - Require status checks to pass before merging
# - Require signed commits
# - Include administrators
