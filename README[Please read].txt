# Book Discovery App

#To instructor:

Project requirements:
- python pip
- mysqldb-python
- python flask
- flask wtforms
- peewee orm
- flask-peewee

Why did we use python and why these requirements/dependencies?
We wanted to focus on newer technologies, while still retaining core information
we gained from class.  PHP is quickly becoming an outdated technology (Google, youtube, twitter have switched to python...Facebook is switching to python and C).  We wanted to capitalize the opportunity that this project presented to practice and sharpen our skillsets.  I would like to thank Mrs. Xiomara Casado for keeping an open mind and allowing us to pursue this opportunity.  


Instructions for running:

Once the requirements above are installed, set your mysql settings in config.py to your local mysql settings.

Execute the simple http server by running the following command:  python main.py

Visit [domain.com] or [localhost] : 1933 to enjoy.



You can ignore everything below this line (this is instructions for git, our version control system used in this project).

To get:

```
git clone git@github.com:radicalcakes/bookend.git
```
Then, you must cd into the folder and run this command:

```
source venv/bin/activate
```

You are now all setup.

## General rules

1. Prefer many granular commits over a single, large commit with numerous,
   unrelated changes.

2. Always use informative commit messages.

3. Don't be ashamed to ask for help. :)

## Working on a new feature (if you're comfortable with git's rebase and merge)

1. Create a new branch for your feature, e.x., "facebook_oauth".

    ```
    git checkout -b facebook_oauth
    ```

2. Write awesome code, then add and commit your changes.

    ```
    vim awesome.py
    git add awesome.py
    git commit -m 'added awesome code, taught toaster to feel'
    ```

3. Repeat step 2 until you feel your feature is ready to be integrated into the
   master branch.

4. Pull the latest changes to master and rebase your feature branch.

    ```
    git checkout master
    git pull
    git rebase master facebook_oauth
    ```

5. Resolve rebase conflicts and merge your feature branch into master.

    ```
    git checkout master
    git merge facebook_oauth
    ```

6. Resolve merge conflicts and push the updated master branch to bitbucket.

    ```
    git push
    ```

## Working on a new feature (if you're uncomfortable with git's rebase and merge)

1. Create a new branch for your feature, e.x., "facebook_oauth".

    ```
    git checkout -b facebook_oauth
    ```

2. Write awesome code, then add and commit your changes.

    ```
    vim awesome.py
    git add awesome.py
    git commit -m 'added awesome code, taught toaster to feel'
    ```

3. Repeat step 2 until you feel your feature is ready to be integrated into the
   master branch.

4. Push your branch to github, then ask someone to merge your changes into 
   master.

    ```
    git push origin facebook_oauth
    ```

## Pulling the latest changes

1. Commit or stash your recent changes, if any.

    ```
    git add new_thing.py
    git commit -m 'added new_thing'
    ```

    OR

    ```
    git stash # remember to call "git stash pop" later
    ```

2. Checkout and pull the latest changes to the master branch.

    ```
    git checkout master
    git pull
    ```

3. Checkout your feature branch again, continue writing awesome code.

    ```
    git checkout facebook_oauth
    ```