from flask import Flask,render_template

appilcationinstance=Flask(__name__)

@appilcationinstance.route('/s')
def sfile():
    return render_template('h1.html')

@appilcationinstance.route('/f')
def food():
    return render_template('h2.html')


if __name__=='__main__':
    appilcationinstance.run(debug=True)