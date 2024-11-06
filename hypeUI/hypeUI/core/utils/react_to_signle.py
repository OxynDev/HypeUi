import os
from bs4 import BeautifulSoup

def inline_css_and_js_in_html(html_file_path, ui_dir_name):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    css_links = soup.find_all('link', rel='stylesheet')

    for link in css_links:
        css_link = link.get('href')
        css_file_path = os.path.join(os.path.dirname(html_file_path), css_link.lstrip('/'))

        try:
            with open(css_file_path, 'r', encoding='utf-8') as css_file:
                css_content = css_file.read()

            style_tag = soup.new_tag('style')
            style_tag.string = css_content

            link.replace_with(style_tag)

        except FileNotFoundError:
            print(f"Warning: CSS file '{css_link}' not found. Skipping.")
    
    js_scripts = soup.find_all('script', src=True)

    for script in js_scripts:
        js_link = script.get('src')
        js_file_path = os.path.join(os.path.dirname(html_file_path), js_link.lstrip('/'))

        try:
            with open(js_file_path, 'r', encoding='utf-8') as js_file:
                js_content = js_file.read()

            script_tag = soup.new_tag('script', type='module')
            script_tag.string = js_content

            script.replace_with(script_tag)

        except FileNotFoundError:
            print(f"Warning: JavaScript file '{js_link}' not found. Skipping.")
    
    with open(f'{ui_dir_name}/out.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))
    
    print("CSS and JavaScript inlined successfully!")
    return str(soup)


