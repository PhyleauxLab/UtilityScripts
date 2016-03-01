1. remove a line containing this text from all files in a target directory  
`sed -i '/TEXT TO MATCH/d' FOLDER TO SEARCH/*`
2. find and replace a given string recursively in all files with a given suffix or string in name.
`find . -name “FILENAME SUFFIX OR STRING” -print0 | xargs -0 sed -i '' -e ’s/OLD TEXT/NEW TEXT/g’`
