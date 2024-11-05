# Tests

This is a list of manual tests. In the future, look at automated testing.

## psst

- [ ] `psst`

```
# Help menu
psst
psst --help
```

## secrets

- [ ] `psst secrets`

```
# Help menu
psst secrets
psst secrets --help
```

- [ ] `psst secrets generate`

```
# Help menu
psst secrets generate --help
```

- [ ] `psst secrets generate --secrets-list`
```
# Generate for each secrets list
psst secrets generate --secrets-list base
psst secrets generate --secrets-list oci
psst secrets generate --secrets-list pcm
```

- [ ] `psst secrets generate --secret-name`
```
# Generate for specific secrets
psst secrets generate --secret-name access_pwd
psst secrets generate --secret-name access_pwd --secret-name db_admin_pwd

# Generate for invalid secret name [FAIL]
psst secrets generate --secret-name INVALID_pwd
psst secrets generate --secret-name access_pwd --secret-name INVALID_pwd
```

- [ ] `psst secrets generate --prefix`
```
# Generate using a prefix
psst secrets generate --prefix PRE_

# Generate a specific secret and use a prefix
psst secrets generate --prefix PRE_ --secret-name access_pwd

# Generate using a prefix for each secrets list
psst secrets generate --prefix PRE_ --secrets-list base
psst secrets generate --prefix PRE_ --secrets-list oci
psst secrets generate --prefix PRE_ --secrets-list pcm
```

- [ ] `psst secrets generate --suffix`
```
# Generate using a suffix
psst secrets generate --suffix _SUF

# Generate a specific secret and use a suffix
psst secrets generate --suffix _SUF --secret-name access_pwd

# Generate using a suffix for each secrets list
psst secrets generate --suffix _SUF --secrets-list base
psst secrets generate --suffix _SUF --secrets-list oci
psst secrets generate --suffix _SUF --secrets-list pcm
```

- [ ] `psst secrets generate --prefix --suffix`
```
# Generate using a prefix and suffix
psst secrets generate --prefix PRE_ --suffix _SUF

# Generate a specific secret and use a prefix and suffix
psst secrets generate --prefix PRE_ --suffix _SUF --secret-name access_pwd

# Generate using a prefix and suffix for each secrets list
psst secrets generate --prefix PRE_ --suffix _SUF --secrets-list base
psst secrets generate --prefix PRE_ --suffix _SUF --secrets-list oci
psst secrets generate --prefix PRE_ --suffix _SUF --secrets-list pcm
```

## vault

- [ ] `psst vault create`

```
# Create a vault with full list
type="oci"
vault_name="TODO"
comp_id="TODO"
region="TODO"
prefix=""
suffix=""

psst vault create \
    --type $type \
    --vault-name $vault_name \
    --compartment-id $comp_id \    
    --region $region \
    --secrets-list $secrets_list \
    --prefix $prefix \
    --suffix $suffix

# Create a vault with a specific secret
type="oci"
vault_name="TODO"
comp_id="TODO"
region="TODO"
secrets_list="base"
secret_name="access_pwd"
prefix=""
suffix=""

psst vault create \
    --type $type \
    --vault-name $vault_name \
    --compartment-id $comp_id \    
    --region $region \
    --secrets-list $secrets_list \    
    --secret-name $secret_name \
    --prefix $prefix \
    --suffix $suffix
```


- [ ] `psst vault update`

```
# Update a vault with full list
type="oci"
vault_id="TODO"
key_id="TODO"
comp_id="TODO"
region="TODO"
prefix=""
suffix=""

psst vault update \
    --type $type \
    --vault $vault_id \
    --key $key_id \
    --compartment-id $comp_id \    
    --region $region \
    --secrets-list $secrets_list \
    --prefix $prefix \
    --suffix $suffix

# Update a vault with a specific secret
type="oci"
vault_id="TODO"
key_id="TODO"
comp_id="TODO"
region="TODO"
secrets_list="base"
secret_name="access_pwd"
prefix=""
suffix=""

psst vault update \
    --type $type \
    --vault $vault_id \
    --key $key_id \
    --compartment-id $comp_id \    
    --region $region \
    --secrets-list $secrets_list \    
    --secret-name $secret_name \
    --prefix $prefix \
    --suffix $suffix
```