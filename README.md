# Team Assignment Program

This Python program reads a CSV file containing a list of players and assigns them to three teams - Sharks, Dragons, and Raptors. It then generates a text file with the team rosters and creates individual letters for each player's family.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ericsryan/techdegree_project_1.git
   cd techdegree_project_1
   ```

2. **Ensure Python is Installed:**
   This program requires Python. If you haven't installed it yet, you can download it from [python.org](https://www.python.org/downloads/).

3. **Install Required Packages:**
   This program uses the built-in `csv` module and does not require additional packages.

4. **Prepare CSV File:**
   Place your CSV file containing the list of players in the project directory. Make sure the file follows the same format as the provided example.

## Usage

1. **Run the Program:**
   ```bash
   python team_assignment.py
   ```

2. **Output:**
   - The program will generate a `teams.txt` file containing the team rosters.
   - Individual letters for each player's family will be created as separate text files in the project directory.

3. **Viewing Team Rosters:**
   Open the `teams.txt` file to view the team rosters.

4. **Player Letters:**
   Individual letters for the players' families will be saved in the project directory with filenames in the format `firstname_lastname.txt`.

## CSV File Format

Ensure your CSV file follows this format:

```csv
Name,Height (inches),Soccer Experience,Guardian Name(s)
Player 1,Height 1,YES/NO,Guardian 1, Guardian 2
Player 2,Height 2,YES/NO,Guardian 1, Guardian 2
...
```

- `Name`: Player's full name.
- `Height (inches)`: Player's height in inches.
- `Soccer Experience`: Either "YES" or "NO" indicating if the player has soccer experience.
- `Guardian Name(s)`: Full name(s) of the player's guardian(s).

## Example CSV File

```csv
Name,Height (inches),Soccer Experience,Guardian Name(s)
Sara Mitchell,42,YES,Rob Mitchell, Sarah Mitchell
Jake Smith,38,YES,Jim Smith, Jane Smith
...
```

Feel free to reach out if you have any questions or need further assistance!