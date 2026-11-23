import sys


def round_tenths_float(n: float) -> float:
    if n >= 0:
        return int(n * 10 + 0.5) / 10
    else:
        return int(n * 10 - 0.5) / 10


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

                temp_int = float(line[idx + 1 :])

                st = stats.get(station)

                if st is None:
                    st = stats[station] = [temp_int, temp_int, temp_int, 1]
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
        mean_val = round_tenths_float(sum_t / count)
        output.append(f"{station.decode("utf-8")};{min_t};{mean_val};{max_t}\n")

    sys.stdout.write("".join(output))


if __name__ == "__main__":
    main()


# __init__ че делает для чего нужен

# uv lock путь библиотек при одном томл
