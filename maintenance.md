# Maintenance

A short checklist for the monthly update. The link check workflow runs on the first day of each month and opens an issue if links are broken.

## Monthly

1. Fix or remove every link in the latest broken links issue.
2. For each GitHub entry, check the repository page:
   - Archived, or marked deprecated: remove it.
   - No commits in the last 12 months: remove it.
   - License changed to one that does not fit the criteria: remove it.
   - Repository moved: update the link.
3. Check that tags in parentheses are still correct (license, language, commercial cloud).
4. Look for new entries:
   - arXiv listings for cs.CL, cs.IR and cs.DB with the terms "web extraction", "web scraping", "wrapper induction", "web agent benchmark" and "main content extraction".
   - Accepted papers at ACL, EMNLP, NAACL, WWW, SIGIR, VLDB, ICLR and NeurIPS (Datasets and Benchmarks) when their lists come out.
   - GitHub topics: web-scraping, browser-automation, web-agents, llm.
   - New drafts from the IETF AIPREF working group, EDPB and national data protection authorities, and new court decisions on scraping.
5. Check every new entry against the criteria in [contributing.md](contributing.md) before adding it.
6. Update the "last checked" date in the readme.
7. Run `npx awesome-lint` and fix all errors.

## Adding web-extraction-eval

When the web-extraction-eval repository is public, add it like any other entry: under Evaluate, in the right subsection, in alphabetical order, with a one-line description of what it measures and its license and language. It must meet the same criteria as other entries.
