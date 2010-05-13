#!/usr/bin/env python
# encoding: utf-8
"""
skype.py

Created by Adam Hitchcock on 2010-05-13.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import foursquare
import json
from optparse import OptionParser, OptionGroup

#stores passwords
import street_cred as cred


fs = foursquare.Foursquare(foursquare.BasicCredentials(cred.u, cred.p))
j=""

help_message = '''
The help message goes here.
'''

def setup_options(args):
    """for help see: http://docs.python.org/library/optparse.html#module-optparse"""
    parser = OptionParser()
    
    ## uncomment to specify number of args
    # expected_arg_count = 2
    # if len(args) != expected_arg_count:
    #     parser.error("incorrect number of arguments")
    
    ## Normal options
    parser.add_option("-q", "--quiet", action="store_false", dest="verbose", default=True, help="don't print status messages to stdout")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="Displays verbose output")
    
    ## Grouped options
    group_four = OptionGroup(parser, "Foursquare")
    group_four.add_option("-c", "--checkin", action="store_true", dest="first_group", default=False, help="first group flag")
    group_four.add_option("-u", "--username", action="store", dest="password", default=None, help="set password")
    group_four.add_option("-p", "--password", action="store", dest="username", default=None, help="set username")
    # group_four.add_option("-v", "--vid")
    
    
    ## Workflows
    group_flow = OptionGroup(parser, "Workflows")
    group_flow.add_option("--home", action="callback", callback=lambda *args:fs.checkin(vid='1026020'), help="Home checkin")
    group_flow.add_option("--skype", action="callback", callback=lambda *args:fs.checkin(vid='1026020'), help="Skype checkin")
    group_flow.add_option("--olark", action="callback", callback=lambda *args:fs.checkin(vid='2491212'), help="Olark checkin")
    
    parser.add_option_group(group_four)
    parser.add_option_group(group_flow)
    
    return parser.parse_args() # returns (options, args)

def main(argv=None):
    if argv is None:
        argv = sys.argv
        
    (options, args) = setup_options(argv[1:])
    
if __name__ == "__main__":
    sys.exit(main())