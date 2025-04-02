from yoomoney import Client

access_token = "4100119079609641.753F9FAF302F212692018D3E6A0328788B6AC4DB75E9AA7B8E449D451CA14FF2FD27757FE65CD601385BA266034F0A354FFAB6A883C70E22D9BFEDE95B60025E8FCE12352230E947593B4AB05481273DF80F4AB9277CCF6D4EB0545C915E7390F81FA2BC0B5EA40961700618B36CF88DF71F5F5F376190CF88B520D9B3536488"

def check():
    client = Client(access_token)
    balance = client.account_info().balance
    print("Баланс:", balance)
    # history = client.operation_history(records=3)
    # print(history)
    # for operation in history.operations:
    #     if operation.status == "success":
    #         print(operation.label)
    #         print(operation.amount)

check()