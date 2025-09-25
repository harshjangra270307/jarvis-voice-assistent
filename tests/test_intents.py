from intents import IntentEngine

def test_intent_parser_english():
    ie = IntentEngine('phrases/phrases.txt')
    text = "Jarvis, call John"
    intent, args = ie.parse(text, 'en')
    assert intent == "call"
    assert "John" in args[0]

def test_intent_parser_hindi():
    ie = IntentEngine('phrases/phrases.txt')
    text = "जाविस, कॉल करो मोहन"
    intent, args = ie.parse(text, 'hi')
    assert intent == "call"
    assert "मोहन" in args[0]

