import json
import click
import getpass
#import oci

import psst.secrets
import psst.ocivault

class Config(object):

    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group(no_args_is_help=True)
@click.option('--verbose', is_flag=True)
@pass_config
def cli(config, verbose):
    """PeopleSoft Secrets Tool"""
    config.verbose = verbose

@cli.group()
def secrets():
    """Working with PeopleSoft Environment secrets"""
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
