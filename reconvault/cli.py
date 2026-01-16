import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="reconvault",
        description="ReconVault - Pentest recon automation toolkit"
    )
    sub = parser.add_subparsers(dest="command")

    scan = sub.add_parser("scan", help="Run recon scans on a target")
    scan.add_argument("target", help="IP or domain")
    scan.add_argument("--full", action="store_true", help="Run full port scan")
    scan.add_argument("--web", action="store_true", help="Run web enumeration")

    args = parser.parse_args()

    if args.command == "scan":
        print(f"[+] Target: {args.target}")
        print(f"[+] Full scan: {args.full}")
        print(f"[+] Web enum: {args.web}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
