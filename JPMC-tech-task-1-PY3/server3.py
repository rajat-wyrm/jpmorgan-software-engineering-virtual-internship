################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

#from itertools import izip
from random    import normalvariate, random
from datetime  import timedelta, datetime

import csv
import dateutil.parser
import os.path

import operator
import json
import re
import threading

#from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import http.server
from socketserver   import ThreadingMixIn

################################################################################
#
# Config

# Sim params

REALTIME    = True
SIM_LENGTH  = timedelta(days = 365 * 5)
MARKET_OPEN = datetime.today().replace(hour = 0, minute = 30, second = 0)

# Market parms
#       min  / max  / std
SPD  = (2.0,   6.0,   0.1)
PX   = (60.0,  150.0, 1)
FREQ = (12,    36,   50)

# Trades

OVERLAP = 4

################################################################################
#
# Test Data

def bwalk(min, max, std):
    """ Generates a bounded random walk. """
    rng = max - min
