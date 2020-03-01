zip -g function.zip main.py
aws lambda update-function-code --function-name nook-number --zip-file fileb://function.zip
