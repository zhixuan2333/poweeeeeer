#!/usr/bin/env python
import click
import cv2

def reverse_all_files(input: str, output: str):
    import os

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
    if not output:
        output = input.split('.')[0] + '_reverse.' + input.split('.')[1]

    file = cv2.imread(input)
    reverse = cv2.bitwise_not(file)
    cv2.imwrite(output, reverse)

    click.echo(f"Reverse {input} to {output}")


@click.group()
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