#!/usr/bin/env bash
set -euo pipefail
# markdown 원고를 docx/pdf로 변환 (인용 처리 포함)
pandoc docs/manuscript.md -o docs/manuscript.docx --citeproc
pandoc docs/manuscript.md -o docs/manuscript.pdf  --pdf-engine=xelatex --citeproc
