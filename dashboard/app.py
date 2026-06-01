from dash import Dash, html, dash_table
import pandas as pd

cves = pd.read_csv("data/cves.csv")

app = Dash(__name__)

app.layout = html.Div([

    html.H1("Threat Intelligence Dashboard"),

    html.H2(f"Total CVEs: {len(cves)}"),

    dash_table.DataTable(
        data=cves.head(20).to_dict("records"),
        page_size=10
    )

])

if __name__ == "__main__":
    app.run(debug=True)