import os

ENTRY = (
    "Oxygen: 1 star. Free trial auto-renews into a lifetime subscription "
    "you can't cancel. Cancellation is fatal."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
