## Project dependencies

    pip install --upgrade pip
    pip install --upgrade RPi.GPIO
    pip freeze > requirements.txt
    sed -i '/pkg-resources/d' requirements.txt
