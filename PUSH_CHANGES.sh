#!/bin/bash

# Checkout the develop branch
git checkout develop

# Pull the latest changes from remote develop branch
git pull origin develop

# Merge develop into main
git checkout main
git merge develop

# Push main to remote
git push origin main
