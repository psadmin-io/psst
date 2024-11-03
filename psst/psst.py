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
@click.option('-p','--prefix',
              default="",
              help="Add a prefix to the secret names")
@click.option('-s','--suffix',
              default="",
              help="Add a suffix to the secret names")
def generate(secrets_list, name, prefix, suffix):
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
        dict[prefix + s + suffix] = eval("psst.secrets." + secrets_list + "." + s + ".generate()")

    click.echo(json.dumps(dict, indent=4))

@cli.group()
def vault():
    """Working with secrets in Vaults"""
    pass

@vault.command("create")
@click.option('-t','--type', default="oci",
              show_default=True,
              help="The type of vault to create")
@click.option('-n','--name', required=True,
              help="")
@click.option('-c','--compartment-id', required=True,
              help="Set the compartment for the vault, key and secrets")
@click.option('-r','--region',
              help="Set the region, overriding the default cloud configuration value")
@click.option('-l', '--secrets-list', 
              default="base",
              show_default=True,
              help="The secrets list to generate [base,pcm,oci]")
@click.option('-p','--prefix',
              default="",
              help="Add a prefix to the secret names")
@click.option('-s','--suffix',
              default="",
              help="Add a suffix to the secret names")
def create(type, name, compartment_id, region, secrets_list, prefix, suffix):
    """Create a vault with generated secrets."""
    if type == "oci":
        ocicfg = psst.vault.oci.config(region)

        dict = {}
        secrets = []

        list_module = eval("psst.secrets." + secrets_list )
        for module in getmembers(list_module, ismodule):
            secrets.append(module[0])

        for s in secrets:
            dict[prefix + s + suffix] = eval("psst.secrets." + secrets_list + "." + s + ".generate()")

        vault = psst.vault.oci.create(ocicfg, name, compartment_id, dict)

@vault.command("update")
@click.option('-t','--type',
              default="oci",
              show_default=True,
              help="The type of vault to create")
@click.option('-v','--vault', required=True,
              help="Vault ID (OCID for OCI, etc)")
@click.option('-k','--key', required=True,
              help="Key ID (OCID for OCI, etc)")
@click.option('-c','--compartment-id', required=True,
              help="Set the compartment for the vault, key and secrets")
@click.option('-r','--region',
              help="Set the region, overriding the default cloud configuration value")
@click.option('-l', '--secrets-list', 
              default="base",
              show_default=True,
              help="The secrets list to generate [base,pcm,oci]")
@click.option('-p','--prefix',
              default="",
              help="Add a prefix to the secret names")
@click.option('-s','--suffix',
              default="",
              help="Add a suffix to the secret names")
def update(type, vault, key, compartment_id, region, secrets_list, prefix, suffix):
    """Update a vault with generated secrets."""

    if type == "oci":
        ocicfg = psst.vault.oci.config(region)  # set region local here vs passing to function?        
        
        dict = {}
        secrets = []

        list_module = eval("psst.secrets." + secrets_list )
        for module in getmembers(list_module, ismodule):
            secrets.append(module[0])

        for s in secrets:
            dict[prefix + s + suffix] = eval("psst.secrets." + secrets_list + "." + s + ".generate()")

        vault = psst.vault.oci.update(ocicfg, vault, key, compartment_id, dict)