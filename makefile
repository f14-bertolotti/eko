

src/grammar/parser.py: src/grammar/grammar.lark
	python3 -m lark.tools.standalone src/grammar/grammar.lark > src/grammar/parser.py

test: 
	python3 src/test.py

