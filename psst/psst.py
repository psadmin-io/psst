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
@click.option('-cm', '--cloud-manager', 
              default=False, 
              help="Set Cloud Manager Mode for passwords and length requirements", 
              is_flag=True)
@click.option('-oci', '--oci-image', 
              default=False, 
              help="Create JSON for OCI-based PeopleSoft Images", 
              is_flag=True)
@click.option('-n', '--name',
              help="Generate specific named secrets",
              multiple=True)
def generate(cloud_manager, oci_image, name):
    """Generate a dictionary of secrets"""

    dict = {}
    secrets = []    
    
    if name:
        # If named secrets, use that list
        for n in name:
            secrets.append(n) if n in dir(psst.secrets) else print(n + " is not a vaild secret name, ignoring.")
    else:
        if oci_image:
            # TODO is this all we need or do we need defaults PLUS these?
            secrets.append("connect_pwd")
            secrets.append("access_pwd")
            secrets.append("admin_pwd")
            secrets.append("weblogic_admin_pwd")
            secrets.append("webprofile_user_pwd")
            secrets.append("gw_user_pwd")
            secrets.append("domain_conn_pwd")
            secrets.append("opr_pwd")
            secrets.append("db_admin_pwd")
        else:   
            # Else use all secrets
            secrets.append("db_user_pwd")
            secrets.append("access_pwd")
            secrets.append("es_admin_pwd")
            secrets.append("es_proxy_pwd")
            secrets.append("wls_admin_user_pwd")
            secrets.append("db_connect_pwd")
            secrets.append("pia_gateway_admin_pwd")
            secrets.append("pia_webprofile_user_pwd")
            secrets.append("domain_conn_pwd")
            secrets.append("pskey_password")
            if cloud_manager:
                secrets.append("db_admin_pwd")
                secrets.append("windows_password")

    for s in secrets:
        dict[s] = eval("psst.secrets." + s + ".generate(cloud_manager)")
    click.echo(json.dumps(dict, indent=4))

@cli.group()
def vault():
    """Working with secrets in Vaults"""
    pass

@vault.command("generate")
@click.option('--type', default="oci", show_default=True)
@click.option('--name', required=True)
@click.option('--compartment-id', required=True)
@click.option('-cm', '--cloud-manager', 
              default=False, 
              help="Set Cloud Manager Mode for passwords and length requirements", 
              is_flag=True)
def generate(type, name, compartment_id, cloud_manager):
    """Generate a vault. Currently defaults a lot, including generated secrets..."""
    if type == "oci":
        # TODO this all needs error checking
        ocicfg = psst.vault.oci.config()
        # TODO - generate dict
        dict = {}
        dict["db_user_pwd"] = psst.secrets.db_user_pwd.generate(cloud_manager)
        dict["access_pwd"] = psst.secrets.access_pwd.generate(cloud_manager)
        dict["es_admin_pwd"] = psst.secrets.es_admin_pwd.generate()
        dict["es_proxy_pwd"] = psst.secrets.es_proxy_pwd.generate()
        dict["wls_admin_user_pwd"] = psst.secrets.wls_admin_user_pwd.generate()
        if cloud_manager:
            dict["db_admin_pwd"] = psst.secrets.db_admin_pwd.generate()
        dict["db_connect_pwd"] = psst.secrets.db_connect_pwd.generate()()
        dict["pia_gateway_admin_pwd"] = psst.secrets.pia_gateway_admin_pwd.generate()
        dict["pia_webprofile_user_pwd"] = psst.secrets.pia_webprofile_user_pwd.generate()
        dict["domain_conn_pwd"] = psst.secrets.domain_conn_pwd.generate
        dict["pskey_password"] = psst.secrets.pskey_password.generate()
        if cloud_manager:
            dict["windows_password"] = psst.secrets.windows_pwd.generate()
              
        vault = psst.vault.oci.create(ocicfg, name, compartment_id, dict)
