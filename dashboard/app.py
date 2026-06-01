from dash import Dash, html
import pandas as pd

app = Dash(__name__)

cves = pd.read_csv("data/cves.csv")
ips = pd.read_csv("data/malicious_ips.csv")
iocs = pd.read_csv("data/iocs.csv")
ransomware = pd.read_csv("data/ransomware.csv")

app.layout = html.Div([

    html.H1("Threat Intelligence Dashboard"),

    html.Hr(),

    html.H2(f"Total CVEs: {len(cves)}"),

    html.H2(f"Malicious IPs: {len(ips)}"),

    html.H2(f"IOC Pulses: {len(iocs)}"),

    html.H2(f"Ransomware Records: {len(ransomware)}")

])

if __name__ == "__main__":
    app.run(debug=True)