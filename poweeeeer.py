#!/usr/bin/env python
import os
import click
import cv2

__version_info__ = (1, 0, 0)
__version__ = '.'.join(map(str, __version_info__))

def reverse_all_files(input: str, output: str):
    if os.path.isfile(input):
        click.echo(f"{input} is a file. Please ***not*** use -d option to reverse a file")
        return

    if not os.path.exists(input):
        click.echo(f"Directory {input} does not exist")
        return

    if not output:
        output = input + '_reverse'

    # Create output directory if not exists
    if not os.path.exists(output):
        os.makedirs(output)

    files = os.listdir(input)
    
    for file in files:
        input_path = os.path.join(input, file)
        output_path = os.path.join(output, file)
        reverse_file(input_path, output_path)

        click.echo(f"Reverse {input_path} to {output_path}")

def reverse_file(input: str, output: str):
    if not os.path.exists(input):
        click.echo(f"File {input} does not exist")
        return
    
    if os.path.isdir(input):
        click.echo(f"{input} is a directory. Please use -d option to reverse all files in the directory")
        return
    
    if not output:
        output = input.split('.')[0] + '_reverse.' + input.split('.')[1]

    file = cv2.imread(input)
    reverse = cv2.bitwise_not(file)
    cv2.imwrite(output, reverse)

    click.echo(f"Reverse {input} to {output}")


@click.group()
@click.version_option(__version__)
def cli():
    pass

@cli.command()
@click.argument('input')
@click.option("-d", "--directory", is_flag=True, help="If you want to reverse all images in the directory", default=False)
@click.option("-o", "--output", help="Output directory or output file name", required=False, type=click.Path())
def reverse(input: str, directory: bool, output: str):
    """Reverse color"""
    if directory:
        reverse_all_files(input, output)
    else:
        reverse_file(input, output)

if __name__ == '__main__':
    cli()