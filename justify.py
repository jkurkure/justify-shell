from rich.console import Console
console = Console()

console.print("[green]Welcome to[/green] [red][italic]JustifyShell[/italic][/red]")
console.print("[green]The first line of text you enter will be the [bold]benchmark[/bold] for the rest of the essay.[/green]\n")

PROMPT = "[yellow]!>- [/yellow]"
moveUp = lambda:print('\033[1A', end="")
clear = lambda n:print(("\b" * n) + (" " * n) + ("\b" * n), end="")

line0 = console.input(PROMPT)
benchmark = len(line0)
moveUp()
clear(benchmark + len(PROMPT))

moveUp()
console.print(f"[blue]Targeting {benchmark} characters per line.[/blue]\n")
print(line0)

buf = ""
while True:
    console.print(f"[purple]{buf}[/purple]")
    line = console.input(PROMPT)

    if line == ":q":
        moveUp()
        clear(len(line) + len(PROMPT))
        moveUp()
        clear(len(buf))

        console.print(buf)
        exit()
    else:
        moveUp()
        clear(len(line) + len(PROMPT))
        moveUp()
        clear(len(buf))
        buf += " " + line

        if len(buf) == benchmark:
            console.print(buf)
            buf = ""
        else:
            while len(buf) > benchmark:
                console.print(buf[:benchmark])
                buf = buf[benchmark:]