# Awesome Awesome Security [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

> A curated list of curated lists in security.

Security has hundreds of excellent "awesome" lists, and no good index of them. Searching GitHub for
`awesome security` returns abandoned forks next to actively maintained references with no way to tell
them apart. This list is the index: one entry per list, grouped by domain, annotated with popularity
and maintenance status so you can tell at a glance which one is worth your afternoon.

**Scope:** curated *collections* of security resources — not individual tools, not blogs, not courses.
If a repository's purpose is to point you at other things, it belongs here. If it *is* the thing, it
doesn't.

## Contents

- [Meta — Lists of Lists](#meta--lists-of-lists)
- [General & Foundational](#general--foundational)
- [Offensive Security & Red Teaming](#offensive-security--red-teaming)
- [Web, API & Application Security](#web-api--application-security)
- [Blue Team, Detection & Incident Response](#blue-team-detection--incident-response)
- [Threat Intelligence](#threat-intelligence)
- [Malware Analysis & Reverse Engineering](#malware-analysis--reverse-engineering)
- [Vulnerability Research, Fuzzing & Exploit Development](#vulnerability-research-fuzzing--exploit-development)
- [Cloud, Container & Kubernetes](#cloud-container--kubernetes)
- [DevSecOps & Software Supply Chain](#devsecops--software-supply-chain)
- [Mobile Security](#mobile-security)
- [Hardware, Embedded, IoT & ICS/OT](#hardware-embedded-iot--icsot)
- [Wireless, Telecom & Protocol](#wireless-telecom--protocol)
- [OSINT & Reconnaissance](#osint--reconnaissance)
- [Cryptography](#cryptography)
- [Blockchain, Web3 & Smart Contracts](#blockchain-web3--smart-contracts)
- [AI & ML Security](#ai--ml-security)
- [Privacy](#privacy)
- [Bug Bounty](#bug-bounty)
- [CTF & Training](#ctf--training)
- [Social Engineering](#social-engineering)
- [GRC, Careers & Industry Reading](#grc-careers--industry-reading)
- [Non-English](#non-english)
- [Contributing](#contributing)

## Legend

Entries are ordered by star count within each section. Each ends with a generated annotation: `★`
star count and the month of the last commit.

Stars measure reach, not quality — a dormant list with 10k stars is often worse for your purposes
than a current one with 500. Read the descriptions; that's where the judgment is.

| Marker | Meaning |
| --- | --- |
| ⚠️ `archived` | Repository is archived and read-only. Still useful as a snapshot; nothing new will land. |
| 💤 `dormant` | No commits in over 18 months. Links rot; verify before relying on it. |

Metadata last refreshed **2026-07-31**. Run `./scripts/refresh.py` to update it — see [Contributing](#contributing).

## Meta — Lists of Lists

- [sindresorhus/awesome](https://github.com/sindresorhus/awesome) — The root of the entire awesome ecosystem. Its security section is thin, but this is where the format and the quality conventions come from. — ★491k · 2026-06
- [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) — Not security-exclusive, but the sysadmin/network/security cheatsheet collection so widely referenced that omitting it would be strange. — ★236k · 2024-11 · 💤 dormant
- [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) — The most-starred index of security lists, spanning offensive, defensive, forensics and CTF. The closest thing to a canonical entry point, though it leans toward breadth over pruning. — ★117.3k · 2026-07
- [0xor0ne/awesome-list](https://github.com/0xor0ne/awesome-list) — A steadily updated reading list of exploitation, kernel and embedded security writeups. Closer to a link feed than a taxonomy. — ★3.9k · 2026-07
- [taielab/awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists) — Aggregates security lists and tools with automated daily updates, so entries skew fresh. — ★1.4k · 2025-12
- [pe3zx/my-infosec-awesome](https://github.com/pe3zx/my-infosec-awesome) — One practitioner's cross-domain index, notably strong on exploitation and Windows internals. — ★1.2k · 2026-07

## General & Foundational

- [The-Art-of-Hacking/h4cker](https://github.com/The-Art-of-Hacking/h4cker) — Companion repository to Omar Santos's books and video courses; thousands of references plus labs and cheat sheets. — ★28.7k · 2026-07
- [vitalysim/Awesome-Hacking-Resources](https://github.com/vitalysim/Awesome-Hacking-Resources) — Long-running general collection of learning material, wargames and practice environments. — ★17.3k · 2026-05
- [carpedm20/awesome-hacking](https://github.com/carpedm20/awesome-hacking) — An early, influential general list. Historically important; increasingly dated. — ★16.8k · 2024-06 · 💤 dormant
- [sbilly/awesome-security](https://github.com/sbilly/awesome-security) — The general-purpose security list: tooling, libraries and reading across network, host and application layers. A sensible first stop when you don't yet know which subdomain you need. — ★14.7k · 2026-01
- [rmusser01/Infosec_Reference](https://github.com/rmusser01/Infosec_Reference) — An unusually deep, opinionated reference organized by topic with commentary explaining *why* each source matters. — ★6k · 2025-10
- [onlurking/awesome-infosec](https://github.com/onlurking/awesome-infosec) — Weighted toward education — courses, degree programs, books and massive open syllabi rather than tools. — ★5.7k · 2025-11
- [jekil/awesome-hacking](https://github.com/jekil/awesome-hacking) — Tool-centric index grouped by activity: recon, exploitation, post-exploitation, forensics. — ★3.9k · 2026-05
- [0xsyr0/Awesome-Cybersecurity-Handbooks](https://github.com/0xsyr0/Awesome-Cybersecurity-Handbooks) — A red teamer's working notes published as structured handbooks. Practical command-level detail, not link lists. — ★3.9k · 2026-07
- [brootware/awesome-cyber-security-university](https://github.com/brootware/awesome-cyber-security-university) — Structures free resources into a progressive self-study curriculum rather than a flat list. — ★3.2k · 2025-08
- [fabionoth/awesome-cyber-security](https://github.com/fabionoth/awesome-cyber-security) — Broad mixed collection of tools, courses and reference material. — ★1.9k · 2026-06

## Offensive Security & Red Teaming

- [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) — Payloads and bypasses per vulnerability class. Technically a resource rather than an index, but it is the single most-used offensive reference on GitHub. — ★79.6k · 2026-07
- [enaqx/awesome-pentest](https://github.com/enaqx/awesome-pentest) — The reference penetration testing list: tools, books, labs and certifications, carefully organized and actively curated. The best-maintained entry in this category. — ★26.8k · 2026-07
- [blaCCkHatHacEEkr/PENTESTING-BIBLE](https://github.com/blaCCkHatHacEEkr/PENTESTING-BIBLE) — Thousands of collected articles and writeups. Large and popular, but unstructured and unmaintained. — ★13.9k · 2023-04 · 💤 dormant
- [HackTricks-wiki/hacktricks](https://github.com/HackTricks-wiki/hacktricks) — An enormous searchable wiki of techniques covering pentesting, privilege escalation and cloud. Effectively the field's shared handbook. — ★12k · 2026-07
- [coreb1t/awesome-pentest-cheat-sheets](https://github.com/coreb1t/awesome-pentest-cheat-sheets) — The original cheat-sheet collection. Frozen, but sound on fundamentals. — ★4.4k · 2024-02 · ⚠️ archived
- [Orange-Cyberdefense/arsenal](https://github.com/Orange-Cyberdefense/arsenal) — Cheat-sheet-driven launcher for common pentest commands. A tool, but it functions as an executable index of technique. — ★3.8k · 2024-11 · 💤 dormant
- [rootkit-io/awesome-malware-development](https://github.com/rootkit-io/awesome-malware-development) — Offensive tooling development: loaders, injection, evasion. Read alongside the detection lists to understand both sides. — ★1.8k · 2026-04
- [JoasASantos/Awesome-Red-Team-Operations](https://github.com/JoasASantos/Awesome-Red-Team-Operations) — Red team operations tooling and tradecraft, organized by capability. — ★1.7k · 2022-08 · 💤 dormant
- [RistBS/Awesome-RedTeam-Cheatsheet](https://github.com/RistBS/Awesome-RedTeam-Cheatsheet) — Dense technique reference skewed toward Active Directory attack paths. — ★1.3k · 2023-12 · 💤 dormant
- [0xMrNiko/Awesome-Red-Teaming](https://github.com/0xMrNiko/Awesome-Red-Teaming) — Organized along the attack lifecycle — initial access through exfiltration — which makes it easy to map to an engagement plan. — ★919 · 2026-07
- [ByteSnipers/awesome-pentest-cheat-sheets](https://github.com/ByteSnipers/awesome-pentest-cheat-sheets) — A fork of the archived `coreb1t` collection, carried further before also going quiet. — ★673 · 2024-06 · 💤 dormant
- [marcosValle/awesome-windows-red-team](https://github.com/marcosValle/awesome-windows-red-team) — Windows-specific offensive tradecraft: Active Directory, lateral movement, defense evasion. — ★604 · 2026-07

## Web, API & Application Security

- [analysis-tools-dev/static-analysis](https://github.com/analysis-tools-dev/static-analysis) — Exhaustive index of SAST tools and linters across every language. The definitive answer to "what can scan this codebase?" — ★14.7k · 2026-06
- [qazbnm456/awesome-web-security](https://github.com/qazbnm456/awesome-web-security) — The most thorough and best-maintained web security list: research papers, writeups and tooling per vulnerability class. — ★13.6k · 2026-07
- [0xInfection/Awesome-WAF](https://github.com/0xInfection/Awesome-WAF) — Everything about web application firewalls, including fingerprinting and a well-known bypass catalogue. — ★7.6k · 2026-03
- [infoslack/awesome-web-hacking](https://github.com/infoslack/awesome-web-hacking) — Practical web hacking material — books, tools, labs — with a gentler on-ramp than `qazbnm456`. — ★7.2k · 2026-07
- [paragonie/awesome-appsec](https://github.com/paragonie/awesome-appsec) — Application security for *builders*: secure coding guidance organized by language and framework. — ★7k · 2025-02
- [arainho/awesome-api-security](https://github.com/arainho/awesome-api-security) — The best collection of API security tooling and research, and still the strongest starting point for API work. — ★3.9k · 2026-05 · ⚠️ archived
- [lirantal/awesome-nodejs-security](https://github.com/lirantal/awesome-nodejs-security) — Node.js and npm ecosystem security, maintained by a Node security working group member. — ★3k · 2026-07
- [Escapingbug/awesome-browser-exploit](https://github.com/Escapingbug/awesome-browser-exploit) — Browser and JavaScript engine exploitation tutorials and writeups. Niche and deep. — ★2.3k · 2023-09 · 💤 dormant
- [guardrailsio/awesome-golang-security](https://github.com/guardrailsio/awesome-golang-security) — Go-specific security tooling, libraries and hardening guidance. — ★2k · 2024-06 · 💤 dormant
- [doyensec/awesome-electronjs-hacking](https://github.com/doyensec/awesome-electronjs-hacking) — Electron desktop application security from the consultancy that publishes most of the research on it. — ★679 · 2025-05

## Blue Team, Detection & Incident Response

- [paralax/awesome-honeypots](https://github.com/paralax/awesome-honeypots) — Comprehensive honeypot and deception index covering every protocol and interaction level. — ★10.5k · 2026-06
- [meirwah/awesome-incident-response](https://github.com/meirwah/awesome-incident-response) — The canonical IR list — evidence collection, memory and disk analysis, timeline tooling and playbooks. Still actively maintained after a decade. — ★9.3k · 2026-07
- [decalage2/awesome-security-hardening](https://github.com/decalage2/awesome-security-hardening) — Hardening guides and benchmarks for operating systems, network gear and applications. Unusually practical. — ★6.5k · 2026-05
- [fabacab/awesome-cybersecurity-blueteam](https://github.com/fabacab/awesome-cybersecurity-blueteam) — The definitive defensive list: monitoring, hardening, detection, DFIR and security operations tooling. If you own defense, start here. — ★5.5k · 2024-07 · 💤 dormant
- [0x4D31/awesome-threat-detection](https://github.com/0x4D31/awesome-threat-detection) — Threat detection and hunting: frameworks, datasets, detection rule repositories and research. — ★4.7k · 2026-01
- [pedramamini/awesome-yara](https://github.com/pedramamini/awesome-yara) — YARA rule repositories, tooling and the people who write them. Essential for detection and malware triage. — ★4.2k · 2026-06
- [infosecB/awesome-detection-engineering](https://github.com/infosecB/awesome-detection-engineering) — Detection engineering as a discipline — rule development, testing, detection-as-code pipelines. The most current list in this category. — ★1.3k · 2026-07
- [jatrost/awesome-kubernetes-threat-detection](https://github.com/jatrost/awesome-kubernetes-threat-detection) — Kubernetes-specific detection: audit log sources, attack techniques and mapped detections. — ★409 · 2023-09 · 💤 dormant
- [cr0nx/awesome-linux-attack-forensics-purplelabs](https://github.com/cr0nx/awesome-linux-attack-forensics-purplelabs) — Linux attack, detection and forensics resources framed as purple team exercises. — ★341 · 2023-02 · 💤 dormant
- [hevnsnt/Awesome_Incident_Response](https://github.com/hevnsnt/Awesome_Incident_Response) — A leaner, more recently curated IR list; a useful complement to `meirwah`. — ★295 · 2025-09

## Threat Intelligence

- [hslatman/awesome-threat-intelligence](https://github.com/hslatman/awesome-threat-intelligence) — The reference CTI list: feeds, platforms, standards, frameworks and research. Comprehensive and well maintained. — ★10.5k · 2026-05
- [kbandla/APTnotes](https://github.com/kbandla/APTnotes) — The historical archive of public APT campaign reports, organized by year. Primary sources rather than links about them. — ★3.7k · 2024-01 · 💤 dormant
- [ARPSyndicate/awesome-intelligence](https://github.com/ARPSyndicate/awesome-intelligence) — Broader intelligence tradecraft — OSINT, HUMINT, SIGINT — beyond the cyber-specific. — ★2.4k · 2025-06 · ⚠️ archived
- [aptnotes/data](https://github.com/aptnotes/data) — Machine-readable index and metadata for the APTnotes corpus. Use this if you want to ingest the archive programmatically. — ★1.8k · 2024-12 · 💤 dormant
- [jacobdjwilson/awesome-annual-security-reports](https://github.com/jacobdjwilson/awesome-annual-security-reports) — Vendor and industry annual reports collected in one place. Invaluable when you need defensible statistics. — ★1.2k · 2026-07

## Malware Analysis & Reverse Engineering

- [rshipp/awesome-malware-analysis](https://github.com/rshipp/awesome-malware-analysis) — The standard malware analysis list: sandboxes, unpackers, corpora, static and dynamic tooling. The foundations it covers have not moved much. — ★14.1k · 2024-06 · 💤 dormant
- [wtsxDev/reverse-engineering](https://github.com/wtsxDev/reverse-engineering) — Large tool-oriented RE collection spanning disassembly, debugging and binary analysis. — ★10.3k · 2023-07 · 💤 dormant
- [cugu/awesome-forensics](https://github.com/cugu/awesome-forensics) — Digital forensics tooling organized by evidence type: disk, memory, network, mobile. — ★5.1k · 2026-05
- [alphaSeclab/awesome-reverse-engineering](https://github.com/alphaSeclab/awesome-reverse-engineering) — Enormous multi-platform RE index with Chinese and English annotations. Exhaustive, if unwieldy. — ★5k · 2021-09 · 💤 dormant
- [tylerha97/awesome-reversing](https://github.com/tylerha97/awesome-reversing) — Reverse engineering learning path — books, courses, disassemblers and practice binaries. — ★4.5k · 2023-08 · 💤 dormant
- [onethawt/idaplugins-list](https://github.com/onethawt/idaplugins-list) — The index of IDA Pro plugins. Narrow and indispensable if IDA is your daily driver. — ★3.8k · 2024-05 · 💤 dormant
- [gmh5225/awesome-game-security](https://github.com/gmh5225/awesome-game-security) — Game security, anti-cheat and kernel-mode protection research. Frequently updated and hard to find elsewhere. — ★3.3k · 2026-07
- [ExpLife0011/awesome-windows-kernel-security-development](https://github.com/ExpLife0011/awesome-windows-kernel-security-development) — Windows kernel security and driver development resources. Old, and still cited. — ★2.1k · 2022-09 · 💤 dormant
- [packing-box/awesome-executable-packing](https://github.com/packing-box/awesome-executable-packing) — Executable packing and unpacking: packers, detectors, datasets and academic literature. — ★1.6k · 2026-05
- [fr0gger/Awesome_Malware_Techniques](https://github.com/fr0gger/Awesome_Malware_Techniques) — Catalogue of malware techniques mapped to analysis approaches. — ★864 · 2023-04 · 💤 dormant
- [digitalisx/awesome-memory-forensics](https://github.com/digitalisx/awesome-memory-forensics) — Memory forensics specifically — acquisition, Volatility/Rekall plugins, and analysis writeups. — ★559 · 2025-02
- [Karneades/awesome-malware-persistence](https://github.com/Karneades/awesome-malware-persistence) — Persistence mechanisms across platforms, with detection notes for each. — ★304 · 2026-03
- [fabacab/awesome-malware](https://github.com/fabacab/awesome-malware) — Curated malware source code and samples for research. Handle with appropriate care. — ★276 · 2021-03 · 💤 dormant

## Vulnerability Research, Fuzzing & Exploit Development

- [secfigo/Awesome-Fuzzing](https://github.com/secfigo/Awesome-Fuzzing) — The most complete fuzzing list: books, courses, fuzzers, corpora and tutorials. — ★5.9k · 2024-04 · 💤 dormant
- [sergey-pronin/Awesome-Vulnerability-Research](https://github.com/sergey-pronin/Awesome-Vulnerability-Research) — Vulnerability research methodology and learning material, oriented toward getting started. — ★1.3k · 2020-12 · 💤 dormant
- [huhusmang/Awesome-LLMs-for-Vulnerability-Detection](https://github.com/huhusmang/Awesome-LLMs-for-Vulnerability-Detection) — Tracks the fast-moving literature on using language models to find vulnerabilities. — ★1.2k · 2026-07
- [cpuu/awesome-fuzzing](https://github.com/cpuu/awesome-fuzzing) — Academically oriented fuzzing list tracking recent papers and research fuzzers. Fresher than `secfigo`. — ★983 · 2026-07
- [strongcourage/awesome-directed-fuzzing](https://github.com/strongcourage/awesome-directed-fuzzing) — Directed and targeted fuzzing literature specifically. Narrow, current, research-grade. — ★591 · 2026-07
- [IamAlch3mist/Awesome-Embedded-Systems-Vulnerability-Research](https://github.com/IamAlch3mist/Awesome-Embedded-Systems-Vulnerability-Research) — Embedded and firmware vulnerability research: emulation, rehosting and bug hunting. — ★503 · 2026-07

## Cloud, Container & Kubernetes

- [toniblyx/my-arsenal-of-aws-security-tools](https://github.com/toniblyx/my-arsenal-of-aws-security-tools) — The AWS security tooling reference — defensive, offensive, auditing and DFIR. Actively maintained and hard to beat. — ★9.5k · 2026-07
- [4ndersonLin/awesome-cloud-security](https://github.com/4ndersonLin/awesome-cloud-security) — Multi-cloud security list covering AWS, Azure and GCP tooling side by side. — ★2.5k · 2026-03
- [magnologan/awesome-k8s-security](https://github.com/magnologan/awesome-k8s-security) — The reference Kubernetes security list: benchmarks, policy engines, runtime security and research. — ★2k · 2026-07
- [jassics/awesome-aws-security](https://github.com/jassics/awesome-aws-security) — AWS security learning path — services, blogs, certifications — complementing `toniblyx`'s tool arsenal. — ★1.6k · 2026-04
- [Kyuu-Ji/Awesome-Azure-Pentest](https://github.com/Kyuu-Ji/Awesome-Azure-Pentest) — Azure and Entra ID penetration testing. Azure moves fast, so verify before relying on it. — ★1.2k · 2023-12 · 💤 dormant
- [JoasASantos/Awesome-Cloud-PenTest](https://github.com/JoasASantos/Awesome-Cloud-PenTest) — Offensive cloud testing across providers. — ★760 · 2022-08 · 💤 dormant
- [Funkmyster/awesome-cloud-security](https://github.com/Funkmyster/awesome-cloud-security) — Cloud security resources organized around frameworks and architecture rather than tools. — ★670 · 2025-05
- [Metarget/awesome-cloud-native-security](https://github.com/Metarget/awesome-cloud-native-security) — Cloud-native attack and defense research, notably strong on container escapes. — ★327 · 2023-11 · 💤 dormant
- [kai5263499/awesome-container-security](https://github.com/kai5263499/awesome-container-security) — Container security specifically: image scanning, runtime protection, supply chain. — ★250 · 2026-07

## DevSecOps & Software Supply Chain

- [sottlmarek/DevSecOps](https://github.com/sottlmarek/DevSecOps) — The most actively maintained DevSecOps list: pipeline security, IaC scanning, secrets management, container security. — ★6.8k · 2026-06
- [ossf/scorecard](https://github.com/ossf/scorecard) — Not a list but the OpenSSF tool that scores repository security posture. Included because supply chain work invariably starts here. — ★5.6k · 2026-07
- [devsecops/awesome-devsecops](https://github.com/devsecops/awesome-devsecops) — The community-authoritative DevSecOps list. Foundational, though updates have slowed. — ★5.4k · 2024-05 · 💤 dormant
- [bureado/awesome-software-supply-chain-security](https://github.com/bureado/awesome-software-supply-chain-security) — Supply chain security: SBOM, provenance, signing, SLSA. The best index of a domain that barely existed five years ago. — ★373 · 2026-06
- [We5ter/Awesome-DevSecOps-Platforms](https://github.com/We5ter/Awesome-DevSecOps-Platforms) — Focused on integrated DevSecOps platforms and vulnerability management systems rather than point tools. — ★318 · 2026-02

## Mobile Security

- [ashishb/android-security-awesome](https://github.com/ashishb/android-security-awesome) — The long-standing Android security list — tooling, papers, exploits — still actively updated. — ★9.6k · 2026-07
- [vaib25vicky/awesome-mobile-security](https://github.com/vaib25vicky/awesome-mobile-security) — Covers both platforms with strong coverage of testing methodology and checklists. — ★3.5k · 2024-03 · 💤 dormant
- [saeidshirazi/awesome-android-security](https://github.com/saeidshirazi/awesome-android-security) — Newer Android list weighted toward writeups, labs and current tooling. — ★1.9k · 2026-07
- [ashishb/osx-and-ios-security-awesome](https://github.com/ashishb/osx-and-ios-security-awesome) — The Apple platform counterpart: macOS and iOS security tooling and research. — ★1.7k · 2026-06
- [xtiankisutsa/awesome-mobile-CTF](https://github.com/xtiankisutsa/awesome-mobile-CTF) — Mobile CTF challenges and writeups. The most direct way to build hands-on skill. — ★1.2k · 2022-06 · 💤 dormant

## Hardware, Embedded, IoT & ICS/OT

- [jaredthecoder/awesome-vehicle-security](https://github.com/jaredthecoder/awesome-vehicle-security) — Automotive and CAN bus security — the established reference for vehicle work. — ★4.4k · 2026-05
- [nebgnahz/awesome-iot-hacks](https://github.com/nebgnahz/awesome-iot-hacks) — Collection of real IoT device hacks and teardowns. Valuable as case studies. — ★2.4k · 2020-05 · 💤 dormant
- [fkie-cad/awesome-embedded-and-iot-security](https://github.com/fkie-cad/awesome-embedded-and-iot-security) — The reference embedded/IoT security list, published by a research institute. Rigorous on firmware analysis and emulation. — ★2.4k · 2023-10 · 💤 dormant
- [ITI/ICS-Security-Tools](https://github.com/ITI/ICS-Security-Tools) — Curated ICS security tooling and protocol references, maintained under an academic institute. — ★2k · 2025-04
- [hslatman/awesome-industrial-control-system-security](https://github.com/hslatman/awesome-industrial-control-system-security) — ICS/SCADA security: protocol tooling, research and incident history. — ★2k · 2025-10
- [samanL33T/Awesome-Mainframe-Hacking](https://github.com/samanL33T/Awesome-Mainframe-Hacking) — Mainframe and z/OS security. Tiny field, and this is effectively its only index. — ★494 · 2025-01
- [JoasASantos/Awesome-Hardware-and-IoT-Hacking](https://github.com/JoasASantos/Awesome-Hardware-and-IoT-Hacking) — Hardware hacking tooling: JTAG, UART, side-channel and glitching. — ★405 · 2024-07 · 💤 dormant

## Wireless, Telecom & Protocol

- [W00t3k/Awesome-Cellular-Hacking](https://github.com/W00t3k/Awesome-Cellular-Hacking) — Cellular and telecom security: GSM through 5G, SDR tooling and protocol attacks. — ★4k · 2026-03
- [EnableSecurity/awesome-rtc-hacking](https://github.com/EnableSecurity/awesome-rtc-hacking) — VoIP, WebRTC and real-time communications security, from a consultancy specializing in it. — ★547 · 2026-06

## OSINT & Reconnaissance

- [edoardottt/awesome-hacker-search-engines](https://github.com/edoardottt/awesome-hacker-search-engines) — Search engines for recon: hosts, certificates, code, credentials, DNS. Immediately practical and actively maintained. — ★11k · 2026-07
- [cipher387/osint_stuff_tool_collection](https://github.com/cipher387/osint_stuff_tool_collection) — Over a thousand OSINT tools and services, meticulously categorized. — ★8.6k · 2026-05
- [jakejarvis/awesome-shodan-queries](https://github.com/jakejarvis/awesome-shodan-queries) — Curated Shodan queries for finding exposed systems. Narrow and effective. — ★7.6k · 2024-05 · 💤 dormant
- [Astrosp/Awesome-OSINT-List](https://github.com/Astrosp/Awesome-OSINT-List) — Broad, frequently updated OSINT tool and resource index. — ★3.9k · 2026-07
- [redhuntlabs/Awesome-Asset-Discovery](https://github.com/redhuntlabs/Awesome-Asset-Discovery) — Asset discovery and attack surface enumeration — the reconnaissance groundwork for both offense and defense. — ★2.8k · 2025-01 · 💤 dormant
- [cipher387/Dorks-collections-list](https://github.com/cipher387/Dorks-collections-list) — Index of Google and other search dork collections. — ★2.7k · 2025-04
- [danieldurnea/FBI-tools](https://github.com/danieldurnea/FBI-tools) — Large OSINT and investigation tool collection. Sensationally named; genuinely useful contents. — ★2.6k · 2025-03
- [cipher387/API-s-for-OSINT](https://github.com/cipher387/API-s-for-OSINT) — APIs usable for OSINT automation, which is where most serious recon ends up. — ★2.4k · 2025-05
- [rawfilejson/awesome-osint-arsenal](https://github.com/rawfilejson/awesome-osint-arsenal) — Recently curated OSINT toolkit organized by investigation type. — ★1.6k · 2026-07
- [ubikron/Awesome-AI-OSINT](https://github.com/ubikron/Awesome-AI-OSINT) — AI-assisted OSINT tooling and techniques. — ★735 · 2026-05
- [tracelabs/awesome-osint](https://github.com/tracelabs/awesome-osint) — OSINT resources curated by Trace Labs, oriented toward missing-persons search parties. — ★378 · 2026-02
- [osintambition/Awesome-Browser-Extensions-for-OSINT](https://github.com/osintambition/Awesome-Browser-Extensions-for-OSINT) — Browser extensions for investigation workflows. — ★373 · 2026-05
- [aaarghhh/awesome_osint_blockchain_analysis](https://github.com/aaarghhh/awesome_osint_blockchain_analysis) — Blockchain and cryptocurrency investigation resources. — ★367 · 2025-03
- [soxoj/awesome-osint-mcp-servers](https://github.com/soxoj/awesome-osint-mcp-servers) — MCP servers exposing OSINT capability to AI agents. Very new, and the clearest signal of where recon tooling is heading. — ★350 · 2026-07

## Cryptography

- [pFarb/awesome-crypto-papers](https://github.com/pFarb/awesome-crypto-papers) — Curated cryptography papers and tutorials for people who want to actually understand the primitives. — ★2.1k · 2024-10 · 💤 dormant
- [rust-cc/awesome-cryptography-rust](https://github.com/rust-cc/awesome-cryptography-rust) — Rust cryptography libraries and implementations — increasingly where new crypto code lands. — ★587 · 2026-07

## Blockchain, Web3 & Smart Contracts

- [Anugrahsr/Awesome-web3-Security](https://github.com/Anugrahsr/Awesome-web3-Security) — Broader web3 security: bridges, DeFi protocols, wallets and CTFs. — ★1.6k · 2026-03
- [crytic/awesome-ethereum-security](https://github.com/crytic/awesome-ethereum-security) — Ethereum security from Trail of Bits' blockchain team: analysis tooling, vulnerability classes and audit methodology. The authoritative entry. — ★1.5k · 2024-08 · 💤 dormant
- [saeidshirazi/Awesome-Smart-Contract-Security](https://github.com/saeidshirazi/Awesome-Smart-Contract-Security) — Smart contract security with strong coverage of recent exploits and postmortems. — ★903 · 2026-07
- [Mikerah/awesome-privacy-on-blockchains](https://github.com/Mikerah/awesome-privacy-on-blockchains) — Privacy technology in blockchain systems — mixers, zero-knowledge constructions, private transactions. — ★288 · 2025-11

## AI & ML Security

- [corca-ai/awesome-llm-security](https://github.com/corca-ai/awesome-llm-security) — The most-referenced LLM security list: prompt injection, jailbreaks, tooling and papers. — ★1.7k · 2025-08
- [DeepSpaceHarbor/Awesome-AI-Security](https://github.com/DeepSpaceHarbor/Awesome-AI-Security) — Adversarial machine learning and AI security literature, with strong academic grounding. — ★1.7k · 2026-03
- [ottosulin/awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) — AI security spanning frameworks, standards and offensive research. The most actively maintained here. — ★1.3k · 2026-07
- [stratosphereips/awesome-ml-privacy-attacks](https://github.com/stratosphereips/awesome-ml-privacy-attacks) — Privacy attacks against ML models: membership inference, model inversion, extraction. — ★640 · 2024-03 · 💤 dormant
- [EvanThomasLuke/Awesome-AI-Hacking-Agents](https://github.com/EvanThomasLuke/Awesome-AI-Hacking-Agents) — Autonomous offensive security agents. A brand-new category; expect rapid change. — ★621 · 2026-07

## Privacy

- [lissy93/personal-security-checklist](https://github.com/lissy93/personal-security-checklist) — Actionable personal security and privacy checklist, tiered by effort and threat model. The best thing to hand a non-specialist. — ★22k · 2026-02
- [lissy93/awesome-privacy](https://github.com/lissy93/awesome-privacy) — Privacy-respecting software and service alternatives, organized by what you're replacing. Well maintained with a companion website. — ★9.7k · 2026-07
- [KevinColemanInc/awesome-privacy](https://github.com/KevinColemanInc/awesome-privacy) — Privacy-focused tools and services with an emphasis on self-hosting. — ★1k · 2024-01 · 💤 dormant
- [paulaime/awesome-privacy](https://github.com/paulaime/awesome-privacy) — Recently maintained privacy tool index. — ★405 · 2026-07

## Bug Bounty

- [nahamsec/Resources-for-Beginner-Bug-Bounty-Hunters](https://github.com/nahamsec/Resources-for-Beginner-Bug-Bounty-Hunters) — The standard on-ramp to bug bounty hunting, from a well-known practitioner. Still the best first stop. — ★12.1k · 2024-07 · 💤 dormant
- [djadmin/awesome-bug-bounty](https://github.com/djadmin/awesome-bug-bounty) — Bug bounty programs, writeups and disclosure resources, organized by platform. — ★5.8k · 2026-03

## CTF & Training

- [apsdehal/awesome-ctf](https://github.com/apsdehal/awesome-ctf) — The reference CTF list: frameworks, wargames and per-category tooling for crypto, forensics, pwn and web. — ★11.7k · 2024-07 · 💤 dormant
- [0x90n/InfoSec-Black-Friday](https://github.com/0x90n/InfoSec-Black-Friday) — Annual roundup of security training and tooling deals. Genuinely useful once a year. — ★4.4k · 2025-11
- [husnainfareed/awesome-ethical-hacking-resources](https://github.com/husnainfareed/awesome-ethical-hacking-resources) — Learning resources for ethical hacking: labs, courses and certification paths. — ★3.7k · 2026-04
- [devploit/awesome-ctf-resources](https://github.com/devploit/awesome-ctf-resources) — Leaner, more current CTF resource list focused on practice platforms and tooling. — ★783 · 2026-06

## Social Engineering

- [giuliacassara/awesome-social-engineering](https://github.com/giuliacassara/awesome-social-engineering) — Social engineering resources: psychology, pretexting, phishing tooling and defensive awareness. Effectively the only serious index for this domain. — ★4.2k · 2023-04 · 💤 dormant

## GRC, Careers & Industry Reading

- [TalEliyahu/awesome-security-newsletters](https://github.com/TalEliyahu/awesome-security-newsletters) — Security newsletters and periodicals. The most efficient way to build an ongoing input stream. — ★1.3k · 2026-07
- [Arudjreis/awesome-security-GRC](https://github.com/Arudjreis/awesome-security-GRC) — Governance, risk and compliance: frameworks, audit tooling, policy templates and automation. Fills a real gap, since most security lists ignore GRC entirely. — ★1.1k · 2025-09

## Non-English

- [DropsOfZut/awesome-security-weixin-official-accounts](https://github.com/DropsOfZut/awesome-security-weixin-official-accounts) — 🇨🇳 Index of Chinese security WeChat accounts — a major publishing channel invisible to English-language search. — ★2.3k · 2026-07
- [tom0li/collection-document](https://github.com/tom0li/collection-document) — 🇨🇳 Large collection of Chinese-language security research and articles. — ★2.1k · 2024-09 · 💤 dormant
- [teamssix/awesome-cloud-security](https://github.com/teamssix/awesome-cloud-security) — 🇨🇳 Cloud security resources in Chinese, with notably strong Alibaba Cloud and Tencent Cloud coverage. — ★2.1k · 2024-10 · 💤 dormant
- [international-explore/awesome-privacy-chinese](https://github.com/international-explore/awesome-privacy-chinese) — 🇨🇳 Privacy tools and guidance for Chinese-speaking users. — ★475 · 2025-01 · 💤 dormant
- [Swordfish-Security/awesome-devsecops-russia](https://github.com/Swordfish-Security/awesome-devsecops-russia) — 🇷🇺 Russian-language DevSecOps resources and tooling. — ★352 · 2023-09 · 💤 dormant

## Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion bar and the
one-line entry format.

The `★` and date annotations are generated, never hand-written. After adding an entry, run:

```sh
./scripts/refresh.py
```

It reads every GitHub link in this file, queries the API, rewrites each annotation in place —
including adding or clearing the `archived` and `dormant` markers — and re-sorts each section by
stars. Don't hand-write annotations or hand-sort entries; both get overwritten. A monthly
[GitHub Action](.github/workflows/refresh.yml) runs it automatically.

Set `GITHUB_TOKEN` to avoid rate limits: `GITHUB_TOKEN=$(gh auth token) ./scripts/refresh.py`

## License

[CC0 1.0 Universal](LICENSE) — dedicated to the public domain. Attribution appreciated but not
required; the linked lists remain under their own licenses.
