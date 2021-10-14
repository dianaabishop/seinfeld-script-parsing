from os import walk
import json


combined_question_list = [{"label":"whatis", "question": "what's"}, {"label": "whatis", "question":"what is", "question_word":"what", "aux":"is"}]
punctuation = [".","?","!"]

def get_file_names():
    '''
    gets file names in scripts dir
    returns [] if no file
    '''
    path = "./scripts"
    filenames = next(walk(path), (None, None, []))[2] 
    return filenames


def main():
    script_file_names = get_file_names()

    f = open('combined_question_list.json',)
    combined_question_list = json.load(f)

    for path in script_file_names:
        for q in combined_question_list: 
            # open file and read all lines into contents
            with open(path, "r") as f:
                contents = f.readlines()

            idx_list = []
            num_occurances = 0
            # iterate through the file lines, check against the question words/phrases
            # if the question is found, note the index and increment the num occurances
            for idx, c in enumerate(contents):
                if q["question"] in c.lower(): 
                    num_occurances = num_occurances + 1
                    idx_list.append({"index":idx, "num_occ":num_occurances})
                    
                split_line = c.split(" ")
                # check that there is no punctuation and that the final word is the question word
                if q.get("question_word"," ") in split_line[-1] and not any(map(split_line[-1].__contains__, punctuation)):
                    # check if last word is in the single question word list
                    empty_line = True
                    count = 1
                    while empty_line:
                        line = c[idx+count]   
                        if line:
                            if q.get("aux", " ") in line[0]:
                                idx_list.append({"index":idx, "num_occ":num_occurances})
                                empty_line = False
                        else: 
                            count += 1

            # insert label into text file on relelvant row
            # in the format: ***whatis1 (e.g. question + occurance #)
            add_to_index = 0
            for idx in idx_list:
                contents.insert(idx["index"]+add_to_index, "***{}{}".format(q["label"],idx["num_occ"]))
                add_to_index += 1

            with open(path, "w") as f:
                contents = "".join(contents)
                f.write(contents)

    # if the last word in a line is a question word, have
    # to check the first word of the next line
    
    # need to remove empty newlines if there wasn't punctuation at the end of the previous line, 
    # or just check when doing the multiline check
    # add some logic to ignore it if it gets run more than once
    # add some logic to add new question combos with command line arguments?

if __name__ == '__main__':
	main()