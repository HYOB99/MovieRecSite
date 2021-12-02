from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

#could've used errorhandler instead of app_errorhandler but I wanted to use these errorhandlers across the entire application.
@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500