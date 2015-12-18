Pushing code to Github
======================

To Contribute to the codebase (This is an example using Gamesman5 repository)

Make sure you clone the repository with the following URL:

$ git clone git@github.com:GamesCrafters/Gamesman5.git

Then, when you want to add to the project, make a branch.

$ git branch <your-branch>

$ git checkout <your-branch>

Now, you will have some local changes to your branch. When you want to push to the github repository (which you should do frequently), run the following command:

$ git push origin <your-branch>

As you work, some changes may be made to the master branch. In order to incorporate these changes into your branch, run the following commands.

$ git checkout <your-branch> \# to make sure you are on your own branch

$ git fetch origin

$ git merge origin/master

This will then add several commits to your local copy, at which pount you should run:

$ git push origin <your-branch>

When you finally want to add your changes to the main repository, submit a pull request.
