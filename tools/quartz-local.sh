#!/usr/bin/env bash
set -euo pipefail

mode="${1:-build}"
if [[ "$mode" != "build" && "$mode" != "serve" ]]; then
  echo "usage: $0 [build|serve]" >&2
  exit 2
fi

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
quartz_dir="${QUARTZ_DIR:-${TMPDIR:-/tmp}/agentic-work-atlas-quartz}"

if [[ ! -d "$quartz_dir/.git" ]]; then
  git clone --depth 1 --branch v4 https://github.com/jackyzha0/quartz "$quartz_dir"
fi

cp "$root/quartz.config.ts" "$quartz_dir/"
cp "$root/quartz.layout.ts" "$quartz_dir/"

if [[ -d "$root/quartz-overrides/styles" ]]; then
  cp "$root/quartz-overrides/styles/"*.scss "$quartz_dir/quartz/styles/"
fi

if [[ ! -d "$quartz_dir/node_modules" ]]; then
  npm --prefix "$quartz_dir" ci
fi

cd "$quartz_dir"
if [[ "$mode" == "serve" ]]; then
  npx quartz build --serve -d "$root"
else
  npx quartz build -d "$root"
fi
