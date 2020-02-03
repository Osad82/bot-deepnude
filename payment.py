from liqpay.liqpay import LiqPay

liqpay = LiqPay(public_key, private_key)
res = liqpay.api("request", {
"action"    : "invoice_bot",
"version"   : "3",
"amount"    : "1",
"currency"  : "USD",
"order_id"  : "order_id_1",
"phone"  : "380950000001"
})


print(res)
