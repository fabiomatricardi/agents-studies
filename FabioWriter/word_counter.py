import re
import click

def count_markdown_words(content):
    # 1. Remove Markdown links, images, and HTML tags
    text = re.sub(r'!\[.*?\]\(.*?\)', '', content)  # Images
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)      # Links
    text = re.sub(r'<.*?>', '', text)               # HTML tags
    
    # 2. Remove Markdown formatting characters (headers, bold, italic, code blocks)
    text = re.sub(r'#+\s+', '', text)               # Headers
    text = re.sub(r'[*_`~]+', '', text)             # Bold/Italic/Code/Strikethrough
    text = re.sub(r'[-*+]\s+', '', text)            # List bullets
    text = re.sub(r'\d+\.\s+', '', text)            # Ordered list numbers

    # 3. Split by whitespace and filter out empty strings
    words = text.split()
    return len(words)

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    """Simple CLI to count words in a Markdown file, excluding syntax."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    word_count = count_markdown_words(content)
    
    click.echo(f"File: {filename}")
    click.secho(f"Word Count: {word_count}", fg='green', bold=True)

if __name__ == '__main__':
    main()