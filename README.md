# Book Discovery App

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