'''Converts json to yml given an AWS CLI command as input.
   Run this command from a bash shell, invoking the Python3 interpreter.    
   Example: python3 json2yml.py "aws lambda list-functions"
   Note: the AWS CLI command must be enclosed in double quotes, otherwise
   argv will turn the command into a list.
'''
import yaml
import sys
import json
import subprocess

#Capture the aws CLI command entered in the shell
cmd = sys.argv[1]

# returns output as byte string
returned_output = subprocess.check_output(cmd, shell=True)

#Use json.loads to process the byte string
json_input = json.loads(returned_output)

#Verify if yml safe_dump will take the json_input in the form given
yaml_stream = yaml.safe_dump(json_input, default_flow_style=False)

#save the file
with open("Output.yaml", "w") as text_file:
    text_file.write(yaml_stream)
