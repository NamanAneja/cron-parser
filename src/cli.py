import click

from src.controller.cron_controller import CronController


@click.command()
@click.argument('expression')
def cli(expression):
    output = CronController().evaluate(expression)
    click.echo(output)
