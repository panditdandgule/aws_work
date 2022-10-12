from email.policy import Policy
import boto3
import json
import os,sys
from boto3.s3.transfer import TransferConfig
import threading
import logging
from ast import literal_eval
import re

file_path='I:\\Scoopons\\AWS\\boto\\pythonboto3\\s3_operations\\inputdata.txt'

def read_file():
    
    with open(r'I:\\Scoopons\\AWS\\boto\\pythonboto3\\s3_operations\\inputdata.txt','r') as f:
        data=f.read()
  
    return data


def stepfunction_exec():
    cmd_str=read_file()
    #print(cmd_str)

 
    sfn_client=boto3.client('stepfunctions',region_name='ap-south-1')
    state_machine_arn='arn:aws:states:ap-south-1:165191621515:stateMachine:MyStateMachine'

    re_str="({.+?\})"
    stats_re = re.compile(re_str, re.MULTILINE | re.DOTALL)

    for match in stats_re.findall(cmd_str):
        response=sfn_client.start_execution(
            stateMachineArn=state_machine_arn,
            input=match)
        print(response)
    print("Successful")
    


if __name__=='__main__':
    
    stepfunction_exec()