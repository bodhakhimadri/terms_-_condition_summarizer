# Git Workflow

## Branch Structure

- main        : Stable production-ready code
- develop     : Integration branch
- feature/*   : Individual feature development

## Workflow Steps

1. Create feature branch from develop
2. Write code and commit locally
3. Push feature branch to GitHub
4. Create Pull Request to develop
5. Leader merges PR into develop
6. All members pull develop

## Rules

- No direct commits to main
- Only leader merges to develop
- One feature per branch
- Always pull before starting work

## Common Commands

git checkout develop  
git pull origin develop  
git checkout -b feature/branch-name  
git add .  
git commit -m "message"  
git push origin feature/branch-name
