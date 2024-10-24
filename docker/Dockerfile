FROM python:3.11-alpine3.18

# Setup base
RUN \
    apk add --no-cache \
        git \
    \
    && pip3 install \
        --no-cache-dir \
        --prefer-binary \
        --find-links "https://wheels.home-assistant.io/musllinux/" \
        repository-updater==1.3.0

# Entrypoint
ENTRYPOINT ["repository-updater"]

# Labels
LABEL \
    maintainer="Vioneta <admin@vioneta.com>" \
    org.opencontainers.image.title="Repository Updater" \
    org.opencontainers.image.description="Tool for automatically updating Vioneta Agro add-on repositories." \
    org.opencontainers.image.vendor="Vioneta Agro Community Add-ons" \
    org.opencontainers.image.authors="Vioneta <admin@vioneta.com>" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.url="https://github.com/Vioneta/repository-updater" \
    org.opencontainers.image.source="https://github.com/Vioneta/repository-updater" \
    org.opencontainers.image.documentation="https://github.com/Vioneta/repository-updater/blob/main/README.md"
