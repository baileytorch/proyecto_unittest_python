
if __package__:
    from .presentacion.menu import iniciar_menu
else:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from app.presentacion.menu import iniciar_menu

if __name__ == "__main__":
    iniciar_menu()
