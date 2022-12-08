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
## secrets
```
$ psst secrets generate
{
    "db_user_pwd": "WTM7Dx3ha9wpQbu1A60q7rhTP",
    "access_pwd": "GuA2TyH0Hh62ZXvh9QeSC2dux",
    "es_admin_pwd": "hEQ5dq7KfxcuSOqUBOazcp5ETvR3vs",
    "es_proxy_pwd": "R2DWro330JmqyYkuN2WEvhJ50tzZVX",
    "wls_admin_user_pwd": "v#%uNBJtA4D8$&yK#uzJ$RcqD!Vqiq",
    "db_connect_pwd": "ir92R3mNTv1vAPe1cEYxtG8jI3YV5t",
    "pia_gateway_admin_pwd": "EY8PkYawh4ZvB3O0VbHI3qqPZw3S5b",
    "pia_webprofile_user_pwd": "x2i07XuWeWyj43Jbe4REJpBmEJYpU3",
    "domain_conn_pwd": "WoVv1mWZ25cR93Mmc9m",
    "pskey_password": "JNnPyqu7KF7es8ahGC13Si2BQDtN07"
}
```

### Cloud Manager Mode

Adding the `-cm` flag (`--cloud-manager`) will generate passwords that comply with the Cloud Manager password requirements. It will also generate a Windows user password.

```
psst secrets generate -cm
{
    "db_user_pwd": "do7iBVFD",
    "access_pwd": "q6NtpH0w",
    "es_admin_pwd": "KAQfp7zj5GNZ8M1PyBx7dpzcFq7EwG",
    "es_proxy_pwd": "biS6eCOZNxkTDim7m5wpkEMu3JG3rd",
    "wls_admin_user_pwd": "!Kk!$2Qt$p7X$UIrAO52yq1^r93&Mr",
    "db_admin_pwd": "PVr7EJu5IxcdkU4k3U8a8_0eeVs1GN",
    "db_connect_pwd": "9SgPuuygwSh2i0t8BStvh4o7HN2kqR",
    "pia_gateway_admin_pwd": "FsIUb9ZmuQb9tOKXz0tZGov7F6bMyE",
    "pia_webprofile_user_pwd": "c6cMrNipgKBwEMrp6teVYeb026H3Rp",
    "domain_conn_pwd": "1tqEWEHfVnR4X5G01Nb",
    "pskey_password": "3ObFEV6YVhDesde1A7EJupazHwdqy4",
    "windows_password": "1I6vfbC0x--@M!UM>$&*XyM42!eo@Y"
}
```

### OCI Image Mode

If you are building an OCI Marketplace PeopleSoft Image, you need to provide a JSON-formatted string to set the passwords. Use `-oci` (or `--oci-image`) and `psst` will output a JSON formatted string you can paste directly into User Data.

```
psst secrets generate -oci
{
    "connect_pwd": "nwO6FBKZAuuwDvKPjuN5m1HwCd3frb",
    "access_pwd": "VWQMf7bix6wIO4JwIeVpNHmS0",
    "admin_pwd": "#pcC_Gx4DebI2G6sd02oB9#QsShrV1",
    "weblogic_admin_pwd": "MZf74I9sc78ZTeswrFfO5nWhtxng##",
    "webprofile_user_pwd": "orRI5YwRkKT2vvE8FfFwh8K6UJQsPG",
    "gw_user_pwd": "nn40ZII2iXR8eES2RUw9rpuar9EMuW",
    "domain_conn_pwd": "MkhvZpmGJQr9gai1JtR",
    "opr_pwd": "DUKDgasnZda8nVQ88ZG16djup"
}
```

## vault
```
$ c_id=ocid1.compartment.oc1....
$ psst vault generate --name myvault --compartment-id $c_id 
...
...
Vault created.
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
virtualenv -p python3 venv
. venv/bin/activate

pip install --editable .
```
