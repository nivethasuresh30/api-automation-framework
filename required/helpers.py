import json
import os
import jsonschema


def load_test_data(folder, filename):
    # __file__ is the current script's path
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'inputs', folder))
    file_path = os.path.join(base_path, filename)

    with open(file_path, 'r') as f:
        return json.load(f)


# import json
# import os
# import jsonschema

# def load_test_data(folder, filename):
#     base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'inputs', folder))
#     file_path = os.path.join(base_path, filename)
#     with open(file_path, 'r') as f:
#         return json.load(f)

def load_schema(filename):
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'response'))
    file_path = os.path.join(base_path, filename)
    with open(file_path, 'r') as f:
        return json.load(f)

def validate_schema(response_body, schema_filename):
    schema = load_schema(schema_filename)
    try:
        jsonschema.validate(instance=response_body, schema=schema)
        return True
    except jsonschema.ValidationError as e:
        # Raising an AssertionError makes it play nicely with pytest
        raise AssertionError(f"Schema validation failed: {e.message}")