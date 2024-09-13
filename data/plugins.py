import os
import sys
import aiohttp
import pathlib
import urllib.parse

from rich.console import Console

console = Console()


def clear_cache():
    [p.unlink() for p in pathlib.Path(".").rglob("*.py[co]")]
    [p.rmdir() for p in pathlib.Path(".").rglob("__pycache__")]


async def generate(text):
    url = f"https://paste-pgpj.onrender.com?p={urllib.parse.quote(text)}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                console.print(
                    f"[bold white][[bold red]![bold white]] Paste responded with code {response.status}, unable to generate."
                )
                os.system("pause >nul")
                sys.exit(0)

            return url
