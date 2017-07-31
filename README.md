# Change Version Files
A quick script I wrote using OOP to quickly change version files as it was getting quite boring doing one by one (and also because I wanted to practice some OOP).

Usage:
Change the paths dictionary to each one of the paths in which your '__init__.py' files with your version control are (wherever it's written __version__). Only write the path to the folder in which those files are and the script will append '__init__.py' itself (for most systems it should make your life a little bit easier).


## Tips
When in doubt, you can quickly diff both versions to check the changes ("git diff").
It's very easy to use with git version control, basically only requiring an addition of all files changed (usually verify them first) then committing/pushing to the repo.


### Comments
This was probably something useful for my day-to-day with the systems I work with and it's 99% likely that someone has already written something (better) for the same purpose. I mostly wrote it for fun and to automate a very boring task. All comments and suggestions are welcome :)

I haven't created an automatic search for these files yet but once I do its implementation will be made as an optional feature, as for some systems it's not always wanted to change all the existing version files.

Next steps for this script will also include choosing which systems from the paths dictionary to change at a time.
