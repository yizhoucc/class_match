from flask import render_template, flash, redirect, url_for
from app import app, dbconnector, db
from app.forms import SearchForm, InputForm
''''''
''''''

mydb=dbconnector.connect2db()
# cursor is created each operation


@app.route('/search', methods=['GET', 'POST'])
def search():
    # flash('search')
    form = SearchForm()
    if form.validate_on_submit():
        # do xx xhere to sql
        data=db.searchdb(form, mydb)
        flash('Only [Wechat ID] and [Last Name] BOTH match our records, you can get what you want:')
        for  i in (data):

                for index, j in enumerate(i):
                    if index>2:
                        if j !='':
                            flash(j)

    return render_template('search.html',  title='2 In', form=form)

@app.route('/input', methods=['GET', 'POST'])
def inputdata():
    # flash('input')
    form = InputForm()
    if form.validate_on_submit():
        # do xx xhere to sql
        data=db.insertion(form, mydb)
        flash('SUCCESS! We recorded following infomation:')
        for i in (data):
            if i !='':
                flash(i)


    return render_template('input.html',  title='3 In', form=form)

@app.route('/',methods=['GET', 'POST'])
def index():
        # flash('input')
    form = InputForm()
    if form.validate_on_submit():
        # do xx xhere to sql
        data=db.insertion(form, mydb)
        flash('SUCCESS! We recorded following infomation:')
        for i in (data):
            if i !='':
                flash(i)


    return render_template('input.html',  title='3 In', form=form)