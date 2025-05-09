#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util

    # Define the path and module name
    module_name = "hidden_4"
    module_path = "/tmp/hidden_4.pyc"

    # Load the compiled module
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    hidden_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_module)

    # Get names defined in the module and filter them
    names = dir(hidden_module)
    for name in sorted(name for name in names if not name.startswith("__")):
        print(name)


# this file should be inside the /tmp directory