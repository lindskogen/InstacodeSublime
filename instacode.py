import sublime
import re
import sublime_plugin
import webbrowser
import urllib.parse


class InstacodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        syntax = self.clean_syntax(view.settings().get('syntax'))
        text = view.substr(sublime.Region(0, view.size()))
        self.submit_code(text, syntax)

    def submit_code(self, text, syntax):
        url = "http://instacod.es/?post_code=" + urllib.parse.quote(text) + "&post_lang=" + urllib.parse.quote(syntax)
        webbrowser.open(url)

    def clean_syntax(self, syntax):
        match = re.search('\/(\w+)\.tmLanguage', syntax).group(1)
        return match
