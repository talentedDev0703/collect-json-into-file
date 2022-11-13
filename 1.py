import json
import glob

read_files = []
for i in range(0, 1001) :
    read_files.append("metadata/gods/" + str(i) + ".json")

#read_files = glob.glob("metadata/gods/*.json")
#read_files = ["metadata/gods/0.json", "metadata/gods/1.json"]
output_list = []


for f in read_files:
    with open(f, "rb") as infile:
        output_list.append(json.load(infile))

all_items = []
for json_file in output_list:
    all_items.append(json_file)

with open("metadata.json", "w") as outfile:
    json.dump(all_items, outfile)
