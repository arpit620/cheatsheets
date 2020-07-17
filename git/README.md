# Git CheatSheet

List of frequently used git commands

## Git Private repo

While cloning a private git repo, use `SSH` instead of `HTTPS` with `git clone` command.

## Git config

Set username and email

``` git
git config --global user.name "name"
git config --global user.email "email"
```

Change git username for specific repository (in case of multiple users)\
`git config credential.username "name"`

Change config using editor\
`git config --global --edit`

Set command line coloring\
`git config --global color.ui auto` 

## Basics

``` git
git status
git add .
git commit -m "Commit message"
git push
```

Show logs & limit to recent logs, pretty logs\

``` git
git log
git log -n
git log --pretty=oneline
```

Command line git workflow\
`git log --oneline --decorate --graph --all` 

Show which files were changed and # of lines modified\
`git log --stat` 

Add a patch (partial file commit) [Details](http://codefoster.com/addpatch/)\
`git add -p <file_name>` 

Delete file from git add\
`git rm <filename>` 

Remove file from git add\
`git reset <filename>` 

Check recent commit\
`git show <commit_id>` 

Discard any file changes before staging\
`git checkout <fileName>` 

Discard all changes\
`git checkout .` 

Unstage files to working area, All files\

``` 
git reset HEAD <filename>
git reset HEAD *
```

Force push repo\
`git push --force origin master` 

Get remote branches/ tags\
`git fetch origin` 

Who changed what and when in <file>\
`git blame <file>` 

Create a new tracking branch based on a remote branch\
`git checkout --track <remote/branch>` 

## Branch

Create new branch\
`git branch <new_branch>` 

Switch branch or move to old commit id\

``` 
git checkout <branch>
git checkout <commit_id>
```

Push uncommited changes to a different branch [Details](https://stackoverflow.com/questions/4746672/put-current-changes-in-a-new-git-branch):
```
git checkout -b my_new_branch
git commit
```

List all branches\
`git branch -av` 

Push to existing branch\
`git push origin <branch>` 

Push new branch to remote\
`git push -u origin <new_branch>` 

Merge branch into HEAD branch, no-ff keeps all commits intact\
`git merge <branch>` 
`git merge --no-ff <branch>` 

Check merge\
`git branch --merged` 

Delete branch\
`git branch -d <branch>` 

## Stash

Move unsaved changes to new branch\

``` 
git stash
git chcekout <branch_2>
git stash pop
```

Other stash commands\

``` 
git stash
git stash list
git stash apply stash@{0}
git stash apply 0
```

Add message to Stash\
`git stash push -m "Message"` 

Drop stash\
`git stash drop 2` 

Stash apply and drop\
`git stash pop 2` 

Clear Stash\
`git stash clear` 

## Revert

* For changes on remote repo
* Create new commits which reflect the old code but doesn't delete the previous commits
* Allows to undo the undo

Revert to last ID\
`git revert HEAD` 

## Reset

* Done on local repo
* Delete unwanted changes completely

Soft reset keeps file in staging area\
Mixed reset keeps file in working area\
Hard reset deletes everything\

``` 
git reset --soft HEAD~2
git reset --mixed HEAD~2
git reset --hard HEAD~2
```

Discard local changes\
`git reset --hard HEAD` 

## Rebase

* Reapply commits on top of another base tip
* Redoing the sequence of changes from one branch to another

`git rebase <branch>` 

## Tags

Show all tags\
`git tag` 

Add a tag\
`git tag -a v1.0 -m "Message"` 

Show specific tag\
`git show v1.0` 

Push tags\
`git push --tags origin master` 

## Squash

Combine multiple commits into one [Details](https://github.com/todotxt/todo.txt-android/wiki/Squash-All-Commits-Related-to-a-Single-Issue-into-a-Single-Commit)\
`git rebase -i HEAD~4` 

In the text editor, replace `pick` with `squash` 

## Git vocab

``` 
Repo -> HEAD
Staged -> Index
Unstaged -> Working
```

## Fixing common mistakes and undoing bad changes

* [Video](https://www.youtube.com/watch?v=FdZecVxzJbk)

``` 
git status
git diff
git checkout calc.py
```

Fix last commit history (Changes history)\
`git commit --amend -m "New Message"` 

Add new file. Want it to be part of last commit\
Add to staging\

Add new file and allow to change commit message\
`git commit --amend` 

### Move commits to different branch

* By mistakes have been making commits to wrong branch
* Need to move commits to a different branch
* Cherry pick a commit

`git log` - Pick commit id to cherry pick\
`git checkout <Feature_branch>` \
`git cherry-pick <commit_id>` - Apply commit to feature branch\

					  - Original commits still exist in master branch\

Remove from master\
`git reset [--soft | --mixed | --hard] <commit_id>` 

To remove untracked file\
`git clean -df` => d/f : directory/ files\

### To get HARD reset commits back

`git reflog` - when you last referenced them

* Get hash of id just before you ran hard reset
* `git checkout <commit_id>` 
* Above still doesn't commmit in any branch, instead is in detached state

``` 
git branch backup
git branch
git checkout master
```

If history changed, id which needs to be reverted\
`git revert <commit_id> ` 

See diff b/w 2 commits\
`git diff <id1> <id2>` 

## Rename a branch

Switch to branch you want to rename:\
`git checkout <old_name>` 

Rename local branch:\
`git branch -m <new_name>` 

Delete old branch on remote:\
`git push origin --delete <old_name>` 

Push new branch:\
`git branch origin -u <new_name>` 

## Gitignore files

One which is shared across developers:\
`.gitignore` 

Personal `gitignore` file [Details](https://medium.com/@dave_lunny/exclude-files-from-git-without-committing-changes-to-gitignore-986fa712e78d):\
`.git/info/exclude` 

List all ignored files:\
`git ls-files --others --exclude-from=.git/info/exclude` 
