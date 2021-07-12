import MetaTrader5 as mt5
### Conexão com a plataforma ###


def init(silent=False):
    # estabelece a conexão ao MetaTrader 5 ou termina execução
    if not mt5.initialize():
        print("Falha na inicialização, error code =", mt5.last_error())
        return(False)
        quit()
    elif silent == False:
        print("💪 Conectado com sucesso")
        author()
    return(True)


def author():
    # exibe dados sobre o pacote MetaTrader5
    print("MetaTrader5 package author: ", mt5.__author__)
    print("MetaTrader5 package version: ", mt5.__version__)


def getDealsHistory(dateFrom, dateTo, silent=False):
    # pega histórico de negocios entre as datas inicial e final
    # TODO: aceitar dateTo vazia = hoje
    deals = mt5.history_deals_get(dateFrom, dateTo)
    if deals == None:
        if silent == False:
            print("Nenhum negócio encontrado, código de erro: {}".format(
                mt5.last_error()))
        quit()
    elif len(deals) > 0:
        if silent == False:
            print("Negócios encontrados entre {} e {}: {}".format(
                dateFrom, dateTo, len(deals)))
    return deals


def getAllDealsHistory(silent=False):
    deals = mt5.history_deals_get()
    if deals == None:
        if silent == False:
            print("Nenhum negócio encontrado, código de erro: {}".format(
                mt5.last_error()))
        # quit()
    elif len(deals) > 0:
        if silent == False:
            print("Negócios encontrados entre {} e {}: {}".format(
                dateFrom, dateTo, len(deals)))
    return deals


def getRatesToFrom(symbol, dateFrom, dateTo, timeframe=mt5.TIMEFRAME_D1):
    return mt5.copy_rates_range(symbol, timeframe, dateFrom, dateTo)


def account(number=0):
    # mostrar número da conta ou comparar com numero da conta passado
    if number == 0:
        return mt5.account_info().login
    return (mt5.account_info().login == number)


def end():
    '''Fecha a conexão com terminal MetaTrader 5'''
    mt5.shutdown()


if __name__ == '__main__':
    init(False)
