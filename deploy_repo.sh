#!/bin/bash

cd $(dirname $0)

# reset the state
echo "Resetting..."
rm -rf public
mkdir public
git worktree prune
git worktree add public gh-pages

echo "Removing existing repodata files"
rm -rf public/*/repodata

echo "Copying new files"
cp -Rf REPO/* public/
cat README.md | pandoc -t html --ascii > public/index.html
cp dimension-rpms.repo public/

echo "Publishing..."
cd public && git add --all && git commit -m "Publishing updated repo"
