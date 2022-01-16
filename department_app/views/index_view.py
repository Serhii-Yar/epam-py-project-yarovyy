from flask import render_template
from flask_classy import route, FlaskView


class HomepageView(FlaskView):
    #: base url route for all homepage routes
    route_base = '/'

    @route('/', endpoint='homepage')
    def homepage(self):

        return render_template('index.html')
