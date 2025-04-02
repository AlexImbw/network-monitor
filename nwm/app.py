from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from network_monitor import get_network_traffic

#INSTANCIAMENTO DO APP DASH
app = Dash(__name__)

#DEFINE O TITULO DA PAGINA
app.title="NWM"


#ÁREA DE CONFIGURAÇÃO DO FRONT-END
app.layout = html.Div([
    html.H1("Monitor de Tráfego de Rede"),
    #GRAFICO PAUSADO
    #dcc.Graph(id="grafico-trafego"),

    #TESTE DE FUNCIONAMENTO DA COLETA DE PACOTES
    html.Div([
        html.P("Bytes Enviados"),
        html.Div(id="bytes-enviados")
    ]),
    html.Div([
        html.P("Bytes Recebidos:"),
        html.Div(id="bytes-recebidos"),
    ]),

    dcc.Interval(id="intervalo-atualizacao", interval=2000) #Atualiza a cada 2s
])

#CONFIGURAÇÃO DA CAPTURA DE TRAFEGO

@app.callback(
    [Output("bytes-enviados", "children"),
     Output("bytes-recebidos", "children")],
     [Input("intervalo-atualizacao", "n_intervals")]

)

def update_network_traffic(n_intervals):
    bytes_sent, bytes_recv = get_network_traffic()
    return f"{bytes_sent} bytes", f"{bytes_recv} bytes"

#FAZ O SERVIDOR RODAR NO NAVEGADOR
if __name__ == "__main__":
    app.run()