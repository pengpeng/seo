#!/usr/bin/env python3
"""Wave 2a tracking update: 31 market items"""
import os
os.chdir('/Users/pengpeng/seo')

with open('directions/market/apps.md', 'r') as f:
    apps = f.read()

updates = [
    ('| Listmonk | High performance, self-hosted, newsletter and mailing list manager with a modern dashboard | ⬜ |',
     '| Listmonk | High performance, self-hosted, newsletter and mailing list manager with a modern dashboard | ✅ [报告](directions/market/reports/listmonk.md) |'),
    ('| MaxKB | Ready-to-use, flexible RAG Chatbot | ⬜ |',
     '| MaxKB | Ready-to-use, flexible RAG Chatbot | ✅ [报告](directions/market/reports/maxkb.md) |'),
    ('| Medusa | The world\'s most flexible commerce platform. | ⬜ |',
     '| Medusa | The world\'s most flexible commerce platform. | ✅ [报告](directions/market/reports/medusa.md) |'),
    ('| Memos | Effortlessly craft your impactful content. | ⬜ |',
     '| Memos | Effortlessly craft your impactful content. | ✅ [报告](directions/market/reports/memos.md) |'),
    ('| MTranServer | A high-performance offline translation server with minimal resource requirements | ⬜ |',
     '| MTranServer | A high-performance offline translation server with minimal resource requirements | ✅ [报告](directions/market/reports/mtranserver.md) |'),
    ('| NocoBase | Extensibility-first, open-source, no-code platform | ⬜ |',
     '| NocoBase | Extensibility-first, open-source, no-code platform | ✅ [报告](directions/market/reports/nocobase.md) |'),
    ('| Novel | Notion-style WYSIWYG editor with AI-powered autocompletion | ⬜ |',
     '| Novel | Notion-style WYSIWYG editor with AI-powered autocompletion | ✅ [报告](directions/market/reports/novel.md) |'),
    ('| Odoo | All your business on one platform. | ⬜ |',
     '| Odoo | All your business on one platform. | ✅ [报告](directions/market/reports/odoo.md) |'),
    ('| PDFMathTranslate | PDF scientific paper translation with preserved formats. | ⬜ |',
     '| PDFMathTranslate | PDF scientific paper translation with preserved formats. | ✅ [报告](directions/market/reports/pdfmathtranslate.md) |'),
    ('| Radicale | Free and Open-Source CalDAV and CardDAV Server | ⬜ |',
     '| Radicale | Free and Open-Source CalDAV and CardDAV Server | ✅ [报告](directions/market/reports/radicale.md) |'),
    ('| Rallly | Open-source scheduling and collaboration tool designed to make organizing events and meetings easier | ⬜ |',
     '| Rallly | Open-source scheduling and collaboration tool designed to make organizing events and meetings easier | ✅ [报告](directions/market/reports/rallly.md) |'),
    ('| Refly | The Open-Source Agentic Workspace for Human-AI Collaboration. | ⬜ |',
     '| Refly | The Open-Source Agentic Workspace for Human-AI Collaboration. | ✅ [报告](directions/market/reports/refly.md) |'),
    ('| SeaTable | SeaTable is a no-code database and app-building platform. | ⬜ |',
     '| SeaTable | SeaTable is a no-code database and app-building platform. | ✅ [报告](directions/market/reports/seatable.md) |'),
    ('| Stirling-PDF | A locally hosted one-stop shop for all your PDF needs. | ⬜ |',
     '| Stirling-PDF | A locally hosted one-stop shop for all your PDF needs. | ✅ [报告](directions/market/reports/stirling-pdf.md) |'),
    ('| Twenty | The #1 Open-Source CRM - A modern alternative to Salesforce | ⬜ |',
     '| Twenty | The #1 Open-Source CRM - A modern alternative to Salesforce | ✅ [报告](directions/market/reports/twenty.md) |'),
    ('| Appsmith | Platform to build admin panels, internal tools, and dashboards | ⬜ |',
     '| Appsmith | Platform to build admin panels, internal tools, and dashboards | ✅ [报告](directions/market/reports/appsmith.md) |'),
    ('| Bytebase | World\'s most advanced database DevOps and CI/CD for Developer, DBA and Platform Engineering teams. | ⬜ |',
     '| Bytebase | World\'s most advanced database DevOps and CI/CD for Developer, DBA and Platform Engineering teams. | ✅ [报告](directions/market/reports/bytebase.md) |'),
    ('| Code Server | VS Code in the browser | ⬜ |',
     '| Code Server | VS Code in the browser | ✅ [报告](directions/market/reports/code-server.md) |'),
    ('| Coder | Self-Hosted Cloud Development Environments. | ⬜ |',
     '| Coder | Self-Hosted Cloud Development Environments. | ✅ [报告](directions/market/reports/coder.md) |'),
    ('| Crawl4AI | Open-source LLM Friendly Web Crawler & Scrape | ⬜ |',
     '| Crawl4AI | Open-source LLM Friendly Web Crawler & Scrape | ✅ [报告](directions/market/reports/crawl4ai.md) |'),
    ('| Directus | A composable data platform to build your Headless CMS, BaaS, and more. | ⬜ |',
     '| Directus | A composable data platform to build your Headless CMS, BaaS, and more. | ✅ [报告](directions/market/reports/directus.md) |'),
    ('| Hoppscotch | Open source API development ecosystem. | ⬜ |',
     '| Hoppscotch | Open source API development ecosystem. | ✅ [报告](directions/market/reports/hoppscotch.md) |'),
    ('| JupyterHub | Deploying JupyterHub on Olares | ⬜ |',
     '| JupyterHub | Deploying JupyterHub on Olares | ✅ [报告](directions/market/reports/jupyterhub.md) |'),
    ('| Metabase | Business Intelligence and Embedded Analytics tool that lets everyone work with data | ⬜ |',
     '| Metabase | Business Intelligence and Embedded Analytics tool that lets everyone work with data | ✅ [报告](directions/market/reports/metabase.md) |'),
    ('| Netdata | High-performance, open-source observability platform | ⬜ |',
     '| Netdata | High-performance, open-source observability platform | ✅ [报告](directions/market/reports/netdata.md) |'),
    ('| Halo | Powerful and easy-to-use open source website building tool | ⬜ |',
     '| Halo | Powerful and easy-to-use open source website building tool | ✅ [报告](directions/market/reports/halo.md) |'),
    ('| Jaaz | AI design agent, local alternative for Lovart | ⬜ |',
     '| Jaaz | AI design agent, local alternative for Lovart | ✅ [报告](directions/market/reports/jaaz.md) |'),
    ('| Miniflux | Miniflux is a minimalist and opinionated feed reader. | ⬜ |',
     '| Miniflux | Miniflux is a minimalist and opinionated feed reader. | ✅ [报告](directions/market/reports/miniflux.md) |'),
    ('| Mealie | A Place For All Your Recipes | ⬜ |',
     '| Mealie | A Place For All Your Recipes | ✅ [报告](directions/market/reports/mealie.md) |'),
    ('| Photoview | Photo gallery for self-hosted personal servers | ⬜ |',
     '| Photoview | Photo gallery for self-hosted personal servers | ✅ [报告](directions/market/reports/photoview.md) |'),
    ('| qBittorrent | Free BitTorrent downloader | ⬜ |',
     '| qBittorrent | Free BitTorrent downloader | ✅ [报告](directions/market/reports/qbittorrent.md) |'),
]

ok = 0
for old, new in updates:
    if old in apps:
        apps = apps.replace(old, new)
        ok += 1
        print(f"✅ {old[:60]}...")
    else:
        print(f"❌ NOT FOUND: {old[:70]}")

with open('directions/market/apps.md', 'w') as f:
    f.write(apps)
print(f"\n=== TOTAL: {ok}/{len(updates)} updated ===")
