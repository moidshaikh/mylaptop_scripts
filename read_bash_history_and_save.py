from pathlib import Path
from typing import List


HOME_DIR = Path.home()

def read_history() -> List[str]:
    # bash history file is in homedir
    bash_hist_file = Path(HOME_DIR) / '.bash_history'
    
    if not Path(bash_hist_file).is_file():
        print(f"Invalid file: {bash_hist_file}")

    # reading history file
    with open(bash_hist_file, 'r') as f:
        commands = f.read()
        
    # splitting by lines
    commands = commands.split('\n#')
    # getting actual command
    commands = [x.split('\n')[-1] for x in commands]
    # removing duplicates
    commands = list(set(commands))
    return commands


def write_history(command_list: List[str], outpath='commands.txt') -> None:
    if Path(outpath).is_file():
        with open(outpath, 'r') as f:
            commands = f.read()
    else:
        commands = ""
    curr_commands = commands.split('|n')
    curr_commands = list(set(curr_commands))

    all_commands = command_list + curr_commands

    all_commands = list(set(all_commands))

    print(all_commands)
    with open(outpath, 'w') as f:
        f.write("|n".join(all_commands))
    
    print(f"File {outpath} updated successfuly")
    return len(all_commands)


def main():
    new_commands = read_history()
    print(len(new_commands))
    total_commands_written = write_history(new_commands)
    print(f"Written {total_commands_written} commands")


if __name__ == "__main__":
    main()