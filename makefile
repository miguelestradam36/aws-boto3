.PHONY: awscript
awscript: 
	@pip install -r src\config\requirements.txt --quiet
	@echo Packages installed...
	@pytest src\test\test_installments.py
	@python src\main.py