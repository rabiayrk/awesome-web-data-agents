# Evaluation View

The benchmarks and datasets from the [readme](readme.md#evaluate), side by side. Use it to pick a benchmark that matches what you want to measure.

How to read the columns:

- **Task**: what the system has to produce.
- **Size**: as reported by the authors.
- **Pages**: "Live" means the system works on real websites at test time, so results can change as sites change. "Saved" means fixed HTML snapshots.
- **Metric**: the main score the authors report. A dash means we did not find it in the abstract or readme; check the paper.
- **License**: the data license as stated by the authors, or the repository license marked "repo". A dash means we found none.
- **Vendor**: the authors work for a company that sells a related product.

All rows were checked against the paper abstract or the dataset readme on 2026-11-16.

## Structured Extraction

| Benchmark | Task | Size | Pages | Metric | License | Venue | Vendor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Klarna Product Page Dataset](https://zenodo.org/records/12605480) | Find a target element (such as price or product name) on a product page | 51,701 pages from 8,175 sites | Saved, with screenshots | - | CC-BY-SA-4.0 | TMLR 2024 | |
| [LiveWeb-IE](https://github.com/sbY99/LiveWeb-IE#readme) | Answer extraction queries for text, images and links at four complexity levels | 15 websites in 8 domains | Live | - | Non-commercial research only | ICLR 2026 | |
| [NEXT-EVAL](https://arxiv.org/abs/2505.17125) | Extract data records; test sets are generated from MHTML snapshots with XPath labels | Generated | Saved | F1 | - | Preprint 2025 | |
| [ScrapeGraphAI-100k](https://arxiv.org/abs/2602.15189) | Produce JSON that matches a given schema from real page content | 93,695 extraction events | Saved | - | - | Preprint 2026 | Yes |
| [WebLists](https://arxiv.org/abs/2504.12682) | Navigate, set filters and extract complete lists with a fixed schema | 200 tasks on 50 websites | Live | Recall | - | Preprint 2025 | Yes |
| [WebSRC](https://x-lance.github.io/WebSRC/) | Answer questions that need the page structure | 400K questions on 6.4K pages | Saved | - | - | EMNLP 2021 | |

## Content Extraction

| Benchmark | Task | Size | Pages | Metric | License | Venue | Vendor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Web Content Extraction Benchmark (Bevendorff et al.)](https://github.com/chatnoir-eu/web-content-extraction-benchmark#readme) | Extract main content; combines eight earlier datasets | 8 datasets | Saved | - | Apache-2.0 (repo) | SIGIR 2023 | |
| [WCXB](https://github.com/Murrough-Foley/web-content-extraction-benchmark#readme) | Extract main content from seven page types, not only articles | 2,008 pages from 1,613 domains | Saved | - | CC-BY-4.0 | Preprint 2026 | |
| [WebMainBench](https://arxiv.org/abs/2511.23119) | Extract main content, released with the Dripper model | 7,809 pages from 5,434 domains | Saved | - | - | Preprint 2025 | |

## Information Seeking

These agents mostly answer questions, but many tasks need facts from several pages.

| Benchmark | Task | Size | Pages | Metric | License | Venue | Vendor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [AssistantBench](https://assistantbench.github.io/) | Solve realistic, time-consuming web tasks with checkable answers | 214 tasks | Live | Accuracy | - | EMNLP 2024 | |
| [BEARCUBS](https://bear-cubs.github.io/) | Find factual answers that need live browsing and sometimes multimodal interaction | 111 questions | Live | - | - | 2025 | |
| [BrowseComp](https://arxiv.org/abs/2504.12516) | Find hard-to-find facts with short, verifiable answers | 1,266 questions | Live | - | - | 2025 | Yes |
| [Mind2Web 2](https://osu-nlp-group.github.io/Mind2Web-2/) | Long agentic search with cited answers, graded by an agent judge | 130 tasks | Live | Agent judge with rubrics | - | NeurIPS 2025 | |
| [Online-Mind2Web](https://github.com/OSU-NLP-Group/Online-Mind2Web#readme) | Complete tasks on real sites, graded by the WebJudge LLM judge | 300 tasks on 136 websites | Live | Task success | MIT (repo) | COLM 2025 | |
| [WebBench](https://github.com/Halluminate/WebBench#readme) | Complete read and write tasks on popular websites | 2,454 open tasks on 452 websites | Live | - | MIT (repo) | 2025 | Yes |
| [WebWalkerQA](https://arxiv.org/abs/2501.07572) | Answer questions by moving through the subpages of a given website | 680 queries over 1,373 pages | Starts from a site's root page | - | - | ACL 2025 | |
| [WideSearch](https://github.com/ByteDance-Seed/WideSearch#readme) | Collect many facts that are each checked, and organize them in one output | 200 questions in English and Chinese | Live | Success rate | MIT (repo) | 2025 | |

## What is still missing

Observations from the tables above:

- Only two of the six structured extraction benchmarks (LiveWeb-IE and WebLists) run on live sites. Saved pages cannot show how results drift when sites change.
- Only WebLists reports a cost figure (cost per output row) in its abstract.
- Many entries state no data license, which limits reuse.

Suggestions and corrections are welcome; see [contributing.md](contributing.md).
