from flask import Blueprint, jsonify, request, render_template, url_for, abort
import os
import datetime
import random

bp_do_redirect = Blueprint('test_link', __name__)
@bp_do_redirect.route('/<path:link>')
def redirect_check(link):
    
    if link == os.environ['CREATEDKEY']:
    #If the link is correct, send to finish page
        return render_template('finish.html')

    #if not, give a 403 forbidden (need to let them try again (use _blank for now))
    else:
        return abort(403)
