import oci
import time
import base64

def config():
    config = oci.config.from_file()
    #config["region"] = "" # TODO - set region?

    return config

def create(ocicfg, name, compartment_id, secrets_dict):
    vault = create_vault(ocicfg, name, compartment_id)
    key = create_key(ocicfg, "masterkey", vault.management_endpoint, compartment_id)
    
    for name, content in secrets_dict.items():
        create_secret(ocicfg, vault.id, key.id, compartment_id, name, content, name)

def create_vault(ocicfg, name, compartment_id):
    print("Creating Vault")
    key_management_client = oci.key_management.KmsVaultClient(ocicfg)

    create_vault_response = key_management_client.create_vault(
        create_vault_details=oci.key_management.models.CreateVaultDetails(
            compartment_id=compartment_id,
            display_name=name,
            vault_type="DEFAULT"),
            # TODO - tags?
            # defined_tags={
            #     'EXAMPLE_KEY_Ae1wB': {
            #         'EXAMPLE_KEY_DgAol': 'EXAMPLE--Value'}},
            # freeform_tags={
            #     'EXAMPLE_KEY_SsQ9R': 'EXAMPLE_VALUE_FmkBdwTrzZiqPtjzqoXC'}
        )

    for attempt in range(20):
        print("Checking Vault status ({}): ".format(attempt), end='')
        vault = key_management_client.get_vault(vault_id=create_vault_response.data.id)
        print(vault.data.lifecycle_state)

        if vault.data.lifecycle_state == "ACTIVE":
            break
        else:
            time.sleep(15)

    if vault.data.lifecycle_state != "ACTIVE":
        raise SystemExit("ERROR: There was an issue creating the vault. [{}]".format(vault.data.lifecycle_state))

    return vault.data

def create_key(ocicfg, name, vault_mgmt, compartment_id):
    print("Creating Key")

    key_management_client = oci.key_management.KmsManagementClient(ocicfg, vault_mgmt)

    create_key_response = key_management_client.create_key(
        create_key_details=oci.key_management.models.CreateKeyDetails(
            compartment_id=compartment_id,
            display_name=name,
            key_shape=oci.key_management.models.KeyShape(
                algorithm="AES",
                length=32,
                curve_id="NIST_P384"),
            # defined_tags={
            #     'EXAMPLE_KEY_2F9ex': {
            #         'EXAMPLE_KEY_NSxF4': 'EXAMPLE--Value'}},
            # freeform_tags={
            #     'EXAMPLE_KEY_qmyfO': 'EXAMPLE_VALUE_mj8CwDqoxWLDA4qUDqZu'},
            protection_mode="SOFTWARE")
        )

    for attempt in range(10):
        print("Checking Key status ({}): ".format(attempt), end='')
        key = key_management_client.get_key(key_id=create_key_response.data.id)
        print(key.data.lifecycle_state)

        if key.data.lifecycle_state == "ENABLED":
            break
        else:
            time.sleep(10)

    if key.data.lifecycle_state != "ENABLED":
        raise SystemExit("ERROR: There was an issue creating the key. [{}]".format(key.data.lifecycle_state))

    return key.data

def create_secret(ocicfg, vault_id, key_id, compartment_id, secret_name, secret_content, secret_descr):
    vault_client = oci.vault.VaultsClient(ocicfg)
    create_secret_response = vault_client.create_secret(
        create_secret_details=oci.vault.models.CreateSecretDetails(
            compartment_id=compartment_id,
            secret_content=oci.vault.models.Base64SecretContentDetails(
                content_type="BASE64",
                name=secret_name,
                stage="CURRENT",
                content=base64.b64encode(secret_content.encode('ascii')).decode('ascii') # str > bytes > base64 > str
            ),
            secret_name=secret_name,
            vault_id=vault_id,
            key_id=key_id,
            description=secret_descr
            # defined_tags={
            #     'EXAMPLE_KEY_L44xi': {
            #             'EXAMPLE_KEY_5XG0E': 'EXAMPLE--Value'}},
            # freeform_tags={
            #     'EXAMPLE_KEY_Z8F1a': 'EXAMPLE_VALUE_3RMNoPISLXn1pYITgfle'},
            
            # metadata={
            #     'EXAMPLE_KEY_XXKFm': 'EXAMPLE--Value'},
        )
    )

    return create_secret_response.data
