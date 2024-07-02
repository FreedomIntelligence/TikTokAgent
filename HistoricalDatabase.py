import json
import argparse
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filePath", type=str)
    parser.add_argument("--startingNum", type=int)
    parser.add_argument("--part", type=str)
    args = parser.parse_args()
    return args
args = get_args()

text_data = ""
counter = 0
counter1 = 0
for i in range(70):
    file_path = args.filePath + str(args.startingNum + i) + "\\data.json"
    try:

        with open(file_path, 'r') as file:
            data = json.load(file)
            for x in range(5):
                key = str(x+1)
                if key in data and "Thought" in data[key]:
                    #text_data += str(data[key]["Action"]) + "\n"
                    if str(data[key]["Action"]) == "page down":
                        counter += 1
                else:
                    print(f"Missing data for file {i+501}, entry {x+1}")
            key = str(5)

            if key in data and "Action" in data[key]:
                if str(data["5"]["Action"]) != "page down":
                    counter1 += 1
            else:
                print("Missing data")
            
            for x in range(5):
                    key = str(x+1)
                    if key in data and args.part in data[key]:
                        text_data += str(data[key][args.part]) + "\n"
                    else:
                        print(f"Missing data for file {i+args.startingNum}, entry {x+1}")

                    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Invalid JSON in file: {file_path}")

if args.part == "Action":
    print(str(counter+counter1))   
else:
    print(text_data)