import psst.vault

def generate_dms(vault_list, prefix):
    lines = []
    # TODO - trim prefix
    for secret in vault_list:
        new_line = f"update PSOPRDEFN set PTOPERPSWDV2 = '{secret['content']}', ENCRYPTED = 0 where OPRID = '{secret['name']}';"
        lines.append(new_line)
        new_line = f"encrypt_password '{secret['name']}';"
        lines.append(new_line)

    dms_text = '\n'.join(lines)

    return dms_text
