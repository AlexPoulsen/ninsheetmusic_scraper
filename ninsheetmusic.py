import requests
import pathlib
import sys
import os
import errno
import urllib
import re


def get_filename_from_cd(cd, counter):
	"""
	Get filename from content-disposition
	"""
	if not cd:
		return None
	fname = re.findall('filename=(.+)', cd)
	if len(fname) == 0:
		return "unnamed_" + str(counter) + ".mid"
	out = fname[0].split("\"", 1)[1].rsplit("\"", 1)[0]
	if out is None:
		out = "unnamed_" + str(counter) + ".mid"
	return out


dl = []
counter = 1
print("4129 ", end="")
for n in range(0, 4129):
	dl.append("https://www.ninsheetmusic.org/download/mid/" + str(n + 1))
	print("|", end="")
	if counter % 120 == 0:
		print("\n", end="     ")
	counter += 1
print("\n")


path = pathlib.Path(".") / "ninsheetmusic_sources"
try:
	os.makedirs(path)
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
counter = 1
failed = []
print("downloading files")
print("     ", end="")
for file in dl:
	new_filename = get_filename_from_cd(urllib.request.urlopen(file).headers.get('content-disposition'), counter)
	if new_filename is not None:
		urllib.request.urlretrieve(file, str(path / new_filename))
	else:
		failed.append([file, str(path / "unnamed_" + str(counter) + ".mid")])
	print("|", end="")
	if counter % 120 == 0:
		print("\n", end="     ")
	counter += 1
print("\n")
failed_answer = input("Retry files with a failed name retrieve? [y/N] ")
if failed_answer.lower() == "y":
	for file in failed:
		urllib.request.urlretrieve(*file)
		print("|", end="")
		if counter % 120 == 0:
			print("\n", end="     ")
		counter += 1
	print("\n")
elif failed_answer.lower() == "n":
	pass
else:
	for file in failed:
		urllib.request.urlretrieve(*file)
		print("|", end="")
		if counter % 120 == 0:
			print("\n", end="     ")
		counter += 1
	print("\n")
