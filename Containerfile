FROM registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9 


COPY precheck.py /usr/local/bin/validation/precheck.py
COPY precheck.sh /usr/local/bin/validation/precheck.sh


RUN chmod +x /usr/local/bin/validation/precheck.py \
    && chmod +x /usr/local/bin/validation/precheck.sh

RUN sed -i '/exec \$SCRIPT -- "\${@}"/i /usr/local/bin/validation/precheck.sh "\$@"' \
    /bin/entrypoint
