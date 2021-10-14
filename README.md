# Seinfeld Script Parsing

### What Does This Do?
This script iterates through the text files contained in the `scripts` directory and annotates them when question word combinations are found (e.g. "what is", "where does"). It gets these question words (and contractions) to check from the `combined_question_list.json` file and keeps count of occurances across script files. 


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

This should annotate all of the scripts and write the labeled files to the `processed_scripts` folder. It also creates a json file with a final count for each question/aux combo in the `process_scripts` dir named `final_counts.json`.

If you would just like to test the script, you can run it in test mode by doing the following. Running the script in test mode will use a limited subset of test questions (contained in test_question_list.json) and only on one file (the first file that is returned from the directory search). 
`python parse_scripts.py --test True`

You can also run the full list of questions on a specific script file by doing the following:
`python parse_scripts.py --file "S1_E1.txt"`

Some potentially useful helper scripts:
* Create empty files - may not be that useful now that they've all be transferred to text already, but I added this so I could create empty files and just paste the text into them. To run:
`./create_files.sh -s SEASON_NUM -n NUM_EPISODES`
e.g. `./create_files.sh -s 1 -n 23` - will create 23 empty text files in the `scripts` folder in the format `S1_E1.txt`

* Delete processed files - this deletes all files from the processed_scripts directory; simple, but helpful for testing. To run:
`./delete_processed_files.sh`
