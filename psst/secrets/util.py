import psst.secrets
from inspect import getmembers, ismodule

def generate_secrets(secrets_list, secret_name, prefix, suffix):

	dict = {}
	secrets = []

	if secret_name:
		for n in secret_name:
			if n in dir(eval("psst.secrets." + secrets_list)):
				secrets.append(n) 
			else:
				raise ValueError(f"Secret name '{n}' is not a valid name in the '{secrets_list}' list.")
	else:
		list_module = eval("psst.secrets." + secrets_list )
		for module in getmembers(list_module, ismodule):
			secrets.append(module[0])

	for s in secrets:
		dict[prefix + s + suffix] = eval("psst.secrets." + secrets_list + "." + s + ".generate()")

	return dict