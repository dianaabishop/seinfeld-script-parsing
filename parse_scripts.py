from os import walk
import json
import argparse

PUNCTUATION_LIST = [".","?","!"]

'''
add command line arguments for passing optional parameters
'''
parser = argparse.ArgumentParser()

parser.add_argument('-t', '--test', action='store', dest='test',
                    required=False, type=bool, metavar='<>',
                    help='Runs the script on a shorter list of questions and one script file')

parser.add_argument('-f', '--file', action='store',dest='file',
                    required=False, type=str, metavar='<>',
                    help='Enter a specific script to run the test on')

results = parser.parse_args()
FILE = results.file
TEST_RUN = results.test

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

    if TEST_RUN:
        script_file_names = [script_file_names[0]]
        f = open('test_question_list.json',)
    else:
        f = open('combined_question_list.json',)

    combined_question_list = json.load(f)

    if FILE: 
        script_file_names = [FILE]

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

    # write the final question counts to a json file in processed_scripts
    with open('./processed_scripts/final_counts.json', 'w') as f:
        json.dump(label_count_dict, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
	main()