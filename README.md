# psst
PeopleSoft Secrets Tool
```
$ psst --help
Usage: psst [OPTIONS] COMMAND [ARGS]...

  PeopleSoft Secrets Tool

Options:
  --help  Show this message and exit.

Commands:
  secrets  Working with PeopleSoft Environment secrets
```

# Usage
```
$ psst secrets generate
{
    "access_pwd": "WrKT6ap3",
    "db_connect_pwd": "IVkCZNjUOKhaQdv8eB8aOQZ6ZP0jp5",
    "db_user_pwd": "FPeX9qSu",
    "domain_conn_pwd": "FD57pUkA1FddEIpMgGe",
    "pia_gateway_admin_pwd": "nWJ04cGQygPiWnoknyPsPf4f1ajIUW",
    "pia_webprofile_user_pwd": "T64BvQ9K3iwfvesjs0na30UDFoIFG0",
    "pskey_password": "4Kt9nCgAGIDgR4wHTUqEZeh4z0hZEy",
    "wls_admin_user_pwd": "ispTFU7ami!oGME@n^ARtKTv6K@Tf&"
}
```

# Installing
```
cd psst
pip install .
```

# Setting up for development
```
pip install virtualenv 

cd psst
virtualenv venv
. venv/bin/activate

pip install --editable .
```
