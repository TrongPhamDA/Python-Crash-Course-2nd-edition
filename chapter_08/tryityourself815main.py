# 8-15. Printing Models: Put the functions for the
# example printing_models.py in a separate file
# called printing_functions.py. Write an import
# statement at the top of printing_models.py, and
# modify the file to use the imported functions

from tryityourself815module import print_models as pm, show_completed_models as sm
print("\nEx 8.15 Printing Models\n" + "-"*70)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs[:], completed_models)
sm(completed_models)