import os

class Config:

    @property
    def test_val_1(default = null):
        os.environ.get('TEST_A', default)