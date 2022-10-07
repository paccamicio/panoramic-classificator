from os import getenv

from dotenv import load_dotenv

# loads the .env file
load_dotenv()

# global variables
PATH_CLASSIFIER = getenv('PATH_CLASSIFIER')
CLASSES_CLASSIFIER = ["Not panoramic", "Panoramic"]



