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