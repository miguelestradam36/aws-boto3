def installation():
    assert __import__("boto3")
    assert __import__("pyyaml")