from flask import Flask, app,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

appilcationinstance=Flask(__name__)
appilcationinstance.config['SECRET_KEY']='csrftoken '
@appilcationinstance.route('/s')
def sfile():
    return render_template('h1.html')

@appilcationinstance.route('/f')
def food():
    return render_template('h2.html')

@appilcationinstance.route('/html_form',methods=['GET',"POST"])
def html_form():
    if request.method=='POST':
        form_data=request.form
        return form_data['name']
    return render_template('html_form.html')

class NameForm(Form):
    name=StringField(validators=[Required()])
    submit=SubmitField()

@appilcationinstance.route('/webform',methods=['GET','POST'])
def webform():
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data
        return name
    return render_template('webform.html',form=form)
if __name__=='__main__':
    appilcationinstance.run(debug=True)