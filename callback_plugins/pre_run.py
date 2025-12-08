from ansible.plugins.callback import CallbackBase
from ansible.errors import AnsibleError
import subprocess

class CallbackModule(CallbackBase):
    CALLBACK_NAME = "pre_run"
    CALLBACK_VERSION = 2.0

    def v2_playbook_on_start(self, playbook):

        result = subprocess.run(
            ["python3", "/usr/local/bin/my_script.py"],
            capture_output=True,
            text=True
        )

        if result.stdout:
            for line in result.stdout.splitlines():
                self._display.display("SCRIPT: " + line)

        if result.stderr or result.returncode != 0:
            for line in result.stderr.splitlines():
                self._display.error("SCRIPT ERR: " + line)
            self.abort_job()


    def abort_job(self):
        
        raise AnsibleError("Pre-run script failed")