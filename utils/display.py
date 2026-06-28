# ponytail: simple table display using tabulate or fallback manual formatting
def print_table(data):
    if not data:
        print("Tidak ada data.")
        return
    try:
        from tabulate import tabulate
        print(tabulate(data, headers="keys", tablefmt="grid"))
    except ImportError:
        # ponytail: minimal fallback format string table
        headers = list(data[0].keys())
        header_str = " | ".join(f"{h:>10}" for h in headers)
        print(header_str)
        print("-" * len(header_str))
        for row in data:
            print(" | ".join(f"{str(row[h]):>10}" for h in headers))
