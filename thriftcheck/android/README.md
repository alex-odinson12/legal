# ThriftCheck: Vintage Resale AI – Android legal pages

Package: com.thriftcheck.scanner. Developer name on Google Play: Fablewood Studio.

Source of truth: source/en/*.md (English only for now). Edit the Markdown for a change in data practices, then run:

    python3 build.py --effective-date YYYY-MM-DD

Requires Python Markdown. Commit Markdown and generated HTML together. Use the real publication date; do not silently change the effective date for spelling corrections. The build command never publishes.

Stable public path: /legal/thriftcheck/android/en/<privacy|terms>/.
Do not rename these paths after they are referenced by an app release. No JavaScript, analytics, external fonts or cookies are added by these pages. GitHub Pages itself receives ordinary web requests.

Every factual statement is checked against the client and server code; the claim-by-claim evidence lives in the app repository: com.thriftcheck.scanner/docs/legal/legal_EVIDENCE_FINAL_2026-11-14.md (client ad46b6f, server 45d3f0d).

14.11.2026: first Android edition, prepared and committed locally, not published; publication waits for the app owner's approval. Existing app policies and the root site index are unchanged.
