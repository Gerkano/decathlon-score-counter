from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from export_to_json import open_and_export
from utils import save_file
import log_settings

UPLOAD_FOLDER = 'static/files'

app = Flask(__name__)
app.config['SECRET_KEY'] = '5sfJAid482fdKhdfs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class UploadFileForm(FlaskForm):
    chosen_file = FileField('csv', validators=[
        FileRequired(),
        FileAllowed(['csv'], 'CSV only restricted!')
    ])
    submit = SubmitField("Upload contestant data")

@app.route('/', methods=["GET", "POST"])
def upload():
    form = UploadFileForm()
    if form.validate_on_submit():
        try:
            file = form.chosen_file.data
            save_file(file, UPLOAD_FOLDER)
            flash("File has been uploaded")
            open_and_export(file, UPLOAD_FOLDER)
            flash(". Data exported to JSON with calculated points and rank")
        except Exception as e:
            flash(f", but something went wrong. Data is either incorrect or corrupted")
            log_settings.critical_log(f"Exception occured: {e}")
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)