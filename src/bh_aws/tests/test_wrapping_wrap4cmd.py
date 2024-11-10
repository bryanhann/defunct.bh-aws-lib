from bh_aws.aws.ec2.describe_key_pairs import DESCRIBE_KEY_PAIRS
from bh_aws.wrapping import DUMMY
from bh_aws.wrapping import wrap4cmd

def test_underscore():
    """Test implemented
    """
    assert wrap4cmd('describe_key_pairs') == DESCRIBE_KEY_PAIRS

def test_hyphenated():
    """Test implemented
    """
    assert wrap4cmd('describe-key-pairs') == DESCRIBE_KEY_PAIRS

def test_unimplemented():
    """Test unimplemented
    """
    assert wrap4cmd('xxx_not_an_implemented_command_xxx') == DUMMY

