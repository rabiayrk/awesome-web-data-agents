# Awesome Web Data Agents [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Collecting data from the web with large language models and browser agents.

This list follows the collection pipeline: load a page, move through a site, clean the HTML, extract structured data, measure how well that worked, and stay within technical and legal limits. Web agents that book trips or fill in forms are out of scope unless they are used to collect data.

Tags in parentheses show the license and main language. "Commercial cloud" means the same team also sells a hosted version; the open source project works without it. "Vendor" marks a benchmark or dataset published by a company that sells a related product. All entries were last checked on 2026-11-16.

## Contents

- [Fetch and Render](#fetch-and-render)
- [Navigate](#navigate)
- [Clean](#clean)
  - [Cleaning Tools](#cleaning-tools)
  - [Cleaning Research](#cleaning-research)
- [Extract](#extract)
  - [Extraction Tools](#extraction-tools)
  - [Extraction Research](#extraction-research)
- [Evaluate](#evaluate)
  - [Structured Extraction Benchmarks](#structured-extraction-benchmarks)
  - [Content Extraction Benchmarks](#content-extraction-benchmarks)
  - [Information-Seeking Benchmarks](#information-seeking-benchmarks)
  - [Evaluation Studies](#evaluation-studies)
- [Comply](#comply)
  - [Standards and Signals](#standards-and-signals)
  - [Compliance Studies](#compliance-studies)
  - [Court Cases](#court-cases)
  - [EU Law and Data Protection](#eu-law-and-data-protection)

## Fetch and Render

Crawlers and browsers that load pages for an agent or an extraction step.

- [Crawlee](https://github.com/apify/crawlee#readme) - Node.js crawling library with HTTP crawlers and headless browser crawlers on Playwright or Puppeteer (Apache-2.0, TypeScript, commercial cloud).
- [Crawlee for Python](https://github.com/apify/crawlee-python#readme) - Python version of Crawlee with BeautifulSoup and Playwright crawlers (Apache-2.0, Python, commercial cloud).
- [Kernel Images](https://github.com/kernel/kernel-images#readme) - Docker and unikernel images that run sandboxed Chromium with a CDP port and a live view (Apache-2.0, Go, commercial cloud).
- [Lightpanda](https://github.com/lightpanda-io/browser#readme) - Headless browser for automation and agents written from scratch in Zig instead of building on Chromium (AGPL-3.0, Zig, commercial cloud).
- [Spider](https://github.com/spider-rs/spider#readme) - Rust crawling engine that streams pages as they arrive and renders JavaScript only where needed (MIT, Rust, commercial cloud).
- [Steel Browser](https://github.com/steel-dev/steel-browser#readme) - Self-hosted browser API that manages Chrome sessions, cookies and pages for agents over CDP (Apache-2.0, TypeScript, commercial cloud).

## Navigate

Agents and agent interfaces that drive a browser through a site.

- [agent-browser](https://github.com/vercel-labs/agent-browser#readme) - Command-line browser for AI agents that reads pages as an accessibility tree and acts on elements from the shell (Apache-2.0, Rust).
- [Browser Use](https://github.com/browser-use/browser-use#readme) - Browser agent where the model writes Python in a persistent REPL that controls Chrome over CDP (MIT, Python, commercial cloud).
- [Nanobrowser](https://github.com/nanobrowser/nanobrowser#readme) - Chrome extension that runs a web automation agent in your own logged-in browser with a cloud or local model (Apache-2.0, TypeScript).
- [Playwright MCP](https://github.com/microsoft/playwright-mcp#readme) - MCP server that lets LLMs control a Playwright browser through the accessibility tree instead of screenshots (Apache-2.0, TypeScript).
- [Skyvern](https://github.com/Skyvern-AI/skyvern#readme) - Workflow automation that uses vision LLMs to find page elements instead of fixed XPath selectors (AGPL-3.0, Python, commercial cloud).
- [Stagehand](https://github.com/browserbase/stagehand#readme) - Browser agent SDK for TypeScript, Python and Go with `act`, `extract` and `observe` calls (MIT, TypeScript, commercial cloud).

## Clean

Turning raw HTML into main content, text or Markdown before an LLM sees it.

### Cleaning Tools

- [MinerU-HTML](https://github.com/opendatalab/MinerU-HTML#readme) - Main content extractor that uses a small language model to keep the article body and drop navigation and ads (Apache-2.0, Python).
- [Newspaper4k](https://github.com/AndyTheFactory/newspaper4k#readme) - Article, title and metadata extraction for news sites, maintained fork of Newspaper3k (MIT, Python).
- [Readability.js](https://github.com/mozilla/readability#readme) - Standalone version of the content extractor used in Firefox Reader View (Apache-2.0, JavaScript).
- [Reader](https://github.com/jina-ai/reader#readme) - Open source code behind the `r.jina.ai` service that converts a URL into Markdown for LLM input (Apache-2.0, TypeScript, commercial cloud).
- [Resiliparse](https://github.com/chatnoir-eu/chatnoir-resiliparse#readme) - Toolkit for web archive processing with HTML-to-text and main content extraction (Apache-2.0, Rust with Python bindings).
- [Trafilatura](https://github.com/adbar/trafilatura#readme) - Crawler and extractor for main text and metadata with output as text, Markdown, JSON or XML (Apache-2.0, Python).

### Cleaning Research

- [Beyond a Single Extractor](https://arxiv.org/abs/2602.19548) - Shows that combining several HTML-to-text extractors keeps more useful pages for LLM pretraining than one fixed extractor (2026, preprint).
- [Dripper](https://arxiv.org/abs/2511.23119) - Treats main content extraction as sequence labeling with a small model and releases the WebMainBench test set (2025, preprint).
- [HtmlRAG](https://arxiv.org/abs/2411.02959) - Keeps cleaned HTML instead of plain text in retrieval-augmented generation and prunes it into a block tree (WWW 2025).
- [NeuScraper](https://arxiv.org/abs/2402.14652) - Neural scraper that extracts the primary text of web pages for cleaner pretraining corpora (ACL 2024).
- [ReaderLM-v2](https://arxiv.org/abs/2503.01151) - 1.5B model that converts HTML to Markdown or JSON; model weights are CC-BY-NC-4.0 (2025, preprint).

## Extract

Getting structured records out of pages, either with an LLM on every page or by generating reusable scrapers.

### Extraction Tools

- [Crawl4AI](https://github.com/unclecode/crawl4ai#readme) - Async crawler that outputs Markdown and extracts JSON with CSS or XPath schemas or with an LLM (Apache-2.0, Python, commercial cloud).
- [Firecrawl](https://github.com/firecrawl/firecrawl#readme) - Self-hostable API server that scrapes, crawls and searches and returns Markdown or schema-based JSON; SDKs are MIT (AGPL-3.0, TypeScript, commercial cloud).
- [LLM Scraper](https://github.com/mishushakov/llm-scraper#readme) - Library that turns a Playwright page into typed data from a Zod or JSON schema and can also generate scraping code (MIT, TypeScript).
- [Maxun](https://github.com/getmaxun/maxun#readme) - Self-hostable no-code platform that records browser actions into reusable extraction robots (AGPL-3.0, TypeScript, commercial cloud).
- [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai#readme) - Library that builds LLM scraping pipelines as graphs for websites and local HTML, XML or JSON files (MIT, Python, commercial cloud).
- [webclaw](https://github.com/0xMassi/webclaw#readme) - Extraction engine with CLI, MCP server and self-hostable server that turns pages into Markdown, JSON or LLM context (AGPL-3.0, Rust, commercial cloud).

### Extraction Research

- [AutoScraper](https://arxiv.org/abs/2404.12753) - LLM agent that generates reusable scrapers for a site in two stages and measures if they work on other pages of the same site (EMNLP 2024).
- [Cross-Domain Web Information Extraction at Pinterest](https://arxiv.org/abs/2508.01096) - Production attribute extraction that combines text, structure and visual layout in a compact page representation for small models (2025).
- [Evaporate](https://arxiv.org/abs/2304.09433) - Compares direct LLM extraction with LLM-written extraction code on semi-structured documents, including HTML pages (PVLDB 2023).
- [Infogent](https://arxiv.org/abs/2410.19054) - Navigator, extractor and aggregator agents that collect information across several websites for one query (2024).
- [MarkupLM](https://arxiv.org/abs/2110.08518) - Pre-trains a model on text together with HTML markup for web document understanding (ACL 2022).
- [SCRIBES](https://arxiv.org/abs/2510.01832) - Uses reinforcement learning so an LLM writes one extraction script for a group of similar pages instead of reading each page (2025, preprint).
- [WebFormer](https://arxiv.org/abs/2202.00217) - Transformer over HTML layout for extracting structured fields such as product title and price (WWW 2022).
- [XPath Agent](https://arxiv.org/abs/2502.15688) - Two-stage LLM agent that writes XPath queries from a few sample pages and one natural language query (2024, preprint).

## Evaluate

Benchmarks, datasets and studies that measure extraction and collection quality. The [evaluation view](evaluation.md) compares the benchmarks in one table.

### Structured Extraction Benchmarks

- [Klarna Product Page Dataset](https://zenodo.org/records/12605480) - 51,701 labeled product pages from 8,175 e-commerce sites for finding a target element on a page (CC-BY-SA-4.0, TMLR 2024).
- [LiveWeb-IE](https://github.com/sbY99/LiveWeb-IE#readme) - Extraction benchmark run against live websites instead of saved snapshots, with four task complexity levels (non-commercial research license, ICLR 2026).
- [NEXT-EVAL](https://arxiv.org/abs/2505.17125) - Framework that builds record extraction test sets from MHTML snapshots with XPath labels and compares heuristic and LLM methods (2025, preprint).
- [ScrapeGraphAI-100k](https://arxiv.org/abs/2602.15189) - 93,695 real schema-constrained extraction calls collected through ScrapeGraphAI telemetry (2026, preprint, vendor).
- [WebLists](https://arxiv.org/abs/2504.12682) - 200 tasks where an agent must navigate, set filters and extract complete lists with a fixed schema; reports recall (2025, preprint, vendor).
- [WebSRC](https://x-lance.github.io/WebSRC/) - 400K question-answer pairs over 6.4K web pages that require reading the page structure (EMNLP 2021).

### Content Extraction Benchmarks

- [WCXB](https://github.com/Murrough-Foley/web-content-extraction-benchmark#readme) - 2,008 pages of seven page types, from articles to product listings, with baseline results for 14 extractors (CC-BY-4.0, 2026).
- [Web Content Extraction Benchmark (Bevendorff et al.)](https://github.com/chatnoir-eu/web-content-extraction-benchmark#readme) - Code and data for a SIGIR 2023 reproducibility study that compares main content extractors on eight datasets (Apache-2.0, Python).

### Information-Seeking Benchmarks

These agents mostly answer questions, but many tasks require collecting facts from several pages.

- [AssistantBench](https://assistantbench.github.io/) - 214 realistic, time-consuming web tasks with answers that can be checked automatically (EMNLP 2024).
- [BEARCUBS](https://bear-cubs.github.io/) - 111 information-seeking questions that need live web access and sometimes multimodal interaction (2025).
- [BrowseComp](https://arxiv.org/abs/2504.12516) - 1,266 questions about hard-to-find facts with short answers that are easy to verify (2025, vendor).
- [Mind2Web 2](https://osu-nlp-group.github.io/Mind2Web-2/) - 130 long agentic search tasks graded by an agent judge that also checks the cited sources (NeurIPS 2025 Datasets and Benchmarks).
- [Online-Mind2Web](https://github.com/OSU-NLP-Group/Online-Mind2Web#readme) - 300 tasks on 136 live sites plus WebJudge, an LLM judge for agent runs; the paper finds earlier reported agent results too optimistic (MIT, COLM 2025).
- [WebBench](https://github.com/Halluminate/WebBench#readme) - 2,454 open tasks on 452 live websites, split into read tasks and write tasks (MIT, 2025, vendor).
- [WebWalkerQA](https://arxiv.org/abs/2501.07572) - Questions that require an LLM to move through a site's subpages to find the answer (ACL 2025).
- [WideSearch](https://github.com/ByteDance-Seed/WideSearch#readme) - 200 questions in English and Chinese that require collecting many similar facts, such as metrics for every company in a sector (MIT, 2025).

### Evaluation Studies

- [Beyond BeautifulSoup](https://arxiv.org/abs/2601.06301) - Tests what non-expert users can scrape with off-the-shelf LLM tools on 35 sites with login, anti-bot and CAPTCHA controls (2026, preprint).

## Comply

Rules and research on what may be collected and how. This section is not legal advice; check the law in your own jurisdiction.

### Standards and Signals

- [ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt#readme) - Community list of AI crawler user agents with ready robots.txt, .htaccess, nginx and other server configs (MIT).
- [Cloudflare Content Signals Policy](https://blog.cloudflare.com/content-signals-policy/) - Adds `search`, `ai-input` and `ai-train` signals to robots.txt; the policy text is CC0 (2025, vendor).
- [Cloudflare Pay per Crawl](https://blog.cloudflare.com/introducing-pay-per-crawl/) - Private beta that lets site owners charge AI crawlers per request with HTTP 402 (2025, vendor).
- [IETF AI Preferences Working Group](https://datatracker.ietf.org/wg/aipref/about/) - Drafts a vocabulary for AI usage preferences and ways to attach it through robots.txt and HTTP headers; not an RFC yet (2025).
- [llms.txt](https://llmstxt.org/) - Proposal for a Markdown file at the site root that gives LLMs a short guide to the site; it does not control access (2024).
- [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309) - IETF standard for the Robots Exclusion Protocol, including how crawlers parse and cache robots.txt (2022).

### Compliance Studies

- [Consent in Crisis](https://arxiv.org/abs/2407.14933) - Audit of 14,000 web domains behind C4, RefinedWeb and Dolma that tracks how robots.txt and terms of service restrict AI use over time (NeurIPS 2024 Datasets and Benchmarks).
- [ScrapeBench](https://arxiv.org/abs/2611.11306) - Tests whether AI agents follow terms of service and robots.txt when asked to scrape 1,626 sites that prohibit it (NeurIPS 2026 Evaluations and Datasets Track).

### Court Cases

- [hiQ Labs v. LinkedIn](https://cdn.ca9.uscourts.gov/datastore/opinions/2022/04/18/17-16783.pdf) - Ninth Circuit opinion on scraping public profiles and the Computer Fraud and Abuse Act (US, 2022).
- [Kneschke v. LAION](https://justiz.hamburg.de/resource/blob/1126574/2495057737fed4883eec42dce4d2430b/ki-und-urheberrecht-hanseatisches-oberlandesgericht-weist-berufung-zurueck-data.pdf) - Court press release in German: downloading a photo for an AI training dataset was covered by text and data mining exceptions, and a plain-language opt-out was not machine-readable (Germany, Hamburg Higher Regional Court, 2025).
- [Meta Platforms v. Bright Data](https://archive.org/download/gov.uscourts.cand.406956/gov.uscourts.cand.406956.181.0.pdf) - Order granting summary judgment to a scraping company that collected public data while logged off (US, N.D. Cal., 2024).
- [X Corp. v. Bright Data](https://archive.org/download/gov.uscourts.cand.415869/gov.uscourts.cand.415869.83.0.pdf) - Order dismissing contract and tort claims against a scraping company, partly because they were preempted by the Copyright Act (US, N.D. Cal., 2024).

### EU Law and Data Protection

- [AI Act, Article 53](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) - Requires providers of general-purpose AI models to have a policy that respects text and data mining opt-outs (EU, 2024).
- [CNIL Recommendations on AI System Development](https://www.cnil.fr/en/ai-system-development-cnils-recommendations-to-comply-gdpr) - French data protection authority guidance, including how to collect personal data by web scraping under legitimate interest (France, 2025).
- [Directive (EU) 2019/790, Article 4](https://eur-lex.europa.eu/eli/dir/2019/790/oj) - Text and data mining exception that rightholders can opt out of in a machine-readable way for online content (EU, 2019).
- [Dutch DPA Guidance on Scraping](https://www.autoriteitpersoonsgegevens.nl/documenten/handreiking-scraping-door-particulieren-en-private-organisaties) - Guidance in Dutch on scraping by private parties and organisations under the GDPR (Netherlands, 2024).
- [EDPB Guidelines 03/2026 on Web Scraping](https://www.edpb.europa.eu/public-consultations/guidelines-on-web-scraping_en) - Draft guidelines on web scraping for generative AI; public consultation ended on 2026-10-30 (EU, 2026).
- [EDPB Opinion 28/2024](https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en) - Opinion on AI models covering anonymity, legitimate interest and the effect of unlawful processing during development (EU, 2024).
- [General-Purpose AI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) - Voluntary code with transparency, copyright, and safety and security chapters for AI Act compliance (EU, 2025).
- [Joint Statement on Data Scraping](https://ico.org.uk/media2/migrated/4026232/joint-statement-data-scraping-202308.pdf) - Statement by 12 data protection authorities that publicly accessible personal data is still protected (international, 2023).

## Related Lists

- [awesome-browser-automation](https://github.com/angrykoala/awesome-browser-automation#readme) - Browser automation and testing tools.
- [awesome-web-agents](https://github.com/steel-dev/awesome-web-agents#readme) - Tools and frameworks for building AI web agents.
- [awesome-web-scraping](https://github.com/lorien/awesome-web-scraping#readme) - General web scraping libraries by language.
- [GUI Agents Paper List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List#readme) - Research papers on GUI and web agents.

## Contributing

Suggestions are welcome. Read the [contribution guidelines](contributing.md) first.
