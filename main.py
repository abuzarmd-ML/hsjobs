import sys
from code.parameters import check_params
from code.data import processData
from code.models import setSeed, trainModel

from code.models import predict
from subprocess import call

if __name__ == '__main__':

    # PARAMETERS
    if check_params(arg=sys.argv[1:]) == 0:
        exit(0)

    # Seed
    setSeed()
    
    # DATA PIPELINE
    processData()

    # Model train 
    trainModel()

    # todo: temporal function here

    # run the telegram bot
    call(["python", "code/chatbot.py"])
    