import click

from src.controller.cron_controller import CronController


@click.command()
@click.argument('expression')
def cli(expression):
    # parser = CronExpression(expression).parse()
    output = CronController().evaluate(expression)
    # output = parser.format_as_table()
    click.echo(output)

# if __name__ == '__main__':
#     cli()