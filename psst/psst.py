import json
import click
from inspect import getmembers, ismodule

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

@secrets.command("generate")
@click.option('-l', '--secrets-list', 
              default="base",
              show_default=True,
              help="The secrets list to generate [base,pcm,oci]")
@click.option('-n', '--name',
              help="Generate specific named secrets",
              multiple=True)
def generate(secrets_list, name):
    """Generate a dictionary of secrets"""

    dict = {}
    secrets = []

    if name:
        # If named secrets, use that list
        for n in name:
            secrets.append(n) if n in dir(psst.secrets) else print(n + " is not a vaild secret name, ignoring.")
    else:
        list_module = eval("psst.secrets." + secrets_list )
        for module in getmembers(list_module, ismodule):
            secrets.append(module[0])

    for s in secrets:
        dict[s] = eval("psst.secrets." + secrets_list + "." + s + ".generate()")
    click.echo(json.dumps(dict, indent=4))

@cli.group()
def vault():
    """Working with secrets in Vaults"""
    pass

@vault.command("generate")
@click.option('--type', default="oci",
              show_default=True,
              help="The type of vault to create")
@click.option('--name', required=True,
              help="")
@click.option('--compartment-id', required=True,
              help="Set the compartment for the vault, key and secrets")
@click.option('--region',
              help="Set the region, overriding the default cloud configuration value")
@click.option('-cm', '--cloud-manager',
              default=False,
              is_flag=True,
              help="Set Cloud Manager Mode for passwords and length requirements")
def generate(type, name, compartment_id, region, cloud_manager):
    """Generate a vault. Currently defaults a lot, including generated secrets..."""
    if type == "oci":
        # TODO this all needs error checking
        ocicfg = psst.vault.oci.config(region)
        # TODO - generate dict
        # TODO - rework this to work like `generate` with secrets-list
        dict = {}
        dict["db_user_pwd"] = psst.secrets.db_user_pwd.generate(cloud_manager)
        dict["access_pwd"] = psst.secrets.access_pwd.generate(cloud_manager)
        dict["es_admin_pwd"] = psst.secrets.es_admin_pwd.generate(cloud_manager)
        dict["es_proxy_pwd"] = psst.secrets.es_proxy_pwd.generate(cloud_manager)
        dict["wls_admin_user_pwd"] = psst.secrets.wls_admin_user_pwd.generate(cloud_manager)
        if cloud_manager:
            dict["db_admin_pwd"] = psst.secrets.db_admin_pwd.generate(cloud_manager)
        dict["db_connect_pwd"] = psst.secrets.db_connect_pwd.generate(cloud_manager)
        dict["pia_gateway_admin_pwd"] = psst.secrets.pia_gateway_admin_pwd.generate(cloud_manager)
        dict["pia_webprofile_user_pwd"] = psst.secrets.pia_webprofile_user_pwd.generate(cloud_manager)
        dict["domain_conn_pwd"] = psst.secrets.domain_conn_pwd.generate(cloud_manager)
        dict["pskey_password"] = psst.secrets.pskey_password.generate(cloud_manager)
        if cloud_manager:
            dict["windows_password"] = psst.secrets.windows_password.generate(cloud_manager)
              
        vault = psst.vault.oci.create(ocicfg, name, compartment_id, dict)
