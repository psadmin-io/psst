import json
from typing_extensions import Required
import click

import psst.secrets
import psst.vault

class Config(object):

    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group(no_args_is_help=True)
@pass_config
def cli(config):
    """PeopleSoft Secrets Tool"""
    pass    

@cli.group()
def secrets():
    """Working with secrets"""
    pass

@secrets.command()
def generate():
    """Generate a dictionary of secrets"""
    dict = {}

    dict["access_pwd"] = psst.secrets.access_pwd.generate()
    dict["db_connect_pwd"] = psst.secrets.db_connect_pwd.generate()
    dict["db_user_pwd"] = psst.secrets.db_user_pwd.generate()
    dict["domain_conn_pwd"] = psst.secrets.domain_conn_pwd.generate()
    dict["pia_gateway_admin_pwd"] = psst.secrets.pia_gateway_admin_pwd.generate()
    dict["pia_webprofile_user_pwd"] = psst.secrets.pia_webprofile_user_pwd.generate()
    dict["pskey_password"] = psst.secrets.pskey_password.generate()
    dict["wls_admin_user_pwd"] = psst.secrets.wls_admin_user_pwd.generate()

    click.echo(json.dumps(dict, indent=4))

@cli.group()
def vault():
    """Working with secrets in Vaults"""
    pass

@vault.command()
@click.option('--type', 'string', default="oci", show_default=True)
@click.option('--name','string',required=True)
@click.option('--compartment-id','string',required=True)
def generate(type, name, compartment_id):
    """Generate a vault"""
    if type == "oci":
        # TODO this all needs error checking
        ocicfg = psst.vault.oci.config()
        vault = psst.vault.oci.create(ocicfg, name, compartment_id)            
