# type: ignore[attr-defined]

import typer
from rich.console import Console

from todoist_quick_capture import version
from todoist_quick_capture.add import add_task
from todoist_quick_capture.get_token import get_api_token

app = typer.Typer(
    name="todoist_quick_capture",
    help="Awesome `todoist_quick_capture` is a Python cli/package created with https://github.com/Undertone0809/python-package-template",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(
            f"[yellow]todoist_quick_capture[/] version: [bold blue]{version}[/]"
        )
        raise typer.Exit()


@app.command(name="")
def main(
    task: str,
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the todoist_quick_capture package.",
    ),
) -> None:
    api_token = get_api_token(None)
    task = add_task(text=task, token=api_token)


if __name__ == "__main__":
    app()
