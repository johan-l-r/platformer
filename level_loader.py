def load(file_path: str): 
  with open(file_path, "r") as file: 
    content = file.read()

  tilemap = []

  # get list of lines 
  file_lines: list[str] = content.splitlines()

  for line in file_lines: 
    # remove whitespaces and str into list of chars 
    chars = list(line.replace(" ", ""))

    row = []

    for char in chars: 
      row.append(int(char))

    tilemap.append(row)
