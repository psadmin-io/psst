node default {
    $db_user = hiera('ocivault::db_user')
    #$env_name = hiera('env_name') # not in vault but in normal yaml data
    #$db_user_pwd = hiera('db_user_pwd')
    #$fail = hiera('fail')

    notify {"OCI Vault: db_user is $db_user":}
    #notify {"OCI Vault: db_user_pwd is $db_user_pwd":}
    #notify {"OCI Vault: env_name is $env_name":}
}