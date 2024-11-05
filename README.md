# psst
PeopleSoft Secrets Tool
```
$ psst --help
Usage: psst [OPTIONS] COMMAND [ARGS]...

  PeopleSoft Secrets Tool

Options:
  --help  Show this message and exit.
  

Commands:
  secrets  Working with secrets for PeopleSoft
  vault    Working with secrets in Vaults
```

# Usage
## secrets
```bash
# Generate All Secrets
$ psst secrets generate
{
    "access_pwd": "zXZ0kpiXTn8rwkRzggKBzVAxR",
    "db_admin_pwd": "-u54SJov0fzgv44pmrizA_-rzhaKyn",
    "db_connect_pwd": "t4C0BNaNrW6SPWwrgMxWmi1ueqt1aI",
    "db_user_pwd": "FmabnvU06h9zCP4aYD3H9KTTK",
    "domain_conn_pwd": "qWnuRiGm0StaFXip72w",
    "es_admin_pwd": "ppf56GVbYdegTndz5MAamGV0aKwqro",
    "es_proxy_pwd": "SJzTRAwKVGeDSRfhM4QeYGVCQVIPZz",
    "pia_gateway_admin_pwd": "HIyPDK3gn96XOTchJv8Zdt5hiSje8K",
    "pia_webprofile_user_pwd": "w8BTTtNwfbkEBb8W8Xi6vX1icZz7OA",
    "pskey_password": "RKGPonFu2Oju8agoP8NA0wVrbKvund",
    "windows_password": "Pa-(.aQJIjm%|k0JBopN{TwZ2AC>pn",
    "wls_admin_user_pwd": "1K84nxQhByDE1fVciy%ZZ61Wdd&K#o"
}

# Generate Specific Secrets
$ psst secrets generate --secret-name db_user_pwd --secret-name access_pwd
{
    "db_user_pwd": "WTM7Dx3ha9wpQbu1A60q7rhTP",
    "access_pwd": "GuA2TyH0Hh62ZXvh9QeSC2dux"
}

# Generate for Variable Usage
$ secret_name=db_user_pwd
$ secret_value=$(psst secrets generate --secret-name $secret_name | jq -r .$secret_name)
$ echo $secret_value
bRwoom0IoB0Fpuf2bsNZgOVfF
```

### Secrets List
When using `secrets generate` you can specify a secret list using `--secrets-list`, otherwise `base` is the default. Each type of list contains a set of secrets to generate for different use cases. The lists contain both the secret names, as well as the validation rules.

Review each list's README for more details.

- [base](./psst/secrets/base)
- [oci](./psst/secrets/oci)
- [pcm](./psst/secrets/pcm)

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

### Prefix/Suffix
Secret names can have a prefix or suffix added to them.

```bash
$ psst secrets generate --prefix "PRE_" --suffix "_SUF"
{
    "PRE_access_pwd_SUF": "H1FF57w2AzqJduBo55t2zaBpJ",
    "PRE_db_admin_pwd_SUF": "KdOi#7DvT472OqOY7IQzoZ37IUjCF7",
    "PRE_db_connect_pwd_SUF": "paQizHZc3ePigm7kGD7bn6CRn8CE6W",
    "PRE_db_user_pwd_SUF": "kV2Bc0I5mobXupuAPe58ZsIOv",
    "PRE_domain_conn_pwd_SUF": "9KweV17DN7wc2DBABzo",
    "PRE_es_admin_pwd_SUF": "oYgISZqeHejo29Fj1RQNyYpVwm5bHk",
    "PRE_es_proxy_pwd_SUF": "QQaO2DVfSeIhWCcNMOkQO5fDS5HDWx",
    "PRE_pia_gateway_admin_pwd_SUF": "tZwjqMyVEBIYYrnvCzUE132WhRFjkH",
    "PRE_pia_webprofile_user_pwd_SUF": "54uSV7XoguPesv86gz8Xp4q7R3bsbm",
    "PRE_pskey_password_SUF": "nnwUHwj0DOJQaTC8Efy1wM0vxBeNig",
    "PRE_windows_password_SUF": "S.o8oP,@+%DC5G]FwhRE}6|2kjecSX",
    "PRE_wls_admin_user_pwd_SUF": "CruYP28X1V%pVXBD#b"
}
```

## vault

### Create
Creates a new vault and populates with new generated secrets.

```
vault_name=test-vault
region=us-ashburn-1
comp_id=ocid1.compartment.oc1....

psst vault create \
    --name $vault_name  \
    --type oci \
    --region $region \
    --compartment-id $comp_id
```

### Update
Updaets an existing vault with new generated secrets.

```
vault_id=test-vault
key_id=ocid1.key...
region=us-ashburn-1
comp_id=ocid1.compartment.oc1...

psst vault update \
    --vault $vault_id \ 
    --key $key_id \
    --type oci \
    --region $region \
    --compartment-id $comp_id
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
