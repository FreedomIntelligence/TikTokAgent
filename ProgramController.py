import subprocess
import time
import os
import json
import sys
import io
import argparse

"""Input Format
python controller1.py --counter ___ --address "address to MobileAgent-main" --grounding "groundingdino path" --description "demographic description --adb "adb path" --api "api key"
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--counter", type=int)
    parser.add_argument("--address", type=str)
    parser.add_argument("--grounding", type=str)
    parser.add_argument("--adb", type=str)
    parser.add_argument("--api", type=str)
    parser.add_argument("--description", type=str)
    args = parser.parse_args()
    return args
def run_conda_command(command, address):
    try:
        # Activate the environment and run the command
        full_command = f'conda activate mobileagent && cd {address} && {command}' #You can change mobileagent to the name of your virtual environment or delete it if it isnt a conda environment
        result = subprocess.run(full_command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        print(f"Error Output: {e.stderr}")

def create_folder(base_path, folder_name):
    # Construct the full path for the new folder
    path = os.path.join(base_path, folder_name)
    
    try:
        # Create the folder
        os.makedirs(path, exist_ok=True)
        print(f"Folder created successfully at: {path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def modify_string_in_function(file_path, old_string, new_string):
    # Read the contents of the file
    lines = read_file(file_path)

    # Modify the specific string within the function
    modified = False
    for i, line in enumerate(lines):
        if old_string in line:
            lines[i] = line.replace(old_string, new_string)

    # Write the modified contents back to the file
    write_file(file_path, lines)

def create_json_file(file_path, data):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write data to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"JSON file created successfully at: {file_path}")

if __name__ == "__main__":
    args = get_args()
    address = args.address
    counter = args.counter
    max = counter + 70
    file_path = address + "\\run.py" 
    base_path = address + "\\results" 
    initial_data = {}
    while counter<max: 
        folder_name = "test" + str(counter)
        create_folder(base_path, folder_name)
        json_file_path = base_path + "\\" + folder_name + "\\data.json"
        create_json_file(json_file_path, initial_data)
        Demographic_Description = args.description 
        GroundingDinoPath = args.grounding 
        API_KEY = args.api 
        ADB_PATH = args.adb 
        run_conda_command('python run.py --grounding_ckpt ' + GroundingDinoPath + ' --adb_path ' + ADB_PATH + ' --api "' + API_KEY + '" --instruction "You are on the home screen of the android phone. There you will see the Tiktok application. Please tap it to open it. Once you are there, you will be on the For You page. There you will find short videos, and live videos that are labeled as LIVE now. If you see a video that is labeled as LIVE now (you will either see a red/pink box with the words LIVE now, or you will see a line that says Tap to watch LIVE), please scroll to the next video immediately, just scroll down as soon as you see it. To scroll in any video, use the page down scroll. You MUST only use the page down scroll when you are in the TikTok app. Do NOT use the page up option. Now if you see a short video, when you are watching the short video, please be on the lookout to see if the video falls into any of these categories (crime, violent/harmful, sexual, self-harm, drugs) based on the given flagging criteria. Here are the criteria for flagging a video as each category. Flagging a video as sexual involves identifying various cues that indicate the content is of a sexual nature. These include nudity, sexual gestures, provocative clothing,sexualized poses, explicit language, and sexual conversations that imply sexual context. The setting, behavior, and content focus are critical, such as environments typically associated with sexual activity, actions implying sexual intent, and content aimed at arousing the viewer. For example, women wearing tight clothes and showing parts of the body such as cleavage or the butt, would be considered sexual. Flagging a video as displaying self-harm involves identifying various visual and contextual cues that indicate the content depicts or promotes self-injurious behavior. Visual cues include scenes of individuals inflicting harm on themselves, such as cutting, burning, or hitting. For example, a person shown with visible wounds or engaging in actions that cause injury to themselves would be considered indicative of self-harm. It can also encompass on screen descriptions that discuss or encourage self-harm, such as someone describing their self-harm experiences or giving instructions on how to self-harm. Contextually, the setting, behavior, and content focus are critical, such as environments typically associated with self-harm, actions implying self-injury, and content aimed at normalizing or encouraging self-harm behavior. Flagging a video that involves drugs or drug use involves identifying various visual and contextual cues that indicate the content is related to illegal substances. Visual cues include the presence of drugs, drug paraphernalia, or individuals consuming drugs. For example, scenes showing people smoking, injecting, or ingesting substances would be considered indicative of drug use. It can also include on screen instructions, for example, the text shown on the video may describe the effects of drug use or provide information on obtaining drugs. Contextually, the setting, behavior, and content focus are critical, such as environments typically associated with drug use, actions implying drug consumption, and content aimed at promoting or normalizing drug use. Flagging a video as violent and/or harmful involves identifying various visual and contextual cues that indicate the content is of a violent and/or harmful nature. Visual cues include physical altercations, use of weapons, blood, injuries, and people getting hurt in general. For example, scenes showing people fighting, brandishing knives or guns, or displaying wounds would be considered violent. Something like a car crash could be considered harmful. It can also include text for example, the text shown on the video may describe violent acts or incite violence, or describe something or someone inflicting or receiving an injury. Contextually, the setting, behavior, and content focus are critical, such as environments typically associated with violence and/or harm, actions implying aggressive intent, and content aimed at glorifying or promoting violent and/or harmful behavior. Flagging a video as involving crime involves identifying various visual and contextual cues that indicate the content depicts or promotes criminal activities. Visual cues include scenes of illegal actions such as theft, vandalism, assault, or drug trafficking. For example, individuals breaking into a property, engaging in physical altercations, or exchanging illegal substances would be considered criminal. It can also include descriptions that are on the video, for example, the text shown on the video may describe how to commit a crime or boast about criminal activities. Contextually, the setting, behavior, and content focus are critical, such as environments typically associated with criminal activity, actions implying illegal intent, and content aimed at glorifying or normalizing crime. If the short video that you viewed fits one or more categories, please pause it immediately and then scroll immediately after. If the video is already paused (white pause triangle in the middle of the screen), then please scroll immediately. If you dont see anything that may seem to fall into any of the categories (crime, violent/harmful, sexual, self-harm, drugs), then please scroll in the fashion of this described person. His/Her description is: ' + Demographic_Description + '(end of description) Please like videos that you think they would like based on the description, and also please if the heart button/like button is already red and if you had previously liked the video that you are currently watching already, then scroll immediately. If the video doesn’t fall into any of the categories (crime, violent/harmful, sexual, self-harm, drugs), or you don’t think they would like the video, or the video has already been liked (red heart and already liked before) or if the video is already paused (white triangle in the middle and previously paused) then please scroll immediately."',address)


        old_string = f"C:\\\\Users\\\\sneez\\\\Downloads\\\\TikTokAgent\\\\MobileAgent-main\\\\results\\\\test{counter}\\\\data.json" #change these to fit in the format of your path
        new_string = f"C:\\\\Users\\\\sneez\\\\Downloads\\\\TikTokAgent\\\\MobileAgent-main\\\\results\\\\test{counter+1}\\\\data.json"
        modify_string_in_function(file_path, old_string, new_string)

        old_string = f"C:\\\\Users\\\\sneez\\\\Downloads\\\\TikTokAgent\\\\MobileAgent-main\\\\results\\\\test{counter}"
        new_string = f"C:\\\\Users\\\\sneez\\\\Downloads\\\\TikTokAgent\\\\MobileAgent-main\\\\results\\\\test{counter+1}"
        modify_string_in_function(file_path, old_string, new_string)

        counter += 1
