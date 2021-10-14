# Seinfeld Script Parsing

### What Does This Do?

### How To Run The Script
Git clone the repository onto your local computer with:
`git clone git@github.com:dianaabishop/seinfeld-script-parsing.git` 

If you haven't used Github before, you will need to do the following on your laptop to allow for this
ssh repo cloning.

1. Go to Github.com > Settings
2. Select `SSH and GPG Keys` from the sidebar menu
3. Press the `New SSH Key` button + give it a title e.g. "Diana's Laptop"
4. Open your terminal and enter `ssh-keygen -t rsa` 
5. This will create a public SSH key on your computer which you can view and copy the contents of by:
```
cat ~/.ssh/id_rsa.pub
```
6. Take the output of the `cat` command and paste the whole string into the `Key` textbox on Github.com and select `Add SSH Key`. 

You should now be all set to clone the repository locally! (e.g. run that first `git clone...` command)

Now you're ready to run the script!
`cd seinfeld-script-parsing` 
`python parse_scripts.py`

This should annotate all of the scripts and write the labeled files to the `processed_scripts` folder


### How to make edits