from nlp_text_corrector import asr_post_process

def test_convert():
    assert asr_post_process.convert("Book a first class flight ticket for my two childs of age twenty one and sixteen on thirty first march twenty twenty one which leaves after seven forty five pm") == "Book a first class flight ticket for my 2 childs of age 21 and 16 on 31st march 2021 which leaves after 7:45 pm"
    assert asr_post_process.convert("send an email to chandra at iamplus dot com") == "send an email to chandra@iamplus.com"