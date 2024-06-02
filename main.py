import sys

def test_pydantic_core():
    try:
        from pydantic_core import SchemaValidator, ValidationError
        v = SchemaValidator({
        'type': 'typed-dict',
        'fields': {
        'name': {'type': 'typed-dict-field', 'schema': {'type': 'str'}},
        'age': {'type': 'typed-dict-field', 'schema': {'type': 'int', 'ge': 18}},
        'is_developer': {'type': 'typed-dict-field', 'schema': {'type': 'default', 'schema': {'type': 'bool'}, 'default': True}}
        }})
        r1 = v.validate_python({'name': 'Samuel', 'age': 35})
        assert r1 == {'name': 'Samuel', 'age': 35, 'is_developer': True}
        print("pydantic-core: Success")
    except Exception as e:
        print(f"pydantic-core: Failed ({e})")

def test_cryptography():
    try:
        from cryptography.fernet import Fernet
        # Simple test to ensure encryption and decryption works
        key = Fernet.generate_key()
        cipher = Fernet(key)
        message = b"Test message"
        encrypted = cipher.encrypt(message)
        decrypted = cipher.decrypt(encrypted)
        assert message == decrypted
        print("cryptography: Success")
    except Exception as e:
        print(f"cryptography: Failed ({e})")

def test_pandas():
    try:
        import pandas as pd
        # Simple test to create a DataFrame and perform basic operations
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        assert df['col1'].sum() == 3
        print("pandas: Success")
    except Exception as e:
        print(f"pandas: Failed ({e})")

def test_numpy():
    try:
        import numpy as np
        # Simple test to create an array and perform basic operations
        arr = np.array([1, 2, 3])
        assert np.sum(arr) == 6
        print("numpy: Success")
    except Exception as e:
        print(f"numpy: Failed ({e})")

def test_uvloop():
    try:
        import uvloop
        uvloop.install()
        print("uvloop: Success")
    except Exception as e:
        print(f"uvloop: Failed ({e})")

def test_pillow():
    try:
        from PIL import Image, ImageDraw
        # Simple test to create an image and draw on it
        img = Image.new('RGB', (100, 100), color='red')
        draw = ImageDraw.Draw(img)
        draw.rectangle([(10, 10), (90, 90)], outline='black')
        print("Pillow: Success")
    except Exception as e:
        print(f"Pillow: Failed ({e})")

def main():
    test_pydantic_core()
    test_cryptography()
    test_pandas()
    test_numpy()
    test_uvloop()
    test_pillow()

if __name__ == "__main__":
    main()

