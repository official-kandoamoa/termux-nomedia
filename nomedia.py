import os
import re

def create_nomedia(root_path="."):
    # Optional: filter folders using regex (e.g., skip hidden folders starting with .)
    skip_pattern = re.compile(r'^\.')  # Skip hidden/dot folders (optional)

    created = []
    skipped = []
    errors = []

    # Walk through all subdirectories
    for dirpath, dirnames, filenames in os.walk(root_path):
        # Optional: Remove hidden dirs from traversal (comment out to include them)
        dirnames[:] = [d for d in dirnames if not skip_pattern.match(d)]

        nomedia_path = os.path.join(dirpath, ".nomedia")

        if os.path.exists(nomedia_path):
            skipped.append(nomedia_path)
            continue

        try:
            # Create a 0-byte .nomedia file
            open(nomedia_path, 'w').close()
            created.append(nomedia_path)
        except Exception as e:
            errors.append((nomedia_path, str(e)))

    # Summary
    print(f"\n✅ Created  : {len(created)}")
    print(f"⏭️  Skipped  : {len(skipped)} (already exist)")
    print(f"❌ Errors   : {len(errors)}")

    if created:
        print("\n--- Created ---")
        for p in created:
            print(f"  {p}")

    if errors:
        print("\n--- Errors ---")
        for path, err in errors:
            print(f"  {path} → {err}")

if __name__ == "__main__":
    target = os.getcwd()  # Uses current working directory
    print(f"📁 Target: {target}")
    create_nomedia(target)