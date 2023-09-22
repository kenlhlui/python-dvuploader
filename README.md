<p align="center">
    <h1 align="center">Python DVUploader</h1>
</p>

Python equivalent to the [DVUploader](https://github.com/GlobalDataverseCommunityConsortium/dataverse-uploader) written in Java. Complements other libraries written in Python and facilitates the upload of files to a Dataverse instance via [Direct Upload](https://guides.dataverse.org/en/latest/developers/s3-direct-upload-api.html).

**Features**

* Parallel direct upload to a cloud storage provider
* Files are streamed directly instead of being buffered in memory
* Supports multipart uploads

-----

<p align="center">
    <img src="./static/demo.gif" width="600"/>
</p>

-----

## Getting started

To get started with Catalax, you can install it via pip:

**From source**

```bash
python3 -m pip install git+https://github.com/JR-1991/python-dvuploader.git
```

## Quickstart

In order to perform a direct upload, you need to have a Dataverse instance running and a cloud storage provider. The following example shows how to upload files to a Dataverse instance. Simply provide the files of interest and utilize the `upload` method of a `DVUploader` instance.

```python
from dvuploader import DVUploder, File

files = [
    File(filepath="./small.txt"),
    File(directoryLabel="some/dir", filepath="./medium.txt"),
    File(directoryLabel="some/dir", filepath="./big.txt"),
]

DV_URL = "https://demo.dataverse.org/"
API_TOKEN = "XXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
PID = "doi:10.70122/XXX/XXXXX"

dvuploader = DVUploder(files=files)
dvuploader.upload(
    api_token=API_TOKEN,
    dataverse_url=DV_URL,
    persistent_id=PID,
)
```

