Imagine having a piece of code you want to expose to the world by publishing it to pypi with poetry.
You dont want to keep track of your version inside of the `pyproject.toml`, but instead use SBOT and git tags.
You can keep the `version` tag in the `pyproject.toml` file pointing at `0.0.0` - it never needs to change in the repository.

The flow is quite simple.
1. On each push to `main`, we use SBOT to check wheter we need a major/minor/or patch release. `sbot update version`
2. SBOT will create the apropriate tag on git. `sbot release version && sbot push version`
3. We get the current version via SBOT and store it in a variable. `$version = sbot get version`
4. We can now set the sbot version from the variable with the poetry version command. `poetry version {$version}`
5. The version is now set in the *pipeline* `pyproject.toml` (no need to commit it) and we can publish the new version of our package to pypi. `poetry publish`
6. All done!

