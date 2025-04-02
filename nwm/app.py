from dash import Dash, html, dcc


app = Dash(__name__)

app.layout = html.Div([
    html.H1("Monitor de Tráfego de Rede"),
    dcc.Graph(id="grafico-trafego"),
    dcc.Interval(id="intervalo-atualizacao", interval=2000) #Atualiza a cada 2s
])

if __name__ == "__main__":
    app.run()