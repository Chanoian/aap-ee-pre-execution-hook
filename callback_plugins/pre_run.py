from ansible.errors import AnsibleError
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

            # Print stdout lines
            if result.stdout:
                for line in result.stdout.splitlines():
                    self._display.display(f"SCRIPT: {line}")

            # Print stderr lines
            if result.stderr:
                for line in result.stderr.splitlines():
                    self._display.error(f"SCRIPT ERR: {line}")

                # Fail the job template
                raise AnsibleError("Pre-run script reported errors")

        except Exception as e:
            raise AnsibleError(f"Failed to run pre script: {e}")
