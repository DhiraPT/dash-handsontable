"""The code below is an example of how to use the HotTable component in a Dash app."""

import dash
from dash import html
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
        licenseKey='non-commercial-and-evaluation',
        afterGetColHeader='''function(col, TH) {
            if (col === -1) {
                TH.innerHTML = "<div class=\\"relative\\" role=\\"presentation\\"><span class=\\"colHeader cornerHeader\\" role=\\"presentation\\">Corner</span></div>";
            }
        }''',
        afterSelection='''function(row, col, row2, col2) {
            document.getElementById('selected-cells-output').innerText = `Selected Cells: [${row}, ${col}, ${row2}, ${col2}]`;
            const currentData = this.getData();
            document.getElementById('current-data-output').innerText = `Current Data: ${JSON.stringify(currentData)}`;
            const currentDataAtRow = this.getDataAtRow(row);
            document.getElementById('current-data-at-row-output').innerText = `Current Data at Row ${row}: ${JSON.stringify(currentDataAtRow)}`;

            // Change the color of cells at row
            const rows = this.countRows();
            const cols = this.countCols();
            for (let i = 0; i < rows; i++) {
                for (let j = 0; j < cols; j++) {
                    if (i === row) {
                        this.setCellMeta(i, j, 'className', 'highlighted');
                    } else {
                        this.setCellMeta(i, j, 'className', '');
                    }
                }
            }
            this.render();
        }''',
    ),
    html.Button("Export to CSV", id="export-btn"),
    html.Div(id='selected-cells-output'),
    html.Div(id='current-data-output'),
    html.Div(id='current-data-at-row-output')
])


if __name__ == '__main__':
    app.run_server(debug=True)
