from flask import Flask, render_template, request
import re

app = Flask(__name__)
# only index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_urls', methods=['POST'])
def extract_urls():
    input_text = request.form.get('urls')
    if not input_text:
        return render_template('index.html', urls=[], emails=[], codes=[], error="No input provided")

    # Extract all URLs from the input text
    raw_urls = re.findall(r'https?://\S+', input_text)

    # Remove commas or unwanted trailing characters from URLs
    clean_urls = [url.rstrip(',') for url in raw_urls]

    # Extract all email addresses from the input text
    emails = re.findall(r'[\w\.]+@[\w\.-]+', input_text)

    # Extract all codes matching specific format patterns (example: PTID-CDE-DEC-23-12 and others)
    codes = re.findall(r'\b[A-Z]+-[A-Z]+-[A-Z]+-\d+-\d+\b|\b[A-Z]+-[A-Z]+-[A-Z]+-[A-Z]+-[A-Z]+(?:_\w+)*(?: \w+)*\b', input_text)

    return render_template('index.html', urls=clean_urls, emails=emails, codes=codes, error=None)

if __name__ == '__main__':
    app.run(debug=True)
