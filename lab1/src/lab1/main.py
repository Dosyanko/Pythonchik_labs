import sys


def rounding(total: int, count: int) -> int:
    return (2 * total + count) // (2 * count)


def main() -> None:
    if len(sys.argv) != 2:
        print("Invalid parameters.", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    stats = {}

    try:
        with open(filepath, "rb") as f:
            for line in f:
                idx = line.find(b";")
                if idx == -1:
                    continue

                station = line[:idx]

                temp_int = int(float(line[idx + 1 :]) * 10)

                st = stats.get(station)
                if st is None:
                    stats[station] = [temp_int, temp_int, temp_int, 1]
                else:
                    if temp_int < st[0]:
                        st[0] = temp_int
                    if temp_int > st[1]:
                        st[1] = temp_int
                    st[2] += temp_int
                    st[3] += 1
    except (FileNotFoundError, IOError, PermissionError) as e:
        print(f"File opening error: {e}", file=sys.stderr)
        sys.exit(1)

    output = []
    for station in sorted(stats.keys()):
        min_t, max_t, sum_t, count = stats[station]
        mean_val = rounding(sum_t, count)
        output.append(
            f"{station.decode("utf-8")};{min_t/10:.1f};{mean_val/10:.1f};{max_t/10:.1f}\n"
        )

    sys.stdout.write("".join(output))


if __name__ == "__main__":
    main()
