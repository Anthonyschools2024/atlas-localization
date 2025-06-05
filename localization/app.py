from flask import Flask
from flask_babel import Babel, _, ngettext

# --- Basic Flask App Setup ---
app = Flask(__name__)
# For Flask-Babel, you'd typically configure language settings, e.g.:
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['LANGUAGES'] = {
    'en': 'English',
    'es': 'Español',
    'fr': 'Français'
}
babel = Babel(app)

# --- Example Global Variables (or they could be in functions/routes) ---
# These are the strings we want to mark for translation.

# Simple string marked for translation using _()
WELCOME_MESSAGE = _("Welcome to our application!")
LOGIN_PROMPT = _("Please log in to continue.")
ERROR_NOT_FOUND = _("Error: The requested page was not found.")

# Example function that might return a translatable string
def get_status_message(is_success):
    if is_success:
        return _("Operation completed successfully.")
    else:
        return _("Operation failed. Please try again.")

# Example usage of ngettext() for pluralization
def get_item_count_message(number_of_items):
    # The ngettext function will choose the correct string based on number_of_items.
    # The `%(num)d` is a placeholder for the number.
    # Note: In Flask-Babel, you can often pass the number directly for interpolation.
    message_template = ngettext("You have %(num)d item.",
                                "You have %(num)d items.",
                                number_of_items)
    return message_template % {'num': number_of_items}

# --- Example Usage (e.g., in a Flask route, or just for demonstration) ---
# In a real Flask app, these would be part of your routes or views.
if __name__ == '__main__':
    # Simulate different scenarios
    current_items = 1
    print("--- Simulating Application Output ---")
    print(WELCOME_MESSAGE)  # This will be "Welcome to our application!" initially
    print(get_status_message(True))
    print(get_item_count_message(current_items))

    current_items = 5
    print(get_item_count_message(current_items))

    # In a real Flask app, you might have something like:
    # @app.route('/')
    # def home():
    #     greeting = _("Hello, User!")
    #     items = 3
    #     item_info = ngettext("You have %(num)d new message.",
    #                          "You have %(num)d new messages.",
    #                          items) % {'num': items}
    #     return f"{greeting} {item_info}"

    # To actually run this as a Flask app (optional for just seeing translations):
    # app.run(debug=True)
    print("--- End of Simulation ---")
    print("\nTo see translations, you would run Babel to extract these strings,")
    print("translate them, compile them, and then run the app in the context")
    print("of a specific locale (e.g., by setting the locale in Flask-Babel).")
