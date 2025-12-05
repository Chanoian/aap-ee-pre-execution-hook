from ansible.plugins.callback import CallbackBase
import subprocess

class CallbackModule(CallbackBase):
    CALLBACK_NAME = 'pre_run'
    CALLBACK_VERSION = 2.0

    def v2_playbook_on_start(self, playbook):
        self._display.banner("PRE-RUN SCRIPT OUTPUT")

        try:
            result = subprocess.run(
                ["python3", "/usr/local/bin/my_script.py"],
                capture_output=True,
                text=True
            )

            if result.stdout:
                for line in result.stdout.splitlines():
                    self._display.display("SCRIPT: " + line)

            if result.stderr:
                for line in result.stderr.splitlines():
                    self._display.error("SCRIPT ERR: " + line)

        except Exception as e:
            self._display.error(f"Failed to run pre script: {e}")
