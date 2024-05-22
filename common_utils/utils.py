import requests


def download_file(url: str, filetype: str = "txt") -> str:
    local_file_path = f"data.{filetype}"

    response = requests.get(url)
    if response.status_code == 200:
        with open(local_file_path, 'wb') as f:
            f.write(response.content)
    else:
        raise IOError("Failed to download file.")

    return local_file_path
