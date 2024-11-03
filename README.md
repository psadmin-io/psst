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
```bash
# Generate All Secrets
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

# Generate Specific Secrets
$ psst secrets generate --name db_user_pwd --name access_pwd
{
    "db_user_pwd": "WTM7Dx3ha9wpQbu1A60q7rhTP",
    "access_pwd": "GuA2TyH0Hh62ZXvh9QeSC2dux"
}

# Generate for Variable Usage
$ secret_name=db_user_pwd
$ secret_vaule=$(psst secrets generate --name $secret_name | jq -r .$secret_name)
$ echo $secret_vaule
bRwoom0IoB0Fpuf2bsNZgOVfF
```

### Secrets List
When using `secrets generate` you can specify a secret list using `--secrets-list`, otherwise `base` is the default. Each type of list contains a set of secrets to generate for different use cases. The lists contain both the secret names, as well as the validation rules.

Review each list's README for more details.

- [base](./secrets/base)
- [oci](./secrets/oci)
- [pcm](./secrets/pcm)

Usage:

```bash
$ psst secrets generate --secrets-list oci
{
    "access_pwd": "sN1mV7QhBDkfcncrYBR3cGknC",
    "db_admin_pwd": "e0tSbOXKRZ3Q-Zhfv0y#BOncOImmRf",
    "db_user_pwd": "IkrcBdW1YfTfMrbbxZCrWeet4",
    "domain_conn_pwd": "tzcx9XRy9Nu0z6uyozO",
    "pia_gateway_admin_pwd": "xVztVe63wGhHDkIEs8zsOYzpyjQFf6",
    "pia_webprofile_user_pwd": "vbwOrkaw0vbosx9M7sHMHy9qVHZndX",
    "wls_admin_user_pwd": "Eh#&!o6K924iWKmPKynMrZjwKXUfTV"
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
