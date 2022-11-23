import pytest


def test_installments():
    """
    Pytest function
    Params: No arguments/parameters
    Objective: Check if boto3 and yaml modules has been installed into python
    """
    try:
        import boto3
        import yaml
        assert type(boto3)
        assert type(yaml)
    except:
        raise SystemExit(1)