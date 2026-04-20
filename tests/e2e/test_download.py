


def test_file_links_not_empty(download_page):
    download_page.navigate("https://the-internet.herokuapp.com/download")
    links = download_page.get_file_links()
    assert len(links) > 0, "Expected at least one file link, but found none."

def test_download_file(download_page, tmp_path):
    download_page.navigate("https://the-internet.herokuapp.com/download")
    file_name = 'test.txt'
    file_path = tmp_path / file_name
    download_page.download_file(file_path)
    assert file_path.exists(), f"Expected file {file_name} to be downloaded, but it was not found."