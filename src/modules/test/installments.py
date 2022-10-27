import pytest

def installation():
    try:
        assert __import__("boto3")
        assert __import__("yaml")
    except:
        raise SystemExit(1)