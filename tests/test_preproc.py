from mytoolbox.preproc import clean_text

def test_preproc():
    assert type(clean_text(['hello world', 'hellow woorld'])) == str
