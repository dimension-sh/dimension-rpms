#!/bin/bash

cd $(dirname $0)

# reset the state
echo "Resetting..."
rm -rf public
mkdir public
git worktree prune
git worktree add -B gh-pages origin/gh-pages

echo "Removing existing files"
rm -rf public/*

echo "Copying new files"
cp -R REPO/* public/
pandoc -t html --ascii README.repo.md > public/index.html

echo "Publishing..."
cd public && git add --all && git commit -m "Publishing updated repo"
git push origin
