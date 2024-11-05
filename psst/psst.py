import json
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

@secrets.command("generate")
@click.option('-l', '--secrets-list', 
              default="base",
              show_default=True,
              help="The secrets list to generate [base,pcm,oci]")
@click.option('-sn', '--secret-name',
              help="Name of a specific secret to generate",
              multiple=True)
@click.option('-p','--prefix',
              default="",
              help="Add a prefix to the secret names")
@click.option('-s','--suffix',
              default="",
              help="Add a suffix to the secret names")
def generate(secrets_list, secret_names, prefix, suffix):
    """Generate a dictionary of secrets"""
    secrets_dict = psst.secrets.util.generate_secrets(secrets_list, secret_names, prefix, suffix)
    click.echo(json.dumps(secrets_dict, indent=4))

@cli.group()
def vault():
    """Working with secrets in Vaults"""
    pass

@vault.command("create")
@click.option('-t','--type', default="oci",
              show_default=True,
              help="The type of vault to create")
@click.option('-vn','--vault-name', required=True,
              help="The name of the vault")
@click.option('-c','--compartment-id', required=True,
              help="Set the compartment for the vault, key and secrets")
@click.option('-r','--region',
              help="Set the region, overriding the default cloud configuration value")
@click.option('-l', '--secrets-list', 
              default="base",
              show_default=True,
              help="The secrets list to generate [base,pcm,oci]")
@click.option('-sn', '--secret-name',
              help="Name of a specific secret to generate",
              multiple=True)
@click.option('-p','--prefix',
              default="",
              help="Add a prefix to the secret names")
@click.option('-s','--suffix',
              default="",
              help="Add a suffix to the secret names")
def create(type, vault_name, compartment_id, region, secrets_list, secret_names, prefix, suffix):
    """Create a vault with generated secrets."""
    if type == "oci":
        ocicfg = psst.vault.oci.config(region)
        secrets_dict = psst.secrets.util.generate_secrets(secrets_list, secret_names, prefix, suffix)
        vault = psst.vault.oci.create(ocicfg, vault_name, compartment_id, secrets_dict)

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
@click.option('-sn', '--secret-name',
              help="Name of a specific secret to generate",
              multiple=True)
@click.option('-p','--prefix',
              default="",
              help="Add a prefix to the secret names")
@click.option('-s','--suffix',
              default="",
              help="Add a suffix to the secret names")
def update(type, vault, key, compartment_id, region, secrets_list, secret_names, prefix, suffix):
    """Update a vault with generated secrets."""

    if type == "oci":
        ocicfg = psst.vault.oci.config(region)  # set region local here vs passing to function?        
        secrets_dict = psst.secrets.util.generate_secrets(secrets_list, secret_names, prefix, suffix)
        vault = psst.vault.oci.update(ocicfg, vault, key, compartment_id, secrets_dict)