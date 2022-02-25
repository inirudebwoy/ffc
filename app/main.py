import os

import ldclient
from fastapi import FastAPI
from ldclient.config import Config

app = FastAPI()

store_id = os.environ.get("STORE_ID")
environment = os.environ.get("ENV")
sdk_key = os.environ.get("SDK_KEY")
ldclient.set_config(Config(sdk_key))
client = ldclient.get()

@app.get("/")
def read_root():
    
    # anonymous user
    if client.variation("exit-sms-feature", {"key": "aa0ceb", "custom": {"store_id": store_id}}, False):
        exit_sms_feature = "enabled"
    else: 
        exit_sms_feature = "disabled"

    # known user
    if client.variation("new-payment-system", {"key": "123", "custom": {"store_id": store_id}}, False):
        payment_system = "new"
    else:
        payment_system = "old"

    # known user
    if client.variation("widget-generator", {"key": "456", "custom": {"store_id": store_id}}, False):
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
