project = 'CorosUpdate'
author = 'Your Name'
release = '1.0'

extensions = []
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static'] 

def setup(app):
    app.add_js_file("chatbot.js") 
