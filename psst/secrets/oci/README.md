# OCI Image

If you are building an OCI Marketplace PeopleSoft Image, you need to provide a JSON-formatted string to set the passwords. Use `-oci` (or `--oci-image`) and `psst` will output a JSON formatted string you can paste directly into User Data.

> 🟥 [Oracle's instructions](https://docs.oracle.com/en/applications/peoplesoft/peoplesoft-common/tutorial-deploy-demo-image/index.html#step_seven).

# Secrets List

- connect_pwd
- access_pwd
- admin_pwd
- weblogic_admin_pwd
- webprofile_user_pwd
- gw_user_pwd
- domain_conn_pwd
- opr_pwd

# Example

```
psst secrets generate --secrets-list oci
{
    "access_pwd": "OIC0nIBWjxiC7w4G1Ys5iDcJg",
    "admin_pwd": "otTr-ttUMQ5Niw3PPgAXPN7Jt71Pio",
    "connect_pwd": "j0QctR9nR8QICvP9znIeHnP0gcvzUX",
    "domain_conn_pwd": "Xs15redI6Jz9xDv3Sq6",
    "gw_user_pwd": "r5vaJeFd8SEwZpQBS7j6NukKpmf9Sd",
    "opr_pwd": "r29TniCn",
    "weblogic_admin_pwd": "44W^hqFV24$wWoU3KZ&tR6$TP9TJCv",
    "webprofile_user_pwd": "99DOzSoODmvpBi0qp83KShQGwWVdp1"
}
```