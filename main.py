import os
import sys
import asyncio
import webbrowser

from rich import print
from data.plugins import *
from rich.prompt import Prompt
from rich.console import Console

console = Console()


async def main():
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")

            text = Prompt.ask(
                "[bold white][[bold yellow]>[bold white]] [bold cyan]Enter your text"
            )
            url = await generate(text)
            print(
                f"[bold white][[bold green]+[bold white]] Generated at: [bold cyan]{url}"
            )

            open_prompt = console.input(
                "[bold white][[bold yellow]?[bold white]] [bold cyan]Would you like to open the generated paste in your browser? [bold cyan](y/n) "
            )

            if open_prompt.lower() == "y":
                webbrowser.open(url)

            console.input(
                "[bold white][[bold yellow]/[bold white]] [bold cyan]Press Enter to continue or CTRL+C to exit[/bold cyan]"
            )
    except KeyboardInterrupt:
        print(
            "\n[bold white][[bold red]![bold white]] [bold cyan]Exiting...[/bold cyan]"
        )
        sys.exit(0)


if __name__ == "__main__":
    clear_cache()
    asyncio.run(main())
