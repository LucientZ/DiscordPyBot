A .env file is to be put in this directory. Running `python3 ./src/init.py` or `make init` will prompt each environment variable in the console. This file can also be created manually. The format of the `.env` file is the following.

```python
    TOKEN="{Bot Token}"
    STATUS="{Bot Discord Status}"
    SYNC_ON_START={True | False}
```