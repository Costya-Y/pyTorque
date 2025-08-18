from __future__ import annotations

import typer
from typing import Optional
from .client import TorqueClient
from .config import TorqueConfig

app = typer.Typer(help="CLI for Quali Torque API")

@app.callback()
def main(
    base_url: Optional[str] = typer.Option(None, envvar="TORQUE_BASE_URL", help="Torque base API URL"),
    api_token: Optional[str] = typer.Option(None, envvar="TORQUE_API_TOKEN", help="API token"),
):
    pass

@app.command()
def blueprints(base_url: Optional[str] = typer.Option(None), api_token: Optional[str] = typer.Option(None)):
    cfg = TorqueConfig.from_env(base_url=base_url, api_token=api_token)
    client = TorqueClient(cfg)
    bps = client.list_blueprints()
    for bp in bps:
        typer.echo(f"{bp.id}\t{bp.name}")

if __name__ == "__main__":
    app()
