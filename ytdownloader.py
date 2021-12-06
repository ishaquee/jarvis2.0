from rich.console import Console
from time import sleep

console = Console()

console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
console.print(locals())
console.print("FOO", style="white on blue")

console.log("Hello, World!")

console.print_json('[false, true, null, "foo"]')





with console.status("Working..."):
    console.rule("[bold red]Chapter 2")

from rich.console import Console

console = Console(width=20)

style = "bold white on blue"
console.print("Rich", style=style)
console.print("Rich", style=style, justify="left")
console.print("Rich", style=style, justify="center")
console.print("Rich", style=style, justify="right")


console = Console()
#console.input("What is [i]your[/i] [bold red]name[/]? :smiley: ")

console = Console(record=True)
error_console = Console(stderr=True)


# console = Console()
# with console.screen():
#     console.print(locals())
#     sleep(5)


console.print("foo [not bold]bar[/not bold] baz", style="bold")

console.print("Hello", style="#af00ff")
console.print("Hello", style="rgb(175,0,255)")
console.print("DANGER!", style="red on white")
console.print("Danger, Will Robinson!", style="blink bold red underline on white")

console.print("Google", style="link https://google.com")


from rich.style import Style


danger_style = Style(color="red", blink=True, bold=True)
console.print("Danger, Will Robinson!", style=danger_style)


from rich.console import Console
from rich.theme import Theme
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})
console = Console(theme=custom_theme)
console.print("This is information", style="info")
console.print("[warning]The pod bay doors are locked[/warning]")
console.print("Something terrible happened!", style="danger")


from rich.console import Console
from rich.theme import Theme
console = Console(theme=Theme({"repr.number": "bold green blink"}))

console.print("The total is 128")
from rich import print
print(r"foo\[bar]")
print("[bold red]alert![/bold red] Something happened")



from rich.console import Console
from rich.text import Text

console = Console()
text = Text("Hello, World!")
text.stylize("bold magenta", 0, 6)
console.print(text)


from rich import print
from rich.panel import Panel
from rich.text import Text
panel = Panel(Text("Hello", justify="right"))
print(panel)






from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme

class EmailHighlighter(RegexHighlighter):
    """Apply style to anything that looks like an email."""

    base_style = "example."
    highlights = [r"(?P<email>[\w-]+@([\w-]+\.)+[\w-]+)"]


theme = Theme({"example.email": "bold magenta"})
console = Console(highlighter=EmailHighlighter(), theme=theme)
console.print("Send funds to money@example.org")


from rich import print
from rich.pretty import Pretty
from rich.panel import Panel

pretty = Pretty(locals())
panel = Panel(pretty)
print(panel)






import rich.repr

@rich.repr.auto
class Bird:
    def __init__(self, name, eats=None, fly=True, extinct=False):
        self.name = name
        self.eats = list(eats) if eats else []
        self.fly = fly
        self.extinct = extinct


BIRDS = {
    "gull": Bird("gull", eats=["fish", "chips", "ice cream", "sausage rolls"]),
    "penguin": Bird("penguin", eats=["fish"], fly=False),
    "dodo": Bird("dodo", eats=["fruit"], fly=False, extinct=True)
}
from rich import print
print(BIRDS)


from rich.console import Console


def foo(n):
    return bar(n)


def bar(n):
    return foo(n)


console = Console()

try:
    foo(1)
except Exception:
    console.print_exception(max_frames=20)



# from rich.prompt import Confirm
# is_rich_great = Confirm.ask("Do you like rich?")
# assert is_rich_great


MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""
from rich.console import Console
from rich.markdown import Markdown

console = Console()
md = Markdown(MARKDOWN)
console.print(md)


from rich import print
from rich.panel import Panel
print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))



from rich.progress import track


# import time

# from rich.progress import Progress

# with Progress() as progress:

#     task1 = progress.add_task("[red]Downloading...", total=100)
#     task2 = progress.add_task("[green]Processing...", total=100)
#     task3 = progress.add_task("[cyan]Cooking...", total=100)

#     while not progress.finished:
#         progress.update(task1, advance=0.5)
#         progress.update(task2, advance=0.3)
#         progress.update(task3, advance=0.9)
#         time.sleep(0.02)




# from time import sleep

# from rich.table import Column
# from rich.progress import Progress, BarColumn, TextColumn

# text_column = TextColumn("{task.description}", table_column=Column(ratio=1))
# bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))
# progress = Progress(text_column, bar_column, expand=True)

# with progress:
#     for n in progress.track(range(100)):
#         progress.print(n)
#         sleep(0.1)        

from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)


import time

from rich.live import Live
from rich.table import Table

table = Table()
table.add_column("Row ID")
table.add_column("Description")
table.add_column("Level")

with Live(table, refresh_per_second=4) as live:  # update 4 times a second to feel fluid
    for row in range(12):
        live.console.print(f"Working on row #{row}")
        time.sleep(0.4)
        table.add_row(f"{row}", f"description {row}", "[red]ERROR")


import random
import time

from rich.live import Live
from rich.table import Table


def generate_table() -> Table:
    """Make a new table."""
    table = Table()
    table.add_column("ID")
    table.add_column("Value")
    table.add_column("Status")

    for row in range(random.randint(2, 6)):
        value = random.random() * 100
        table.add_row(
            f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
        )
    return table


with Live(generate_table(), refresh_per_second=4) as live:
    for _ in range(40):
        time.sleep(0.4)
        live.update(generate_table())        