test:
	@if pip show pytest > /dev/null 2>&1; then  python3 -m pytest tests/unit --verbose -s; else make -s install; fi

install:
	@if pip install -r requirements.txt; then make -s test; else echo "Failed to execute the tests!!!"; fi