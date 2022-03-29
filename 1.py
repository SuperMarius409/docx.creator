import re
#import docx
import wikipedia
#from docx import Document
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import get 
import urllib.request
import wikipedia
import requests
import time
import glob
import shutil
import os

link = "https://eduboom.ro/lectii-pe-materii/matematica/5-clasa"
print(link)
html = urlopen(link)
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all()
print(images)