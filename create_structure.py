import os

# プロジェクトのルートディレクトリ
base_dir = 'MyMiBandProject'

# 各ディレクトリの構成
directories = [
    os.path.join(base_dir, 'android-app', 'app', 'src', 'main', 'java', 'com', 'example'),
    os.path.join(base_dir, 'android-app', 'app', 'src', 'main', 'res', 'layout'),
    os.path.join(base_dir, 'android-app', 'app', 'src', 'main', 'res', 'values'),
    os.path.join(base_dir, 'android-app', 'app', 'src', 'main', 'res', 'drawable'),
    os.path.join(base_dir, 'android-app', 'app', 'src', 'test'),
    os.path.join(base_dir, 'flask-server')
]

# 各ディレクトリを作成
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# ファイルの作成
files = [
    os.path.join(base_dir, 'android-app', 'app', 'src', 'main', 'java', 'com', 'example', 'MainActivity.kt'),
    os.path.join(base_dir, 'android-app', 'app', 'src', 'main', 'java', 'com', 'example', 'ApiService.kt'),
    os.path.join(base_dir, 'android-app', 'app', 'src', 'main', 'java', 'com', 'example', 'HeartRateData.kt'),
    os.path.join(base_dir, 'android-app', 'app', 'src', 'main', 'AndroidManifest.xml'),
    os.path.join(base_dir, 'android-app', 'app', 'build.gradle'),
    os.path.join(base_dir, 'android-app', 'build.gradle'),
    os.path.join(base_dir, 'android-app', 'settings.gradle'),
    os.path.join(base_dir, 'flask-server', 'app.py'),
    os.path.join(base_dir, 'flask-server', 'requirements.txt'),
    os.path.join(base_dir, 'flask-server', 'README.md'),
    os.path.join(base_dir, 'README.md')
]

# 空のファイルを作成
for file in files:
    with open(file, 'w') as f:
        if 'README.md' in file:
            f.write('# MyMiBandProject\n\nこのプロジェクトの説明\n')
        elif 'requirements.txt' in file:
            f.write('# 必要なパッケージリスト\n')
        else:
            f.write('// TODO: Implement this file\n')

print("ディレクトリ構成が作成されました。")
