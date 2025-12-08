import yaml
import subprocess
from time import sleep
import json

def unsafe_constructor(loader, node):
    # Simply return the underlying data structure without the tag
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    elif isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    else:
        return loader.construct_scalar(node)

yaml.add_constructor('!unsafe', unsafe_constructor, Loader=yaml.SafeLoader)

print("Hello from pre-run script", flush=True)

try:
    with open("/runner/env/extravars", "r") as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
        var_value = data.get("var")
        if var_value is not None:
            print(f"var value: {var_value}", flush=True)
        else:
            print("'var' key not found in data", flush=True)
            
except FileNotFoundError:
    print("Error: /runner/env/extravars file not found", flush=True)
except yaml.YAMLError as e:
    print(f"Error parsing YAML: {e}", flush=True)
except Exception as e:
    print(f"Unexpected error: {e}", flush=True)

print("Doing some checks...", flush=True)

if var_value != "admin":
    raise Exception("var value is not admin")
    sys.exit(1)