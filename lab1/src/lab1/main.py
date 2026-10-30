import math
import sys


def main():
  sys.stdout.reconfigure(encoding="utf-8")
  if len(sys.argv) != 2:
    print("Invalid parameters.", file=sys.stderr)
    sys.exit(1)

  filepath = sys.argv[1]
  stats = {}

  try:
    with open(filepath, "r", encoding="utf-8") as f:
      for line in f:
        line = line.strip()
        if not line:
          continue

        parts = line.split(";")
        if len(parts) != 2:
          continue

        station = parts[0]
        temp_str = parts[1]

        temp_int = int(float(temp_str) * 10)

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

  sorted_stations = sorted(stats.keys())

  for station in sorted_stations:
    min_t, max_t, sum_t, count = stats[station]

    min_val = min_t / 10
    max_val = max_t / 10

    mean_val_tenths = sum_t / count
    rounded_tenths = math.floor(mean_val_tenths + 0.5)
    mean_val = rounded_tenths / 10

    print(f"{station};{min_val:.1f};{mean_val:.1f};{max_val:.1f}")


if __name__ == "__main__":
  main()