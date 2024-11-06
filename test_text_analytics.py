from text_analytics import format_string, list_to_word_amount_list
import pytest

def test_format_string():
    assert format_string("") == ""
    assert format_string("Test String that simulates a normal text. Nothing too strange here, just normal punctuation. Three-year-old boy, he is happy!") == "test string that simulates a normal text nothing too strange here just normal punctuation three year old boy he is happy"
    assert format_string("Hi! My name is Camila, and I'm testing my functions... with different! special? Chartacters*+!¿/ I THINK that-it's_funny. To, write like 345 thIS¡ ´´ ; : yes# $ % & phone / ( )= mouse.") == "hi my name is camila and im testing my functions with different special chartacters i think that its funny to write like this yes phone mouse"

def test_list_to_word_amount_list():
    assert list_to_word_amount_list([]) == []
    assert list_to_word_amount_list(["the", "the", "is", "is", "boy", "boy", "happy", "sad"]) == [["the", 2], ["is", 2], ["boy", 2], ["happy", 1], ["sad", 1]]
    assert list_to_word_amount_list(["well", "well", "i", "i", "i", "fly", "yes", "no", "no", "not", "funny", "face", "face",
                                     "face", "face", "sad", "angry"]) == [["well", 2], ["i", 3], ["fly", 1], ["yes", 1],
                                                                          ["no", 2], ["not", 1], ["funny", 1],["face", 4],
                                                                          ["sad", 1],["angry", 1]]
    
pytest.main(["-v", "--tb=line", "-rN", __file__])