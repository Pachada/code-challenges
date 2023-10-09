"""
Stable internships | AlgoExpert
A company has hired N interns to each join one of N different teams. 
Each intern has ranked their preferences for which teams they wish to join, 
and each team has ranked their preferences for which interns they prefer.

Given these preferences, assign 1 intern to each team. 
These assignments should be "stable," meaning that there is no unmatched pair of an intern and a 
team such that both that intern and that team would prefer they be matched with each other.

In the case there are multiple valid stable matchings, the solution that is most optimal for the 
interns should be chosen (i.e. every intern should be matched with the best team possible for them).

Your function should take in 2 2-dimensional lists, one for interns and one for teams. 
Each inner list represents a single intern or team's preferences, 
ranked from most preferable to least preferable. 
These lists will always be of length N, with integers as elements. 
Each of these integers corresponds to the index of the team/intern being ranked. 
Your function should return a 2-dimensional list of matchings in no particular order. 
Each matching should be in the format [internIndex, teamIndex].

Sample Input
interns = [
  [0, 1, 2],
  [1, 0, 2],
  [1, 2, 0]
]
teams = [
  [2, 1, 0],
  [1, 2, 0],
  [0, 2, 1]
]
Sample Output
// This is the most optimal solution for interns
[
  [0, 0],
  [1, 1],
  [2, 2]
]
// This is also a stable matching, but it is suboptimal for the interns
// because interns 0 and 2 could have been given better team matchings
[
  [2, 0],
  [1, 1],
  [0, 2]
]
"""

# O(n**2) space | O(n**2) time
def stableInternships(interns, teams):
    """
    Assigns interns to teams in a stable manner based on their preferences and team rankings.

    Args:
        interns (List[List[int]]): A list of lists representing the preferences of each intern. Each intern's preferences are represented by a list of team indices in the order of their preference.
        teams (List[List[int]]): A list of lists representing the rankings of each team. Each team's rankings are represented by a list of intern indices in the order of their ranking.

    Returns:
        List[List[Optional[int], int]]: A list of lists representing the final assignments of interns to teams. Each intern's assignment is represented by a list containing the intern index and the team index.

    Example:
        ```python
        interns = [[1, 2], [0, 2], [0, 1]]
        teams = [[0, 1, 2], [1, 0, 2], [2, 1, 0]]
        assignments = stableInternships(interns, teams)
        print(assignments)
        ```
"""

    # Initialize a list called `choose_interns` with `None` values for each team, representing that no intern is assigned to any team yet.
    choose_interns = [[None, i] for i in range(len(interns))] # N space
    
    # Create a list called `free_interns_idx` containing the indices of all interns, representing that all interns are initially free.
    free_interns_idx = [*range(len(interns))]
    
    # Create a list called `interns_options_checked` with all values set to 0, representing that no intern's options have been checked yet.
    interns_options_checked = [0]*len(interns)
    
    # Create a list called `teams_options` which maps each team member to their index in the team list.
    teams_options = [{val:i for i,val in enumerate(team)} for team in teams] # N space
    
    # Enter a while loop that continues until there are no more free interns.
    while free_interns_idx: # N time
        
        # Pop an intern index from `free_interns_idx` to get the current intern.
        current_intern_idx = free_interns_idx.pop()
        
        # Iterate over the options of the current intern using a for loop.
        for _ in range(len(interns[current_intern_idx])): # N time
            
            # Get the current team option for the intern using `interns[current_intern_idx][interns_options_checked[current_intern_idx]]`.
            intern_current_team_option = interns[current_intern_idx][interns_options_checked[current_intern_idx]]
            
            # Increment `interns_options_checked[current_intern_idx]` to move to the next option for the current intern.
            interns_options_checked[current_intern_idx] += 1
            
            # If the chosen intern for the current team option is `None`, assign the current intern to that team and break the loop.
            if choose_interns[intern_current_team_option][0] is None:
                choose_interns[intern_current_team_option][0] = current_intern_idx
                break
            
            # If the chosen intern for the current team option is not `None`, compare the ranks of the current intern and the assigned intern for the team option.
            else:
                current_inter_team_rank = teams_options[intern_current_team_option][current_intern_idx]
                assigned_intern_team_rank = teams_options[intern_current_team_option][choose_interns[intern_current_team_option][0]]
                
                # If the current intern has a lower rank, add the assigned intern back to `free_interns_idx`, assign the current intern to the team, and break the loop.
                if current_inter_team_rank < assigned_intern_team_rank:
                    free_interns_idx.append(choose_interns[intern_current_team_option][0])
                    choose_interns[intern_current_team_option][0] = current_intern_idx
                    break
    
    # Return the `choose_interns` list, which contains the final assignments of interns to teams.
    return choose_interns


if __name__ == "__main__":
    interns = [
    [0, 1, 2],
    [2, 1, 0],
    [1, 2, 0]
  ]
    teams = [
    [2, 1, 0],
    [0, 1, 2],
    [0, 2, 1]
  ]
    print(stableInternships(interns, teams))
        
