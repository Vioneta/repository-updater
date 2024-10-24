#!/usr/bin/env bash
declare -a options

options+=(--token "${INPUT_TOKEN:-}")

if [[ -n "${INPUT_REPOSITORY:-}" ]]; then
  options+=(--repository "${INPUT_REPOSITORY}")
else
  options+=(--repository "${GITHUB_REPOSITORY}")
fi

[[ -n "${INPUT_ADDON:-}" ]] \
  && options+=(--addon "${INPUT_ADDON}")

[[ "${INPUT_FORCE,,}" = "true" ]] \
  && options+=(--force)

# Output version
repository-updater --version

# Update!
exec repository-updater "${options[@]}"
