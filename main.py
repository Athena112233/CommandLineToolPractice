import click

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def say_hello(name):
    click.echo(f"Hello World! Nice meeting you {name}!")

if __name__ == '__main__':
    say_hello()