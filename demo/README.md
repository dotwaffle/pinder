# Pinder demo

## Start the lab

    # create a python virtualenv if necessary
    cd demo
    pip install -r requirements.txt
    vagrant up
    cd ansible
    inv prepare

## Deploy rtr00

    inv deploy_rtr00

## Deploy rtr01

    inv deploy_rtr01

## Verify everything is configured and up

    inv verify
