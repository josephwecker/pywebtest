# webtester
#
# Class and framework for parsing and running a test, giving appropriate
# feedback and results.
#
# Author: Joseph Wecker
# Copyright: 2009 Joseph Wecker
#

class WebTester():
    def __init__(self):
        pass

    def load_script(self, script):
        self.script = script
        parse_result = self._parse_check(script)
        
