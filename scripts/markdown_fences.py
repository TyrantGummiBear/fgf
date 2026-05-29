"""Preserve fenced code blocks (e.g. mermaid) when translating markdown."""

from __future__ import annotations

import re

FENCE_RE = re.compile(r"```[\s\S]*?```", re.MULTILINE)


def repair_fence_newlines(content: str) -> str:
    """Fix markdown where translation glued prose to ``` fences."""
    content = re.sub(r"([^\n`])```(\w*)", r"\1\n\n```\2", content)
    content = re.sub(r"```(#+\s)", r"```\n\n\1", content)
    content = re.sub(r"```(\|)", r"```\n\n\1", content)
    content = re.sub(r"```---", "```\n\n---", content)
    return content


def sync_fenced_blocks(en_content: str, loc_content: str) -> str:
    """Replace locale fenced blocks with English originals (mermaid must stay English)."""
    en_blocks = FENCE_RE.findall(en_content)
    if not en_blocks:
        return loc_content

    loc_content = repair_fence_newlines(loc_content)
    loc_blocks = FENCE_RE.findall(loc_content)

    if len(en_blocks) != len(loc_blocks):
        return loc_content

    for en_block, loc_block in zip(en_blocks, loc_blocks):
        if en_block != loc_block:
            loc_content = loc_content.replace(loc_block, en_block, 1)

    return loc_content
