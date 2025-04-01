

import os
import json
import time
import pandas as pd
import numpy as np
from datetime import datetime
import colorama
from colorama import Fore, Style, Back
import nice_funcs as n
import argparse
import sys
import traceback
import random
from termcolor import colored   
import schedule

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

colorama.init(autoreset=True)

pd.set_option('display.float_format', '{:.2f}'.format)

#config
DATA_DIR = 'MalasKhan/Auto-liquidations/data'
