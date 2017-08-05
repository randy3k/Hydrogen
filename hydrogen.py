import sublime
import sublime_plugin
from .connect import get_connection_files
from .progress_bar import ProgressBar


class ConnectJupyterCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.bar = ProgressBar("Searching for kernels")
        self.bar.start()
        sublime.set_timeout_async(self.run_async, 100)

    def run_async(self):
        self.cfs = get_connection_files(active_only=True)
        self.bar.stop()

        if not self.cfs:
            sublime.message_dialog("No active kernels.")
        else:
            sublime.active_window().show_quick_panel(self.cfs, self.on_select, 100)

    def on_select(self, action):
        if action >= 0:
            print(self.cfs[action])
