# Import necessary modules from Flask for web application functionality
# request: to access incoming request data (like headers for language preference)
from flask import Flask, request

# Import localization utilities from Flask-Babel
# gettext (aliased as _): for marking strings as translatable
# ngettext: for pluralization (imported here, though not used in this specific example,
#           it's good practice to include if pluralization might be needed later)
from flask_babel import gettext as _, ngettext

# Import Babel for managing translations and the underscore alias again for convenience
# (Note: _ was already imported as gettext, this is a stylistic choice or a remnant,
# but functionally harmless as it refers to the same gettext function in this context)
from flask_babel import Babel, _

# --- Application Setup ---

# Initialize the Flask application
# __name__ helps Flask determine the root path for the application
app = Flask(__name__)

# Initialize Babel with the app. This first instantiation is technically valid,
# though it will be immediately re-configured with a locale_selector below.
# All original elements of the code are preserved.
babel = Babel(app)

# --- Babel Configuration ---

# Set the default locale for the application
# This is used if no better match can be found or if locale detection is not set up.
app.config["BABEL_DEFAULT_LOCALE"] = "en" # English

# Specify the directory where translation files (.po, .mo) are stored.
# Flask-Babel will look for translations in './translations/<locale>/LC_MESSAGES/messages.mo'
app.config["BABEL_TRANSLATION_DIRECTORIES"] = "./translations"

# --- Locale Selection ---

# Define a function to determine the best locale for each request.
# This function will be called by Babel for every request to select the appropriate language.
def get_locale():
    # Use request.accept_languages to get the user's preferred languages from the HTTP 'Accept-Language' header.
    # best_match will find the best supported language ("en" or "fr") based on the user's preferences.
    # This is the recommended way to handle language selection dynamically.
    return request.accept_languages.best_match(["en", "fr"]) # Supported languages: English and French

# Re-initialize Babel with the Flask app and our custom locale_selector function.
# This setup ensures that get_locale is used to pick the language for each request.
babel = Babel(app, locale_selector=get_locale)

# --- Application Routes ---

# Define a route for the homepage ("/") of the application.
@app.route("/")
def index():
    # Use the _() function (gettext) to mark the string for translation.
    # Flask-Babel will look up the translation of "Hello, World!"
    # in the appropriate language file based on the selected locale.
    # This will display the localized greeting message.
    return _("Hello, World!")

# --- Main Execution Block ---

# This block ensures that the Flask development server runs only when the script is executed directly
# (not when imported as a module).
if __name__ == "__main__":
    # Run the Flask application.
    # By default, it runs on http://127.0.0.1:5000/
    # debug=True can be added for development, but is not included here to preserve original elements.
    app.run()
