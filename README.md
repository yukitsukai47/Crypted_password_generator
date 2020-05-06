# Crypted_password_generator
パスワードを自動生成してテキストファイルに出力するプログラムです。  
その後、出力したテキストファイルをパスワードで暗号化します。  
復号にはcrypto.pyのオプション -d を使用して行います。  

```
cat (暗号化されたファイル名) | python3 crypto.py -d > (出力したいファイル名)
```

This program automatically generates a password and outputs it to a text file.  
After that, the output text file is encrypted with a password.  
Decryption is done using the crypto.py option -d.  

```
cat (encrypted filename) | python3 crypto.py -d > (name of the file you want to output)
```

# 動作環境(operating environment)
mac or Linux
Python 3系（python3.8確認済み）

# 使い方(How to use)
python3 password_generator.py

<img width="836" alt="screenshot" src="https://user-images.githubusercontent.com/52772923/81141115-94157a00-8fa6-11ea-9e25-41ec2a5fcf68.png">