from flask import Flask, request, g
from flask_babel import Babel, _, ngettext

# Initialize Flask app
app = Flask(__name__)

# --- Flask-Babel Configuration ---
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
# Assuming 'translations' directory is at the project root,
# and app.py is in a 'localization' subdirectory.
# If app.py is at the project root, this would be './translations'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = '../translations'
app.config['LANGUAGES'] = {
    'en': 'English',
    'fr': 'Français'
    # Add other supported languages here
}

babel = Babel(app)

# --- Locale Selector Function ---
# This function is called by Babel for each request to determine the language to use.
@babel.localeselector
def get_locale():
    # 1. Try to get language from user-specific settings if available
    #    (e.g., user profile, session)
    # user = getattr(g, 'user', None)
    # if user is not None and user.locale in app.config['LANGUAGES']:
    #     return user.locale

    # 2. Try to get language from URL parameters
    # lang_from_url = request.args.get('lang')
    # if lang_from_url and lang_from_url in app.config['LANGUAGES']:
    #     return lang_from_url

    # 3. Otherwise, try to use the browser's language preference
    return request.accept_languages.best_match(list(app.config['LANGUAGES'].keys()))

# --- Strings Marked for Translation (from previous tasks) ---
# These can be defined globally, within functions, or wherever needed.
# The _() and ngettext() calls will now use the selected locale.

WELCOME_MESSAGE = _("Welcome to our application!")
LOGIN_PROMPT = _("Please log in to continue.")
ERROR_NOT_FOUND = _("Error: The requested page was not found.")

def get_status_message(is_success):
    if is_success:
        return _("Operation completed successfully.")
    else:
        return _("Operation failed. Please try again.")

def get_item_count_message(number_of_items):
    message_template = ngettext("You have %(num)d item.",
                                "You have %(num)d items.",
                                number_of_items)
    return message_template % {'num': number_of_items}

# --- Example Flask Routes ---
@app.route('/')
def index():
    # Example from Task 7 description
    greeting = _("Hello, World!") # A new string example for this task

    # Using one of our pre-defined translated strings
    # You can also pass variables to translated strings if they are formatted accordingly
    # e.g., _("Welcome, %(user_name)s!", user_name="Guest")
    return f"""
        <h1>{greeting}</h1>
        <p>{WELCOME_MESSAGE}</p>
        <p>{get_status_message(True)}</p>
        <p>{get_item_count_message(1)}</p>
        <p>{get_item_count_message(5)}</p>
        <p>Try adding <code>?hl=fr</code> or <code>Accept-Language: fr</code> in request headers to see French translations.</p>
        <p>Current locale: {get_locale()}</p>
    """

@app.route('/login')
def login_page():
    return f"<p>{LOGIN_PROMPT}</p>"

# --- Main execution ---
if __name__ == "__main__":
    # Make sure debug=False for production
    app.run(debug=True)
