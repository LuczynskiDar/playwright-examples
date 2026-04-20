

def test_upload_file(upload_page, tmp_path):
    upload_page.navigate("https://the-internet.herokuapp.com/upload")
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("This is a test file.")
    upload_page.upload_file(str(test_file))    
    filename = upload_page.get_uploaded_filename()
    assert filename == str(test_file.name)