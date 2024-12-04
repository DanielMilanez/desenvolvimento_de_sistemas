
Utilizar um ambiente virtual facilita a vida do desenvolvedor de diversos aspectos, a instalação de dependencias nos projetos de uma equipe é um bom exemplo de vantagens que a venv porporciona.

Para se crair um ambiente virtual utilize um código em seu prompt `python -m venv venv` a venv será inicializada na sua maquina em forma de pasta, recomendo adicionar o termo ***venv*** no arquivo gitignore, pois, não querermos subir uma venv para nosso repositório no github. `gcm python -Syntax` informa para nós onde estamos localizados.

Aqui está uma lista de códigos utilizados para manipular uma venv, ou realizar operações delas.

```bash
    pip freeze > Requirements.txt
    pip install -r Requirements.txt

    pip uninstall "nome"
    
    .\venv\venv\activate
    deactivate
```