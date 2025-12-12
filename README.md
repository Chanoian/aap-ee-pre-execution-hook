# AAP EE Pre-Execution Hook

This project demonstrates how to use an Ansible callback plugin to run a pre-execution check script before any playbook tasks are executed.

## Mechanism

The `pre_run` callback plugin hooks into the `v2_playbook_on_start` event. This ensures the check runs immediately when the playbook starts.

### Execution Flow

1.  **Trigger**: The callback is triggered automatically when `ansible-playbook` starts.
2.  **Script Execution**: It executes the python script located at `/usr/local/bin/my_script.py`.
3.  **Output Handling**: Standard output from the script is displayed with the `SCRIPT:` prefix.
4.  **Error Handling**:
    *   If the script returns a non-zero exit code or produces output on `stderr`, the callback logs the error (`SCRIPT ERR:`).
    *   It then forcibly terminates the Ansible process using `os.kill(1, signal.SIGTERM)` to prevent the playbook from continuing.
