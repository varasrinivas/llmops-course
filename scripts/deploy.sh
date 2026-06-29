#!/usr/bin/env bash
#
# deploy.sh — Build and deploy the Production LLMOps course to S3.
#
# No secrets or account IDs live in this file. AWS credentials come from your
# environment / profile (e.g. `aws configure`, AWS_PROFILE, or an IAM role).
# Override any of the settings below with environment variables, e.g.:
#
#   BUCKET=my-bucket PREFIX=courses/llmops ./scripts/deploy.sh
#   DISTRIBUTION_ID=XXXX ./scripts/deploy.sh        # also invalidate CloudFront
#
set -euo pipefail

# ── Settings (override via env) ──────────────────────────────────────
BUCKET="${BUCKET:-agenticai.varasrinivas.com}"   # target S3 bucket (public site host)
PREFIX="${PREFIX:-courses/llmops}"               # key prefix within the bucket
DISTRIBUTION_ID="${DISTRIBUTION_ID:-}"           # optional CloudFront dist id for cache invalidation

# ── Paths ────────────────────────────────────────────────────────────
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$HERE"
S3="s3://${BUCKET}/${PREFIX}"

echo "==> Regenerating course and map from module data"
python scripts/generate_course.py
python scripts/generate_map.py

echo "==> Writing redirect index (directory URL -> course map)"
REDIRECT="$(mktemp)"
trap 'rm -f "$REDIRECT"' EXIT
cat > "$REDIRECT" <<'HTML'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Production LLMOps — AI Application Lifecycle</title>
<meta http-equiv="refresh" content="0; url=llmops-course-map.html">
<link rel="canonical" href="llmops-course-map.html">
</head>
<body style="font-family:system-ui,sans-serif;background:#14161b;color:#e9e5dc;padding:40px">
Redirecting to the <a href="llmops-course-map.html" style="color:#7fb89c">Production LLMOps course map</a>…
</body>
</html>
HTML

echo "==> Uploading to ${S3}"
aws s3 cp llmops-course-map.html "${S3}/llmops-course-map.html" --content-type "text/html"
aws s3 cp course/index.html      "${S3}/course/index.html"      --content-type "text/html"
aws s3 cp "$REDIRECT"            "${S3}/index.html"             --content-type "text/html"

if [[ -n "$DISTRIBUTION_ID" ]]; then
  echo "==> Invalidating CloudFront cache for /${PREFIX}/*"
  aws cloudfront create-invalidation \
    --distribution-id "$DISTRIBUTION_ID" \
    --paths "/${PREFIX}/*" >/dev/null
  echo "    invalidation submitted"
else
  echo "==> Skipping CloudFront invalidation (set DISTRIBUTION_ID to enable)"
fi

# Derive the public base URL from the bucket name if it looks like a domain.
BASE="https://${BUCKET}/${PREFIX}/"
echo ""
echo "Deployed. Entry URL:"
echo "  ${BASE}"
echo "  ${BASE}course/index.html        (player)"
echo "  ${BASE}llmops-course-map.html   (map)"
