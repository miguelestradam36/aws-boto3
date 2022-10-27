import pytest


def test_installments():
    try:
        import boto3
        import yaml
        assert type(boto3)
        assert type(yaml)
    except:
        raise SystemExit(1)