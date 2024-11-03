# PeopleSoft Cloud Manager

If you are creating a PeopleSoft Cloud Manager (PCM) stack, you will need to generate secrets in a Vault. Adding `--secrets-list pcm` will generate passwords that comply with the Cloud Manager password requirements.

> 🟥 [Oracle's instructions](https://docs.oracle.com/en/applications/peoplesoft/cloud-manager/index.html)

# Secrets List

- db_connect_pwd
- access_pwd
- db_admin_pwd
- pcm_admin_pwd
- integration_gateway_user_pwd
- weblogic_admin_user_pwd
- web_profile_user_pwd
- domain_connect_pwd

# Example

```
psst secrets generate --secrets-list pcm
{
    "access_pwd": "Z6TI5VRq",
    "db_admin_pwd": "gAaZH_evPJjZvNOsg-k5RJN-I2aP2U",
    "db_connect_pwd": "ssOwfc4t3gWTyym8S5qD4tcDUQWHjU",
    "domain_connect_pwd": "IVDtzbNtbW2CPi4W0zw",
    "integration_gateway_user_pwd": "MzAvdUoCtcyIrNZz5M9Iagu2FG6anu",
    "pcm_admin_pwd": "3wWBaRqqsMIO2IVRg-ty-UvKR4TPyh",
    "web_profile_user_pwd": "RCIAQtPFCDataYMVCddzQnJ5iGXyP2",
    "weblogic_admin_user_pwd": "pt#zTKXYIcubw3yWDu%h1IT84itVxv"
}
```