# Contributing

Please I highly encourage you to follow this guide.

### Setting up the project
1. Clone the repo.
2. Create a virtual enviroment `python3 -m venv env`.
3. Install dependecies `pip3 install -r requirements.txt`.
4. Create a `.env` file.
```
\.env

''''

ALLOWED_ORIGIN = "<allowed url>"
JWT_SECRET_STRING ="<base64 encoded string or a random string is fine>"
DATABASE_URL="sqlite:///./test.db" ## This is the default sqlite please swap out for other databases

''''


````
5. Run the dev server `python3 -m fastapi dev ./app/main.py`.
6. The server should be running at [http://localhost:8000/](http://localhost:8000/)

>**Note:** Depending on the database you are connecting to you may need to to install additional dependecies for the dialect of that database.

### Branching Strategy
Once you have cloned the repo
1. Run `git checkout dev` to switch to the dev branch.
2. Create a new branch with your first name as the label or any other name `git branch <yourname>`.
3. Switch to your personal branch `git checkout <yourname>`.
4. On your personal branch you decide your branching and how you manage it.
5. If creating a feature branch name it with `<yourname/feat>`
6. Once a feature is ready make a PR to dev to merge your code.
>**Note:** You are not to merge any of your personal branches into the dev branch please if you have personal branches merge or squash them before merging with dev.
