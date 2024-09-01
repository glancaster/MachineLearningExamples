# git

install git

## initial

`git config --global user.name "username"`
`git config --global user.email "username.user@example.com"`

## working

`git status`

- .gitignore to track which files/folders to ignore

`git add`

- {file} -> for a specific file
- {.} -> all files

`git commit -m {message}`

`git diff`

- {--staged} -> between staging and last commit

`git log`

- {-p} -> differences
- {--stat} -> shorter -p

# github

add ssh key to your github

## create repository

follow steps after clicking "new repository" to make a new one
clone to local to work locally

- `git clone {https/ssh}`

`git push` -> transfer changes
`git pull` -> get latest
