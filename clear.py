import os
for path in os.listdir():
  if "qn0" in path or "md0" in path:
    os.remove(path)
