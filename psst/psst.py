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
@click.option('-l', '--secrets-list', 
              default="base",
              show_default=True,
              help="The secrets list to generate [base,pcm,oci]")
def generate(type, name, compartment_id, region, secrets_list):
    """Generate a vault with generated secrets."""
    if type == "oci":
        ocicfg = psst.vault.oci.config(region)

        dict = {}
        secrets = []

        list_module = eval("psst.secrets." + secrets_list )
        for module in getmembers(list_module, ismodule):
            secrets.append(module[0])

        for s in secrets:
            dict[s] = eval("psst.secrets." + secrets_list + "." + s + ".generate()")

        vault = psst.vault.oci.create(ocicfg, name, compartment_id, dict)
