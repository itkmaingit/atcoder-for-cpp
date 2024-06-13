.PHONY: init rename run

CC = g++
DIR_PATH = ./problems

# make init date=<PROBLEM_DATE>  diff=<PROBLEM_DIFFICULTY>
init:
	@if [ -z "$${date}" ] || [ -z "$${diff}" ]; then \
        echo "Error: date or diff variable is not set"; \
        exit 1; \
    fi
	@export date=$${date}
	@export diff=$${diff}
	@mkdir -p $(DIR_PATH)/$${date}
	@cp ./sample_code/init.cpp $(DIR_PATH)/$${date}/$${diff}.cpp
	@touch $(DIR_PATH)/$${date}/$${diff}.in
	@touch $(DIR_PATH)/$${date}/$${diff}.res
	@python3 ./scripts/rename.py $${date} $${diff}

# make run date=<PROBLEM_DATE>  diff=<PROBLEM_DIFFICULTY>
run:
	@if [ -z "$${date}" ] || [ -z "$${diff}" ]; then \
        echo "Error: date or diff variable is not set"; \
        exit 1; \
    fi
	@$(CC) $(DIR_PATH)/$${date}/$${diff}.cpp -o $(DIR_PATH)/$${date}/$${diff}.out
	@$(DIR_PATH)/$${date}/$${diff}.out < $(DIR_PATH)/$${date}/$${diff}.in | tee $(DIR_PATH)/$${date}/$${diff}.txt
