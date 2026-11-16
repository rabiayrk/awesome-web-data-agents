# Contribution Guidelines

Thanks for helping. This list stays small on purpose, so please check the criteria below before you open a pull request.

## Scope

The list is about collecting data from the web with LLMs and agents: fetching, navigating, cleaning, extracting, evaluating, and the rules around it. General web agents, test automation and RPA tools fit only if they are clearly used for data collection.

## Inclusion criteria

Tools:

- The main use is web data collection or extraction, or the project is browser infrastructure built for agents.
- OSI-approved open source license. Source-available licenses such as SSPL, and non-commercial licenses, are not accepted for tools.
- At least one commit in the last 12 months, not archived and not marked deprecated.
- Documentation with install steps and a usage example.
- Works without a paid API key. An SDK that only calls a paid service does not fit.
- If the same team sells a hosted version, add "commercial cloud" to the tags.
- No tools whose main purpose is avoiding bot detection, solving CAPTCHAs or selling proxies.

Benchmarks and datasets:

- The task requires extracting or collecting data from web pages, not only clicking through a site or buying something.
- A paper, dataset or code repository is publicly available.
- State the data license if the authors give one.
- Mark it "vendor" if the authors work for a company that sells a related product.

Papers:

- About LLM or learned methods for web extraction, content cleaning, scraper generation, or evaluation of these.
- Peer-reviewed, or a preprint with enough detail to reproduce. Give the venue if it has one, otherwise "preprint".

Law and policy:

- Link the primary source (standard, official journal, court document, regulator page) when it is available.
- Give the jurisdiction and year.

Project maintainers follow the same rules for their own projects.

## Format

- One entry per pull request when possible, with a short note on why it fits.
- Use this format: `- [Name](link) - Description (License, Language).`
- For GitHub repositories, link to `https://github.com/owner/repo#readme`.
- The description says what the project does in plain words. No marketing terms, no star counts.
- Do not start the description with the project name.
- Start with a capital letter and end with a period.
- Keep entries in alphabetical order within each section.
- Each link appears only once in the list.
- Run `npx awesome-lint` before you open the pull request.

## Removal

Any entry is removed when its link is dead and no new location exists. Tools are also removed when the repository is archived, there have been no commits for 12 months, or the license changes to one that does not fit. Benchmarks, datasets and papers do not need recent commits, but archived benchmark repositories are replaced by a paper or dataset link if one exists. Open an issue if you see one of these.
