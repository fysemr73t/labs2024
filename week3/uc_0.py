# A very simple Universal Constructor
import sys
import shutil
import subprocess

# Set the number of generations
MAX_GEN = 2

def replicate():
    # Grab my name, isolate my generation, and
    # create my child's name. The name should be
    # of the form: `uc.GENERATION.py`
    my_name = sys.argv[0]
    print(f'{my_name}, step 1: {my_name}')

    my_parts = my_name.split('.')
    my_parts = my_parts[0].split('_') + my_parts[1:]
    print(f'{my_name}, step 2: {my_parts}')

    my_gen = int(my_parts[1])
    child_gen = my_gen + 1
    print(f'{my_name}, step 3: {my_gen}, {child_gen}')

    child_name = my_parts[0] + '_' + str(child_gen) + '.py'
    print(f'{my_name}, step 4: {child_name}')

    # Stop the replication after MAX_GENS
    if child_gen >= MAX_GEN:
        print(f'{my_name}: Generation stopped.')

    else:
        # Copy my code into a file with my child's name
        shutil.copyfile('./' + my_name, './' + child_name)

        # Create command to start the child
        cmd = ['python3', child_name]
        print(f'{my_name}, step 5: {cmd}')

        # Start the child running by asking the shell to run `cmd`
        subprocess.run(cmd)
        # subprocess.Popen(cmd)  # don't wait

    # Terminate self
    print(f'{my_name} TERMINATED')

if __name__ == '__main__':
    replicate()
