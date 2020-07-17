from flask import render_template, request, flash, redirect, url_for
from sharesscraper import app
from sharesscraper.data import my_table_data, detailed_data

@app.route('/', methods=['GET', 'POST'])
def home_view():
    if request.method == "POST":
        if request.form.get('searchObject') == '':
            flash("Please enter a name into the search bar to search for the person", "warning")
            return render_template('home.html', table_data=my_table_data, number=len(my_table_data))
        return redirect(url_for('search_for_view', searchFor=request.form.get('searchObject')))

    return render_template('home.html', table_data=my_table_data, number=len(my_table_data))

@app.route('/<pk>/detail/')
def detail_view(pk):
    data, chart_data = detailed_data(my_table_data[int(pk) - 1][3], my_table_data[int(pk) - 1])
    return render_template('detail.html', data=data, net_worth=chart_data["netWorthHistoryData"]
                           , bought_shares=chart_data["boughtSharesInData"]
                           , sold_shares=chart_data["soldSharesIn"])

@app.route('/query:<searchFor>/')
def search_for_view(searchFor):
    print(searchFor)
    search_object = [searchFor.title(), searchFor]
    edited_table = []
    for foo in range(0, len(my_table_data)):
        if search_object[0] in my_table_data[foo][0] or search_object[1] in my_table_data[foo][0]:
            edited_table.append(my_table_data[foo])
    if len(edited_table) == 0:
        flash("Sorry we could't find anyone with the name " + search_object[1] + ".", "error")
        return render_template('home.html', table_data=edited_table, number=len(edited_table))
    return render_template('home.html', table_data=edited_table, number=len(edited_table))

