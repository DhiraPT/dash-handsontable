"""The code below is an example of how to use the HotTable component in a Dash app."""

import dash
from dash import html
from dash.dependencies import Input, Output, State
from dash_handsontable import HotTable


app = dash.Dash(__name__)
app.title = 'Dash Handsontable'

app.layout = html.Div([
    HotTable(
        id='table',
        data=[
            ['', 'Tesla', 'Volvo', 'Toyota', 'Ford'],
            ['2019', 10, 11, 12, 13],
            ['2020', 20, 11, 14, 13],
            ['2021', 30, 15, 12, 13]
        ],
        rowHeaders=True,
        colHeaders=True,
        height='auto',
        autoWrapRow=True,
        autoWrapCol=True,
        contextMenu=True,
        outsideClickDeselects=False,
        licenseKey='non-commercial-and-evaluation'
    ),
    html.Button("Export to CSV", id="export-btn"),
    html.Button("Get Selected Cells", id="get-selected-cells-btn"),
    html.Div(id='selected-cells-output'),
    html.Button("Get Current Data", id="get-current-data-btn"),
    html.Div(id='current-data-output'),
    html.Button("Get Current Data At Row", id="get-current-data-at-row-btn"),
    html.Div(id='current-data-at-row-output')
])


@app.callback(
    Output('table', 'exportData'),
    Output('table', 'exportDataParams'),
    Input('export-btn', 'n_clicks')
)
def export_data(n_clicks):
    if n_clicks:
        return True, {"filename": "export.csv"}
    return dash.no_update


@app.callback(
    Output('selected-cells-output', 'children'),
    Input('get-selected-cells-btn', 'n_clicks'),
    State('table', 'selectedCells')
)
def get_selected_cells(n_clicks, selected_cells):
    if n_clicks:
        return str(selected_cells)
    return dash.no_update


@app.callback(
    Output('table', 'getData'),
    Input('get-current-data-btn', 'n_clicks'),
    State('table', 'selectedCells'),
    prevent_initial_call=True
)
def get_current_data(n_clicks, selected_cells):
    if n_clicks and selected_cells:
        return {'row': selected_cells[-1][2], 'col': selected_cells[-1][3], 'row2': selected_cells[-1][0], 'col2': selected_cells[-1][1]}
    return dash.no_update

@app.callback(
    Output('current-data-output', 'children'),
    Input('table', 'currentData'),
    prevent_initial_call=True
)
def display_current_data(current_data):
    return str(current_data)


@app.callback(
    Output('table', 'getDataAtRow'),
    Input('get-current-data-at-row-btn', 'n_clicks'),
    State('table', 'selectedCells'),
    prevent_initial_call=True
)
def get_current_data_at_row(n_clicks, selected_cells):
    if n_clicks and selected_cells:
        return {'row': selected_cells[-1][0]}
    return dash.no_update

@app.callback(
    Output('current-data-at-row-output', 'children'),
    Input('table', 'currentDataAtRow'),
    prevent_initial_call=True
)
def display_current_data_at_row(current_data_at_row):
    return str(current_data_at_row)


if __name__ == '__main__':
    app.run_server(debug=True)
