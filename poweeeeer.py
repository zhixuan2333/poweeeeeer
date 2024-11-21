#!/usr/bin/env python
import os
import click
import cv2

__version_info__ = (1, 2, 0)
__version__ = '.'.join(map(str, __version_info__))

def reverse_all_files(source: str, output: str):
    if os.path.isfile(source):
        click.echo(f"{source} is a file. Please ***not*** use -d option to reverse a file")
        return

    if not os.path.exists(source):
        click.echo(f"Directory {source} does not exist")
        return

    if not output:
        output = source + '_reverse'

    # Create output directory if not exists
    if not os.path.exists(output):
        os.makedirs(output)

    files = os.listdir(source)
    
    for file in files:
        input_path = os.path.join(source, file)
        output_path = os.path.join(output, file)
        reverse_file(input_path, output_path)

        click.echo(f"Reverse {input_path} to {output_path}")

def reverse_file(source: str, output: str):
    if not os.path.exists(source):
        click.echo(f"File {source} does not exist")
        return
    
    if os.path.isdir(source):
        click.echo(f"{source} is a directory. Please use -d option to reverse all files in the directory")
        return
    
    if not output:
        output = source.split('.')[0] + '_reverse.' + source.split('.')[1]

    file = cv2.imread(source)
    reverse_image = cv2.bitwise_not(file)
    cv2.imwrite(output, reverse_image)

    click.echo(f"Reverse {source} to {output}")

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__)
def cli():
    pass

@cli.command()
@click.argument('source')
@click.option("-d", "--directory", is_flag=True, help="If you want to reverse all images in the directory", default=False)
@click.option("-o", "--output", help="Output directory or output file name", required=False, type=click.Path())
def reverse(source: str, directory: bool, output: str):
    """Reverse color

    \b
    Example:
        ./poweeeeer.py reverse image.png
        ./poweeeeer.py reverse -d image/
    """
    if directory:
        reverse_all_files(source, output)
    else:
        reverse_file(source, output)

if __name__ == '__main__':
    cli()