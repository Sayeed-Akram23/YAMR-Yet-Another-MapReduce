# Makefile for automating project steps

# Default target
all: write read mapreduce

# Step 1: Write Data
write:
	@echo "Step 1: Writing Data"
	@cd client_folder && py write.py one
	@echo "Step 1 completed."

# Step 2: Create Worker Nodes
worker_nodes:
	@echo "Step 2: Creating Worker Nodes"
	@py server.py &
	@py client.py
	@echo "Step 2 completed."

# Step 3: Read Data
read:
	@echo "Step 3: Reading Data"
	@cd server_folder && py read.py one merger
	@echo "Step 3 completed."


# Step 4: Apply Mapper Across All Worker Nodes
map:
	@echo "Step 4: Applying Mapper"
	@read -p "Enter number of partitions to fetch from: " NUM_PARTITIONS; \
	for i in $$(seq 0 $$((NUM_PARTITIONS - 1))); do \
		cat "server_folder/partition$$i/one$$i" | python server_folder/mapper.py > "server_folder/partition$$i/p$$i"; \
	done
	@echo "Step 4 completed."

# Step 5: Integrate Content of Mapper Files
reduce:
	@echo "Step 5: Integrating Mapper Output"
	@py server_folder/shuff.py p
	@echo "Step 5 completed."
	@echo "Step 6: Shuffling and Reducing"
	@python server_folder/reducer.py
	@echo "Step 6 completed."

# # Step 6: Shuffling and Reducing
# reduce:
	


# Clean up generated files
clean:
	@echo "Cleaning up generated files"
	@rm -rf client_folder/files* server_folder/partition* merger
	@echo "Cleanup completed."

.PHONY: all write worker_nodes read mapreduce clean
