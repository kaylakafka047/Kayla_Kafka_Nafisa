# --- File: printing_functions.py (Simulasi modul terpisah) ---
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Mencetak model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nModel berikut telah selesai dicetak:")
    for completed_model in completed_models:
        print(completed_model)

# --- File Utama: printing_models.py ---
# from printing_functions import print_models, show_completed_models

unprinted = ['phone case', 'robot pendant', 'dodecahedron']
completed = []

print_models(unprinted, completed)
show_completed_models(completed)