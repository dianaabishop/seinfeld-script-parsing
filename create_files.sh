# to run ./create_files.sh -s SEASON_NUM -n NUM_EPISODES
# example: ./create_files.sh -s 4 -n 24 
# this would create S4_E1.txt through S4_E24.txt (empty files)

while getopts s:n: flag
do
    case "${flag}" in
        s) season_num=${OPTARG};;
        n) num_episodes=${OPTARG};;
    esac
done

for (( i = 1 ; i <= ${num_episodes} ; ++i )) ; do
    touch scripts/S${season_num}_E$i.txt
done
