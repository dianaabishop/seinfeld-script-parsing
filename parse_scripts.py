from os import walk
import json

PUNCTUATION_LIST = [".","?","!"]

def get_file_names():
    '''
    gets file names in scripts dir
    returns [] if no file
    '''
    path = "./scripts"
    filenames = next(walk(path), (None, None, []))[2] 
    return filenames


def main():
    # script_file_names = get_file_names()
    script_file_names = ["S3_E12.txt"]

    # f = open('combined_question_list.json',)
    f = open('test_question_list.json',)
    combined_question_list = json.load(f)

    label_count_dict = {}

    for file_name in script_file_names:
        for i, q in enumerate(combined_question_list): 

            if not label_count_dict.get(q["label"]):
                label_count_dict[q["label"]] = 0
            # open file and read all lines into contents
            p = './scripts/{}'.format(file_name) if i == 0  else './processed_scripts/{}'.format(file_name)
            with open(p, "r") as f:
                contents = f.readlines()

            idx_list = []
            num_occurances = 0
            # iterate through the file lines, check against the question words/phrases
            # if the question is found, note the index and increment the num occurances
            for idx, c in enumerate(contents):
                utf_string = c.decode('utf-8')
                if q["question"] in utf_string.lower(): 
                    label_count_dict[q["label"]] += 1
                    idx_list.append({"index":idx, "num_occ":label_count_dict[q["label"]]})
                    
                split_line = utf_string.split(" ")
                # check that there is no punctuation and that the final word is the question word
                if q.get("question_word"," ") in split_line[-1] and not any(map(split_line[-1].__contains__, PUNCTUATION_LIST)):
                    # check if last word is in the single question word list
                    empty_line = True
                    count = 1
                    while empty_line:
                        line = contents[idx+count]  
                        if line != "\n":
                            new_split_line = line.strip().split(" ")
                            if q.get("aux", " ") in new_split_line[0]:
                                label_count_dict[q["label"]] += 1
                                idx_list.append({"index":idx, "num_occ":label_count_dict[q["label"]]})
                            empty_line = False
                        else: 
                            count += 1

            # insert label into text file on relelvant row
            # in the format: ***whatis1 (e.g. question + occurance #)
            add_to_index = 0
            for index in idx_list:
                contents.insert(index["index"]+add_to_index, "***{}{}".format(q["label"],index["num_occ"]))
                add_to_index += 1

            with open("./processed_scripts/{}".format(file_name), "w") as f:
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