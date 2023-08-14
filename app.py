from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

def text_format(aster, insert, factor, note_url):
    """Format the markdown with appropriate tabs and asterisks."""
    return '\t' * factor + ('*' if aster else '') + f' [{insert}]({note_url})\n'

def bear_note_url(identifier, title):
    """Return a callback URL for Bear app."""
    title=title.replace(" ","%20")
    return f'bear://x-callback-url/open-note?id={identifier}&header={title}' if identifier else ""

def process_html(html_content, identifier, checks):
    """Process the HTML content and return a markdown formatted Table of Contents."""
    bs = BeautifulSoup(html_content, 'html.parser')
    collectList = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5'])
    scrapResult = "# Table of Contents\n"

    for tag in collectList:
        insert = tag.get_text()
        note_url = bear_note_url(identifier, insert)
        scrapResult += text_format(checks[tag.name], insert, int(tag.name[1]) - 1, note_url)

    scrapResult += '***\n'
    return scrapResult

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    """Scrape the HTML content and return a Table of Contents."""
    html_file = request.files.get('html_file')
    if not html_file:
        return jsonify({'error': 'HTML file not provided!'}), 400

    html_content = html_file.read().decode('utf-8')
    identifier = request.form['identifier']

    if not identifier:
        return jsonify({'error': 'Identifier not provided!'}), 400

    checks = {
        'h1': request.form.get('checkh1', ''),
        'h2': request.form.get('checkh2', ''),
        'h3': request.form.get('checkh3', ''),
        'h4': request.form.get('checkh4', ''),
        'h5': request.form.get('checkh5', '')
    }

    scrap_result = process_html(html_content, identifier, checks)
    return scrap_result

if __name__ == '__main__':
    app.run(debug=True)