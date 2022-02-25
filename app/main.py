import os

from fastapi import FastAPI

app = FastAPI()
from UnleashClient import UnleashClient

store_id = os.environ.get("STORE_ID")
environment = os.environ.get("ENV")

client = UnleashClient(
    url="https://us.app.unleash-hosted.com/usbb1001/api/",
    app_name="Default",
	environment=environment,
    custom_headers={'Authorization': os.environ.get("UNLEASH_TOKEN")},
	)

client.initialize_client()

@app.get("/")
def read_root():
    
    if client.is_enabled("exit-sms-feature", context={'storeId': store_id}):
        exit_sms_feature = "enabled"
    else: 
        exit_sms_feature = "disabled"


    if client.is_enabled("new-payment-system", context={'storeId': store_id}):
        payment_system = "new"
    else:
        payment_system = "old"

    if client.is_enabled("widget-generator", context={'storeId': store_id}):
        widget_generator = "enabled"
    else:
        widget_generator = "disabled"

    return {
        "env": environment,
        "store_id": store_id,
        "exit-sms-feature": exit_sms_feature,
        "payment-system": payment_system,
        "widget-generator": widget_generator
        }
