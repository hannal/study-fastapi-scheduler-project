.PHONY: testall lint refmt

testall:
	@pytest .

lint:
	@black . --check --config ./pyproject.toml

refmt:
	@black . --config ./pyproject.toml
