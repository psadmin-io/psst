import psst.secrets
from inspect import getmembers, ismodule

def generate_secrets(name, secrets_list, prefix, suffix):

	dict = {}
	secrets = []

	if name:
		# If named secrets, use that list
		for n in name:
			secrets.append(n) if n in dir(psst.secrets) else print(n + " is not a valid secret name, ignoring.")
	else:
		list_module = eval("psst.secrets." + secrets_list )
		for module in getmembers(list_module, ismodule):
			secrets.append(module[0])

	for s in secrets:
		dict[prefix + s + suffix] = eval("psst.secrets." + secrets_list + "." + s + ".generate()")

	return dict