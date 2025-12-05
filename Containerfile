FROM registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9 

USER root

# Copy your python script
COPY my_script.py /usr/local/bin/my_script.py
RUN chmod +x /usr/local/bin/my_script.py

# Copy your callback plugin
COPY callback_plugins/ /usr/share/ansible/plugins/callback/

# Ensure Ansible sees the plugin
ENV ANSIBLE_CALLBACK_PLUGINS=/usr/share/ansible/plugins/callback
ENV ANSIBLE_CALLBACKS_ENABLED=pre_run