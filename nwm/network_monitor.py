import psutil

def get_network_traffic():
    #CAPTURA E RETORNA OS BYTES ENVIADOS E RECEBIDOS

    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv