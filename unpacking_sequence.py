def main():
    servers = [
        ("Web-01", "192.168.1.10", "active", (85.5, 16.2)),
        ("DB-Primary", "192.168.1.50", "active", (92.1, 64.0)),
        ("Cache-01", "192.168.1.100", "maintenance", (12.0, 4.5)),
        ("API-Gateway", "192.168.1.25", "active", (45.8, 8.1)),
        ("Web-02", "192.168.1.11", "inactive", (0.0, 0.0)),
    ]

    # TODO: Write your header print statement here
    print(f"{"Server":15} | {"CPU %":>8} | {"Memory (GB)":>12}")
    # TODO: Write your loop with nested unpacking and filters here
    for server, _, _, (cpu, mem) in servers:
        if cpu > 40.0:
            print(f"{server:15} | {cpu:>8.1f} | {mem:12.1f}")
    # TODO: Print your formatted rows here


if __name__ == '__main__':
    main()