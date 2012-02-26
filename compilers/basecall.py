import sublime
import sublime_plugin
import urllib2
import threading

class BaseCall(threading.Thread):

    def __init__(self, sel, string, timeout, level, rm_new_lines):
        self.sel = sel
        self.original = string
        self.timeout = timeout
        self.result = None
        self.level = level
        self.rm_new_lines = rm_new_lines
        threading.Thread.__init__(self)

    def exec_request(self):
        return

    def run(self):
        try:
            self.result = self.exec_request()
        except (urllib2.HTTPError) as (e):
            sublime.error_message('%s: HTTP error %s contacting API' % (__name__, str(e.code)))
        except (urllib2.URLError) as (e):
            sublime.error_message('%s: URL error %s contacting API' % (__name__, str(e.code)))
